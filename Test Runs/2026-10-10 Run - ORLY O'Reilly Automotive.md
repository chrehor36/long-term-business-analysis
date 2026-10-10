# Company Run — O'Reilly Automotive, Inc. (NASDAQ: ORLY) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md` (operator rule 10). Research folder:
`Test Runs/_research 2026-10-10 ORLY/` (raw filings in its `cache/` subfolder, gitignored).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Contamination, declared:** the dispatching message said there are earlier run files about O'Reilly; I did not open,
list or search them, and do not know their dates, boxes or contents. The git status shown at session start lists two
other 2026-10-10 run files by name (MA Mastercard, MSA MSA Safety) and the recent commit subjects name LOW, LOPE, LRCX and
LSTR runs with their boxes; none bears on this company and none was opened or used. The project memory index (loaded
automatically) carries a line on queue state and "57 gate-clearers, nothing buyable"; it names no company and was not used. At the close, a `git log` to confirm my own commit showed the subjects of
other same-day commits (MSA, MA and NDSN runs, with their boxes and figures); seen after this run's Q7 was written and
committed, and not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $86.45 (close 2026-10-09; `tools/run.py` live quote, **aggregator, flagged** per operator rule 5). The price is
  post-split: the board approved a 15-for-1 split as a stock dividend on 2025-03-12, distributed after the close on
  2025-06-09, trading split-adjusted from 2025-06-10 (8-K filed 2025-03-13, accession 0000898173-25-000010). All per-share
  figures below are on the post-split count.
- **Shares by class:** one class, common stock $0.01 par. Cover of the 10-Q for the quarter to 2026-06-30: **808,960,792
  shares outstanding as of 2026-08-03** (10-Q filed 2026-08-07, accession 0000898173-26-000045). `Screens/cover_shares.py`
  parsed no cover count ("read the filing by hand"); read by hand. Check against issued less treasury: the balance sheet
  shows 816,165,813 shares "issued and outstanding" at 2026-06-30 and 841,909,238 at 2025-12-31; the company carries no
  treasury stock (repurchased shares are retired, the issued and outstanding counts are one line). The fall of 7.2 million
  shares from 30 June to 3 August is consistent with the continuing open-market repurchases (Q6). No 8-K or prospectus
  after the 10-Q changes the count (8-Ks of 2026-08-11 and 2026-08-14 are a debt offering; 2026-10-01 is an earnings-date
  notice, accession 0000898173-26-000048).
- **Market cap:** 808.961M x $86.45 = **$69,935M**.
- **Net debt at the latest filed balance sheet (2026-06-30):** long-term debt $7,014.5M (senior notes plus $1,345.0M of
  commercial paper, all carried as long-term) less cash $262.2M = **$6,752.4M**. Operating leases ($2,120.6M non-current plus
  $452.3M current) are left out, and said so (Q7, On what the floor is earned). Subsequent event not stated in that filing:
  $1.6B of new senior notes (4.800% 2029 $700M, 5.050% 2031 $500M, 5.550% 2037 $400M) issued 2026-08-14 (8-K accession
  0001104659-26-097090), proceeds "to repay a portion of amounts outstanding under its commercial paper program" and
  general purposes (8-K 2026-08-11, accession 0001104659-26-094110); refinancing, roughly neutral to net debt until spent;
  not added, because the 10-Q does not state it.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-27, accession 0000898173-26-000009); 10-Q for the
  quarter to 2026-06-30 (filed 2026-08-07, accession 0000898173-26-000045); proxy DEF 14A (filed 2026-03-27, accession
  0000898173-26-000014); 8-Ks of 2026-06-01 (buyback authorization, 0000898173-26-000033), 2026-07-10 (officer, 0000898173-26-000039),
  2026-07-29 with its earnings release (0000898173-26-000042), 2026-08-11 and 2026-08-14 (notes), 2026-10-01; the 10-Ks for
  FY2007 (0000898173-08-000015), FY2008 (0001193125-09-041373), FY2009 (0001193125-10-043016), FY2010 (0001193125-11-049998),
  FY2012 (0000898173-13-000006), FY2014 (0000898173-15-000076), FY2016 (0000898173-17-000091), FY2017 (0000898173-18-000077),
  FY2019 (0000898173-20-000007), FY2020 (0000898173-21-000012), FY2021 (0000898173-22-000012), FY2022 (0000898173-23-000011),
  FY2023 (0000898173-24-000009), FY2024 (0000898173-25-000008).
- **One figure cross-checked against the filed statement:** inventory at 2025-12-31, XBRL $5,731M; the filed consolidated
  balance sheet of the FY2025 10-K prints "Inventory | 5,731,385" (thousands). Agrees. Also checked: net cash from operating
  activities FY2025, XBRL $2,762M against the filed cash-flow statement "2,761,993". Agrees.
- `python tools/run.py ORLY`, arithmetic lines only (each checked against the filed cash-flow statement of the FY2025
  10-K for 2023 to 2025):

  | FY | OCF | SBC | D&A | capex | OCF - SBC - capex | OCF - SBC - D&A |
  |---|---|---|---|---|---|---|
  | 2021 | 3,207 | 25 | 328 | 443 | 2,739 | 2,854 |
  | 2022 | 3,148 | 26 | 358 | 563 | 2,559 | 2,764 |
  | 2023 | 3,034 | 28 | 409 | 1,006 | 2,000 | 2,597 |
  | 2024 | 3,050 | 29 | 462 | 1,023 | 1,998 | 2,559 |
  | 2025 | 2,762 | 35 | 511 | 1,169 | 1,558 | 2,216 |
  | 5-yr mean | | | | | **2,171** | **2,598** |

  USD millions. The tool's statement-line scan found no securities inside operating cash, no other stock-pay line, no
  intangible or software payment beside capex. Its own warning: the 3-year and 5-year windows differ by 17%. OCF is moved
  year to year by "the timing of payment for transferrable federal renewable energy tax credits" (FY2025 10-K, MD&A,
  operating activities; the same phrase in the FY2023 and FY2024 10-Ks), and income taxes paid were $315M, $640M and
  $1,068M in 2023, 2024 and 2025 against provisions of $658M, $658M and $702M (XBRL, IncomeTaxesPaid; tax expense):
  the cash series swings with tax timing that the five-year mean mostly but not wholly averages out (Q4, Q7).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the share as a business: the question is whether I would "be happy buying this stock
