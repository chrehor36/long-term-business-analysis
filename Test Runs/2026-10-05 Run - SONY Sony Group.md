# Company Run — SONY GROUP CORPORATION (TSE Prime: 6758; NYSE ADR: SONY) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*(Copied from the template before any fetch, 2026-10-05. Working folder: `Test Runs/_research 2026-10-05 SONY/`; every
document relied on is saved there as fetched, with a text extraction beside it. The file was then filled in one pass
after the reading, not question by question; see the self-audit.)*

**POSITION NOTE, declared before any verdict:** not checked. This run was dispatched under a blind rule that forbids
opening `PORTFOLIO.md`, the 2026-07-14 run file that covered this ticker, any other run file or holding review about Sony,
the session-state files and the queue register, and forbids trying to learn whether anyone holds the name. None of them
was opened.

**CONTAMINATION, declared.** (1) The dispatch names an earlier run file for this ticker (2026-07-14, pre-v4.1, run with
two other names), so I know the name was worked before; I do not know what it concluded. (2) To find the format of a
v5 run of a Japanese filer I listed the `Test Runs/` files dated 2026-10-0x and read the head of the Nihon Kohden run
(another company, not forbidden). The listing showed holding reviews dated today for six other tickers and none for
Sony; that is weak information about holdings and I have not used it. (3) The auto-loaded memory index speaks of the
queue in general ("nothing buyable"); nothing in it names Sony. (4) The session-start git status and the recent commit
messages name other tickers (BRK.B, CCB, TSCO) and nothing about Sony. (5) `tools/run.py SONY --quote 6758.T` was run
for its arithmetic lines; its output is defective for this filer (see Step 0) and nothing it printed is used.

**Fiscal-year labels.** Sony's year ends 31 March and it calls the year ended March 2026 "FY2025". This file writes years
by their end: **FY3/26** = April 2025 to March 2026; **Q1 FY3/27** = April to June 2026. Money is yen unless marked;
"bn" is billions of yen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ADR **$23.45**, NYSE close 2026-10-05; TSE **¥3,723**, close 2026-10-05 (Yahoo Finance chart API,
  `yahoo_SONY.json`, `yahoo_6758.T.json`; **aggregator, flagged** under operator rule 5). 52-week range on the TSE
  ¥3,043 to ¥4,776 (same source, flagged). USD/JPY 158.065 on 2026-10-05 (Yahoo `JPY=X`, flagged).
- **ADR ratio 1 ADS : 1 share**, from the depositary: Form F-6 filed 2025-03-14 by JPMorgan Chase Bank, N.A. as
  depositary (accession `0001193805-25-000308`, `F6_e664280_f6-sony.htm`): "each American Depositary Share representing
  one (1) share of common stock of Sony Group Corporation". JPMorgan succeeded Citibank, N.A. as depositary under the
  Second Further Amended and Restated Deposit Agreement of 2025-04-01 (exhibit 99(a) of the same filing). The 20-F cover
  says the same. Cross-check: ¥3,723 / 158.065 = $23.55 against $23.45 (0.4 percent, the two closes are hours apart).
- **Shares by class** (one class, common): the 20-F cover gives 5,907,667,254 outstanding at 2026-03-31. The Q1 FY3/27
  results 6-K gives issued 5,965,316,326 less treasury 92,854,256 = **5,872,462,070 outstanding at 2026-06-30**
  (6-K of 2026-07-31, accession `0001104659-26-088915`). Buybacks after that date: 37.4M shares July to September
  (buyback 6-Ks `0001104659-26-094573`, `0001104659-26-107340`, `0001104659-26-113566`), less option exercises, so about
  5,837M at 2026-09-30. The filed June figure is used. `Screens/cover_shares.py` was not run: the cover of a 20-F filer is
  read directly above.
- **Market cap:** 5,872.5M × ¥3,723 = **¥21,863bn** (about $138bn at 158.065).
- **Sovereign for the earnings currency (JPY):** **4.148%**, the 30-year JGB on 2026-10-02, from Japan's Ministry of
  Finance `jgbcme.csv` (issuing authority; saved as `jgbcme.csv`). The 10-year was 3.097 percent the same day. Sales by
  customer location FY3/26: Japan 10.6 percent, US 32.6 percent, Europe 22.7 percent (20-F, risk factors); the reporting
  currency is the yen and the sector method's CONVENTION C11 practice (run at the sovereign of the reporting currency,
  exposure stated) is followed by analogy.
