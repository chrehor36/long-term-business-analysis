# Company Run — Mastercard Incorporated (NYSE: MA) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Dispatched run.** Brief: `Screens/_daily/_dispatch_brief.md`, slots filled by the dispatcher's message of 2026-10-10. The
lock in `Screens/_daily/` was present when this run began, written by the dispatching session ("interactive v5 re-runs
batch 8"); this analyst did not write, touch or remove it. Research folder: `Test Runs/_research 2026-10-10 MA/` (raw
filings and XBRL under its `cache/`, ignored by git).

**Contamination, declared and not used.** (1) The session's opening git status and recent commit subjects named other
companies' runs and folds (LOW, LOPE, LRCX, LSTR, AYI, BDC, ARCB research folders); none concerns Mastercard and none was
opened. (2) The project memory index, loaded with the session, carries general queue-state lines and no line about
Mastercard. (3) The governing text itself, at Q7's range convention, says "Visa's run said the growth input decided
everything"; Visa is a competitor named in the brief; the sentence is a remark about method, carries no verdict on either
company, and nothing in this run rests on it. (4) The brief says earlier run files about Mastercard exist; none was opened,
listed or searched, and `Test Runs/` was never listed.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $589.14 (close 2026-10-09; printed by `tools/run.py` from an aggregator, flagged per operator rule 5: a live
  quote only).
- **Shares by class** from the latest filing's cover: Class A 869,464,115 and Class B 6,545,825 (10-Q for the quarter to
  2026-06-30, filed 2026-07-30, accession `0001141391-26-000083`; `python Screens/cover_shares.py MA`). **The charter note,
  read before adding:** Class B is non-voting, carries the same dividend, and "Shares of Class B common stock are convertible
  on a one-for-one basis into shares of Class A common stock" (10-K FY2025, Note 14, accession `0001141391-26-000013`); the two
  classes are economically one, so they are added: **876.0M shares**. Check against the balance sheet of 2026-06-30: 1,406M
  Class A issued less 536M treasury = 870M (rounded), plus 7M Class B; the 10-Q's own share roll gives 870.7M A and 6.5M B at
  2026-06-30. No 8-K or prospectus after the 10-Q changes the count (filings list of 2026-10-09: Forms 3, 4 and 144 only
  since 2026-07-30). `tools/run.py` printed a stale weighted-average count (906.0M); not used.
- **Market cap:** 876.0M x $589.14 = **$516.1B**.
- **Sovereign for the earnings currency:** USD, **5.60%**, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, issuing authority). The filer's reporting currency is USD; its revenue is earned in many
  currencies and billed largely in USD and EUR (10-K FY2025, "Foreign Currency"), and the filer's own valuation unit is USD.
