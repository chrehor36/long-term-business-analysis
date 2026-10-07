- **JAKK (JAKKS Pacific, Inc.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 22 of 218. Register entry 154** (re-derived, not inherited: line-start
  `- **` counted **by index** in the slice from this file's `## COMPLETED FROM THE QUEUE` heading
  line (index 501) to the line **starting with** `## THE WRITE-EARLY PROTOCOL` (index 12430 - an
  exact-string match returns nothing there, it carries trailing text). **153 entries stood above
  this one**, which is exactly what the dispatch brief predicted. **JAKK appeared ONCE elsewhere
  in the file and it is not a register entry**: the HAS entry cites it as a peer -
  *"unleveraged NTOA vs MAT 33.9 / JAKK 8.8 / FNKO -45.6; JAKK files 'the toy industry has no
  significant barriers to entry'"* - so an independent prior run had already read this 10-K and
  pulled the same sentence. After insertion: 154.)
  **Price US$24.085**, the live quote at **2026-09-21 09:44 ET**, aggregator (Yahoo Finance chart
  endpoint), **flagged as an aggregator, live quote only**; raw metadata saved to
  `Test Runs/_research 2026-09-21 JAKK/price_raw_aggregator.json`. The seven prior closes were
  23.79 / 24.17 / 24.33 / 24.31 / 24.24 / 24.33 / 24.13, so the quote is not an outlier print.
  **Shares 11,445,012, a SINGLE class of common stock, $.001 par**, read off the cover of the
  **10-Q for the quarterly period ended 2026-06-30, accession `0001185185-26-003186`, filed
  2026-07-31**, as-of date 2026-07-31, verbatim: *"The number of shares outstanding of the
  issuer's common stock is 11,445,012 as of July 31, 2026."* No split after the measurement date
  (`split_factor_after('JAKK','2026-06-30')` = 1.0; there IS a 1-for-10 reverse split dated
  2020-07-10, older than every anchor used, which does not enter the cap but does enter any
  per-share series read from a pre-2020 filing). No second class - the FY2025 10-K cover says
  *"being the only class of its common stock"*, and the Series A Senior Preferred was **redeemed
  in full on 2024-03-11** for $20.0M cash plus 571,295 common shares at $26.26.
  **CAP, STRUCK BY HAND: 11,445,012 x $24.085 = $275.65M.** The screen carried **291**.
  **-5.3%, and the screen cap REPRODUCES EXACTLY**: at the SAME share count and the close of
  2026-08-28 ($25.42) the formula gives **$290.93M**. A stale-price difference, not a count
  error - the ADM/IIIN/SGC shape, not the BELFB (6.29x) or MCFT (1000x) shape.
  **Sovereign 5.34%, US Treasury daily par yield curve, 30-year par yield, 2026-09-18** (the
  newest published print; 2026-09-21 is a Monday), struck fresh from the issuing authority
  through `tools/sources.py`. **FRED DGS30 not used.** Not inherited from the brief, which
  deliberately supplied none.
  **PASS/FAIL LINE: Q1 IN, Q2 OUT. Q2 closed the file, on [E3-03] criterion 2 - the product has
  close substitutes, and the registrant says so itself.** The FY2025 10-K (accession
  `0001185185-26-000723`) states the whole case in its own risk factors: *"**Sales of products
  under trademarks or trade or brand names licensed from others account for substantially all of
  our net sales**"*; *"the **toy industry has no significant barriers to entry**"*; *"Our
  competitors have obtained and are likely to continue to obtain **licenses that overlap our
  licenses**"*; and JAKKS competes *"directly against one or both of two of the toy industry's
  most dominant companies, **Mattel and Hasbro**"*, plus **Rubies II** in costumes.
  **THE COMPETITOR ROW, and it is the finding**: royalty expense as a percentage of net sales,
  FY2023-25 aggregate, each from `us-gaap:RoyaltyExpense` in that registrant's own 10-K -
  **JAKK 16.05% · FNKO 16.60% · HAS 7.81% · MAT 4.69%**. The row splits into the two companies
  that **own** their characters and the two that **rent** them; the renters pay **2.1x to 3.4x**
  the rent and cannot cover it (operating margin over the same window: **JAKK +5.73%, FNKO
  -4.47%**, against **MAT +11.15%** and HAS -6.05% / +9.94% ex $2,213.1M of goodwill impairment
  in FY2023+FY2025). All four registrants' sales fell over the window (-1.6% to -31.3%), so the
  variable that separates them is not the industry, it is **who owns the character**. Class
  **NONE, not PROVISIONAL**: no moat is claimed, and every peer I could not obtain (Rubies II,
  MGA, Basic Fun, Moose, LEGO private; Spin Master SEDAR+, Bandai Namco TDnet) is a **further**
  competitor in a market the registrant says has no barriers to entry, so completing the row
  changes the count and not the finding.
  **[E4-04] scores the same way independently**, applied as the 2026-09-20 ruling requires (this
  IS judgeable from the filings, so NOT a perimeter close): the advantage is **bought again each
  licence term rather than defended**, and the FY2025 MD&A attributes its own 19.0% segment
  decline to *"limited theatrical releases"* and to *"lower Nintendo sales"* - **[E3-51]**'s
  surfer, not the wave.
  **FOUR SCREEN FLAGS, ALL FOUR RESOLVED AT STEP 0.** (1) `wc_note` **336% REPRODUCES to the
  decimal and the finding around it is BROKEN**: FY2021 operating cash was **NEGATIVE $5,879k**,
  so no line "made the cash"; accounts payable was the **THIRD**-largest working-capital line
  behind inventory (7.71x OCF) and receivables (7.44x); the FY2021 liquidity note names those two
  and never mentions payables; and **`WC_TAGS` reads only `IncreaseDecreaseInAccountsPayable`,
  understating its own filed line by 27%** (the filed line is $25,017k including the Meisheng
  related-party half, a ratio of **425%**). **The tag list contains no receivables tag and no
  inventory tag, so the flag can only ever name a payable** - a tooling defect reported to the
  operator, not fixed here. (2) `best_year_dep` **0.44** and `best_year_dep_oe` **0.892**
  **REPRODUCE to three decimals**; the two years are **FY2022 and FY2023**, and the three
  remaining years of the priced window average **MINUS $3.34M**. (3) Both level-shift **refusals
  were correct and are completed**: the truncated strings finish at "$-16.2M to $70.6M" (OE) and
  "$-5.9M to $86.1M" (OCF), and the full **seventeen** filed years were rebuilt - **eight of
  seventeen are negative**, FY2013+FY2014 together consumed **$124.7M** of owner earnings.
  (4) `spread_caveat` obeyed: the band rebuilt across **seven** windows gives roughly **$7M to
  $13M** on the full filed history against the screen's **$19M to $22M**, and **-$3.8M to +$22.0M**
  across all constructions. Headed **COMPUTATION - NOT A CLEARANCE**; no valuation reported.
  **PERIMETER, from fields the screen left EMPTY** (empty is not cleared): the **Series A
  Preferred redemption of 2024-03-11** issued 5.0% of today's share count and paid out $20M inside
  the priced window; the **JPMorgan ABL was replaced by a BMO revolver on 2025-06-24** with a
  3.00:1.00 interest-coverage covenant; **Hong Kong Meisheng ceased to be a related party** after
  the 2025 annual meeting while remaining a **$75.3M (2025) / $98.4M (2024)** contract manufacturer
  - 13.2% and 14.2% of net sales, so *less* disclosure on a relationship that did not shrink; a
  **dividend was initiated in 2025** ($11.2M) in the year owner earnings went negative, funded from
  cash and not from issuance (ATM never drawn, the 2022 shelf **expired unused**, a new S-3 filed
  2025-10-29); and the Q2 FY2026 10-Q carries **$11.1M of IEEPA tariff refunds** in non-operating
  income which the earnings release itself names as the driver of the quarter's swing to profit -
  **[E4-41]**, removed before any mean is trusted.
  **RECORDED, NOT SCORED** (Q3 was never reached and cannot promote a name **[E2-37, E2-38,
  E3-39]**): JAKKS furnishes its earnings release as **EX-10.1, not EX-99.1** - a retrieval hazard
  for this queue; **[E4-29] fires** (two of seven headline bullets are Adjusted EBITDA and TTM
  Adjusted EBITDA, defined to add back *"restricted stock compensation expense"* against $10.9M of
  FY2025 SBC), and the **DEF 14A of 2026-04-22 says bonus pay has been based "exclusively upon
  Adjusted EBITDA" since at least 2019, "as adjusted in the sole discretion of the Compensation
  Committee"**, with a 2025 bonus *"based solely upon the market performance of our common stock"*
  (**[E3-50]**); **no guidance and no growth target anywhere** - [E4-22]'s third flag does NOT
  fire; share count **+17.7% since Nov 2022** but with no market issuance, so **[E5-15] does not
  fire either**; and the proxy's self-disclosed Pay-versus-Performance correction is a deviation
  **toward** candor **[E2-69]**. **[E5-11] strength (3)**, where this name's arithmetic is
  interesting, is a *licence* obligation and not debt: **minimum royalty guarantees $189.8M at
  2025-12-31, $57.4M due within twelve months**, up **2.6x** from $71.9M/$31.0M at 2021-12-31
  while sales fell; balance-sheet debt is essentially gone.
  **[E4-51], the strongest fact AGAINST this verdict, and it survives**: gross margin **ROSE**
  26.5% → 32.4% (FY2022-25) through a 28.3% revenue collapse, the balance sheet went from **$2.9M
  of equity (2019) to $249.1M (2025)** with all term debt and the preferred retired, and **Q2 2026
  net sales were +17%**. It does not move the verdict because the FY2025 MD&A attributes the gross
  margin to *"lower inventory obsolescence costs"* while noting *"royalty rates were higher
  year-over-year"*; Costumes' gross margin went the **other** way on *"higher royalty guarantee
  shortfalls"*; **operating margin fell 8.31% → 2.49% and pre-tax return on average equity 49.5% →
  26.8% → 18.5% → 6.0%** over the identical window; and a margin series cannot answer a question
  about **substitutes at the buyer**, which is what criterion 2 asks. The deleveraging is conceded
  and is **[E2-38]** - *"Good jockeys will do well on good horses, but not on broken-down nags."*
  **NO BAND ARMED, NO PORTFOLIO ROW** - the QLYS ruling: this failed on the **business**, so the
  reversal condition is recorded in words in the run file. **JAKKS becomes re-runnable only if the
  royalty ratio falls decisively and durably toward the IP-owners' 5-8% of sales** - wholly-owned
  brands carrying the majority of net sales - **or if the minimum-guarantee obligation shrinks
  against a rising sales base.** A good quarter does not do it; a share price does not do it.
  Run file: `Test Runs/2026-09-21 Run - JAKK JAKKS Pacific.md`; research folder
  `Test Runs/_research 2026-09-21 JAKK/`.