- **Filings read** (operator rule 4):
  - **Form 20-F FY3/26**, filed 2026-06-18, accession `0001193125-26-274893` (`20F_FY3-26.htm`, text `20F_FY3-26.txt`):
    risk factors, Item 5 (segment discussion, liquidity, mid-range plan), Item 16E (purchases of equity), the
    consolidated statements, notes 4 (segments), 8, 9, 11, 27 and 33 (the Financial Services spin-off).
  - **Forms 20-F FY3/17 to FY3/25** (accessions `0001193125-17-203939`, `-18-196263`, `-19-175182`, `-20-179707`,
    `-21-195631`, `-22-183263`, `-23-169510`, `-24-167500`, `-25-143137`), for the condensed statements of "Sony
    without the Financial Services segment" (balance sheets 2016 to 2025, cash flows FY3/22 to FY3/25) and the segment
    profit tables FY3/15 onward.
  - **6-K of 2026-07-31**, Q1 FY3/27 consolidated results (`0001104659-26-088915`) and the presentation
    (`0001104659-26-088922`).
  - **6-K of 2026-08-11**, the definitive agreement with TSMC for the image-sensor joint venture
    (`0001104659-26-093634`).
  - **Buyback 6-Ks** of 2026-08-12, 2026-09-14 and 2026-10-05 (above).
  - **Form F-6** of 2025-03-14 (above).
  - **No proxy in the US sense**; Item 6 of the 20-F (directors and pay) is where it would be read. Not reached.
- **One figure cross-checked against the filed statement:** consolidated net cash provided by operating activities
  FY3/25 **¥2,321,675M** in the SEC XBRL facts (tag `ifrs-full:CashFlowsFromUsedInOperatingActivities`, 20-F FY3/25,
  `0001193125-25-143137`) equals the comparative column of the cash-flow statement in the FY3/26 20-F (F-10). Inventories
  at 2025-03-31, **¥1,310,770M**, also agree between the two. The FY3/26 XBRL facts were not yet in the SEC companyfacts
  file when fetched.
- `python tools/run.py SONY --quote 6758.T`: **not usable for this filer and not used.** It printed a USD sovereign
  (5.63 percent, the wrong currency), a share count of 1,250.7M (a pre-split US GAAP weighted average; the five-for-one
  split of 2024-10-01 is missed), and owner earnings from US GAAP tags that stop at FY3/21 and include the Financial
  Services segment. Every number below is taken from the filings by hand (`owner_cash_computation.py`, output beside it).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, so the 22 percent fall from the 52-week high says nothing by itself; "It just tells us prices"
**[M2006-077]**. The margin of safety is an attitude here: if the case needs pencil and paper "it’s too close to think
about" **[M1996-084]**. No macro view enters **[M2000-094]**: the memory-chip price surge, tariffs and the yen are carried
only as facts about the business, not as forecasts. The currency foundation bears on the holder: Sony earns mainly in
dollars and euros, reports in yen and would be held through a dollar ADR; the rows say only that "Any currency-related
investment is a bet on how government now, and in the future, will behave" **[M2011-025]**, and the run takes no currency
view. The analyst's habits govern the method: look for "what’s wrong in things" **[M2025-013]**, and ask "What do I not
know that I need to know?" **[M1999-129]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The **2026 Kumamoto Earthquake of 2026-07-28** is not in the FY3/27 forecast, "as it is currently difficult to
   reasonably estimate such impact" (6-K `0001104659-26-088915`). Sony's image-sensor fabs are in Kumamoto
   (20-F FY3/26, Item 4 property table: Sony Semiconductor Manufacturing, Kikuchi-gun, Kumamoto).
2. The I&SS segment swung from a loss of ¥7.8bn (FY3/17, the year of the 2016 Kumamoto earthquake) to a record ¥357.3bn
   (FY3/26); its capex plan was raised by about ¥200bn (20-F FY3/22), raised again by ¥0.4tn "mainly allocated to image
   sensor capital expenditures" (20-F FY3/23), then cut: Sony is "carefully selecting investments and reducing capital
   expenditures for the I&SS segment" (20-F FY3/26).