- **Net debt at the latest filed balance sheet (2026-06-30, 10-Q `0001141391-26-000083`):** total debt $24,643M (short-term
  $2,459M including $710M commercial paper, long-term $22,184M) less cash and cash equivalents $11,291M and investments
  $318M = **$13,034M**. Restricted cash ($488M) and restricted security deposits held for customers ($2,196M, matched by an
  equal liability) are left out: they are not the company's to use. Operating leases left out, said so. **Subsequent event
  the filing states:** the agreement of March 2026 to buy BVNK Holdings for $1.5B (plus up to $0.3B contingent), expected to
  close before the end of the third quarter of 2026 (10-Q Note 2). No 8-K reports the close (none required at that size);
  the $1.5B is added as cash committed: **net debt for Q7, $14,534M.**
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-11, accession `0001141391-26-000013`); 10-Q Q2 2026 (filed
  2026-07-30, `0001141391-26-000083`); 10-Q Q1 2026 (filed 2026-04-30, `0001141391-26-000031`); proxy statement (DEF 14A,
  filed 2026-04-27, `0001141391-26-000021`); 8-Ks of 2026-05-07 (`0001141391-26-000034`, controller), 2026-06-02
  (`0001141391-26-000037`, leadership changes), 2026-06-08 (`0001193125-26-261669`, $5B notes), 2026-06-17
  (`0001141391-26-000041`, meeting votes); and for the cycle the 10-Ks for FY2009 (`0001193125-10-034065`, covering 2008 and
  2009), FY2010 (`0001193125-11-044721`), FY2012 (`0001141391-13-000003`), FY2015 (`0001141391-16-000085`), FY2017
  (`0001141391-18-000009`), FY2020 (`0001141391-21-000018`), FY2022 (`0001141391-23-000020`) and FY2024
  (`0001141391-25-000011`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$17,648M**,
  as printed by `tools/run.py` from XBRL, matches the filed Consolidated Statement of Cash Flows in the 10-K
  (`0001141391-26-000013`, page 73) exactly; FY2024 $14,780M and FY2023 $11,980M also match.
- `python tools/run.py MA`, arithmetic lines only (its yields and "growth the price assumes" are not used, Part VII): OCF
  less stock pay less capital spending (property plus capitalized software) FY2023 $10,432M, FY2024 $13,060M, FY2025
  $15,836M; three-year mean $13,109M; five-year mean $11,501M on the same basis. D&A FY2025 $1,143M against capital spending
  $1,215M. Stock pay from the cash-flow statement ($597M FY2025) is in the figure. The owner-cash series used at Q7 is rebuilt
  from the filed statements at Q4 (acquisitions, interest and the BVNK commitment are not in `tools/run.py`'s figure).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety: the business is widely known as a good one, so the danger
is a price that needs a pencil, and "if you have to actually do it on — with pencil and paper, it’s too close to think
about" **[M1996-084]**. The second is "a share is a business": the question is what Mastercard's network will earn,
"Not by selling it to somebody else" **[M1997-052]**. No macro view enters **[M2000-094]**; cross-border travel is read as a
property of the business (it fell 29% in 2020 and recovered), never as a forecast. Who is paid to tell **[M2020-037]**: the 10-K leads with
"Adjusted net revenue", "Adjusted net income" and "Adjusted diluted EPS" (10-K FY2025, page 6), which is the company's own
advocacy, read as such. **Contrary evidence, written down as found** **[M1997-127]**: (a) rebates and
incentives paid to issuers and merchants rose from 24.1% of gross revenue in 2009 (10-K FY2009) to roughly 38% in 2025
(computed below), so the network is paying a rising share of what it bills to keep its customers; (b) litigation provisions
recur in seventeen of the nineteen years 2007 to 2025 and two of them were each more than $1B; (c) the April 2026 putative
class of U.S. merchants for credit interchange since 2019, and Block and Intuit's opt-out claims "in excess of $5 billion"
(10-Q Q2 2026), are new or enlarged since the 10-K; (d) the company borrowed $5B in June 2026 while buying back stock at
about $500 a share and shareholders' equity fell to $5.6B.

## THE STANDING RULE
The rule binds the buyer: a purchase of this stock with the buyer's own unborrowed money, sized so that a fall of half or
more could be sat through, risks nothing the buyer has and needs **[M2012-081]**; bought on margin it would break the rule,
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in the target alters this; its own debt and
its settlement guarantee are weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** Mastercard runs a four-party card network: it does not issue cards, lend, or
  set merchant discount rates; it charges issuers and acquirers assessments on the dollar volume of cards carrying its
  brands (domestic and cross-border) and on the transactions it switches, pays a large and rising share of those charges
  back to issuers and merchants as "rebates and incentives", and sells services built on the network ("value-added
  services and solutions", 41% of 2025 net revenue). One reportable segment: "All of the segment’s activities are
  interrelated, and each activity is dependent upon and supportive of the other" (10-K FY2025 Note 22, `0001141391-26-000013`).
- **The key variables, and how predictable they have been** **[M1998-044]**. (1) Card spending on its brands: GDV $2,454B in
  2009 (10-K FY2009, `0001193125-10-034065`, down 3.3% in dollars, up 1.4% in local currency in the recession) to $10.6T in
  2025 (10-K FY2025), about 9.6% a year compounded; flat in 2020 on a local basis (10-K FY2020, `0001141391-21-000018`).
  (2) Cross-border travel spending, the richest stream and the volatile one: cross-border fees fell 2.5% in 2009 and 37% in
  2020 (volume down 29% local), then grew 32% local in 2021, 45% in 2022 and 15% in 2025. (3) The net take after incentives:
  payment-network net revenue per dollar of GDV was about 0.176% in 2009 (domestic, cross-border and processing fees $5,933M
  less rebates $1,618M, over GDV) and about 0.183% in 2025 ($19,476M over $10.6T): held, through Durbin (2011), the EU
  Interchange Fee Regulation (2015) and the pandemic. (4) Regulation and litigation, a cost every year (Q4). (5) The rival
  rails: account-to-account and government schemes (Pix, UPI, FedNow), wallets, stablecoins, named by the company as
  competitors (10-K FY2025, Competition).
- **Do the past statements tell me the future ones** **[M2008-033]**? On (1) to (4), yes: sixteen years of filings through two
  shocks show the same shape, volume compounding, the take held, margins widening from 44.3% (2009) to 57.6% (2025). On (5)
  the past says less: the filer itself writes that the industry "is subject to rapid and significant technological changes"
  (10-K FY2025, Risk Factors). The forecast that matters is about customers and governments, not about a technology the
  company must out-invent: will consumers and merchants keep paying through card networks, and will states push their own
  rails **[M2017-019]**, **[M2023-030]**. The switching technology itself (authorize, clear, settle) is decades old.
- **How far off could I be** **[M2011-084]**? The worst year in the window (2020) cut net revenue 9% and left a 52.8% operating
  margin; the worst year in the record (2008) was a litigation year (operating loss of $535M on $2,483M of settlements, 10-K
  FY2009) with a 39.0% margin before them. The error band is wide on growth and narrow on survival.
- **Routing.** The filer's own "rapid technological change" language is boilerplate set against a sixteen-year record in
  which the economics did not change fast: the take held and the margin rose. The ten-year question that is genuinely open
  (how far account-to-account and government rails take share) is a question about what could destroy the castle, and the
  framework puts it at Q2 (Q2, Change, and what it does to a castle); it does not put the forecast of the economics out of
  reach, so it does not close the file here **[M1998-008]** read against **[M2012-065]**. I can say where the industry stands
  and where this company stands in it **[M2012-065]**: second of two global open networks, behind Visa, far ahead of the rest.
- **Doubt test** **[M2002-092]**: the doubt I hold is about the size of the rival rails' bite, not about how the business
  makes money; that doubt is carried to Q2 test 11 and to Q7's "how sure", not used to stop here.
- **VERDICT: IN.** The earning power and competitive position five to ten years out can be given "a reasonable fix"
  **[M2012-065]**: a fee on electronic spending that has grown with it for sixteen years, the forecast resting on consumer and
  merchant behaviour **[M2017-019]**. Filing fact: GDV $2.45T (2009) to $10.6T (2025); payment-network take about 0.18% at both
  ends.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The castle **[M1995-038]**: a payment brand accepted almost everywhere, carried on billions of cards issued by banks that
also issue the one other global open brand, with a switching network and a rulebook that merchants, acquirers and issuers
all plug into. The reason the customer comes is that everyone else is already there.
- **The attacker with money** **[M2011-015]**, **[M1997-103]**. The plainest test in the record: Discover, with a bank's
  balance sheet behind it since 1985, ran payment-services volume of $402.5B in 2024 (DFS 10-K FY2024,
  `0001393612-25-000009`) against Mastercard's GDV of about $9.8T that year; Capital One, the largest U.S. card issuer by
  balances, bought it on 2025-05-18 and wrote in its own 10-K that "we cannot be certain that we will achieve global market
  parity with Visa or Mastercard. In addition, Visa and Mastercard have entered into long-term arrangements with financial
  institutions, some of which are exclusive, or nearly exclusive" and that its rivals "have provided financial incentives to
  card issuers, such as large cash signing bonuses for new programs" (COF 10-K FY2025, `0000927628-26-000024`, Risk Factors).
  That is the competitor, asked **[M2017-091]**, answering that the castle holds, and naming the price of holding it.
- **Pricing power and the agony before a rise** **[M2005-020]**. In 2009, with GDV up 1.4% in local currency, "net pricing
  actions contributed approximately 6 percentage points to our net revenue growth", including "price increases in April 2009
  and October 2009" (10-K FY2009). Value-added services list "pricing" among their 2025 growth drivers (10-K FY2025). Against
  it: the issuer-facing price is bid down every renewal (below).
- **Unit volume and share of mind** **[M1999-054]**. Switched transactions grew in every year read, including 2020 (+3%, to
  90.1B) and 2025 (+10%, to 175.5B); processed transactions grew 6.9% in 2009 (the earlier definition, not comparable in
  level). GDV grew in local currency in 2009 and was flat in 2020.
- **Would the customer still choose it over the low bid** **[M2017-009]**? Here the castle has two faces. The merchant and the
  cardholder do not bid networks against each other: merchants have sued since 2005 and still accept the card, and volume
  grew through it, the "customers are mad at you and you’re growing" test **[M2000-032]**. The issuer does bid them: rebates
  and incentives were 24.6% of gross revenue in 2007, 24.1% in 2009, 26.8% in 2012, 29.2% in 2015, 31.9% in 2017, 32.4% in
  2019, 35.2% in 2020, 36.7% in 2021, about 37.0% in 2022 and about 38.5% in 2025 (10-Ks FY2009, FY2012, FY2015, FY2017,
  FY2020, FY2022, FY2025; the last two computed from the stated rebates of $13,084M and $20,522M against net revenue plus
  rebates). Visa shows the same drift from a lower level: client incentives 16.5% of gross in FY2013, 17.1% in FY2015, 28.3%
  in FY2025 (V 10-K FY2015 `0001403161-15-000013`; FY2025 `0001403161-25-000089`). The company says so itself: "we may have
  to increase the amount of these incentives and pricing discounts" (10-K FY2025, Risk Factors). The two networks compete
  for the issuer on price; yet the net take held at about 0.18% of GDV and the operating margin rose, so the bidding has not
  yet been the kind where rivals "beat each other’s brains out" **[M2013-052]**.
- **The low-cost position** **[M2018-043]**: a switch's cost per transaction falls with volume; Mastercard's adjusted
  operating expenses grew 14% in 2025 against 16% net revenue growth; scale is the moat's mechanism **[M1995-039]**. Visa is
  larger (payments volume $13.9T, processed transactions 257.5B in FY2025) and runs a higher margin, so Mastercard is not the
  low-cost operator of the pair; the pair together is low-cost against any entrant.
- **The brand in the customer's mind** **[M2015-038]**: the cardholder rarely asks for the network by name; the issuer and the
  merchant's acceptance carry the brand. The brand's protection is acceptance, not affection.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Widening: services grew from $784M of "other revenues" in 2009 to
  $13,315M in 2025 (23% growth in 2025, 3 points from acquisitions); the take held; switched transactions roughly doubled from
  2020 to 2025. Narrowing: the incentive share (above); regulation that moved price from issuers (Durbin's debit cap and
  routing, 2011; the EU caps, 2015) and now threatens the network's own routing (the 10-K names "proposed legislation in the
  U.S. to extend routing mandates to credit", the Credit Card Competition Act proposals); the FTC consent order of December
  2022 requiring Mastercard to let merchants route tokenized online debit to other networks (10-K FY2022,
  `0001141391-23-000020`).
- **What could destroy, modify or reduce it** **[M2000-014]**, **[L2006-008]**. Would a card network be built today against
  instant account-to-account rails? The filer names the threat itself: government "digital public infrastructure" (Pix in
  Brazil, UPI in India, FedNow in the U.S.) "increasingly being considered as alternatives to traditional domestic payment
  solutions and schemes such as ours", stablecoins, and "pricing pressure related to real-time account-based payment
  schemes" (10-K FY2025). The evidence so far: UPI (2016) and Pix (2020) are years old, and Mastercard's GDV outside the U.S.
  still grew 12% (2024) and 10% (2025) in local currency; the Brazilian real remains one of the filer's four primary
  functional currencies. None of the national schemes, nor China UnionPay, files with the SEC: **flagged as non-filers**;
  their share is not on this record. The company's answer is to buy into the threat (Vocalink, 2017; account-to-account
  businesses since; BVNK, stablecoin infrastructure, $1.5B, agreed 2026). This is the one test whose answer is a judgment
  about governments.
- **The competitor row** (same span where the filings allow; operating margin = operating income over net revenue):

  | Company | Metric | FY2009 | FY2020 | FY2025 | Source |
  |---|---|---|---|---|---|
  | Mastercard | net revenue / operating margin | $5.10B / 44.3% | $15.30B / 52.8% | $32.79B / 57.6% | 10-Ks FY2009, FY2020, FY2025 |
  | Visa (fiscal year to September) | net revenue / operating margin | $6.91B / 51.2% | $21.85B / 64.5% | $40.00B / 60.0% | V XBRL; 10-K FY2025 `0001403161-25-000089` |
  | American Express (closed loop, a bank) | net income / year-end equity | $2.13B / 14.8% | $3.14B / 13.6% | $10.83B / 32.4% | AXP XBRL; 10-K FY2025 `0000004962-26-000080` (network volumes $1,897B) |
  | Discover (to 2024; acquired by Capital One 2025-05-18) | net income / year-end equity | equity not in XBRL | $1.14B / 10.5% | FY2024 $4.54B / 25.3% | DFS 10-K FY2024 `0001393612-25-000009`; COF 10-K FY2025 |
  | PayPal (rides the card rails, competes at checkout) | operating margin | FY2016 14.6% | 15.3% | 18.3% (TPV $1.79T, transactions down 4%) | PYPL XBRL; 10-K FY2025 `0001633917-26-000024` |

  Visa's FY2012 and Mastercard's FY2008 margins were cut by litigation (Visa operating income $2.14B in FY2012; Mastercard an
  operating loss in 2008); each recovered the next year.
- **The parts table.** Not applicable: one reportable segment, and the filer states its parts are interdependent (Note 22).
  Value-added services (41% of 2025 net revenue) are read with the network, not as a separate castle; no operating profit
  is reported by part.
- **The field's returns over the last full cycle**, judged in words **[M1999-108]**: the two open networks earned operating
  margins between 44% and 65% in the trough of 2009, the pandemic of 2020 and the peak of 2025; a durable castle protecting
  excellent returns, not ordinary ones **[L2007-004]**. The closed-loop and lending rivals earn bank returns that swing with
  credit (AXP 13.6% to 32.4%; Discover 10.5% to 25.3%); the checkout rival earns about a third of the network margin.
- **Contrary evidence, written down** **[M1997-127]**: the incentive share rose in every period read, at both networks. The
  speakers said of one card franchise that it was "not what it was 20 years ago, relative to the competition" and that a card
  without "special value" "gets more commodity-like" **[M1996-036]**; that is a row about one company (American Express,
  1996), weighed under the CONVENTION on rows about one company, not a verdict on this one.
- **VERDICT: IN.** The castle stands on the evidence: the best-funded attacker in the field says in its own filing that it
  cannot be sure of parity **[M2011-015]**; volume grew through the recession, the pandemic and two decades of merchant
  litigation **[M2000-032]**; price held net of incentives and the field's returns stayed excellent through the cycle
  **[L2007-004]**. Its narrowing risks (incentives, routing law, state rails) are real and carried to Q7's question of how sure; on the
  filings they are a judgment about degree, not a castle shown open, and not a future that cannot be judged **[M2000-019]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, measured on tangible assets **[M2011-060]**. At 2025 year-end the
  operating capital is small: property, equipment and right-of-use assets $2,303M; capitalized customer incentives $10,401M
  (cash paid to issuers up front, Note 7); other intangibles $5,554M (capitalized software and acquired intangibles);
  receivables $4,609M; against accrued expenses $13,272M and payables $999M (10-K FY2025). Operating income of $18,897M is
  about 100% of the first three alone and about 220% of the net figure. Goodwill ($9,560M) is left out for the business and
  counted for the allocation **[M2011-060]**; acquisitions are weighed at Q6.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending (property plus capitalized
  software) was $1,215M in 2025, 3.7% of net revenue, against depreciation and amortization of $1,143M; the filer gives no
  maintenance split, so the guess is that spending about equal to D&A keeps the network in place **[L2000-035]** and very
  little more is needed to carry volume. The real growth capital is of two other kinds: (1) up-front incentives to win and
  renew issuer contracts, which show in operating cash as the change in prepaid expenses ($3,388M paid out in 2025, $3,835M
  in the first half of 2026 alone, against amortization of $2,098M in 2025), and (2) acquisitions, $10,864M of cash paid for
  businesses 2016 to 2025 (largest: $4,436M in 2021, $2,511M in 2024 including Recorded Future at $2.7B) (10-Ks FY2017 to
  FY2025, cash-flow statements). Both are counted in owner cash at Q7.
- **The growth arithmetic** **[M2001-019]**, **[L2007-010]**: net revenue rose from $5,098M (2009) to $32,791M (2025), about 12.3%
  a year, while the business needed a few hundred million to a little over a billion of capital spending a year and returned
  more than all of its free cash to owners (Q6). It is close to the first of the speakers' three businesses, "more and more
  money every year without putting up anything to get it, or very little" **[M1998-081]**, with the qualification that the
  incentive prepayments are a growing toll on the growth.
- **The caps** **[M1997-095]**, **[M1999-067]**: growth of 12% to 17% a year cannot run past the world's card spending forever;
  Q7 carries growth for ten years only and none after.
- **WEIGHS FOR.** Very high returns on the capital the business actually needs, and growth that has needed little added
  capital **[M1998-081]**, **[M1995-047]**; the rising up-front incentives and the acquisition spending are the two charges that
  keep it from the purest form, and both are deducted at Q7. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, nine year-ends and the latest quarter** **[M2025-032]** (USD millions; `tools/run.py`
  transcription of the first-filed XBRL, checked against the filed balance sheets in the 10-Ks FY2020, FY2022, FY2024, FY2025
  and the 10-Q of 2026-06-30):

  | year-end | equity | cash | receivables | goodwill | other intangibles | debt (current + long-term) | retained earnings | treasury stock | capitalized customer incentives |
  |---|---|---|---|---|---|---|---|---|---|
  | 2017 | 5,497 | 5,933 | n/t | 3,035 | n/t | n/t | 22,364 | n/t | 1,898 |
  | 2018 | 5,395 | 6,682 | 2,276 | 2,904 | 991 | 6,334 | 27,283 | n/t | n/r |
  | 2019 | 5,893 | 6,988 | 2,514 | 4,021 | 1,417 | 8,527 | 33,984 | n/t | 3,710 |
  | 2020 | 6,391 | 10,113 | 2,646 | 4,960 | 1,753 | 12,672 | 38,747 | n/t | 4,306 |
  | 2021 | 7,312 | 7,421 | 3,006 | 7,662 | 3,671 | 13,901 | 45,648 | n/t | 5,124 |
  | 2022 | 6,298 | 7,008 | 3,425 | 7,522 | 3,859 | 14,023 | 53,607 | 51,354 | 5,970 |
  | 2023 | 6,929 | 8,588 | 4,060 | 7,660 | 4,086 | 15,681 | 62,564 | 60,429 | 6,740 |
  | 2024 | 6,485 | 8,442 | 3,773 | 9,193 | 5,453 | 18,226 | 72,907 | 71,431 | 8,404 |
  | 2025 | 7,737 | 10,566 | 4,609 | 9,560 | 5,554 | 19,000 | 85,035 | 83,224 | 10,401 |
  | 2026-06-30 | 5,611 | 11,291 | 5,047 | 9,498 | 5,466 | 24,643 | 91,771 | 92,226 | n/r |

  (n/t: not transcribed by the tool for that year; n/r: not read for that date. Capitalized customer incentives are the
  current and non-current "customer and merchant incentives" of the prepaid and other-assets notes: 10-Ks FY2017 Note 6,
  FY2020, FY2022, FY2024 Note 7, FY2025 Note 7; 2016 was $1,613M.)

  **What moved and why.** (1) Equity sits near $5B to $8B while retained earnings climbed from $22.4B to $85.0B: every dollar
  earned, and more, went out as buybacks and dividends (treasury stock $83.2B at 2025 year-end, $92.2B at mid-2026). (2) Debt
  tripled, $6.3B (2018) to $19.0B (2025) to $24.6B (mid-2026, after $5.0B of notes in June 2026), while cash rose only from
  $6.7B to $11.3B: the buybacks are partly borrowed. (3) Goodwill and intangibles grew from about $3.9B to $15.0B: the services
  business was partly bought. (4) Receivables held at 14% to 15% of net revenue (2018: $2,276M on $14,950M; 2025: $4,609M on
  $32,791M); nothing out of line with sales. (5) **The prepaid account the speakers name as a tell** **[M1995-064]**:
  capitalized customer incentives rose from $1,613M (2016, 15.0% of net revenue) to $10,401M (2025, 31.7%), 6.4 times while
  net revenue rose 3.0 times, and the first half of 2026 added $3,835M of prepaid cash against $2,238M a year earlier
  (10-Q Q2 2026, cash-flow statement). What the figures say: the network is paying more up front to win and keep issuers, and
  the income statement recognizes that cost over the contract lives (amortization $2,098M in 2025 against prepaid cash of
  $3,388M), so reported earnings run ahead of cash by roughly $1.3B a year at present. What they do not say: the filing
  explains the policy plainly (Note 1, "Fixed incentives [...] are generally capitalized and amortized over the life of the
  agreement on a straight-line basis"), the auditor names rebates and incentives as a critical audit matter, and the cash
  leaves through operating cash flow, which is the base used here. Read with the rest: an explained, visible build, not a
  hidden one; it is weighed, and the cash basis removes it from the earnings figure.
- **The real costs.** Depreciation and amortization ($1,143M) is matched by capital spending ($1,215M); software
  amortization is "very real" **[L2012-003]** and is not added back. Stock pay $597M (2025), $526M, $460M: deducted
  **[L2015-003]**. **Litigation, the recurring one-time item** **[L2016-007]**: provisions of $3M (2007), $2,483M (2008),
  $7M, $5M, $770M (2011), $20M, $95M, $0 (2014), $61M, $117M, $15M, $1,128M (2018, including the EC fine of €571M), $0 (2019),
  $73M, $94M, $356M, $539M, $680M, $504M (2025), and $82M in the first half of 2026 (10-Ks FY2009 to FY2025; 10-Q Q2 2026);
  cash paid for legal settlements $929M (2023), $496M (2024), $647M (2025). Seventeen of nineteen years carry a charge; over
  2007 to 2025 they total about $6.95B, about $0.37B a year, and about $0.57B a year in 2023 to 2025. The company
  excludes them as "Special Items" from its adjusted figures; this run counts them, through operating cash. Restructuring
  ($190M in 2024 by the difference between Special Items of $870M and litigation of $680M) is counted the same way.
- **EBITDA in the filer's own mouth**: no instance found in the 10-K FY2025 or the 2026 proxy (text search for "EBITDA").
- **The habits carried to Q5** (CONVENTION of 2026-10-06, section A): (a) **an adjusted figure featured** **[L2016-006]**: the 10-K's
  highlights page leads with "Adjusted net revenue", "Adjusted net income" and "Adjusted diluted EPS" (10-K FY2025 page 6);
  the July 2026 earnings release gives GAAP first and the adjusted figures beside them (8-K `0001141391-26-000081`, Exhibit
  99.1); (b) **beating expectations** **[L2002-041]**: the CEO's first sentence in that release is "We delivered above
  expectations"; (c) **targets made**: the pay plans set annual adjusted targets; the 2025 annual plan paid
  145% of target, but the PSU targets for 2024 and 2025 were missed (84.2% to 90.0% scores), so the record is not one of
  consistently reaching declared targets (proxy 2026, `0001141391-26-000021`). Recorded as a WEIGHING against **[M1994-018]**.
- **One check of the accounts against cash**: owner cash (operating cash less stock pay less capital spending) was
  $15,836M in 2025 against net income of $14,968M; over 2021 to 2025, $57.5B of owner cash before acquisitions against
  $57.7B of net income (10-Ks FY2022 and FY2025). Over five years cash and earnings run level once stock pay and capital spending are charged; the incentive prepayments
  are inside that cash figure.
- **The recast earnings for Q7**: owner cash = operating cash flow less stock pay less property and software spending less
  cash paid for businesses; for the all-equity basis, interest added back after tax at the 21% statutory rate. The
  equity-method convention does not arise (equity investments of $1,705M are carried at fair value or measurement
  alternative, losses of $88M in 2025, outside operating cash).
- **VERDICT on the accounts: no confusion and no suspicion; WEIGHS AGAINST** **[M1994-018]**. The accounts are clear and the
  key judgments are disclosed **[M1994-018]**; what weighs is the recurring litigation excluded from the featured figures, the
  growing gap between incentives paid and incentives expensed **[M1995-064]**, and the adjusted figure featured **[L2016-006]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet **[M2007-081]**; the reading here is the 10-Ks, the 2026 proxy,
the earnings release and the 8-Ks.
- **The first yardstick, the record against the hand dealt** **[M1994-008]**. Both open networks were dealt the same hand
  (bank-owned associations turned public companies, 2006 and 2008, the same regulation and the same merchant suits). Against
  Visa over 2009 to 2025: net revenue 6.4 times for Mastercard ($5.10B to $32.79B) against 5.8 times for Visa ($6.91B to
  $40.00B); operating margin up 13.3 points for Mastercard (44.3% to 57.6%) against 8.8 points for Visa (51.2% to 60.0%); the
  smaller network closed part of the gap while paying the higher incentive share. The services business was built and bought
  under the same managements. Present leadership: Michael Miebach, CEO since 2021; a new CFO (Ling Hai) and Chief Services
  Officer named in June 2026 from inside the company (8-K `0001141391-26-000037`); a new controller from inside (8-K
  `0001141391-26-000034`). Succession from within **[M2014-059]**.
- **The second yardstick, how they treat the owners** **[M1994-009]**: read at Q6, Part B (pay, board). The CEO's 2025 pay was
  $35.4M, against $30.1M (2024) and $25.7M (2023), 284 times the median employee (proxy 2026, `0001141391-26-000021`).
- **The tells of dishonesty, searched for in the documents read** (none of the following found): a proposition too good to be
  true **[M2007-091]**; reports that dance around the key figure **[M1995-111]** (the filings give GDV, cross-border volume,
  switched transactions, rebates and incentives, and each lawsuit with its claimed damages, year after year); a management
  fixed on its stock price in its reports **[M2004-067]**; owners as patsies **[L2001-002]** in the disclosures read. The
  legal note is long and specific, which is the candour **[L1994-023]** the rows ask for.
- **The habits carried from Q4**, read with the record **[M2013-088]**: the adjusted figures featured, with litigation that
  recurs every year excluded; "We delivered above expectations" in the July 2026 release; annual targets set on adjusted
  figures. Against them: GAAP comes first in the release; the long-term PSU targets were missed in 2024 and 2025 and paid
  below target on the financial measures (92.9% before the market modifier), which is not the record of a management that
  always reaches its declared numbers **[L2002-041]**.
- **The competition-law record, written down as found** **[M1997-127]**: the European Commission's 2007 decision on intra-EEA
  interchange (the basis of later damages suits); its January 2019 negative decision on the central acquiring rule with a
  fine of €571M (10-K FY2020); the U.K. Supreme Court's 2020 ruling against Mastercard and Visa on U.K. domestic interchange;
  the FTC's December 2022 complaint and consent agreement on Mastercard's compliance with the Durbin debit-routing rules,
  under the present CEO (10-K FY2022); the ACCC's 2022 complaint over debit agreements with Australian merchants, hearing on
  liability concluded June 2026, undecided (10-Q Q2 2026); a DOJ civil investigative demand on the U.S. debit program in 2023
  (10-K FY2025; no instance found in the legal notes of the 2026 10-Qs by text search for "Department of Justice"). These are
  findings and charges about how the network prices and routes against merchants and rival networks, disclosed in full. I
  read them as evidence on how the money is made (Q12's question) and on legal cost (Q4, Q9), not as evidence that the
  people deceive their partners; the rows' integrity test is whether one can count on the people "to behave in the future
  [...] as they behaved in the past" with the owners **[M2015-005]**, and the filings show no deception of owners. The FTC
  consent under the present management is the nearest thing to doubt in the record, and it is a regulator's finding about a
  routing practice, settled by changing it.
- **Love of the business** **[M2000-098]**: not readable for a hired management from these documents beyond tenure (the CEO
  and the new CFO are long-serving insiders) and the ownership requirements (6x salary for the CEO, all NEOs compliant,
  proxy 2026). Frequent Form 4 and Form 144 filings since July 2026 show routine insider sales (filings list of 2026-10-09);
  not read one by one.
- **VERDICT on integrity: IN** **[M2013-088]** read against the filings: no tell of dishonesty toward owners found; the
  competition-law record is recorded above and carried to Q9 and Q12. **Ability WEIGHS FOR** **[M1994-008]**: the record
  against the stronger rival, with the same hand, is better on growth and on margin gained.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**. Mastercard keeps almost nothing: over 2021 to 2025 it paid out
  $57.4B in buybacks and dividends (buybacks $5,904M, $8,753M, $9,032M, $10,954M, $11,727M; dividends $1,741M, $1,903M,
  $2,158M, $2,448M, $2,756M) against owner cash after acquisitions of $50.2B, 114%, the difference borrowed (debt $13.9B to
  $19.0B), and in the first half of 2026 $10.5B of buybacks and dividends against $6.8B of operating cash, with $5.6B of new
  debt (10-Ks; 10-Q Q2 2026). What it does keep goes into incentive prepayments, software and acquisitions, which Q3 found
  earn very high returns in the network and unproven returns in the bought services. The rows say a business that cannot use
  its earnings should pay them out **[M2008-104]**, and this one does.
- **Buybacks** **[L1999-023]**, **[L2011-003]**. Board authorizations are in dollars with no stated price ceiling ($11.0B,
  $12.0B, $14.0B in 2023 to 2025; 10-K FY2025 Note 14) **[L2016-002]**. Average prices paid (10-Ks, split-adjusted for the
  10-for-1 split of 2014): $25.89 (2011), $43.07 (2012), $59.78, $76.14, $91.70, $95.18, $125.05 (2017), $188.26, $245.89,
  $312.68 (2020), $356.82, $340.60, $379.49, $475.35, $555.78 (2025); about $513 in the first half of 2026 (17.6M shares for
  $9,034M, 10-Q Q2 2026); $81.8B spent 2011 to 2025. **The convention's test** (the buyback with no stated price, read against
  the bottom of the Q7 range, run when Q7 is reached and recorded here): the bottom of today's Q7 range is $196.74 a share
  (all-equity, Q7 below); every purchase since 2019 was made above it, and the 2025 and 2026 purchases ($556, about $513) sit
  near or above the midpoint of the literal range ($499.20). They are not "below its intrinsic value, conservatively-calculated"
  **[L1999-023]**. The purchases of 2011 to 2017 were made at prices far below today's quotation and were, read by what they
  did, good for the continuing owners; the convention reads them against the range, and the range is today's. In 2026 the
  buying is partly financed by debt; and a pay plan that rewards a buyback whatever its price **[M2016-049]**, **[M2006-041]**
  is what the proxy describes: the PSU targets take in "an initial assumption for share buybacks" (proxy 2026). **Weighs
  against.**
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**. Acquisitions are paid in cash: $10.9B for businesses 2016 to 2025
  (Recorded Future $2.7B in 2024; $4.4B in 2021), BVNK $1.5B agreed in 2026. No all-stock deal: **the Part A STOP does not
  arise** **[L2009-019]**. No serial issuance: diluted weighted shares fell from 1,260M in 2012 (126.0M before the 10-for-1 split of 2014) to 906M in
  2025 (10-K XBRL), and the cover count is 876M today. Value got
  against value given cannot be read: the bought businesses' earnings are not filed separately; services grew 23% in 2025
  with 3 points from acquisitions. Undecided.
- **Dividends** **[L2012-015]**: raised every year read ($2.37, $2.74, $3.15 a share declared 2023 to 2025; $0.87 a quarter in
  2026), about a sixth of owner cash; clear and consistent.
- **Part A WEIGHS AGAINST**: the money is returned, as the retention test asks, but returned through buybacks at prices above
  any conservative value and partly with borrowed money **[L2011-003]**.
### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**. The annual plan pays on adjusted net income (67%) and adjusted net
  revenue (33%); the adjustments exclude "litigation judgments and settlements", a cost incurred in seventeen of nineteen
  years and produced by the company's own conduct; 2025 paid 145% of target before the reserve (proxy 2026, pages 67 to 68).
  "you get what you reward for" **[M2016-083]**: management is paid as if the antitrust bill did not exist. The PSUs (60% of
  long-term pay) run on three one-year adjusted revenue and adjusted EPS growth targets, with EPS targets that assume
  buybacks, modified by total return relative to the S&P 500 **[M2000-062]** (relative, which removes the market's ride in
  part). Stock options (ten-year term, no step-up) are still granted **[L1994-021]**, **[M1997-043]**.
- **How they treat themselves against the owners** **[M1994-009]**: CEO pay $35.4M in 2025, up 38% in two years. The ratchet
  the rows name **[L2005-015]**, **[M2012-095]** is in the proxy's own words: "Total compensation is established within a range
  around the median of market-competitive levels", with an outside consultant retained (proxy 2026). No hedging or pledging, no gross-ups, no
  repricing, a one-year post-vest hold on PSUs, ownership requirements met (proxy 2026): the better half of the ledger.
- **The board** **[M2007-120]**: an independent chair (Merit Janow) separate from the CEO **[L2014-026]**; ten of eleven
  nominees independent; non-employee directors paid about $370,000 to $615,000 a year, mostly in stock (proxy 2026). Whether
  directors bought shares with their own savings **[L2019-008]**: not found in the documents read.
- **The owners as partners** **[L1994-023]**: the 10-K is detailed and plain on volumes, incentives and litigation; the
  featured adjusted figures cut the other way (Q4).
- **Part B WEIGHS AGAINST**: the pay formula excludes a recurring real cost and rewards buybacks at any price
  **[M2016-083]**, and its level is set by peer medians **[L2005-015]**; the board structure is sound.
- **Q6: WEIGHS AGAINST** on both parts; no STOP.

## Q7 — WHAT IS IT WORTH? STOP.
Arithmetic in `Test Runs/_research 2026-10-10 MA/q7.py` (inputs from the filed cash-flow statements: 10-Ks FY2020, FY2022,
FY2024, FY2025; interest paid from the 10-K FY2025 debt note for 2023 to 2025, interest expense for 2019 to 2022).
- **The cash input** (Q4's recast; USD millions; all-equity = equity-only plus interest after tax at 21%):

  | year | operating cash | stock pay | capital spending | cash paid for businesses | owner cash, equity-only | owner cash, all-equity |
  |---|---|---|---|---|---|---|
  | 2021 | 9,463 | 273 | 814 | 4,436 | 3,940 | 4,280 |
  | 2022 | 11,195 | 295 | 1,097 | 313 | 9,490 | 9,862 |
  | 2023 | 11,980 | 460 | 1,088 | 0 | 10,432 | 10,809 |
  | 2024 | 14,780 | 526 | 1,194 | 2,511 | 10,549 | 11,000 |
  | 2025 | 17,648 | 597 | 1,215 | 0 | 15,836 | 16,373 |
  | **five-year average** | | | | | **10,049** | **10,465** |

- **The specifics applied** (Q7, six specifics, CONVENTION). (a) Cycles: the series that defines the cycle is owner cash; 2021,
  the first window year, is not a trough in it (owner cash before acquisitions $8,716M all-equity, above 2019's $7,382M and
  2020's $6,562M), though the filer describes cross-border volume as still recovering; the literal window is used, and the
  2019 to 2025 span is shown beside. (b) Decline: none. (c) Acquisitions: deducted (the five-year average carries $7.3B of
  them), and the total growth is credited, measured on owner cash before acquisitions, aggregate not per share: $8,716M (2021)
  to $16,373M (2025) all-equity, **17.1% a year** (17.3% equity-only). The organic pair is shown beside; the filer reports
  organic growth only for revenue (acquisitions added 1 point in 2025, none in 2024), so the pair takes growth one point
  lower (CONVENTION of this run: the only organic measure the filer gives). (d) Working capital: inside operating cash. (e)
  Growth spending: the filer gives no maintenance split and capital spending is about equal to D&A, so no maintenance-only
  case can be separated; the all-spending case is central and the D&A basis is shown beside. The growth spending that
  matters (incentive prepayments, acquisitions) is already charged. (f) The cap: 17.1% for ten years, then zero nominal
  growth at the sovereign; not above the shown rate. Net debt $14,534M (Step 0, including BVNK).
- **Value range, all-equity (central)**: no-growth case $186.9B for the business, **$196.74 a share**; shown-growth case
  $716.8B, **$801.66 a share**; top over bottom **4.07**. **Equity-only beside**: $204.86 to $797.34 (3.89).
  **Beside it**: the 2019 to 2025 span (base $9,120M, growth 14.2%): $169.32 to $554.31 (3.27); the D&A basis: $201.19 to
  $808.18; the organic pair (base before acquisitions $11,917M, growth 16.1%): $226.33 to $846.01. Price **$589.14**.
- **The floor** (CONVENTION, about ten percent, after the company's own tax, no conversion; Whose tax): the expected return at
  $589.14 on the all-equity basis (enterprise value $530.6B) is **1.97%** in the no-growth case and **7.15%** in the
  shown-growth case, the top of the range (equity-only 1.95% and 7.16%). Ten years of growth at about **23% a year** would be
  needed for the five-year average to earn ten percent at this price. **No case in the range clears the floor.**
- **Fair price (a reporting figure, never a verdict; Part VII)**: the price at which the midpoint of the range earns the floor,
  computed as the average of the two end cases' cash streams valued at 10% (a definition stated for this run; the reporting
  convention does not say whether "the midpoint" is the midpoint value or the midpoint stream): **$240.00 a share
  all-equity (central)**, **$248.96 equity-only**; on the 2019 to 2025 span $175.50. No cheap price is reported.
- **How it closes.** By width alone the range is wider than about three to one (4.07 central; 3.27 on the longer span) and
  "the range must be so wide that no useful conclusion can be reached" **[L2000-025]** would send it to TOO HARD. But here a
  useful conclusion is reached at every point of the range: even the shown-growth case returns 7.15% at the price, below the
  floor at which "we drop out of the game" **[M2003-149]**. The framework's own specifics close a price above the top of the
  range OUT "however wide the range, by the floor convention", "the expected return at the price then being below the
  minimum" (Q7, the PG specifics and specific (f)); the same reason holds when the price is inside the range but above what
  every case in it is worth at the floor. The case is not close: it needs no pencil to see that $589 is nowhere near far
  enough below a range whose bottom is $197 **[M2009-005]**, **[M1996-084]**. The width is the cause I set aside, and the choice is
  confessed under "What in the framework was wrong or unclear".
- **Q6's buyback test, recorded back**: the bottom of the range, $196.74, is below every price paid since 2018 (Q6).
- **VERDICT: OUT** at the floor **[M2003-149]**: valued, and the price does not clear the minimum return in any case of the
  range; "You can turn any investment into a bad deal by paying too much" **[M2019-015]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7 (the floor)**: value range $196.74 to $801.66 a share (all-equity, central; equity-only $204.86 to $797.34)
against $589.14; expected return at the price 1.97% to 7.15% across the range, below the floor of about ten percent; fair
price $240.00 all-equity, $248.96 equity-only. Q1 IN, Q2 IN, Q3 weighs FOR, Q4 accounts IN weighing against, Q5 integrity
IN with ability weighing FOR, Q6 weighs AGAINST. Integrity facts recorded (the competition-law record at Q5), judged IN at Q5.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]***.)*
- **Q8, the bond:** the all-equity owner-cash yield at the price is $10,465M over $530.6B, 1.97%, against the 30-year Treasury
  at 5.60% (2026-10-09).
- **Q9, debt:** total debt $24,643M at 2026-06-30 (senior notes; $710M commercial paper; the 2026 notes carry no financial
  covenants), cash $11,291M; operating income $18,897M against interest expense $722M in 2025, about 26 times (10-K FY2025;
  10-Q Q2 2026). A committed $8B revolving facility to 2030 backs the commercial paper and is meant in part for "liquidity in
  the event of one or more settlement failures by the Company’s customers" (10-Q Q2 2026, debt note).
- **Q9, sudden demands:** Mastercard guarantees settlement between its customers; gross settlement exposure $89.6B, net of
  collateral and other mitigation $72.9B at 2025 year-end, "short-term and generally limited to a few days", with "a low level
  of losses" historically (10-K FY2025 Note 20), against equity of $7.7B. Certain indemnifications "do not provide a stated
  maximum exposure" (same note).
- **Q9, litigation still open (10-Q Q2 2026, Note 14):** Block and Intuit, opt-outs, "aggregate single damages in excess of
  $5 billion"; two other opt-outs above $250M, trial September 2026; a putative class filed April 2026 for U.S. credit
  interchange since 2019, which Mastercard and Visa say the 2018 release bars; the U.K. commercial-card collective action,
  more than £1B; U.K. and Pan-European merchant claims of over £0.5B; Portugal consumers €0.4B (trial October 2026); the
  Netherlands €0.3B; the ATM operators class, more than $1B single damages against both networks; the ACCC case. Under the
  2011 sharing agreements Mastercard pays 12% of a global MDL settlement, 36% of one involving only Mastercard and its
  issuers (10-K FY2025 Note 19).
- **Q12, how the money is made:** the competition-law record listed at Q5 (EC 2019 fine €571M; U.K. Supreme Court 2020; FTC
  consent 2022 on debit routing; ACCC pending). No business of the kinds the rows name (casinos, tobacco, loading schemes) is
  in the filings read; the company enables crypto co-brand cards and stablecoin flows (10-K FY2025, about 130 crypto
  co-brand programs), a subject the rows touch at **[M2022-078]**; not weighed.
- **Q10:** nothing beyond the box.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): Step 0,
      Q1, Q2, Q3, Q4, Q5, Q6, Q7 with the box each in its own pathspec commit. (The file was copied from the template and its
      skeleton replaced section by section as each closed; the template's headings are kept.)
- [x] Dispatched: the brief allowed the per-question commits; the lock in `Screens/_daily/` was the dispatching session's,
      present throughout, never touched. No git lock was met. The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; `Test Runs/` was never listed; what
      was seen by accident is declared under contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row
      (`Test Runs/_research 2026-10-10 MA/check_quotes.py`, PASS); every filing fact carries its accession or the filing it
      came from; no number without a filing or a CONVENTION.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 are NOT REACHED; nothing after it
      is a clearance.
- [x] Owner cash after every real cost from operating cash (stock pay, capital spending, acquisitions deducted), never a
      net-income proxy; the sovereign from the U.S. Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (foundations, Q2, Q4, Q5); the facts for later questions are under AFTER THE
      STOP.
- [x] No point-in-time anchor: the run is dated today and cites rows of any year.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yields, growth figure and stale weighted share count were not.
- [x] `python tools/check_framework.py` PASS before the final commit (2026-10-10); `check_quotes.py` PASS (92 ids).

**Known weaknesses, stated.** (1) Interest for 2021 and 2022 in the all-equity owner cash is the expense, not the cash paid
(not found in the 10-Ks read); the effect is under $0.1B a year. (2) The capitalized-incentive series has gaps (2018 not
read). (3) The DOJ matter's status in 2026 is inferred only from its absence in the 2026 10-Qs. (4) Directors' own share
purchases were not traced. (5) Visa, AmEx and PayPal figures before FY2013 come from XBRL as transcribed, cross-checked only
where a 10-K was opened (Visa FY2015 and FY2025, AmEx FY2025, PayPal FY2025, Discover FY2024, Capital One FY2025).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7's two closes collide.** The range convention closes TOO HARD when the top exceeds about three times the bottom and
OUT only when the range is narrower; specific (f) and the PG specifics close OUT "however wide the range" when the price is
above the top, because the expected return is then below the floor. Neither sentence covers a price inside a wide range that
fails the floor in every case of the range (here 1.97% to 7.15% against about ten percent). I closed OUT on the floor,
because the reason the rows give for TOO HARD, that "no useful conclusion can be reached" **[L2000-025]**, does not hold
when every case gives the same answer; a reader who applies the width test first gets TOO HARD (NATURE or WORK unnamed by
the text). The framework should say which test runs first. (2) **The no-growth bottom makes a three-to-one range almost
impossible for any business that has grown faster than about 14% a year at a 5.6% rate**, so the width test sends every fast
grower to TOO HARD by construction, whatever is known about it. (3) **"The midpoint of the range" in the fair price** is not
defined as a value or a cash stream; I used the average of the two end streams valued at 10% and said so. (4) **Rows on
competition-law conduct have no stated home**: the findings against a company's pricing and routing practices could be read
at Q5 (integrity), Q9 (legal exposure) or Q12 (how the money is made); I recorded them at Q5, judged them there, and carried
them to Q9 and Q12. (5) **The template's Step 0 line on `tools/run.py`** asks for "owner cash after every real cost", but the
tool omits acquisitions and interest; the series had to be rebuilt by hand at Q4. (6) **The brief's error**: its lines of
evidence name "the DOJ debit case" as a Mastercard litigation provision. The Department of Justice's debit monopolization
suit was filed on 2024-09-24 against Visa, not Mastercard (V 10-K FY2025, `0001403161-25-000089`, legal note); Mastercard
received only a civil investigative demand on its U.S. debit program in 2023 (10-K FY2025 Note 19), with no provision, and the
matter is not listed in the legal notes of its 2026 10-Qs. The brief's Discover line ("acquired by Capital One in 2025;
check") is correct: closed 2025-05-18 (COF 10-K FY2025).