if the market closed for five years" **[M1997-109]**, and for a parts retailer the answer rests on the cars on the road, not
on the quote. The second is the margin of safety: a share that has compounded for decades and trades at a high multiple of
its owner cash invites the pencil, and "if you have to actually do it on — with pencil and paper, it’s too close to think
about" **[M1996-084]**. No macro view enters: "macro conclusions are — just never enter into the discussion" **[M2000-094]**;
the 30-year Treasury at 5.60% is used as the yardstick at Q7, not as a forecast. Who is paid to tell me: the company issues
annual guidance and the sell side follows it (Q4, Q5). The analyst's habit applied: the writer has an incentive to find this
famous compounder good, so contrary evidence is written down as found, in its own section below, and the scuttlebutt that
is on the public record (the competitors' filings) is aimed "to possibly reject your original hypothesis" **[M1998-144]**.
**Contrary evidence, written down as found** **[M1997-127]**:
1. Owner cash after all capital spending fell from $2,739M (2021) to $1,558M (2025) while operating income rose; capital
   spending more than doubled in 2023 (Step 0 table). Written before reading the reasons.
2. Shareholders' equity went from +$2,686M (2009) to -$1,836M (2026-06-30); retained earnings negative since 2017; long-term
   debt from $684M (2009) to $7,015M (2026-06-30). The return on equity is therefore meaningless and the buyback is
   debt-assisted.
3. Accounts payable ($7,104M) exceed inventory ($5,731M) at 2025-12-31, and $5.1B of those payables sit in supplier finance
   programmes run by third-party banks (10-Q 2026-06-30, accession 0000898173-26-000045, note on supplier finance programs):
   the working capital the business does not fund is funded by its suppliers' banks, which can withdraw.

## THE STANDING RULE
The rule binds the buyer: "We are never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in this run
contemplates a purchase on borrowed money or at a size that could force a sale; the name's own debt is the target's and is
weighed at Q9, not here. No breach found.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The business, from the FY2025 10-K (accession 0000898173-26-000009).** A specialty retailer and distributor of
replacement parts, tools, supplies and accessories for cars and light trucks: 6,585 stores at 2025-12-31 (6,447 in 48 US
states and Puerto Rico, the rest in Mexico and Canada; 6,695 at 2026-06-30 per the 8-K of 2026-10-01), served by 32 DCs
carrying on average over 156,000 SKUs and 399 Hub stores carrying on average 63,000 SKUs; "More than 95% of our stores
receive multiple same-day deliveries". Sales split about 50% DIY and 50% professional service providers in 2025. One
reportable segment. No financial book, no holding-company parts.

**The test: "a reasonable fix on about what the earning power and competitive position will look like in five or 10
years"** **[M2012-065]**.
- *The key variables and how predictable they are* **[M1998-044]**. The filer names them: "the number of miles driven,
  number of registered vehicles, annual rate of light vehicle sales, and average vehicle age" (10-K FY2025, MD&A). Its own
  figures: miles driven up 2.1%, 1.0% and 0.9% in 2023 to 2025; registered light vehicles up 13.4% from 2014 to 2024, to
  286 million; scrappage "relatively stable, ranging from 4.1% to 5.6% annually"; average age from 11.4 years (2014) to 12.6
  years (2024). These are stocks of cars that change by a few percent a year. They are measurable and they move slowly.
- *Do the past statements tell me the future ones?* **[M2008-033]**. The record says they have. Comparable store sales
  were positive in every year read: 2006 3.3%, 2007 3.7% ("same store sales", 10-K FY2007, which also states "fifteen
  consecutive years of record revenues, positive comparable store sales results and earnings growth since becoming a public
  company in April 1993"); 2008 1.5% consolidated (O'Reilly systems 2.6%, the acquired CSK stores negative); 2009 4.6%;
  2010 8.8%; 2011 4.6%; 2012 3.8%; 2013 4.3%; 2014 6.0%; 2015 7.5%; 2016 4.8%; 2017 1.4%; 2018 3.8%; 2019 4.0%; 2020 10.9%;
  2021 13.3%; 2022 6.4%; 2023 7.9%; 2024 2.9%; 2025 4.7%; first half 2026 7.0% (10-Ks FY2007 to FY2025 and the 10-Q to
  2026-06-30, each "comparable store sales ... increased" sentence; accessions in Step 0). The two hardest tests in the span,
  the 2008-09 credit crisis and the 2020 lockdowns, both show positive comps. Operating margin went from 9.4% (2008, the CSK
  year) to 19.0% by 2015 and has held between 18.9% and 21.9% for the eleven years since (Q2 table).
- *Would the insiders write the forecast down?* **[M2000-105]**. They do: AutoZone's 10-K names "miles driven and the number of
  seven-year-old or older vehicles on the road" as "the two statistics we believe have the closest correlation to our market
  growth over the long-term" (FY2025, accession 0001104659-25-102611; the same sentence in FY2010, 0000950123-10-095687),
  Advance's 10-K names miles driven (FY2025, 0001193125-26-051305), and the filer states a multi-year store-opening and DC plan (Lakeland expansion
  2026, a Fort Worth DC in 2028). This is not an industry whose participants call the ten-year picture "too hard".
- *Is the forecast about customers or about technology?* **[M2023-030]**. Mostly about customers and a stock of cars: does
  a worn part on an aging vehicle get replaced, and from whom. The technology question is the vehicle itself, which the
  filer names as a risk: "Changes in vehicle technology used by the original equipment manufacturers ('OEM') on future
  vehicles, including but not limited to electric, hybrid, and internal combustion engines, may result in less frequent
  repairs, parts lasting longer, or elimination of certain repairs." (10-K FY2025, risk factors.)
- *How far off could I be over ten years?* **[M2011-084]**. The electric-vehicle question bounded with the filer's own
  figures, not a forecast: at the stated scrappage band of 4.1% to 5.6% a year, between about 50% and 60% of today's 286
  million vehicles would still be on the road ten years on (0.944^12 to 0.959^12 over the 2024-to-2036 span; my arithmetic
  on the filing's figures). Even in the extreme case that every new vehicle sold from now on were electric, at least half of
  the fleet in ten years would be today's combustion vehicles, and they would be the oldest, out-of-warranty vehicles that
  the filer says "generate strong demand for automotive aftermarket products". The ten-year earning power is therefore
  bounded on the downside by a fleet already built. The twenty-year picture is less sure, and that is Q2's question
  (Change, and what it does to a castle).
- *Can I name the winner, not just the industry?* **[M2012-067]**. The filings name them: over 2008 to 2025 O'Reilly and
  AutoZone hold high and stable margins, Advance Auto Parts has fallen to losses and Genuine Parts' automotive segment earns
  a fraction of their margin (Q2 competitor row). The industry is not one whose winners are unknown.

**Contrary evidence, written down as found** **[M1997-127]**. The rows warn about retail by name: "it’s easy to sort of think
you understand retail, and then subsequently find out you don’t" **[M2014-052]**; "If we’re looking at some retail business
or something, we would not have the same degree of conviction at all" **[M2012-091]**; "what would bother me is if I think I
understand a business and I don’t" **[M1997-024]**. And the doubt rule: "if you have doubts about something being into your
circle of competence, it isn’t" **[M2002-092]**. Against these, the same doubt row continues "You can certainly understand
Walmart. [...] You can understand Costco." **[M2002-092]**: the speakers do not put retail as a class outside the circle;
they warn against the illusion. The test that separates the two is whether the earning power and position can be foreseen
**[M2012-065]**, and the evidence above (thirty-three years of positive comps through two severe shocks, a demand stock that
the filer measures and that moves by a few percent a year, named winners) is the evidence the rows ask for, not a feeling of
familiarity. The doubt that remains is about the twenty-year mix of the fleet, not about the ten-year economics, and the
framework routes it to Q2.

**Routing.** Not a business of rapid change at the ten-year horizon on the evidence above (the fleet turns over at about
5% a year). Not a bank, not a holding company.

- **VERDICT: IN.** The key variables are named, measured and slow-moving **[M1998-044]**, the statements have told the
  future for three decades **[M2008-033]**, and the winners are visible in the filings **[M2012-067]**; the electric-vehicle
  question is "important and knowable" **[M2006-076]** at ten years and is carried to Q2 for the twenty.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**.

**What the castle is, on the filings.** Not a brand in the consumer's sense: the product is mostly other people's branded and
private-label parts. The castle the filer describes is availability: a store within reach, the right part for that vehicle
on the shelf or delivered the same day, and a parts person who can find it. Its physical form is the tiered network: 32 DCs
averaging over 156,000 SKUs, 399 Hub stores averaging 63,000 SKUs (up to about 115,000), 6,585 stores averaging about 24,000
SKUs, and "More than 95% of our stores receive multiple same-day deliveries" (10-K FY2025). The Hub count was 240 in 2012,
312 in 2016, 356 in 2019, 385 in 2023 and 399 in 2025 (the 10-Ks of those years). The filer itself says the business "is
highly competitive" on "customer service, product availability, store location, brand recognition, and price".

**The tests, each with its filing fact.**
1. *Key factors and how permanent* **[M1995-038]**. Availability through density, built over decades and paid for in
   inventory and DCs. Permanence is tested below by the attacker, by the price, by volume and by the rivals' record.
2. *Would it stand without the lord?* **[L2007-006]**, **[M1996-037]**. Contrary evidence first: the rows single out this
   trade, "For a retailer, hiring that nephew would be an express ticket to bankruptcy" **[L1995-009]**, and "In retailing,
   to coast is to fail" **[L1995-008]**; Advance Auto Parts is the case in the field (below). For it: the results did not
   depend on one person. Three chief executives since 2005, each promoted from the stores (Henslee from 2005, 10-K FY2009;
   Johnson from 2018, 10-K FY2019; Beckham, "29 years" an O'Reilly team member, CEO "since 2024", 10-K FY2025), and the
   operating margin held between 18.9% and 21.9% across both successions. The castle needs steady, competent operation
   **[L2005-010]**; it has not needed a superstar. Weighed as a qualification, not a fail.
3. *The attacker with money* **[M2011-015]**. The field has had well-funded attackers and the record shows what they did.
   Advance Auto Parts, a national chain, "acquired General Parts International, Inc" in 2014 (its 10-K FY2025) (its sales went from $6,494M to $9,844M
   that year, XBRL from its 10-Ks) and has since fallen from a 10.8% operating margin (2011) to 1.0% (2023), -7.8% (2024)
   and -0.5% (FY2025) (AAP 10-K FY2025, accession 0001193125-26-051305; XBRL). Amazon has sold parts online through the whole
   span; its own 10-K reports no automotive line (AMZN 10-K FY2025, accession 0001018724-26-000004: the word "automotive"
   appears only for its Rivian investment), so no metric of its parts business exists in its filings: **flagged**. Over the
   same years O'Reilly's comps never turned negative and its margin rose (Q1, table below). "one competitor is frequently
   enough to ruin a business" **[M2012-108]**: no competitor has done it here; AutoZone is the one that matches it.
4. *Pricing power and the agony before a rise* **[M2005-020]**, **[M2005-017]**. Through the 2021 to 2023 inflation and the
   2025 tariffs the filer passed costs on: "Average ticket values benefited from increases in average selling prices on a
   same-SKU basis [...] driven by increases in acquisition costs of inventory, principally resulting from increased tariffs,
   which were passed on in selling prices" (10-K FY2025); "we have typically been able to pass along these cost increases
   through higher selling prices" (10-K FY2022, FY2023, FY2025; 10-Q 2026-06-30). The gross margin held: 52.7% (2021), 51.2%
   (2022), 51.3% (2023), 51.2% (2024), 51.6% (2025), the dip of 2022 explained by the filer as mix toward professional sales
   and the prior year's benefit of selling through cheaper inventory. Comps stayed positive while prices rose: charging more
   while keeping share **[M2000-031]**.
5. *Unit volume and share of mind* **[M1999-054]**. Positive comps every year 2006 to 2025 (Q1). Sales grew 2.46 times from
   2014 ($7,216M) to 2025 ($17,782M), against 2.0 times at AutoZone ($9,475M FY2014 to $18,939M FY2025) and a fall at
   Advance (XBRL from each filer's 10-Ks). AutoZone's domestic comps were 0.4%, 0.1%, 0.4% in its fiscal 2006 to 2008 against
   O'Reilly's 3.3%, 3.7%, 1.5% (2.6% on O'Reilly systems), and 3.4%, 0.4%, 3.2% in its fiscal 2023 to 2025 against O'Reilly's
   7.9%, 2.9%, 4.7% (AZO 10-K FY2010 and FY2025). The professional share rose from 41% (2012) to 50% (2025) (10-Ks).
6. *The low-cost position* **[L1996-015]**, **[M2004-091]**. Scale in buying is in the filing: "historically we have been
   successful in reducing the effects of merchandise cost increases, principally by taking advantage of supplier incentive
   programs, economies of scale resulting from increased volume of purchases, and selective forward buying" (10-K FY2025).
   The strongest single sign of bargaining power over suppliers is the balance sheet: accounts payable were 43% of inventory
   in 2009 and 124% in 2025 ($818M against $1,913M; $7,104M against $5,731M; XBRL from the 10-Ks), so suppliers now finance
   all of the inventory and more. (Its fragility is Q9's question.) A low-cost producer "of something that’s essential to
   people" **[M2004-091]**: a failed part on a car used to get to work is close to essential.
7. *The brand* **[M2001-090]**. Weak as a consumer brand; the customer, especially the professional, buys availability and
   service. Not where the castle is.
8. *Would the customer still choose it over the low bid?* **[M2017-009]**, **[M2001-014]**. For the professional installer
   with a car on the lift, the part today is worth more than a cheaper part tomorrow; the filer competes on "merchandise
   selection and availability, technical proficiency" before "price" (10-K FY2025, Competition). Evidence: professional
   sales grew faster than DIY (41% to 50% of sales, 2012 to 2025) during the same years that online sellers competed on
   price.
9. *Ask the competitors* **[M1999-130]**. On the public record the competitors' own filings answer it: AutoZone reports
   similar margins and growth; Advance reports a turnaround from losses; Genuine Parts' North America Automotive segment
   EBITDA margin was 7.8% (2024) and 7.1% (2025) (GPC 10-K FY2025, accession 0000040987-26-000003). Nobody in the field is
   gaining on O'Reilly on the filed numbers. Interviews are not on the public record; not done.
10. *Widening or narrowing* **[M1999-108]**. Widening on the evidence over 2008 to 2025: operating margin 9.4% to 19.5%;
    professional share up; Hubs up; share gained against the field. Narrowing signs: the margin's peak was 21.9% (2021) and it
    has eased to 19.5% (2024, 2025), with SG&A pressure the filer attributes to medical and casualty insurance and store pay
    (10-K FY2025), and capital spending has doubled (Q3). Written down; not, on this evidence, a filling-in.
11. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. Three threats named in the filings:
    (a) vehicle technology, electric vehicles above all, which the filer (10-K FY2025), AutoZone ("Increased prevalence of
    electric vehicles [...] can result in less frequent parts failures and reduced need for parts", AZO 10-K FY2025) and
    Advance all name; (b) online sellers; (c) the supply chain and tariffs. (a) is the serious one over twenty years and it is
    slow: Q1's scrappage bound puts at least half of the ten-year fleet in today's combustion cars. It modifies or reduces;
    nothing in the filings shows it destroying the availability castle, since an electric car still wears brakes,
    suspension, steering, batteries, cooling and lighting, and those parts still need to be on hand the same day. The rows'
    warning applies in full: "slow change can be much harder to perceive, and can lull you to sleep easier" **[M2014-038]**.
    Carried to Q7: no growth is credited after year ten (the range convention), and the shown growth is the cap inside it.

**The competitor row** (operating income over sales, filers' own 10-Ks via their XBRL; fiscal years as each filer reports):

| | 2009 | 2012 | 2016 | 2019 | 2021 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| O'Reilly (10-Ks, accessions in Step 0) | 11.1% | 15.8% | 19.8% | 18.9% | 21.9% | 20.2% | 19.5% | 19.5% |
| AutoZone (FY ends Aug; 10-Ks incl. 0001104659-25-102611) | 17.3% | 18.9% | 19.4% | 18.7% | 20.1% | 19.9% | 20.5% | 19.1% |
| Advance Auto Parts (10-Ks incl. 0001158449-10-000032, 0001193125-26-051305) | 8.4% | 10.6% | 8.2% | 7.0% | 7.6% | 1.0% | -7.8% | -0.5% |
| Genuine Parts, Automotive segment operating margin (10-K FY2009 0000950123-10-017728; FY2016 0000040987-17-000007) | 7.4% | 8.6% | 8.8% | n/a | n/a | n/a | n/a | n/a |
| Genuine Parts, North America Automotive segment EBITDA margin (10-K FY2025 0000040987-26-000003) | | | | | | | 7.8% | 7.1% |
| Amazon | no automotive metric in its filings (flagged) | | | | | | | |

Pre-tax return on tangible operating capital (operating income over net property and equipment plus inventory plus
receivables less accounts payable; my construction from each filer's XBRL; operating-lease assets excluded, and including
O'Reilly's $2,391M of lease assets would lower its 2025 figure from 66% to about 45%): O'Reilly 18% (2009), 36% (2012), 54%
(2016), 48% (2019), 84% (2021), 80% (2023), 66% (2025); AutoZone 60% (2012), 58% (2016), 53% (2019), 76% (2021), 74% (2023),
54% (2025); Advance 24% (2009), 37% (2012), 24% (2016), 22% (2019), 3% (2023), -2% (2025). GPC Automotive is a wholesale
distribution model with independently owned NAPA stores, so its margin is not the same business; shown for the field.

**The parts table.** One reportable segment; the filer reports no parts with different economics. Not applicable.

**The field's returns over the last full cycle.** The cycle read is 2007 to 2025, which contains the 2008-09 recession, the
2020 shock and the 2021 to 2023 inflation. In words: the two leaders, O'Reilly and AutoZone, earned excellent and stable
returns on the capital the business needs over the whole span; the third national chain went from adequate to losses; the
distributor earned modest margins. That is not a field of ordinary returns; it is a field where the well-run dense networks
earn excellent returns and the others do not. The improvement at O'Reilly (2008 to 2015, the CSK integration) is credited
because it has held for a full cycle since, through 2020 and the inflation **[M2005-020]**.

**Why this does not close.** Not a castle shown open on the evidence **[M2011-015]**: the attackers in the record have failed
or stayed at the margin. Not a castle whose future cannot be judged **[M2000-019]**: the twenty-year electric question is
real but slow, and its first decade is bounded by a fleet already built. The castle requires continuous good operation,
which is the qualification carried to Q5 and Q7.

- **VERDICT: IN.** A low-cost, availability castle with pricing shown through the inflation **[M2005-020]**, volume and share
  gained against the field **[M1999-054]**, excellent returns protected over a full cycle **[L2007-004]**, and the slow
  electric threat carried to Q7 **[M2014-038]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**1. What it earns on the capital the business needs** **[M2010-090]**, **[M1998-005]**. The capital is property and
equipment plus inventory plus receivables less accounts payable (goodwill of $948M left out, as the rows direct for judging
the business **[M2011-060]**). Pre-tax return on it: 18% (2009, the CSK year), 36% (2012), 54% (2016), 48% (2019), 84% (2021),
80% (2023), 66% (2025) (Q2; my construction from the filer's XBRL, checked against the FY2025 balance sheet). With the
operating-lease assets added ($2,391M at 2025-12-31), 2025 is about 45%. The test for a flattered return **[L1994-009]**: not a
cyclical peak (the 2009 to 2025 span covers two shocks), not leverage (the measure is before financing), and not a monopoly
(the field has a strong rival at the same margin). One flattering item is real: the capital is low because suppliers carry
the inventory (payables 124% of inventory in 2025), a funding source that can shrink (Q9). Return on equity is not used:
equity is negative because buybacks have exceeded retained earnings, and "if you keep the equity low enough by buying shares
back, why, you could make return on equity whatever you want" **[M1998-017]**.

**2. Reinvestment to stand still and to grow** **[L2000-035]**, **[L1999-024]**. Capital spending ran close to depreciation
until 2022 (capex $443M against D&A $328M in 2021; $563M against $358M in 2022) and then doubled: $1,006M (2023), $1,023M
(2024), $1,169M (2025) against D&A of $409M, $462M, $511M; guidance for 2026 is $1.3 to $1.4 billion (8-K 2026-07-29, exhibit
99.1, accession 0000898173-26-000042). The filer names what it is for: new stores (186, 187, 198 and 207 net new in 2022 to
2025; 225 to 235 planned for 2026), DCs (the Lakeland expansion in 2026, a new Fort Worth DC in 2028) and store and
distribution "expansion and enhancement projects" (10-K FY2025; 10-Q 2026-06-30). The filing does not split maintenance from
growth. My best guess, stated as the rows ask **[M2000-144]**: maintenance is about the depreciation charge, $511M in 2025,
since depreciation is "not inappropriate in most companies to use as a proxy for required capital expenditures"
**[M1998-127]**; the rest, about $650M in 2025, is growth. The guess could be off on the high side for maintenance, because
the stores and DCs were built at older prices. Working capital needs no cash from the owner while suppliers keep their terms:
inventory grew $604.5M in 2025 and payables $576.4M (cash-flow statement, 10-K FY2025).

**3. What the added capital earns** **[M2001-019]**, **[M2000-088]**. Over 2019 to 2025: operating income up $1,540M on
tangible capital (with lease assets) up about $1,726M, a pre-tax incremental return near 90%. Over 2022 to 2025 the picture
is weaker: operating income up $507M on tangible capital up about $2,029M (about $2,309M with lease assets), an incremental
pre-tax return of about 22% to 25%. Contrary evidence, written down **[M1997-127]**: the recent spending wave has not yet
shown the old returns; part of it is DC capacity not yet earning, and 2022 started from a margin raised by the 2020-21
demand, but the three-year figure is what it is. Rising earnings alone prove nothing **[M2023-081]**: the test is the rate on
the capital added, and that rate fell from far above to merely good. "The second-best business [...] takes more money, but
the rate at which you invest — reinvest — the money to get that growth is a very satisfactory rate" **[M1998-081]**: the
recent record is that, while the long record is the first kind.

**4. The growth arithmetic and its caps** **[M1997-095]**, **[M2003-120]**. Sales grew at about 8.5% a year from 2014 to 2025
($7,216M to $17,782M); in 2025 net new stores added about 3% to the count (207 on 6,378) and comps 4.7% (Q1). Owner cash per Step 0 did not grow over
2021 to 2025 (it fell), because capital spending doubled and tax payments moved. No growth rate above the discount rate is
carried past year ten (Q7).

- **WEIGHS FOR**, with a caution: the business earns very high returns on the capital it needs over a full cycle
  **[M1998-005]**, **[L2009-012]**, but the capital added since 2022 has earned far less than the base **[M2001-019]**, and part of
  the low capital is suppliers' money that Q9 must weigh. ("Little or no debt" is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, before the income account** **[M2025-032]**. USD millions, first-filed XBRL
from each year's 10-K (accessions in Step 0 and in `tools/run.py`'s list: 0000898173-17-000091 to 0000898173-26-000009),
the FY2025 and 2026-06-30 columns read on the filed statements:

| year-end | assets | equity | cash | receivables | inventory | accounts payable | goodwill | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 7,204 | 1,627 | 147 | 197 | 2,779 | 2,937 | 785 | 1,887 | 290 |
| 2017 | 7,572 | 653 | 46 | 216 | 3,010 | 3,190 | 789 | 2,978 | -613 |
| 2018 | 7,981 | 354 | 31 | 192 | 3,193 | 3,376 | 807 | 3,417 | -909 |
| 2019 | 10,717 | 397 | 40 | 215 | 3,454 | 3,605 | 937 | 3,891 | -889 |
| 2020 | 11,597 | 140 | 466 | 230 | 3,653 | 4,185 | 881 | 4,123 | -1,139 |
| 2021 | 11,719 | -66 | 362 | 273 | 3,686 | 4,695 | 879 | 3,827 | -1,366 |
| 2022 | 12,628 | -1,061 | 109 | 343 | 4,359 | 5,881 | 884 | 4,372 | -2,376 |
| 2023 | 13,873 | -1,739 | 279 | 375 | 4,658 | 6,092 | 898 | 5,570 | -3,132 |
| 2024 | 14,894 | -1,371 | 130 | 357 | 5,096 | 6,525 | 930 | 5,521 | -2,791 |
| 2025 | 16,538 | -763 | 194 | 390 | 5,731 | 7,104 | 948 | 6,017 | -2,329 |
| 2026-06-30 | 17,389 | -1,836 | 262 | 458 | 5,972 | 7,385 | 955 | 7,015 | -3,416 |

What moved and why, in the filer's statements:
- *Assets jump in 2019*: operating-lease assets ($1,928M) came onto the balance sheet with the lease standard; not a
  purchase.
- *Equity and retained earnings*: equity fell from +$1,627M to -$1,836M while net income summed to about $18 billion over
  2016 to 2025; the difference is buybacks ($30.42 billion since 2011 through 2026-07-29, release of that date). Retained
  earnings rise in years of smaller buybacks (2024, 2025) and fall in years of larger ones. Negative equity here is the
  product of returning more than was earned, financed partly by debt, not of losses.
- *Goodwill* barely moved ($785M to $955M): growth has been built, not bought. The 2024 acquisition of Vast Auto in Canada
  (10-K FY2025, investing activities) is the largest recent one, about $161M of "other, including acquisitions".
- *Inventory against sales*: 2.06 times from 2016 to 2025 against sales 2.07 times ($8,593M to $17,782M). In line; the
  tell of "inventories look out of line, you know, with sales" **[M1995-064]** is absent. Receivables 1.98 times, in line.
- *Accounts payable* grew 2.42 times, faster than inventory; $5.1B of payables sit in supplier finance programmes "for
  invoices that were confirmed as valid to the third-party financial institutions", invoices "generally for a term of one
  year" (10-Q 2026-06-30, note on supplier finance). The balance sheet does not say what terms suppliers would offer without
  the banks: that is what the figures "can’t say" **[M2025-032]**.
- *Cash* is kept small ($31M to $466M); liquidity is the revolving facility and commercial paper ($1,345M outstanding at
  2026-06-30).
- *Debt* rose 3.7 times, from $1,887M to $7,015M (2026-06-30), roughly in step with EBITDAR, which the company targets on a
  ratio: "Adjusted debt to EBITDAR | 2.17" at 2026-06-30 (exhibit 99.1, 8-K 2026-07-29).
- *Inventory accounting*: LIFO. "The replacement cost of inventory was $ 6.25 billion and $ 5.32 billion as of December 31,
  2025 and 2024" against carried amounts of $5,731M and $5,096M (10-K FY2025, inventory note): the LIFO reserve rose by about
  $290M in 2025, a charge to cost of goods in a tariff year, which understates rather than flatters the year's profit.

**The real costs.**
- *Depreciation* **[R1996-023]**: $511M in 2025 against capital spending of $1,169M (Q3). Real, charged, and below what is
  being spent.
- *Stock pay* **[L2015-003]**: $35M in 2025 (0.2% of sales), expensed in GAAP income and deducted in the owner cash (Step 0).
  Small.
- *Restructurings, "one-time" items*: none found in the FY2023 to FY2025 statements or the 2026 release; a $19M litigation
  charge in 2015 is the last such item named in the 10-Ks read (10-K FY2016).
- *Self-insurance*: reserves of $443M at 2025-12-31 (the auditor's critical audit matter), current portion up from $149M to
  $297M in 2025; the filer attributes SG&A pressure to "medical and casualty insurance programs" (10-K FY2025). A real and
  rising cost, booked.
- *Taxes*: the effective rate is lowered by purchased "transferrable federal renewable energy tax credits" and the timing
  of their payment moves operating cash by hundreds of millions a year (Step 0). Real money saved, but a programme bought
  year by year, not a permanent rate: the 2026 guidance states an effective rate of 22.5%.
- *EBITDA in the filer's mouth*: the release reports "Adjusted debt to EBITDAR" as a leverage measure and "free cash flow";
  it features no adjusted earnings per share (exhibit 99.1, 8-K 2026-07-29). The rows' measure of coverage is "pre-tax
  earnings/interest, not EBITDA/interest" **[L2012-002]**: pre-tax income $3,240M over interest of $235M in 2025, about 13.8
  times; on the twelve months to 2026-06-30, $3,398M over $253M, about 13.4 times.

**What the accounts say of the management.** The accounts are plain, explained in clear terms, and conservative where there
is a choice (LIFO in an inflation; stock pay in the expense line; no adjusted earnings) **[M1994-018]**. Weighing against,
and carried to Q5: the company issues annual guidance on comps, revenue, margins, EPS, operating cash, capital spending and
free cash flow, and updates it each quarter ("Updated Full-Year 2026 Guidance", exhibit 99.1, 8-K 2026-07-29); the rows
call it "the scourge of earnings "guidance"" **[L2019-006]** and grow "downright incredulous if they consistently reach their
declared targets" **[L2002-041]**. Whether the targets are habitually met is not read here beyond the 2026 update; it is
recorded, not judged.

- **VERDICT on the accounts: IN; WEIGHS FOR.** No confusion and no suspicion **[M1995-063]**: inventory and receivables move
  with sales, no reserves moving to make a year, no adjusted earnings, stock pay expensed, LIFO conservative. Owner cash is
  computed "after interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]** in Step 0 and
  recast at Q7. Guidance weighs against and goes to Q5 **[L2019-006]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**Who they are** (proxy DEF 14A filed 2026-03-27, accession 0000898173-26-000014; 10-Ks). Executive Chairman Greg Henslee
(65; CEO 2005 to 2017; "Affiliated Director"); Executive Vice Chairman David O'Reilly (76; director since 1972, of the founding
family); CEO Brad Beckham (47; 29 years at the company, CEO since 2024); President Brent Kirby; CFO Jeremy Fletcher. Lead
Independent Director Thomas Hendrickson; the audit committee is four independent directors. Every chief executive since 2005
came up from the stores (Q2, test 2).

**The first yardstick: how well they run the business, against the hand dealt** **[M1994-008]**. The hand in 2008 was the CSK
acquisition ("At the date of the acquisition, CSK had 1,342 stores in 22 states", 10-K FY2008; mostly DIY, at a 9.4% consolidated operating margin in 2008); by 2015 the company earned 19.0% and
has held 18.9% to 21.9% since (Q2). Against the competitors' record in the same years, the same hand played better than
Advance played the General Parts acquisition (Q2). Comps positive every year since 1993. A long record, not a promise
**[M1996-038]**.

**The second yardstick: how they treat the owners; the proxy read** **[M1994-009]**.
- *Pay in proportion*. 2025 total compensation: CEO $4,231,108; President $3,588,436; CFO $2,324,316; Executive Chairman
  $1,339,488; Executive Vice Chairman $1,143,048 (Summary Compensation Table). On a company earning $2.5 billion, this is
  modest; the executives do not treat themselves better than the owners in size.
- *Related-party dealings*. The company leases land and buildings for 64 stores and one surplus property from entities
  affiliated with David and Larry O'Reilly or their families, and two stores from Greg Henslee; total payments $4.6 million in
  2025, reviewed by the audit committee, stated "no less favorable to the Company than those that would have been available
  to the Company in comparable transactions with unaffiliated parties". Disclosed, small (about $70,000 a store a year),
  long-standing. Recorded as a fact; not a tell on this evidence.
- *Ownership*. David O'Reilly 3,365,010 shares (about $291M at $86.45, nearly all held indirectly); Henslee 571,895 including
  options; Beckham 298,588 of which 270,075 are exercisable options; the independent directors hold from 1,965 to 18,840
  shares each. Directors and officers as a group under 1%.
- *The letters and reports* **[M1998-036]**. The 10-K and releases explain the business in plain terms, name the drivers,
  name the electric-vehicle risk, and explain each year's cash-flow movements (tax credits, inventory). No instance found, in
  the FY2023 to FY2025 10-Ks and the 2026 releases read, of a mistake discussed as a mistake; also none of a dressed-up
  figure.
- *Integrity record*. Legal proceedings: "litigation incidental to the ordinary conduct of the Company’s business", none
  material (10-K FY2025, Item 3). Clean audit opinions and effective internal control (Ernst & Young, 10-K FY2025). No
  restatement found in the filings read. Clawback policy in place (proxy).

**The habits carried from Q4.** Annual guidance, updated quarterly **[L2019-006]**. Read against the result for the one full
year checked: 2025 guidance (exhibit 99.1 to the 8-K of 2025-02-05, accession 0000898173-25-000005) was comps 2.0% to 4.0%,
revenue $17.4 to $17.7 billion, operating margin 19.2% to 19.7%, diluted EPS $42.60 to $43.10 (pre-split, $2.84 to $2.87
after it), operating cash $2.8 to $3.2 billion, capital spending $1.2 to $1.3 billion; actual: comps 4.7%, revenue $17.78
billion, operating margin 19.5%, diluted EPS $2.97, operating cash $2.76 billion, capital spending $1.17 billion (10-K FY2025).
Above on sales and EPS, inside on margin, below on operating cash. Not the pattern of "consistently reach their declared
targets" **[L2002-041]**; and the beats came from comps, not from reserves or adjustments (Q4). The incentive plan pays on
comps (40%), operating income (40%) and return on invested capital (20%) against targets the committee sets (proxy,
Performance Goals); payouts "have ranged from 50% to 765% of target, exceeding target 4 times" in five years. Recorded; the
ROIC metric's flaw is weighed at Q6, Part B.

**Integrity applied on doubt** **[M2013-088]**. I looked for the tells the framework lists: too-good-to-be-true claims,
reports that dance, the stock price as a focus, serial issuance (the opposite: the share count falls every year), weak
accounting (Q4 found the accounts conservative). None found. The guidance habit is a weight against, not a doubt about
honesty, on this record.

**Ability, weighed.** The rows put a heavy weight on management in retail: "Buying a retailer without good management is like
buying the Eiffel Tower without an elevator" **[L1995-006]**. Here the evidence for ability is the record against the field
over seventeen years and three successions **[M1994-008]**. Against: the recent capital spending has earned far less than the
base (Q3), and the capital allocation is dominated by debt-assisted buybacks whose prices are tested at Q6.

- **VERDICT on integrity: IN** (no tell found; guidance a weight against, not a doubt) **[M2013-088]**, **[M1994-009]**.
  **Ability WEIGHS FOR** **[M1994-008]**, **[L1995-006]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money

**Where the money has gone.** No cash dividend since the 1993 listing ("no cash dividends have been declared since that
time", 10-K FY2025). Operating cash goes to capital spending (Q3) and to buybacks: $30.42 billion for 1.50 billion
split-adjusted shares from January 2011 to 2026-07-29, "at an average price of $20.32" (exhibit 99.1, 8-K 2026-07-29). Shares
outstanding were 141,025,544 at 2010-12-31 (10-K FY2010), about 2,115 million on today's post-split count, against 808,960,792
now: 62% of the company has been bought in. Buybacks have exceeded free cash flow, and debt has filled the gap: long-term debt
from $1,887M (2016) to $7,015M (2026-06-30), commercial paper from $690M to $1,345M in the first half of 2026 alone.

**The retention test** **[R1995-009]**, **[M1998-110]**. Little is retained: net income has been paid out through buybacks
and more. What is retained is the reinvestment in stores and DCs, which has earned very high returns over the long record
and good but much lower ones since 2022 (Q3). Market value rose far faster than the sums kept. Passes on the long record.

**Buybacks, with their prices** (split-adjusted; average price per share and dollars, from each year's 10-K share repurchase
table, pre-split figures divided by 15):

| year | shares (M, post-split) | average price | total ($M) |
|---|---|---|---|
| 2011 | 238.2 | $4.10 | 976 |
| 2012 | 243.0 | $5.95 | 1,445 |
| 2013 | 127.9 | $7.29 | 933 |
| 2014 | 86.1 | $10.06 | 866 |
| 2015 | 73.5 | $15.45 | 1,136 |
| 2016 | 85.5 | $17.61 | 1,505 |
| 2017 | 139.5 | $15.57 | 2,172 |
| 2018 | 90.9 | $18.85 | 1,714 |
| 2019 | 58.2 | $24.64 | 1,433 |
| 2020 | 72.5 | $28.80 | 2,087 |
| 2021 | 68.1 | $36.39 | 2,476 |
| 2022 | 74.4 | $44.11 | 3,282 |
| 2023 | 53.5 | $58.88 | 3,151 |
| 2024 | 29.0 | $71.50 | 2,077 |
| 2025 | 22.7 | $92.26 | 2,097 |
| 2026 to 30 June | 26.7 | $91.17 | 2,430 |
| 2026, July to the 07-29 release | 7.3 | $86.81 | 632 |

Sources: 10-Ks FY2012 (2011, 2012), FY2014 (2013, 2014), FY2016 (2015, 2016), FY2017, FY2019 (2018, 2019), FY2020, FY2022
(2021, 2022), FY2024 (2023, 2024), FY2025 (2025, already post-split); exhibit 99.1 to the 8-K of 2026-07-29 (2026).

**The programme names no price.** Authorizations are dollar amounts ("increase the authorization amount [...] by an
additional $2.0 billion, raising the aggregate authorization under the program to $31.75 billion", 8-K 2026-06-01,
accession 0000898173-26-000033), bought "at prevailing market prices, based on a variety of factors such as price, corporate
requirements, and overall market conditions". The rows: "repurchase announcements almost never refer to a price above which
repurchases will be eschewed" **[L2016-002]**; "what is smart at one price is dumb at another" **[L2011-003]**; "we’re going to
spend $5 billion this year buying a business, we don’t care what the price is. But that’s what companies do when they don’t
attach some kind of a metric to what they’re doing on their buybacks" **[M2016-049]**.

**The test of the prices paid against the bottom of the Q7 range** (run when Q7 was reached, recorded here; the range is
today's, for today's business). Q7's central range is $50.53 to $111.16 a share, the all-spending range beside it $40.68 to
$111.16, and the fair price $38.12 (all-equity) or $43.70 (equity-only). The purchases of 2023 ($58.88), 2024 ($71.50), 2025
($92.26) and 2026 ($91.17, $86.81) all sit above the bottom of the range, and those of 2025 and 2026 sit about twice the fair
price; on Q7's arithmetic, the $5.2 billion spent since January 2025 bought at prices where the midpoint of the range earns
about 5%, not the floor. The purchases of 2011 to 2021 (at $4.10 to $36.39) sit below today's bottom of range, but
today's range values today's larger business, so it cannot say what those purchases were worth when made; the honest reading
is that the long programme retired 62% of the shares at an average of $20.32 and the shares retired are worth several times
that today, while the recent purchases are made at prices the rows would not pay **[L1999-023]**, **[M2015-074]**. A buyback
with no stated price, at prices above the bottom of the range: **weighs against** (the CONVENTION of Q6, read against the Q7
range). The second exception of the rows also bears: the business is spending more than ever on its own expansion (capital
spending $1.3 to $1.4 billion guided for 2026) and buying stock with borrowed money at the same time **[L2016-003]**.

**Issuance and deals** **[L2009-019]**, **[L2014-015]**. No stock-paid acquisition in the span read; acquisitions are small and
paid in cash (CSK in 2008 was the last large one; Vast Auto in 2024). The share count falls every year; no serial issuance.
The one STOP of Part A does not arise.

### Part B: the pay, the board and the owners

- *Pay tied to what the person controls* **[M2003-019]**. The annual plan pays on comparable store sales (40%), operating
  income (40%) and return on invested capital (20%), all inside management's reach (proxy, Performance Goals). One flaw: ROIC
  is "net income [...] plus interest expense, divided by the sum of average debt, and average equity, less average cash",
  and buybacks that shrink equity raise it, the mechanism of "if you keep the equity low enough by buying shares back, why,
  you could make return on equity whatever you want" **[M1998-017]**. Weighs against, at a 20% weight.
- *Options and restricted stock* **[L1994-021]**, **[M2002-084]**. Options "expire after 10 years" (10-K FY2025, share-based
  compensation note), granted at market, with no step-up for retained earnings, in a company that pays no dividend: the
  "ten-year option, a low dividend payout, and compound interest" the 1994 letter warns of. Their cost is expensed (Q4).
  Amounts are modest (stock pay $35M in 2025; CEO option award $1.42M).
- *The size* **[M1994-009]**: CEO $4.2M, the two executive chairmen about $1.1M to $1.3M each, on earnings of $2.5 billion.
  Not a tell.
- *The board* **[M2007-120]**. An Executive Chairman (the former CEO) and an Executive Vice Chairman (the founding family),
  both "Affiliated", with a Lead Independent Director; the audit committee is fully independent. Directors' own holdings are
  small apart from the O'Reilly family (Q5). Whether directors bought shares "with their savings" **[L2019-008]** the proxy
  does not say.
- *The owners as partners*. Plain reporting, no adjusted earnings; guidance issued (Q4, Q5); the release features the
  ten-year shareholder return ("average annual shareholder return of 18% over the past 10 years", proxy). Related-party
  leases of $4.6M disclosed (Q5).

- **Part A WEIGHS AGAINST**: a price-blind, debt-assisted buyback whose recent prices sit above the bottom of the Q7 range
  and at about twice the fair price **[L2016-002]**, **[L2011-003]**, **[M2016-049]**, set against a long record of retiring
  62% of the shares at an average of $20.32 **[R1995-009]**.
- **Part B WEIGHS FOR, narrowly**: modest pay on controllable metrics **[M2003-019]**, against a buyback-flattered ROIC
  metric **[M1998-017]** and ten-year options without a step-up **[L1994-021]**.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at the long government rate **[L2000-021]**, as a range **[L2000-024]**. The arithmetic is in
`Test Runs/_research 2026-10-10 ORLY/q7.py`, its output in `q7_output.txt` beside it. USD millions unless a share figure.

**The cash, after every real cost.** Owner cash = operating cash less stock pay, less the investments in tax-credit funds
(an investing outflow of $34M to $188M a year in 2019 to 2022 that buys the tax saving which shows inside operating cash; the
filer's own free-cash-flow definition deducts it, 10-K FY2025 note (h)), less capital spending. Two forms, by specific (e):
- *Maintenance-only*: depreciation as the maintenance guess (Q3) **[M2000-144]**; acquisitions, being growth spending, not
  deducted. 2016 to 2025: 1,217; 1,151; 1,449; 1,381; 2,335; 2,674; 2,576; 2,593; 2,560; 2,216.
- *All-spending*: capital spending net of asset-sale proceeds, and cash paid for businesses ("Other, including acquisitions",
  $1M to $161M a year) deducted, so that total growth is credited (specific (c)). 2016 to 2025: 905; 921; 1,174; 889; 2,199;
  2,566; 2,382; 2,010; 1,855; 1,574.
- *All-equity basis*: interest paid ($64M to $227M a year, XBRL InterestPaidNet) added back after tax at the company's own
  rate (22.5%, 2026 guidance), against market value plus net debt of $6,752.4M at 2026-06-30 **[L2017-004]**. Unlevered
  five-year (2021 to 2025) averages: maintenance-only **$2,667M**, all-spending **$2,221M**; equity-only (after interest):
  $2,524M and $2,078M.
- *Working capital* (specific (d)) is inside operating cash and so counted: the inventory build is netted by the payables
  build each year. *Whose tax*: the company's own, no conversion. The tax-credit programme is bought year by year (no
  carryforward that runs out inside ten years is found in the filing), so no shelter is priced separately.

**The base and the growth, by the specifics.**
- *The literal window, 2021 to 2025*, shows a decline: unlevered all-spending cash from $2,678M to $1,750M (-10.1% a year),
  maintenance-only from $2,785M to $2,392M (-3.7% a year).
- *Both end years are aberrational on the filer's own description* **[L2005-003]**: 2021's demand was "positively impacted"
  by "government stimulus payments and enhanced unemployment benefits" (10-K FY2021), and 2022's DIY counts fell against "a
  challenging comparison to the strong transaction counts in 2021, which were aided by government stimulus" (10-K FY2022);
  2025's operating cash fell "primarily due to the timing of payment for transferrable federal renewable energy tax
  credits" (10-K FY2025). So specific (a) applies: the base is the average of the latest five years, and the growth is
  measured between the averages of two successive five-year spans, 2016 to 2020 and 2021 to 2025, with the literal window
  shown beside. The business has no trough-to-trough cycle in its owner cash (comps were never negative), so the successive
  five-year spans are this run's reading of "successive cycles": **CONVENTION of this run**, rationale: the specific asks for
  cycle averages and the filer's record has no cycle to mark them, and two spans of the window's own length keep the
  measure symmetrical.
- *Growth between the five-year averages*: unlevered all-spending $1,304M to $2,221M, **11.25% a year**; maintenance-only
  $1,593M to $2,667M, 10.86% a year. This is higher than sales growth (8.5% a year 2014 to 2025) because the earlier span
  carries the pre-2018 tax rate and the later one the margin step of 2020-21. The cap (specific (f)): inside the ten years the
  shown rate is the cap and is used; nothing is carried past year ten (zero nominal growth after it) **[M1997-095]**. Not cut
  back as absurd **[M1999-067]**: it needs owner cash to reach about 2.9 times today's in ten years, which sales growth at the
  past rate with the margin held would roughly supply. The sensitivity is large and is written down: measured instead between
  the 2018-20 and 2023-25 averages (after the tax change), the all-spending growth is 5.27% and the top of the range falls to
  $66.18.

**The range** (all-equity, at the 30-year Treasury of 5.60%, ten years at the growth then flat; per share = value less net
debt of $6,752.4M, over 808.961M shares):
- No-growth end, maintenance-only cash: $47,630M, **$50.53 a share**.
- Shown-growth end, all-spending cash at 11.25%: $96,680M, **$111.16 a share**.
- **Central range $50.53 to $111.16** (top 2.20 times the bottom) against the price of **$86.45**.
- Beside it: all-spending at both ends, $40.68 to $111.16; maintenance-only at both ends, $50.53 to $130.93; the literal window
  (its negative growth carried as the bottom, no growth the top, specific (b)), all-spending $14.06 to $40.68 and
  maintenance-only $35.51 to $50.53.

**The floor** (CONVENTION): about ten percent **[M1994-004]**, **[L2002-020]**, **[M2003-149]**, on owner cash after the company's
tax. At $86.45 the enterprise value is $76,687M; owner cash of $2,221M to $2,667M is a 2.9% to 3.5% yield on it, and the
return that makes the midpoint of the two end streams equal the price is **about 5.3%**, below the floor. At the price, "there’s
just a point at which we drop out of the game" **[M2003-149]**.

**The close.** The range is narrower than three to one, so not TOO HARD **[L2000-025]**. The price sits inside it, about
two-thirds of the way up, and the expected return at the price is about half the floor. Not a screamer: "If you need to use a
computer or a calculator to make the calculation, you shouldn’t buy it" **[M2009-005]**, and the opposite of "startlingly low
in relation to value" **[L2000-025]**.

- **Value range:** $50.53 to $111.16 a share against $86.45 (literal window beside: $14.06 to $50.53 across its two forms).
  **Closes OUT**: the price sits inside a range narrower than three to one, and the expected return at the price is below the
  floor.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$38.12 a share** on the all-equity basis (the price at which
  the average of the two end streams, valued at 10%, less net debt, equals the price: enterprise value $37,587M); the
  equity-only figure beside it **$43.70** (owner cash after interest, $2,524M maintenance-only and $2,078M all-spending at
  11.28% growth, valued at 10%, no net debt deducted). After the company's own tax. No cheap price is reported.
- **VERDICT: OUT** on price **[M2003-149]**, **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** Q7 closed the file OUT. (Fact for the record, under AFTER THE STOP.)

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.**

---
## THE BOX
**OUT, at Q7 (price).** Value range $50.53 to $111.16 a share (all-equity, central) against $86.45; expected return at the
price about 5.3%, below the floor of about ten percent. Q1 IN, Q2 IN, Q3 weighs FOR with a caution, Q4 IN and weighs FOR,
Q5 integrity IN and ability weighs FOR, Q6 Part A weighs AGAINST and Part B FOR narrowly. Reporting figures: fair price
$38.12 (all-equity) and $43.70 (equity-only) against $86.45. No integrity facts left unjudged (Q5 was reached and answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

*Bearing on Q8 (the alternatives).* The 30-year Treasury yields 5.60% (2026-10-09, US Treasury par yield curve). Q7's
arithmetic puts the expected return at $86.45 at about 5.3% on the midpoint of the two end streams (`q7_output.txt`).

*Bearing on Q9 (the target's debt and exposures).*
- Debt at 2026-06-30: principal $7,045M (commercial paper $1,345M at 4.065%; senior notes from 5.750% due 2026 $750M, 3.600%
  due 2027 $750M, 4.350% due 2028 $500M, through 5.100% due 2036 $850M) (10-Q, accession 0000898173-26-000045, financing
  note). After the quarter, $1.6B of notes due 2029, 2031 and 2037 were issued to repay commercial paper (8-Ks of 2026-08-11
  and 2026-08-14).
- Back-up liquidity: a $2.25 billion unsecured revolving facility, "scheduled to mature in March of 2030", used as "a
  liquidity backstop for the repayment" of commercial paper (10-K FY2025; 10-Q 2026-06-30); cash $262M.
- Leverage as the company measures it: "Adjusted debt to EBITDAR | 2.17" at 2026-06-30 (2.06 a year earlier) (exhibit 99.1,
  8-K 2026-07-29). Pre-tax earnings over interest: about 13.4 times on the twelve months to 2026-06-30 (Q4).
- Supplier finance: $5.1 billion of accounts payable at 2026-06-30 and at 2025-12-31 are invoices assigned by suppliers to
  third-party banks, "generally for a term of one year"; "The Company does no t have any assets pledged as security or other
  forms of guarantees" (10-Q, note 6; the "no t" is the filing's own break). If the banks withdrew these programmes, suppliers'
  terms could shorten and the company would need to fund part of a $5.7 billion inventory itself; the filing gives no figure
  for what terms would be without the programmes.
- Operating leases: $2,572.9M of lease liabilities ($452.3M current, $2,120.6M non-current) at 2026-06-30; related-party
  leases are a small part (Q5).
- Self-insurance reserves of $443M at 2025-12-31 (workers' compensation, general liability, health), the auditor's critical
  audit matter (10-K FY2025).
- No derivatives book, collateral calls or cash-out features were found in the 10-K or 10-Q read.
- "little or no debt" **[R1997-001]** is a STOP only for a whole business bought; the facts above are recorded for it.

*Bearing on Q10.* Nothing beyond Q7's figures.

*Bearing on Q12.* The business sells replacement parts and maintenance items for cars and light trucks; none of the
businesses Q12 names (casinos, tobacco, distributor-loading schemes, gambling dressed as investing) is involved.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). The
      template was copied before the first fetch; commits: Step 0 and foundations, Q1, Q2, Q3 (and a figure correction),
      Q4, Q5, Q6, Q7, the close. One departure: Q6's buyback test needs Q7's range, so Q7's arithmetic was run before Q6 was
      written, and Q6's figures were updated in the Q7 commit when the Q7 cash definition was corrected (tax-credit fund
      investments and acquisitions added). Both are in the history.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (`_overnight.lock` was present in `Screens/_daily/` at the start); the fold is the dispatcher's. A run not in
      the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule). Seen by
      accident and declared above under contamination: file names of two other 2026-10-10 runs and recent commit subjects
      in the session's git snapshot, and one memory-index line; none used.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-10 ORLY/check_ids.py`); every filing fact has its
      accession; no number without a row or a filing, except the CONVENTION of this run at Q7 (successive five-year spans
      as the cycle) and my stated maintenance guess at Q3.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash less stock pay, less
      tax-credit fund investments, less capital spending (or depreciation as the maintenance guess), less acquisitions in
      the all-spending case. The sovereign from the issuing authority (US Treasury). The price is an aggregator quote,
      flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations list; Q1 retail rows; Q2 test 2 and test
      10; Q3 the 2022 to 2025 incremental return; Q6 the recent buyback prices); facts for later questions are under AFTER
      THE STOP; no integrity facts are left unjudged.
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; today's rows only).
- [x] Only the arithmetic lines of `tools/run.py` were used (its 3-year "OWNER EARNINGS" headline and yield lines were not
      used; the five-year figures were recomputed from the filed statements).
- [x] `python tools/check_framework.py` PASS before the commit (see the close commit).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) **Q6 needs Q7 before Q7 is reached.** Q6's buyback test reads the prices paid against "the bottom of the Q7
range", and the framework says the test "is run when Q7 is reached and recorded back at Q6"; but the brief's write-early
order commits Q6 before Q7 exists. I ran Q7's arithmetic first and wrote Q6 with it; when Q7's cash definition was then
corrected, Q6's figures had to be changed in a later commit. The brief should say that Q6's buyback line is written at Q7
and committed with it. This is the error I found in the brief (its "Doing the run" section orders the commits question by
question and is silent on the back-reference). (2) **Specific (e) is ambiguous** in its first sentence ("the central case is
owner cash after maintenance only, with the growth spending charged against the growth it buys"); its third sentence ("the
maintenance-only no-growth case is the top of the range and the growth case the bottom" when the inversion holds) shows the
intended pair, and I built the range from that pair: maintenance-only cash at no growth, all-spending cash at the shown
growth. (3) **Specific (a) assumes a cycle the record may not have.** O'Reilly's comps were never negative, so there is no
peak-to-peak or trough-to-trough span to average; I used two successive five-year spans and confessed it as a CONVENTION of
this run. The growth so measured (11.25%) carries the 2018 federal tax-rate cut and the 2020-21 stimulus step; the framework
has no rule for a statutory tax change inside the shown growth, and the sensitivity (5.27% measured after the change) moves
the top of the range from $111.16 to $66.18. The verdict does not depend on it; a range does. (4) **"The midpoint of the
range earns the floor" is not defined as arithmetic.** I computed the fair price as the average of the two end streams valued
at 10%, less net debt; valuing a single stream at the midpoint growth rate gives a different number. (5) **Tax-credit
purchases** sit in investing cash in 2019 to 2022 and in operating cash after 2023, while their benefit is always in
operating cash; the framework's "every real cost" covers it in principle, but no rule names it, and a run that used operating
cash less capital spending would have overstated the 2020 to 2022 owner cash by $164M to $188M a year. I deducted it, as the
filer's own free-cash-flow definition does.