3. Sony's own one-year view of its sensor market is "cautious", the trend toward larger smartphone sensors "will
   moderate", and memory-market uncertainty "will remain" (20-F FY3/26, I&SS).
4. The sensor strategy now rests on a joint venture with TSMC: Sony to contribute about ¥465bn, TSMC about ¥282bn, volume
   production "expected to commence" in 2029, further investment "on the premise that they would receive support from
   the Japanese government" (6-K `0001104659-26-093634`).
5. FY3/21: the mobile sensor market shifted "mainly resulting from the impact of U.S.-China trade friction" and Sony set
   out "to recover market share on a volume basis" (20-F FY3/21). One government decision about one customer moved the
   segment.
6. Apple announced on 2025-08-06 that it is "working with Samsung at its fab in Austin, Texas, to launch an innovative new
   technology for making chips" (Apple newsroom release, `peers/apple_20250806.html`). The release does not say image
   sensors; press reports that it does are aggregator readings, **flagged and not relied on**.
7. Impairments in FY3/26: Bungie ¥120.1bn (G&NS), game content ¥56.3bn, Pixomondo ¥27.1bn plus shutdown costs (Pictures),
   Sony Honda Mobility equity loss ¥44.9bn (All Other) (20-F FY3/26, Item 5 and note 11).
8. Stock-based compensation expense rose from ¥11.1bn (FY3/22) to ¥39.1bn (FY3/26) (20-F notes on share-based payment).
9. Sony features "Adjusted OIBDA" by segment in its results presentation (6-K `0001104659-26-088922`).
10. The memory-semiconductor price surge is named as a cost to PlayStation hardware and to the next-generation platform
    (20-F FY3/26 risk factors; Q1 FY3/27 presentation: "investments for the next-generation platform").
11. The competitor in home consoles reports falling hardware: Microsoft's XBOX revenue fell 7 percent and XBOX hardware
    revenue 29 percent in the year to June 2026 (10-K `0001193125-26-323660`).
12. Five-year average owner cash is ¥601.7bn; the last two years average ¥1,302.8bn. The base years are aberrational
    (inventory build of ¥560bn in FY3/23), "a base year in which earnings were poor can produce a breathtaking, but
    meaningless, growth rate" **[L2005-003]**.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin: it would be bought with cash, unlevered, never on margin ("borrowed
money has no place in the investor's tool kit" **[L2014-005]**), sized so that no outcome at Sony threatens what the buyer has and needs: "We are never going to risk what we have and need
for what we don’t have and don’t need." **[M2012-081]**; "Never risk permanent loss of capital." **[L2023-005]**. Nothing in an ADR creates a call on the holder. No breach.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years. So I’ve got some notion of how the industry will develop and where the company will stand within
the industry." **[M2012-065]**; "a reasonable probability of being able to asses where the business will be in 10 years"
**[M2000-037]**. Sony is a holding company of unlike businesses, so it is read **by its parts** (CONVENTION of Q1, ours):
"A holding company is understood when each part that matters to its earnings can be understood"; "a part that cannot be,
and that matters, keeps the whole outside the circle, since doubt means outside" **[M2002-092]**. The tension against that
convention is carried OPEN: Berkshire bought trading houses "that we could understand as a group, although it didn’t mean
we had deep understanding on any" **[M2023-031]**. Businesses with different balance sheets are read separately
**[L2008-005]**.

**What the parts are, from the filings.** Segment figures FY3/26 (20-F FY3/26, note 4) and Q1 FY3/27 (6-K
`0001104659-26-088915`); segment operating income includes equity-method results and excludes corporate costs.

| Part | Sales FY3/26 | Op. income FY3/26 | Share of segment OI | D&A FY3/26 | R&D FY3/26 | Op. income Q1 FY3/27 (share) |
|---|---|---|---|---|---|---|
| Game & Network Services (G&NS) | 4,685.7 | 463.3 (after Bungie impairment 120.1) | 31.8% | 147.5 | 316.1 | 202.0 (41.7%) |
| Music | 2,120.1 | 447.0 (incl. Peanuts gain 34.7) | 30.7% | 130.9 | n/d | 105.9 (21.9%) |
| Pictures | 1,499.3 | 104.9 | 7.2% | 517.8 (mostly film cost amortization) | n/d | 24.8 (5.1%) |
| Entertainment, Technology & Services (ET&S) | 2,260.5 | 158.6 | 10.9% | 103.1 | 138.0 | 42.6 (8.8%) |
| Imaging & Sensing Solutions (I&SS) | 2,151.5 | 357.3 | 24.5% | 265.1 | 238.5 | 122.2 (25.2%) |
| All Other | 89.1 | (74.6) | (5.1%) | 3.9 | | (13.3) |
| 16.40% stake in Sony Financial Group (SFGI), equity method since 2025-10-01 | | | | | | |

