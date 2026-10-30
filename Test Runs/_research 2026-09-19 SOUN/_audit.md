---
## SELF-AUDIT
- [x] Questions answered in order; the file stopped at Q2 (OUT) and Q3-Q6 are labelled recorded, not governing.
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q1 IN rests on the filed faces; Q3's IN is the binary only).
- [x] No UNRESEARCHED verdict. The unfiled items (the exact LivePerson merger-share count, the cash LivePerson delivered) are named with
      the document that will carry them (the Q3 2026 10-Q) and neither can change the Q2 finding.
- [x] No UNKNOWABLE verdict; the case for it at Q1 is recorded and the reason it was not taken is stated; at Q4 every window is negative.
- [x] Step 0: the filing was read (10-K FY2025 `0001840856-26-000006`, 10-Q Q2 2026 `0001840856-26-000022`, and the others listed), and
      FY2025 operating cash and stock compensation were cross-checked against the filed face (identical to companyfacts); the FY2021
      operating cash was found NOT to match (companyfacts carries the SPAC shell's) and the filed face was used.
- [x] Owner earnings on multi-year means (five-year default, four, three, twelve months), both (c) ends shown, (c) disclosed as a
      judgment; the ten-year window is named as not filed.
- [x] Competitor row filled: four filers (Cerence, LivePerson, Five9, NICE), same metrics and window, from their filed annual statements
      as transcribed, one Cerence figure checked to its face; the unsegmented and non-SEC rivals named and the reason they are absent
      stated.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated 09/18/2026, struck by this run.
- [x] Value stated as a range: none positive on any window; not a point estimate.
- [x] One bar only, and neither applied (nothing above zero to screen); windage count zero.
- [x] Price dated (2026-09-18 close), aggregator flagged, corroborated at the LivePerson closing terms (implied VWAP about $7.08 against
      Yahoo's late-August closes).
- [x] Share classes summed only after the charter was read (one-for-one conversion, ratable dividends and liquidation); the cover count
      and the post-closing pro forma both shown.
- [x] SBC resolved and complete: the add-back plus the SBC capitalised into software; the grant-value measure [E3-70] computed from the
      RSU table; earn-out shares identified as acquisition consideration, not pay.
- [x] Deal read (ROKU lesson): SoundHound the acquirer, the LivePerson deal closed 2026-09-04, no offer for SOUN; ATM programmes and
      the absence of convertibles recorded.
- [x] Every ledger id cited was checked against `principle_ledger.csv` (one row each).
- [x] Run committed to git (template `e1a6ce1`, Step 0 `74456b3`, Q1-Q2 `42d9d26`, Q3-Q6 with audit and register in the commit that
      carries this line; the fold in the fold commit).
- [x] No em dashes written by this run (the required heading and verbatim quotations keep theirs).

### CORRECTIONS MADE BEFORE CLOSE (my own errors, caught before commit of the section that carried them)
1. **A stale revision in my own table**: the Q1 draft summed FY2022 R&D, S&M and G&A to $127.0M using the first-filed G&A; the
   revised figure (FY2023 10-K, $30,443 thousand) gives $127.2M.
2. **An unsourced label**: the Q1 draft called Customer C (49% of FY2023 revenue) "one carmaker". No filing names it; removed.
3. **Two misquotations at Q2**: [E2-45] was quoted as *"with ample capital and skilled personnel"*, which is not a substring of the
   row (*"assuming I had ample capital and skilled personnel"*); and *"basis must be periodically replaced"* was put in [E4-04]'s mouth,
   when it is v4's scoping sentence. Both corrected to the exact text and the right source.
4. **Two counts at Q2**: "four acquisitions in twenty months" (it is five since January 2024, and 32 months to LivePerson), and
   "$36.9M of shares" for what is 36,894,839 shares.
5. **Two people at Q3**: the class action names the CFO of the time (Sharan, who resigned in 2026), not a "former CFO"; the insider with
   the 750,000-share plan is the co-founder serving as interim CFO, not merely "a director".
6. **Two figures at Q4**: "about $134M of stock consideration" for SYNQ3 and Amelia was not a figure I had computed; replaced by the
   filed $101.6M ($33,606 thousand plus $67,945 thousand, FY2024 non-cash face). "About $330M of costs" was wrong; the trailing
   operating loss before the earn-out mark is about $200.8M, so costs were about $404M.
7. **A scope claim at Q3**: "in no later release read" was widened into what was actually searched (every Item 2.02 EX-99.1 to
   2026-08-05, three search terms) and what was not (call transcripts).
8. **A tooling error of my own**: the first `peers/peer_row.py` took the first revenue tag with any data, which for LivePerson is
   `Revenues` ending in 2018, and printed nothing; corrected to merge tags year by year.
9. **A points-over-sovereign range at Q5** mixed the pro forma and cover caps (-9.6 to -14.3); split into -9.6 to -13.6 (pro forma)
   and -10.1 to -14.3 (cover).

### THE BRIEF'S DEFECTS (every brief in this queue has had at least one)
1. **"Name the peers from SOUN's own 10-K competition section"**: the 10-K has no such section and names no competitor (Item 1 speaks
   of unnamed *"big tech"* and *"legacy vendors"*; a search for every name in Cerence's list returned none). Peers were taken from
   Cerence's 10-K, which names SoundHound, and from the LivePerson fairness opinion.
2. **The brief did not mention the LivePerson acquisition**, the largest in the company's history, **closed on 2026-09-04, after the
   latest cover date**, with 36,894,839 shares issued to LivePerson's creditors and 3.0-5.8M to its stockholders. "SOUN has made
   acquisitions" and "check for any pending merger" pointed at the right place, but the cover-count instruction, followed literally,
   would have understated the count by about 8%. The deal-form alert (seven 425/S-4 filings) was about SoundHound as the acquirer,
   not a spread on its own quote.
3. **Hypothesis (a) was right and incomplete**: the SPAC shell left a second stale fact, **FY2021 operating cash of -$0.864M**, inside the
   owner-earnings series the triage used, not only a stale share count. The brief's instinct (check shell-era facts) found both.
4. **The prior the brief flagged as most likely wrong** (that a loss-making, acquisitive, heavily stock-paid AI company is an easy
   close) was **half right**: the close came at Q2, on the filer's own words about free alternatives and price reductions, not at Q4 on
   the losses; and it was not free, because the franchise case had real evidence (design-win stickiness in the filer's words, a named
   rival conceding SoundHound wins business, multi-year renewals, revenue guidance met every year) that had to be argued down on
   criterion 2 rather than waved away.
5. The ledger ids in the brief were all verified present; the brief's register count of 115 was checked by counting (fold).

### LIMITS OF THIS RUN
- **The post-closing share count is a range** (484.0-486.8M): the merger shares to LivePerson's stockholders are not filed; the Q3 2026
  10-Q will carry the count. **The cash LivePerson delivered at closing is not filed.**
- Earnings-call transcripts and investor decks were not read; a spoken profit target, or a spoken withdrawal, would be there.
- The ten-year window is not available from periodic filings; the 2022 S-4's FY2019-20 Legacy statements were not pulled.
- The competitor row uses companyfacts transcriptions of the peers' filed statements with one figure checked to a face; Verint's
  facts stop at FY2024 and it was not used; the big-technology rivals are unsegmented and iFlyTek is not an SEC registrant.
- No unit series (devices, queries, locations) is filed, so [E4-55] could only be run on dollars.
- The [E3-70] grant value uses the RSU table only (options and PSUs are small against 13.6M RSUs granted in FY2025).
- The *Liles* mediation of 2026-08-25 has no filed outcome.
- The watchlist pricing script that wrote the triage row is not on disk (the HBB finding); the triage inputs are reconstructed.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business), at Q2** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** SoundHound licenses voice AI to device makers and runs hosted voice and chat agents for businesses; its own 10-K says
  its products face alternatives *"offered at significantly lower costs or free of charge"* from larger rivals and accepts *"annual
  price reduction commitments"*; reported revenue doubled by acquisition while the filer's own pro forma for the businesses it owned
  fell; RPO fell to $60.0M; it is last on every margin and cash column of a five-filer row. The file closes at Q2 on [E3-03]
  criterion 2. Recorded, not governing: Q3 IN on the binary with converging flags (material weaknesses three years running, a
  "backlog" of *"potential revenue achievable"* 52 times GAAP RPO, missed and dropped adjusted-EBITDA targets, serial issuance to about
  2.4x, stock-price-linked pay); Q4 OUT, gruesome, owner earnings -$125.4M to -$135.4M (five-year) and -$208.5M to -$237.0M (TTM),
  shape #8 with #2 as a feature and #21 THE ROLL-UP proposed; price US$5.93 x 444,109,844 = US$2,633.6M on the cover (about
  US$2.87-2.89bn after the LivePerson closing), headed COMPUTATION — NOT A CLEARANCE, above a value range that lies wholly below zero.
  **FAIL at Q2.**
