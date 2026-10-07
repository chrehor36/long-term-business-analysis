import io
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-21 Run - BELFB Bel Fuse.md"
s = io.open(p, encoding='utf-8').read()
start = s.index("## Q2 \u2014 IS IT A FRANCHISE?")
end = s.index("## Q3 \u2014 ARE THEY HONEST, AND ARE THEY RATIONAL?")
new = u"""## Q2 \u2014 IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."

- **(1) Needed or desired \u2014 YES.** Equipment does not work without power conversion, circuit
  protection, connectors and magnetics. $732.9M of 2025 bookings and a $452.2M backlog at
  2026-01-31 settle it.
- **(2) No close substitute \u2014 NO. THIS IS WHERE THE FILE CLOSES, AND THE COMPANY'S OWN 10-K IS
  THE EVIDENCE.** Three passages, all from the anchor filing (accession `0001437749-26-005354`):

  Item 1, *Competition*: *"We operate in a variety of markets, all of which are highly competitive.
  There are numerous independent companies and divisions of major companies that manufacture
  products that are competitive with one or more of our products. Our ability to compete is
  dependent upon several factors including product performance, quality, reliability, depth of
  product line, customer service, technological innovation, design, delivery time and price."*

  Item 1A, *We conduct business in a highly competitive industry*: *"Our business operates in a
  globally competitive industry, **with relatively low barriers to entry.** We compete principally
  on the basis of product performance, quality, reliability, depth of product line, customer
  service, technological innovation, design, delivery time and price. The industry in which we
  operate has become increasingly concentrated and globalized in recent years and **our major
  competitors, many of which are larger than Bel, have significant financial resources and
  technological capabilities.**"*

  Item 1A, *There are several factors which can cause our margins to suffer*, first bullet,
  **Declines in Selling Prices**: *"**The average selling prices for certain of our products tend
  to decrease over their life cycles, and customers put pressure on suppliers to lower prices even
  when production costs are increasing.** Further, increased competition from low-cost suppliers
  around the world has put additional pressures on pricing. Any drop in demand for our products or
  increase in supply of competitive products could also cause a significant drop in our average
  sales prices."*

  **A customer who believes there is no close substitute does not extract falling prices from a
  supplier whose costs are rising.** That third passage is criterion 2 failing in the one place the
  criterion is observable, written by the registrant about itself, and the second passage names the
  reason in four words: *relatively low barriers to entry*.
- **(3) Not price-regulated \u2014 YES, not regulated.** Government contract cost-accounting standards
  touch the defence work, but no authority sets Bel's prices. Criterion 3 passes and is not the
  reason for the verdict.

**Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04, E4-23]**
The 10-K answers the second itself, in Item 1 under *Intellectual Property*: *"It is management's
opinion that the successful continuation and operation of our business does not depend upon the
ownership of patents or the granting of pending patent applications, but upon **the innovative
skills, technical competence and marketing and managerial abilities of our personnel.**"*
**[E4-23]** is explicit that this is a Q2 finding and a moat defect: *"if a business requires a
superstar to produce great results, the business itself cannot be deemed great ... The
partnership's moat will go when the surgeon goes. You can count, though, on the moat of the Mayo
Clinic to endure, even though you can't name its CEO."* **Recorded here as a moat defect, not at
Q3 as a compliment to the people.** It is **not** the operative reason for the verdict: the
2026-09-20 ruling applies [E4-04] as a **competence limit, never as a fourth franchise criterion**,
so it could at most produce UNKNOWABLE, and criterion 2 has already produced a finding about the
business.

**Primary moat metric, filing-sourced, and its trend.** Gross margin and operating margin, from the
filed statements: gross margin **24.7 / 28.0 / 33.7 / 37.8 / 39.1** and operating margin
**5.8 / 10.0 / 13.8 / 12.0 / 16.4** for FY2021 through FY2025. Income from operations FY2025 is
**$110,996 thousand on $675,455 thousand of net sales = 16.43%**, read off the filed consolidated
statement of operations by hand. The direction is up, sharply, every year on gross margin.
**[E4-32]** says direction outranks existence and calls the widening moat *"the primary criterion
of a great business"* \u2014 so this trend is the strongest thing in the file and it is tested below
rather than waved through.

**THE COMPETITOR ROW \u2014 required [E3-28].** Full workpaper, construction, sources and exclusions:
`Test Runs/_research 2026-09-21 BELFB/WORKPAPER - the competitor row.md`. One construction from each
filer's own SEC data, newest fiscal year; **cross-checked against a filed statement** \u2014 Amphenol's
FY2025 10-K (`0001104659-26-013549`) MD&A says *"Operating income was $5,868.6, or 25.4% of net
sales, in 2025, compared to $3,156.9, or 20.7% of net sales, for 2024"*, and the construction
returns 25.4% and 20.7%.

| Company | rev $m | GM% | OM% | NTA $m | EBIT/NTA | FY end | source |
|---|---|---|---|---|---|---|---|
| **Bel Fuse (subject)** | **675** | **39.1** | **16.4** | **283** | **39.2%** | 2025-12-31 | 10-K `0001437749-26-005354` |
| Amphenol | 23,095 | 36.9 | 25.4 | 15,527 | 37.8% | 2025-12-31 | 10-K `0001104659-26-013549` |
| TE Connectivity | 17,262 | 35.2 | 18.6 | 8,219 | 39.1% | 2025-09-26 | 10-K filed 2025-11-10 |
| Vishay Intertechnology | 3,069 | 19.4 | 1.9 | 2,780 | 2.0% | 2025-12-31 | 10-K filed 2026-02-13 |
| Littelfuse | 2,386 | 38.0 | 1.6 | 1,422 | 2.6% | 2025-12-27 | 10-K filed 2026-02-19 |
| Advanced Energy | 1,799 | 37.7 | 9.3 | 2,087 | 8.0% | 2025-12-31 | 10-K filed 2026-02-13 |
| Methode Electronics | 1,019 | 19.8 | 0.9 | 610 | 1.4% | 2026-05-02 | 10-K filed 2026-06-24 |
| Standex International | 892 | 41.7 | 21.7 | n/a | n/a | 2026-06-30 | 10-K filed 2026-08-14 |
| Allient | 554 | 32.8 | 7.9 | 259 | 17.0% | 2025-12-31 | 10-K filed 2026-03-05 |
| CTS Corporation | 541 | 38.4 | 15.3 | 189 | 43.8% | 2025-12-31 | 10-K filed 2026-02-24 |
| Vicor | 408 | 63.6 | 20.1 | 712 | 11.5% | 2025-12-31 | 10-K filed 2026-03-02 |
| RF Industries | 81 | 33.2 | 2.2 | 25 | 7.2% | 2025-10-31 | 10-K filed 2026-01-14 |

**And the same row over five years, because one year is a snapshot and not a position** (operating
margin %, oldest first, 5y mean, 5y minimum):

| | OM% by year | mean | min |
|---|---|---|---|
| **BELFB** | **5.8 / 10.0 / 13.8 / 12.0 / 16.4** | **11.6** | **5.8** |
| APH | 19.4 / 20.5 / 20.4 / 20.7 / 25.4 | 21.3 | **19.4** |
| TEL | 16.3 / 16.9 / 14.4 / 17.6 / 18.6 | 16.8 | **14.4** |
| SXI | 12.0 / 23.1 / 14.1 / 11.8 / 21.7 | 16.6 | 11.8 |
| CTS | 14.9 / 15.8 / 13.6 / 13.8 / 15.3 | 14.7 | 13.6 |
| LFUS | 18.5 / 19.9 / 15.3 / 7.2 / 1.6 | 12.5 | 1.6 |
| VICR | 15.5 / 6.8 / 12.7 / -0.4 / 20.1 | 10.9 | -0.4 |
| VSH | 14.4 / 17.6 / 14.3 / 0.2 / 1.9 | 9.7 | 0.2 |
| AEIS | 10.4 / 12.6 / 6.9 / 2.5 / 9.3 | 8.3 | 2.5 |
| ALNT | 6.4 / 6.3 / 7.3 / 5.7 / 7.9 | 6.7 | 5.7 |
| MEI | 9.6 / 7.7 / -10.0 / -2.3 / 0.9 | 1.2 | -10.0 |
| RFIL | 7.7 / -5.3 / -5.3 / -4.4 / 2.2 | -1.0 | -5.3 |

- **Peers named: eleven**, taken from the whole SEC-registrant set that sells into the same sockets.
  Buffett says eight **[E3-28]**; eleven were available and eleven were taken.
- **Peers excluded and why, named per the rule:** Molex, Pulse Electronics, Halo, Bourns and Samtec
  are **private**; TDK, Murata, Delta Electronics, Yageo and Sumida are **Japan- and Taiwan-listed,
  not SEC registrants**; Smiths Interconnect does not report separately inside Smiths Group plc.
  **This is the row's one material gap and it is disclosed: Bel's Magnetic Solutions segment (13% of
  2025 sales) competes mainly against those Asian filers.** The gap does not hold the verdict
  PROVISIONAL, because the verdict rests on the subject's own filed statements about its own
  pricing, not on the row.
- **Untapped pricing power? [E3-33] NO, and the filing says the opposite.** Claiming that class
  means claiming *"a monopoly or a near monopoly"* **[E5-28]**, which the company's own
  *"numerous independent companies"* refuses. **[E4-37]**'s inverse metric \u2014 *"you can almost
  measure the strength of a business over time by the agony they go through in determining whether
  a price increase can be sustained"* \u2014 reads directly off the MD&A. Every margin explanation Bel
  gives is a **cost** explanation: facility consolidations, the Mexican peso, the Chinese renminbi,
  the Israeli shekel, PRC minimum wage, gold and copper. The **one** pricing action named anywhere
  in the document is a single line about one segment in one year: *"Gross margin for 2024 was
  favorably impacted by pricing actions on certain contract renewals."* A business with pricing
  power does not itemise one year's contract renewals as a margin driver. **[E2-44]**'s
  two-characteristic test asks whether it can raise prices *"even when product demand is flat and
  capacity is not fully utilized"*; the filing's own answer is the Declines in Selling Prices
  bullet, which is that answer inverted.

**THE DISCONFIRMING CASE, HUNTED HARDEST BECAUSE THE TREND IS THE FAVOURITE HYPOTHESIS [E4-26].**
The case for a franchise is real and must be stated fairly: gross margin up five years running,
**EBIT/NTA of 39.2% level with TE Connectivity and above Amphenol**, a backlog of two-thirds of
annual sales, Class B stock up **1,016% over ten years** (the company's own figure, DEF 14A), and a
defence and commercial-aerospace mix that is genuinely qualification-protected. Four things defeat
it, and all four are filed:

1. **Seventeen years of the same company's own operating margin:**
   `-9.5 / 5.0 / 2.5 / 0.6 / 4.3 / 2.8 / 5.0 / -15.3 / 3.5 / 4.9 / -0.3 / 4.0 / 5.8 / 10.0 / 13.8 /
   12.0 / 16.4`. **Thirteen of seventeen years below 6%, two negative, and no year above 5.8% before
   2022.** **[E2-53]**'s dominance test is *"Once dominant, the newspaper itself, not the
   marketplace, determines just how good or how bad the paper will be. **Good or bad, it will
   prosper.**"* For thirteen of these seventeen years Bel did not prosper. Position did not set the
   economics; the cycle did.
2. **The competitor row removes the environment as the explanation.** Amphenol's worst of the last
   five years is **19.4%** and TE's is **14.4%** \u2014 both above Bel's **best of seventeen**. Same
   industry, same customers, same five years. **[E3-61]** says the row cannot show conduct, and that
   is exactly what makes this useful: it takes the industry off the table as a defence.
3. **[E2-58]'s equation is what actually governs this industry, and the company writes it out.**
   *"persistent over-capacity without administered prices (or costs) equals poor profitability"*,
   long-term profitability set by *"the ratio of supply-tight to supply-ample years"*, and prosperity
   breeding the next glut \u2014 *"nothing fails like success."* Bel's 2016 (-15.3% operating margin on
   $500M of sales) is the supply-ample year; 2023 is the supply-tight one, and the filing prices it
   to the dollar: **raw-material expedite fee revenue of $14.9 million in 2023 against $0.1 million
   in 2024**. Customers paying to jump a queue is the definition of a supply-tight year, and it went
   to zero. [E2-58]'s single exception is *"a cost advantage that is both wide and sustainable ...
   By definition such exceptions are few"*, and Bel has the opposite: fifteen plants whose cost line
   the MD&A says moves with the peso, the renminbi, the shekel, PRC minimum wage, gold and copper.
4. **The margin step-up has a disclosed, non-franchise cause.** Management attributes it to Enercon
   mix (bought for **$325.6M cash** in November 2024 and contributing **$136.6M** of 2025 sales),
   facility consolidations in the PRC and Mexico, and favourable FX. **[E4-36]** asks which of the
   four causes of extreme success the record comes from, and **[E3-51]** names the one that is not
   ownable: *"when a surfer gets up and catches the wave and just stays there, he can go a long,
   long time. But if he gets off the wave, he becomes mired in shallows."* **Bel's own 2009-2021
   record is the shallows**, and the 2022-2025 record is three waves at once \u2014 the component
   shortage, a defence-spending surge, and the datacenter build. A surfing run is not a moat.

**Where [E3-33]'s ultimate-no-brainer class would have lived, the filing says the opposite; where
[E2-53]'s dominance class would have lived, thirteen of seventeen years say the opposite; and where
[E2-58]'s wide-and-sustainable cost exception would have lived, the MD&A lists six input costs it
does not control.**

- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL \u00b7 Direction: **improving, from a very low
  base, on a bought mix and a cost programme \u2014 an improving business, not a widening moat**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED \u2192 ____  [ ] UNKNOWABLE \u2192 ____**

  **OUT, ON THE BUSINESS, at [E3-03] criterion 2, on the registrant's own Item 1 and Item 1A.**
  The verdict is not UNKNOWABLE: the separating test **[E4-19]** asks *"can I name the document
  that would resolve this?"* and there is nothing left to fetch \u2014 the resolving document is the
  10-K itself and it has been read. A company that files *"relatively low barriers to entry"* and
  *"customers put pressure on suppliers to lower prices even when production costs are increasing"*
  has answered criterion 2 about itself. **Permanent, per the four-verdict table.** The [E4-04]
  competence-limit route is not used and would not have been needed.

---
\u26d4 **Q1-Q4 DID NOT ALL CLOSE IN. THE FILE IS CLOSED AT Q2.** Everything below this line is
recorded **BELOW THE GATE** and **IS NOT A CLEARANCE OF ANYTHING**. It is written because the
material was gathered before the gate closed and because operator rule 6 makes the record part of
the run, not because any of it bears on the verdict. **No Q5 output appears in this file**
[operator rule 2]. Any arithmetic below is headed **COMPUTATION \u2014 NOT A CLEARANCE**
[operator rule 3].

"""
io.open(p, 'w', encoding='utf-8').write(s[:start] + new + s[end:])
print("Q2 written")