The filing gives no asset or capex figure by segment ("The CODM does not evaluate segments using discrete asset
information", note 4), with one exception: Sony "invested 227.4 billion yen and 246.7 billion yen of capital in the fiscal
years ended March 31, 2025 and 2026, respectively, mainly for the purpose of increasing image sensor production capacity"
(risk factors). Against group capex of ¥621.0bn and ¥457.7bn, that is 37 and 54 percent of the group's capital spending
going to the part that earned a quarter of the profit.

**The Financial Services remainder, and the sector method.** The spin-off of 2025-10-01 distributed SFGI shares one for
one and left Sony with **16.40 percent**, accounted for by the equity method (20-F, note 33). The shares distributed were
valued at ¥955.7bn (note 20), so the retained stake was worth about ¥187bn on that date (CONVENTION of arithmetic: the
distributed 83.60 percent grossed up to 100 percent and multiplied by 16.40 percent), under 1 percent of the market value.
SFGI's business is mainly life insurance (Sony Life), with a bank and a non-life insurer; life books with cash-out
features are outside the sector method by its CONVENTION C10, so stage zero sends the stake out of that method, and under
Q4's CONVENTION it counts only as dividends received. It does not matter to the whole and is not read further.

**The parts, one by one** (key variables first, as "the first step" **[M1998-044]**):

- **Music (31 percent of segment profit).** Key variables: streams and their price, Sony's share of them, the catalogue.
  Operating income ran 58 (FY3/15), 87, 76, 128, 232, 142, 188, 211, 263, 302, 357, 447 (FY3/26) (segment tables of the
  20-Fs FY3/17, FY3/19, FY3/21, FY3/23, FY3/25, FY3/26; the FY3/21-onward figures are IFRS). Competitor from its own
  filing: Warner Music Group, year to 2025-09-30, revenue $6,707M, operating income $694M (10.3 percent); Recorded Music
  operating income $850M on $5,408M, Music Publishing $224M on $1,306M (10-K `0001319161-25-000034`). Sony Music earned
  21.1 percent on sales (19.4 percent without the Peanuts remeasurement gain). Universal Music Group's results were not
  obtained from a primary filing (its investor site would not serve them). The doubt the filing itself names: "the
  prevalence of digital streaming networks" and "increasing concentration of digital music distributors" (20-F risk
  factors), and AI-made music, which Sony addresses in its strategy text. Reading: the economics of a catalogue earning
  royalties on a growing streaming base can be pictured ten years out in rough outline. **Inside, provisionally.**
- **G&NS (32 percent; 42 percent in Q1 FY3/27).** Key variables: the installed base of the next console generation, the
  share of digital game spending that passes through the PlayStation Store, PS Plus subscriptions, first-party hits.
  Operating income ran 48 (FY3/15), 89, 136, 177, 311, 238, 342, 346, 250, 290, 415, 463. The franchise is thirty years
  old, and the test "Is the forecast about customers or about technology?" **[M2017-019]** points mostly to customers.
  Against it: the next platform is being paid for now in a memory-price surge; Microsoft's XBOX revenue fell 7 percent and
  its hardware 29 percent (10-K `0001193125-26-323660`); Nintendo's net sales doubled to ¥2,313.1bn with operating profit
  ¥360.1bn in its Switch 2 launch year (Consolidated Financial Highlights, 2026-05-08, company IR file
  `peers/nintendo_260508e.pdf`; a TSE filer, no SEC accession); and Sony's own live-service bet failed (Bungie ¥120.1bn,
  game content ¥56.3bn impaired). Whether play stays on a console Sony makes, ten years and one or two hardware
  generations out, is a question I have a model for but a wide one ("how far off we can be" **[M2011-084]**). **Doubt,
  carried; not the deciding part.**
