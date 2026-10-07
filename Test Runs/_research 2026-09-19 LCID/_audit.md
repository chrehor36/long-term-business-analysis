---
## SELF-AUDIT
- [x] Questions answered in order; the file stopped at Q2 (OUT) and Q3-Q6 are labelled recorded, not governing.
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q1 IN rests on the filed faces; Q3's IN is the binary only).
- [x] No UNRESEARCHED verdict. The one named work order (the Mercedes-Benz, BMW and Porsche 2025 annual reports, rung 3) is recorded at
      Q2 as an upgrade of the row, and the reason it does not govern is stated.
- [x] No UNKNOWABLE verdict; the case for it at Q1 is recorded and the reason it was not taken is stated; at Q4 every window is negative.
- [x] Step 0: the filing was read (10-K FY2025 `0001628280-26-011053`, 10-Q Q2 2026 `0001628280-26-052606`, and the others listed), and
      FY2025 operating cash and capex were cross-checked against the filed face: identical to companyfacts.
- [x] Owner earnings on multi-year means (five-year default, four, three, twelve months), both (c) ends shown, (c) disclosed as a judgment.
- [x] Competitor row filled: Lucid recomputed from its own faces; eight peers with figures carried with citation from the RIVN and TM runs;
      the luxury peers named and not pulled, with the document named.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated 09/18/2026.
- [x] Value stated as a range: no positive value on any window; not a point estimate.
- [x] One bar only (Bar 2, the price is above the whole range); windage count zero.
- [x] Price dated (2026-09-18 close), aggregator flagged, corroborated on the post-split basis by the April 2026 offering prices in the 10-Q.
- [x] Run committed to git (template `2f51254`, Step 0 `785ebac`, Q1-Q2 `47b0c6d`, Q3-Q6 with audit and register in the commit that
      carries this line; the fold in the fold commit).
- [x] No em dashes written by this run.

### CORRECTIONS MADE BEFORE CLOSE (my own errors, caught before commit of the section that carried them)
1. **The runway arithmetic** in the Q4 draft said the pool covered "about one more year" and put the post-plan burn at "$4.4bn a year";
   recomputed from the filed pool ($3.0bn) and rates: about two quarters at the H1 2026 rate, about three on the plan-adjusted rate
   ($5,112.1M less $1.4bn is $3.7bn, not $4.4bn).
2. **The preferred's growth** was first written as "9% compounding", about $276M a year. Reading the Series C Certificate of Designations
   (EX-3.1 of 2026-04-29) found the *"Relevant Percentage"* step-up (100.0% to 150.4% at 60 months, 208.4% at 108 months); the filed
   movement of the A and B preferences ($203.4M in six months) confirms about 18% a year, about $550M a year. Corrected in Q3, Q4 and Q5.
3. **A figure I had not computed**: the Q3 draft said "$13.6bn of equity and preferred raised FY2021-H1 2026". Replaced by the sum I did
   compute from the cash-flow financing sections, $7.8bn net for FY2023-H1 2026.
4. **A misattributed quotation**: the Q3 draft put *"Buffett's stated base rate"* inside quotation marks, which is the framework's
   paraphrase, not corpus text; rewritten as [E3-48]'s base rate with only the verbatim words quoted.
5. **An unsourced tick**: "peers imitated: the robotaxi entry, after peers'" was not in any Lucid filing; unticked and said so.
6. **Two small figures**: the investments run down in FY2025 were $2.3bn net, not $2.9bn; the A and B preference rise was $203.4M, not
   $203.2M.

### THE BRIEF'S DEFECTS (every brief in this queue has had at least one)
1. **Hypothesis (a) did not apply**: Lucid has one class of common stock and one undimensioned dei fact; neither HBB layer exists here.
2. **The split was real (the brief's memory was right on the fact, 1:10 effective 2025-08-29) but it was not the cause.** The triage
   guard fired on the yield from the correct post-split count; the brief's hypothesis (c) was the right one, and the wave table's label
   "cap rejected as a broken input" was wrong in both words for LCID.
3. **"The RIVN run's row (Rivian, Lucid, Ford Model e, Tesla, GM, Ford; FY2025 operating margins)"** undersold it: the row is a five-year
   series with Toyota, Stellantis and Honda carried from the TM run, and my recomputation of Lucid reproduced it to the decimal.
4. **"Read the subscription or investment agreements as filed"**: done for the Series C Certificate of Designations and subscription
   agreement and the DDTL credit agreement; the Series A and B certificates were **not** opened, and their step-up is inferred from the
   filed six-month movement, not read. Recorded as a limit.
5. **The prior the brief flagged as most likely wrong** (a pre-profit carmaker is an easy close) was half right: the close came at Q2, on
   Lucid's own pricing record, not at Q4 on the losses; and the Q1 question about non-vehicle revenue turned up something the prior did
   not anticipate: **the one technology licensee and the largest identifiable customer are both in the controlling holder's circle**.
6. **Not in the brief, found by the run:** the 2026 production guidance of 25,000-27,000, reaffirmed on the financing day, is absent from
   every later document read; and `Screens/SURVIVAL SHAPES - index.md` does not list the RIVN run's instance of #8 or the TSLA run's of
   #11, although both run files name them.

### LIMITS OF THIS RUN
- The earnings-call transcripts and slide decks on ir.lucidmotors.com were not read; they are where a spoken withdrawal of the 2026
  guidance, if any, would be.
- The luxury peers' annual reports were not pulled (Q2).
- [E3-70]'s grant-value measure of stock compensation was not computed (it could only lower owner earnings further).
- The watchlist pricing script that wrote the triage row is not on disk (the HBB run's finding); the triage inputs are reconstructed.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business), at Q2** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Lucid sells luxury battery cars that have cost more to build than they sold for in every year, cut prices to sell more
  (FY2023 deliveries +37% on revenue -2%; vehicle revenue per car $96.9k to $73.5k), and sits last in an eleven-name row; the file closes
  at Q2 on [E3-03] criterion 2. Recorded, not governing: Q3 IN on the binary with converging flags (projections, serial issuance, a
  guidance bullseye dropped, adjusted EBITDA, a moved pay target); Q4 OUT, gruesome, owner earnings -$3.3bn (five-year) to -$5.4bn
  (twelve months), shape #8 with #14's feature; price US$4.09 x 394,070,176 = US$1,611.7M, headed COMPUTATION - NOT A CLEARANCE, above
  a range that lies wholly below zero. **FAIL at Q2.**
