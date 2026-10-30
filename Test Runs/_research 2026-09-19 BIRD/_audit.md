---
## SELF-AUDIT
- [x] Questions answered in order; the file stopped at Q1 (UNKNOWABLE) and Q2-Q6 are labelled recorded, not governing.
- [x] No question marked IN. The one IN written (Q3's binary, recorded) is worded as the absence of found disqualifiers [E5-17].
- [x] No UNRESEARCHED verdict. The unfiled items (the post-cover share count, conversions, the dividend's payment, the Q3 quarter) are named
      with the document that will carry them (the Q3 2026 10-Q) and none could change the Q1 verdict.
- [x] The UNKNOWABLE verdict states what cannot be known (how the new business makes money: no record of it exists, by the filer's own
      words) and answers the separating test (no document exists that would resolve it); the case for IN and for OUT are both recorded.
- [x] Step 0: the filing was read (10-Q Q2 2026 `0001437749-26-028446` whole; 10-K FY2025 `0001628280-26-022192` in part; the DEFM14A,
      the DEF 14A and the 8-Ks listed), and five figures were cross-checked against filed faces (FY2025 and FY2024 operating cash, stock
      pay, capex and D&A; H1 2026 continuing operating cash), all identical to companyfacts.
- [x] Owner earnings on multi-year means (five-year default, three-year, twelve months), both (c) ends shown where they can be built, (c)
      disclosed as a judgment, and **the perimeter stated: every annual year is a sold business**; the continuing half-year shown apart.
- [x] Competitor row filled (recorded): five filers, same metrics, latest filed periods, one figure checked to a face; the unsegmented and
      private rivals named as a class and the reason they are absent stated; Applied Digital's capex not resolved and said so.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated 09/18/2026, struck by this run.
- [x] Value stated as a range (nothing to about $0.70-1.90 a share, from the balance sheet), not a point estimate.
- [x] One bar only, and neither applied; windage count zero.
- [x] Price dated (2026-09-18 close), aggregator flagged, corroborated at three filed dates (the 06-18 RSU grant value, the proxy's 05-07
      price, the 09-02 Form 4s).
- [x] Share classes summed only after the charter was read (identical except votes; one-for-one conversion); the DEF 14A record-date total
      matches the cover sum; post-cover changes named.
- [x] SBC resolved and complete; the [E3-70] grant-value measure computed from the RSU table; the notes' share-paid interest identified.
- [x] Deal read (ROKU lesson): the deal form was the registrant's own asset sale, closed 2026-06-09; no offer for BIRD; not a spread.
- [x] Every ledger id cited was checked against `principle_ledger.csv` (one row each; `ledger_check.py`, `ledger_out.txt`).
- [x] Run committed to git (template `4ae1654`, Step 0 `4effd47`, Q1 `2e565af`, Q2-Q4 `a6641a5`, Q5-Q6 with audit and register in the
      commit that carries this line; the fold in the fold commit).
- [x] No em dashes written by this run (the required heading and verbatim quotations keep theirs).
- **Quotation note (prime rule 1):** stripped inline-XBRL text reads *"$ 0.1 million"* and *"( 13,197,322 )"*; in running text the dollar
  sign is closed up to the number (*"$0.1 million"*), and nothing else in any quotation is altered; ellipses mark every cut.

### CORRECTIONS MADE BEFORE CLOSE (my own errors, caught before the commit of the section that carried them)
1. **A misquotation at Q1**: the draft put *"expected"* in quotation marks; the 10-Q says *"We expect our customers to purchase"*. Corrected
   to the exact sentence.
2. **A wrong multiple at Q1**: "overhead about fifteen times its annual lease income". The half-year's overhead runs at about $33M a year
   against about $1.0M of lease receipts: more than thirty times. Corrected.
3. **Two general-knowledge labels at Q2**: IREN as "a former bitcoin miner" and CoreWeave as "the largest pure-play" came from memory, not a
   filing. Removed and reworded ("the largest in the row").
4. **Two overstatements at Q2**: "no filer in the row earns positive owner cash" (QumulusAI's and Applied Digital's did not resolve) and
   "smallest by two to three orders of magnitude" (the lessee is about four times Smartbird's revenue). Both narrowed to what the row shows.
5. **Two bracketed edits inside quotations at Q3** (*"exclude[d]"*, *"agree[s]"*), which prime rule 1 does not allow. Replaced by the exact
   filed text.
6. **Two counts at Q3**: "twice the dividend" raised (it was $22.7M against $3.6M, about six times) and a "ten-page" chronology (eight).
7. **A misread obligation at Q4**: "must be redeemed with 100% of the gross proceeds" of an asset sale; the 8-K gives the holders the
   right to require it. Corrected with the exact clause.
8. **A quotation at Q4 attributed to [E4-20] that is v4's own wording**, not the ledger row's. Reworded without quotation marks.
9. **An unsourced label at Q4**: the lessee's funding source called a "crypto-lending protocol". No filing read says so; replaced with the
   lessee's own words (*"the USD.AI protocol"*). And "lessees" (plural) corrected to the one lessee.

### THE BRIEF'S DEFECTS (every brief in this queue has had at least one)
1. **The name and the business are out of date, and this is the one that matters.** "BIRD (Allbirds, Inc.)" has been **Smartbird, Inc.**
   since 2026-06-15; the Allbirds brand, trademarks, customer lists and inventory were sold to American Exchange Group on 2026-06-09. The
   brief's Q1 prompt (*"after its channel and store changes"*) and its Q2 prompt (*"brand, repeat purchase, pricing, direct-to-consumer
   data"*) both address a business the share no longer buys. Followed literally, the run would have closed a brand at Q2 that belongs to
   someone else. (The brief's own guard, *"do not let the Q2 argument substitute for Q1"*, is what caught it.)
2. **The skip-reason hypotheses missed the decisive reading.** (a) and (b) were right and (c) was right; (d) was refuted (no shell, one
   vintage per cash-flow fact); **the fifth, unlisted reading is the one that explains the row**: the triage's numerator was the losses of a
   business sold before the triage ran.
3. **The reverse-split belief was RIGHT** (1-for-20, effective 2024-09-04, 8-K `0001653909-24-000064`), and so was the implied dual-class
   belief (Class A and B, identical except votes). Recorded as verified, not as defects.
4. **"No screen row" was RIGHT** (confirmed: no BIRD or Allbirds row in any CSV).
5. **"A consumer-brand name recently public with a falling share price"**: public since November 2021, nearly five years; and the latest
   leg of the fall is the pivot's, not the brand's (the price rose from $2.49 to $16.99 on the day the AI plan was announced, 2026-04-15).
6. **The brief did not mention the convertible notes, the ATM or the special dividend**; the standing "Deals" instruction found the asset
   sale's proxy through `deal_note`, and the rest was found by reading the 8-Ks.
7. The ledger ids named in the brief ([E4-27], [E4-52], [E4-26], [E3-41], [E4-28], [E3-03], [E5-20]) were all verified present and used
   as the brief described them. The register count of 116 for SOUN is checked by counting at the fold.

### LIMITS OF THIS RUN
- **The watchlist pricing script is not on disk** (the HBB finding): which count the triage used is bounded (the correct count or the
  split-adjusted pre-IPO count; both trip the yield bound) but not read.
- **The post-cover share count is not filed**: the 2026-09-01 vesting, any ATM sales and any note conversions since 2026-08-10.
- **The dividend's payment is not confirmed by a filing**: the 10-Q and the 8-K of 2026-08-10 give an *"anticipated payment date"* of
  2026-08-20.
- **The lease's implicit rate is reconstructed** from Note 11's schedule, not stated by the filer; **QumulusAI's filings read do not name
  Smartbird**, so the lease is evidenced from the lessor's side only.
- The Q1 2026 10-Q and the FY2021-24 10-Ks were downloaded but their figures enter through companyfacts (single vintage), checked for
  FY2024-25 against the FY2025 face; no earnings-call transcript was read (the FY2025 call was cancelled).
- Kroll's IP-asset analysis in the DEFM14A was not read in full; the brand's value is taken from the bids in the chronology.
- Whether a going-concern paragraph is a "modification as to uncertainty" under Item 304 was not settled from a primary source.
- The competitor row uses companyfacts transcriptions of the peers' statements with one figure checked to a face; the hyperscalers are
  unsegmented and private GPU clouds file nothing.