- **Pictures (7 percent).** Hit-driven film and television, plus Crunchyroll (over 21M paid subscribers). Buffett on
  Paramount: "owning Paramount made me think even further [...] about the whole question of what people do with their
  leisure time. And, you know, what the governing principles are of running an entertainment business of any sort"
  **[M2024-055]**. **Doubt; small.**
- **ET&S (11 percent).** Cameras, audio, televisions; the 20-F names "the ongoing price erosion that frequently affects
  its consumer products", and the television business is going into a partnership with TCL. **Doubt; small.**
- **I&SS (25 percent of profit, about half of capex).** Image sensors, mainly for smartphones, made in Japan in fabs Sony
  owns. Key variables: sensor content per phone (Sony expects the size trend to "moderate"), the sourcing decisions of a
  few phone makers ("changes in the financial condition or business decisions of Sony’s major customers", risk factors),
  the process and stacking race ("increase density in the horizontal plane through process node adaptation [...] and
  [...] in the vertical plane through multi-layered stacking technology"), a fab that does not yet exist (the TSMC joint
  venture, volume production in 2029), government support, and earthquakes. Operating income ran 96 (FY3/15), 14.5,
  (7.8), 164, 144, 236, 146, 156, 212, 194, 261, 357: a loss to a record within the decade, through an earthquake, a trade
  war and two capex reversals. Competitor rows could not be built from filings: Samsung does not report image sensors
  separately and is not an SEC filer; OmniVision's parent files in China; Sony's own share claims are its own. The tests
  bite here:
  - *Is the technology component of significance?* "if something comes in where there’s a technological component
    that’s of significance, or where we think the future technology could hurt the business as it presently exists [...]
    it won’t make it through the filter." **[M1998-008]**; the acquisition criteria ask for "(5) Simple businesses (if
    there's lots of technology, we won't understand it)" **[R1997-001]**.
  - *Would the insiders write it down?* "they would not want to put down on paper their predictions about where 10
    companies you would choose in the tech field would be in 10 years, in terms of their economics. They would say,
    “That’s too hard.”" **[M2000-105]**. Sony itself will not write down the next year's sensor market except as
    "cautious", and its three-year capex plan for the part changed direction twice in four years.
  - *Can I name the winner, not just the industry?* "there’s industries we know that may have a wonderful future, but we
    don’t have the faintest idea who the winners will be" **[M2012-067]**; "Just because Charlie and I can clearly see
    dramatic growth ahead for an industry does not mean we can judge what its profit margins and returns on capital will
    be" **[L2009-005]**. Sony leads today; I have no basis to say it leads in 2036.
  - *Do the past statements tell me the future ones?* **[M2008-033]**. They do not: the segment's record is a range from
    a loss to ¥357bn, and the filing gives no segment assets from which its return on capital could even be read.
  - *Does change threaten it?* "a business that must deal with fast-moving technology is not going to lend itself to
    reliable evaluations of its long-term economics" **[L1993-023]**; "whenever we look at a business and we see lots of
    change coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**.
  **Outside the circle, and it matters.**

**The case for IN, stated as well as I can** **[M2016-055]**. Sony is now chiefly an entertainment company: games, music
and pictures earned 70 percent of segment profit in FY3/26; the sensor business is the world leader, is moving to a
lighter capital model through the TSMC venture, and could be treated as an unknown part of a known whole, the way the
trading houses were read "as a group" **[M2023-031]**. The answer from the rows: the part is a quarter of the profit and
half of the capital spending, which is not a part that does not matter; and a wide uncertainty is not to be cured by a
bigger discount, "we don’t really try to compensate for that sort of thing by having some extra large margin of safety.
We really want to try to go on to something that we understand better." **[M2007-022]**. The by-parts reading is our
CONVENTION, and **[M2023-031]** stays OPEN against it.

**Which cause.** The deciding question is where Sony's image-sensor economics and competitive position will be in ten
years. That is a forecast the industry's insiders would not write down **[M2000-105]**; the rows say of such fields "We
couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries"
**[L1993-023]** and "Our problem -- which we can't solve by studying up -- is that we have no insights into which
participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**. More reading would not
change that, "we’re not going to learn enough in the followings five months to make up for the fact that we went in
deficient in the first place" **[M2008-086]**. The cause is **NATURE**, not WORK. A lower price does not reopen it: "It
doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we
don’t know how to evaluate it." **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)** at Q1 **[M2006-013]**, **[M2002-092]**, **[M1998-008]**, **[M2000-105]**, decided by the
  I&SS part (24.5 percent of segment operating income FY3/26, 25.2 percent in Q1 FY3/27; ¥246.7bn of the group's
  ¥457.7bn capex FY3/26, 20-F `0001193125-26-274893`), with G&NS carried as a second doubt. The file closes here.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**NOT REACHED.** (The competitor figures gathered for Q1 are recorded in the computation section below; they are not a
castle verdict.)

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.**

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The decade of balance sheets was read as evidence for Q1 and is set out in the computation section; it
carries no Q4 verdict.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** The buyback facts are recorded below without a verdict.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.**

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.**

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** What the draft has the buyer do with a TOO HARD: nothing; "if we have trouble finding things within our
circle, we will not enlarge the circle. You know, we’ll wait." **[M1995-018]**. Outside the circle the miss is not
counted as an error **[M2018-087]**, **[M2001-006]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.**

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: Sony is a holding company read by its parts, and the image-sensor part (a
quarter of segment profit, about half of capital spending) is a fast-moving-technology business whose ten-year economics
its own management will not forecast a year ahead; "If something is not very predictable, forget it." **[M1998-044]**.
NATURE, not WORK: the industry is the roadblock, not my reading **[L1993-023]**, **[L1999-018]**, so no research pass is
opened and a lower price does not reopen the file **[M2000-038]**. Q7 was not reached; no range is set beside the price.

---
## COMPUTATION — NOT A CLEARANCE
*Everything below was gathered while answering Q1 or after the file closed. It carries no verdict and no entry
language. It is kept so that a later reader does not repeat the fetch.*

**1. The balance sheets, ten years, before the income account** (operator rule 4 and the habit of **[M2025-032]**).
"Sony without the Financial Services segment", as Sony itself presented it (unaudited condensed statements in Item 5 of
each 20-F); from 2026-03-31 the consolidated statement, the segment having been spun off. US GAAP to March 2020 (and a
US GAAP column for March 2021), IFRS from April 2020. ¥bn. "n/s" = not separated in the schedule.

| 31 March | Total assets | Cash | Trade receivables | Inventories | PP&E | Goodwill + intangibles + content/film | Debt (IFRS: incl. leases) | Stockholders' equity |
|---|---|---|---|---|---|---|---|---|
| 2016 | 5,956.6 | 749.9 | 847.8 | n/s | 801.5 | n/s (film 301.2) | 769.0 | 1,796.9 |
| 2017 | 5,817.1 | 691.8 | 947.6 | n/s | 735.6 | n/s (film 336.9) | 716.1 | 1,770.6 |
| 2018 | 6,256.0 | 1,193.2 | 1,003.6 | 692.9 | 715.8 | 1,343.4 | 710.3 | 2,173.1 |
| 2019 | 7,068.4 | 960.5 | 1,055.7 | 653.3 | 752.8 | 2,045.3 | 562.8 | 2,850.4 |
| 2020 | 7,373.0 | 962.3 | 1,000.0 | 590.0 | 890.6 | 2,056.8 | 480.0 (+ op. leases 333.3) | 3,159.1 |
| 2021 (US GAAP / IFRS) | 9,017.0 / 8,919.3 | 1,289.8 | 1,070.1 / 1,261.3 | 637.4 / 636.7 | 966.2 / 971.3 | 2,218.9 / 2,113.6 | 614.2 / 938.8 | 4,396.8 / 4,341.1 |
| 2022 | 10,239.0 | 1,160.5 | 1,478.6 | 874.0 | 1,095.2 | 2,672.5 | 916.3 | 5,156.1 |
| 2023 | 11,950.1 | 724.4 | 1,668.3 | 1,468.0 | 1,329.2 | 3,322.6 | 1,315.4 | 6,006.3 |
| 2024 | 13,888.4 | 993.3 | 2,033.2 | 1,518.6 | 1,508.2 | 3,953.5 | 1,583.0 | 7,062.7 |
| 2025 | 14,851.4 | 1,764.7 | 1,820.7 | 1,310.8 | 1,500.0 | 4,342.4 | 1,635.5 | 7,695.5 |
| 2026 (consolidated) | 15,683.5 | 2,208.9 | 1,821.9 | 1,227.4 | 1,453.8 | 4,892.1 | 1,669.7 (of which leases 627.7) | 8,119.0 |

Sources: 20-F FY3/17 p.54-55; FY3/19, FY3/21, FY3/22, FY3/24, FY3/25 condensed statements of financial position; 20-F
FY3/26 F-4 to F-5 (accessions in Step 0). The ex-FS equity from 2021 to 2025 carries the investment in Financial Services
at cost (¥550.5bn); the 2026 equity carries the SFGI stake inside the ¥483.7bn of equity-method investments.

What moved, and what the figures cannot say: equity rose about 4.5 times in ten years, and goodwill, intangibles and
content rose about 3.6 times from 2018, so most of the equity built went into bought or produced intangibles (EMI Music
Publishing in 2018, Crunchyroll, Bungie, music catalogues, Peanuts). Inventories more than doubled from March 2021 to
March 2023 (¥636.7bn to ¥1,468.0bn) and have since been worked down by about ¥240bn. PP&E roughly doubled from 2018 to
2024, the sensor build, and has since flattened. Debt including leases is modest against cash: at 2026-03-31 borrowings
excluding leases were ¥1,042.0bn against cash of ¥2,208.9bn. Recognized deferred tax assets rose from ¥95.1bn (2018,
US GAAP) to ¥560.8bn (2026). What the statements cannot say: the capital each part uses, since no segment assets are
disclosed; that is the gap that matters most for a holding company read by its parts.

**2. Owner cash after every real cost, five years** (`owner_cash_computation.py`; ¥bn). OCF less payments for PP&E and
intangibles, less lease cash, less stock-based compensation expense. FY3/22 and FY3/23 from the ex-FS condensed cash
flows (20-F FY3/23); FY3/24 to FY3/26 from continuing operations (20-F FY3/26). Lease cash for FY3/22 and FY3/23 is the
filed "Net cash outflows for leases" (which includes lease interest, so it overstates the deduction by at most about
¥10bn a year on the FY3/24 comparison); thereafter "Payments of lease liabilities". Content spending sits inside OCF
("Increase in content assets"), so it is deducted.

| Year | OCF | Capex | Leases | SBC | Owner cash |
|---|---|---|---|---|---|
| FY3/22 | 813.3 | 420.5 | 83.5 | 11.1 | 298.1 |
| FY3/23 | 415.5 | 590.3 | 89.7 | 15.8 | (280.3) |
| FY3/24 | 1,103.6 | 605.8 | 90.8 | 21.7 | 385.4 |
| FY3/25 | 1,971.3 | 621.0 | 98.9 | 29.4 | 1,222.0 |
| FY3/26 | 1,966.3 | 457.7 | 85.9 | 39.1 | 1,383.6 |
| **Five-year average** | | | | | **601.7** |

Beside it: business acquisitions took ¥1,240.0bn over the five years (¥248.0bn a year), not deducted above; inventory
absorbed a net ¥324.1bn over the five years. Depreciation of PP&E plus amortization of intangibles was ¥513.1bn (FY3/25)
and ¥489.1bn (FY3/26) against capex of ¥621.0bn and ¥457.7bn (20-F FY3/26, notes 9 and 11). At the price the five-year
average is a 2.75 percent owner-cash yield on ¥21,863bn; the two-year average (¥1,302.8bn) is 5.96 percent. Capitalized at
the JGB 30-year with no growth, the five-year figure gives about ¥2,470 a share and the two-year figure about ¥5,348 a
share, against ¥3,723. The two bases differ by more than two to one before any growth is assumed, which is the
base-year problem of **[L2005-003]** in numbers. This is arithmetic, not a range, and not a verdict.

**3. The competitor rows gathered** (for a later Q2, if the file were ever reopened on new facts; not a castle verdict).
| Part | Sony FY3/26 | Competitor, own filing |
|---|---|---|
| Games | G&NS sales ¥4,685.7bn (about $31.1bn at the year's average ¥150.7), OI ¥463.3bn (9.9 percent; 12.4 percent before the Bungie impairment) | Microsoft XBOX revenue $21,790M, year to 2026-06-30, down 7 percent; hardware down 29 percent (10-K `0001193125-26-323660`). Nintendo net sales ¥2,313.1bn, operating profit ¥360.1bn (15.6 percent), year to 2026-03-31 (company IR release 2026-05-08, TSE filer) |
| Music | Sales ¥2,120.1bn, OI ¥447.0bn (21.1 percent) | Warner Music Group revenue $6,707M, OI $694M (10.3 percent), year to 2025-09-30 (10-K `0001319161-25-000034`). UMG: not obtained |
| Image sensors | Sales ¥2,151.5bn, OI ¥357.3bn (16.6 percent) | No competitor files segment results for image sensors that I could reach (Samsung: not separated, not an SEC filer; OmniVision: China filer). Gap |
| Pictures | Sales ¥1,499.3bn, OI ¥104.9bn | Not gathered (the part was not deciding) |

**4. The buyback and its stated rule** (for Q6, not reached). Sony states its returns as a total payout ratio "aiming for
approximately 40%" in FY3/27, with repurchases inside a ¥1.8tn "strategic investment" budget (20-F FY3/26, Item 5.D). The
facilities name a maximum yen amount and share count and no price: FY3/26, 140.9M shares for ¥522.1bn at an average
¥3,705.97 (Item 16E); the facility of 2026-05-08, up to 230M shares or ¥500bn to 2027-05-10, of which 74.47M shares for
¥263.4bn (about ¥3,536 average) were bought by 2026-09-30 (6-K `0001104659-26-113566`). Q6's test for a buyback with no
stated price reads the prices paid against the bottom of the Q7 range, which was not built.

---
## SELF-AUDIT
- [ ] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      *Copied before any fetch: yes. Written question by question: no, filled in one pass after the reading. Committed:
      no, by instruction of the dispatch ("Do not commit").*
- [x] Every v5 id resolves (grep it in `principle_ledger_v5.csv`); every filing fact has its accession; no number
      without a row or a filing. *Ids checked by script against the CSV; Nintendo's figures carry the company document
      and date, as a TSE filer has no SEC accession; aggregator prices are flagged.*
- [x] The order was kept; the first STOP that failed closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; aggregator quotes flagged. *Owner cash is shown only in the computation section.*
- [x] Contrary evidence was written down as it was found **[M1997-127]**.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII). *Not a point-in-time run; anchor is today.*
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII). *None were used: its arithmetic was wrong for
      this filer (Step 0).*
- [x] `python tools/check_framework.py` PASS before the commit. *Run after writing on 2026-10-05: PASS. A script check
      found no v4 (E-) ids and all 39 cited M, L and R ids in `principle_ledger_v5.csv`. No commit was made.*

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The holding-company convention has no test of "matters".** Q1 says a part "that matters to its earnings" keeps the
whole outside if it cannot be understood, but gives no line: is it a share of profit, of capital, of value? Here the
answer was easy (a quarter of profit, half of capex), but a part at 5 or 10 percent would split two analysts. I used
profit and capital together and said so. (2) **The dispatch named a "currency row for a yen earner held through a dollar
ADR" in the foundations; there is none.** The foundations carry one currency sentence (**[M2011-025]**) and the sector
method's C11 is a practice "carried until decided"; nothing tells a v5 run which sovereign to use when the reporting
currency (yen) differs from most of the earnings (dollars and euros) and from the holder's (dollars). I used the JGB
under operator rule 5 and stated the mix. (3) **`tools/run.py` is wrong for a 20-F filer that changed GAAP and split its
shares**: USD sovereign, a pre-split weighted-average share count, US GAAP tags ending FY3/21 with the Financial Services
segment inside. Part VII already says to read only its arithmetic lines; for this filer even those were wrong, and a run
that trusted them would have shown an 18 percent "yield". (4) **The template's write-early line conflicts with a dispatch
that forbids commits**; I recorded the conflict rather than tick the box. (5) **Q1 test 3 ("Do the past statements tell me
the future ones?") meets a filer that discloses no segment assets.** The framework has no line for a holding company
whose filing withholds the capital of its parts; I treated the absence as evidence against understanding the part, which
is a reading, not a rule.
