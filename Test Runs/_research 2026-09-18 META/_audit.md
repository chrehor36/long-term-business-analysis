## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT, on the business); Q3-Q6 recorded beneath explicit RECORDED,
  NOT GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed segment notes and the
  impression and price series FY2019 to H1 2026; superintelligence, enterprise AI and Reality Labs as businesses are excluded
  by name.
- [x] The one UNRESEARCHED verdict (Q3, recorded) names its artifacts and where they live: the New Mexico verdict record (First
  Judicial District Court, 2026-03-24) and the FTC's 2023 Order to Show Cause.
- [x] The one UNKNOWABLE verdict (Q4, recorded) states what cannot be known: the split of $130-145bn a year between holding the
  advertising position and building new businesses, and the return on the second; no filing states either.
- [x] Step 0: the skip reason tested on the inline XBRL of the latest 10-Q (the count is tagged per class with a dimension, which
  companyfacts omits); the entity checked; the filing read with accession numbers; OCF, SBC, D&A, capex, finance-lease principal
  and revenue cross-checked to the FY2025 10-K face, with the two vintage differences named.
- [x] Owner earnings on the five-year default and on three-year, nine-year, pre-build and twelve-month windows; both (c) ends
  with the D&A end declared INVALID under [E5-20] and shown as display; finance-lease principal subtracted; acquisitions in their
  own column; the off-balance-sheet leases, the Venture and the commitments quantified beside the table; SBC at the [E3-70]
  grant-value measure read by hand from the RSU tables.
- [x] Competitor row filled from five SEC filers (Alphabet with its Services segment, Amazon's advertising line, Snap, Pinterest,
  Reddit), companyfacts re-fetched and one operating-cash figure per peer found on its own FY2025 10-K face; the unlisted
  rivals (TikTok/ByteDance, X, OpenAI) named; the class not PROVISIONAL, with the directional reason.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched directly; the cached
  09/17 row from `sources.sovereign()` recorded and not used.
- [x] Value stated as a round-number range under COMPUTATION — NOT A CLEARANCE ($250-500bn at the floor with no growth, the top
  on the invalid D&A end).
- [x] One bar (the screamer test); windage count zero, stated.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, the series corroborated by three Form 4 sale prices inside the
  day's range.
- [x] Share count from the latest 10-Q cover with its accession; the A/B addition justified from the charter's equal-status,
  dividend, liquidation, merger and conversion clauses; dilution (RSUs and the 2026 options) shown beside the cap.
- [x] Deal check run on EDGAR: none live.
- [x] Run committed after the template, after Step 0, after Q1-Q2, and after Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`, a sweep of every id in the file: none missing).
- [x] No em dashes in anything this session wrote (the template's headings and the required `COMPUTATION — NOT A CLEARANCE`
  heading carry them; one heading of mine that carried one was changed to a colon before the Q3-Q6 commit).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded 10-Ks, 10-Qs, 8-Ks, proxy, charter, court opinion, peers' 10-Ks and companyfacts
  were left out of every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Step 0, corrected before its commit:** a first draft said the 8-Ks *"of the last two years"* carried Item 7.01 (the last
   7.01 was 2023-03-14); rewritten as *"filed since 2024-08"*. A first attempt to write Step 0 through a bash heredoc failed on an
   apostrophe (the brief's warning); rewritten through a file.
2. **Q1-Q2, corrected before commit:** impressions were first compounded *"2.07 times over FY2021-25"* using the FY2021
   growth rate (which is FY2020 to FY2021); corrected to 1.88 times from FY2021 to FY2025. The twelve-month operating-income
   increase was first written $40.1bn (it is $40.2bn). *"formats replaced three times (feed, Stories, Reels)"* is two
   replacements; corrected. The court quotation was first introduced as the court *"ultimately finds"*; the opinion's sentence
   begins *"The Court ultimately finds"* and is now quoted whole.
3. **Q1-Q2's first commit attempt failed** because `git add` refused an ignored research file (`legal_10Q_2026Q2.txt`) and the
   chained commit did not run; the commit was re-run without it (`5f8d195`). Nothing was lost.
4. **Q3-Q6, corrected before commit:** a sentence citing a *"2,854M-class"* historical share count had no source on disk and was
   replaced by the filed weighted basic counts (2,574M FY2023, 2,521M FY2025); the multistate youth trial was described as
   *"begun"* on 2026-08-12 when the 10-Q says it was *"scheduled to begin"*; the no-growth value per share was $95 (it is $97).
5. **A judgment disclosed, not an error:** the FTC opinion was read from the court's own server, a rung the v4 evidence ladder
   does not list (it lists SEC, company and exchange rungs); the GOOGL run used the court-record rung the same way. It is cited
   for what the court found and what Meta argued, not for any number.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **"Latest 10-K: FY2025, filed 2026-01-29 (per the dei public-float fact)" (section 1):** held (`0001628280-26-003942`). The
   brief did not give the 10-K accession; supplied here.
2. **The skip-reason hypothesis (section 1):** held exactly, and more precisely than stated: the cover *does* carry
   `dei:EntityCommonStockSharesOutstanding`, twice, each fact dimensioned by `us-gaap:StatementClassOfStockAxis`; companyfacts
   drops dimensioned facts. "No share count from dei" means "no *undimensioned* share count".
3. **"Capex 15.1, 15.1, 18.6, 31.4, 27.3, 37.3, 69.7" (section 2):** FY2021-23 are the gross figures from the earlier faces; the
   FY2025 face nets a small *"Proceeds relating to property and equipment"* line (FY2023 27,045 against 27,266). Immaterial;
   named in Step 0.
4. **"FinanceLeasePrincipalPayments $2.5bn FY2025 ... finance-lease capex is capex the capex tag does not see" (section 2):**
   held; the screen's capex end subtracts finance-lease right-of-use *additions* ($613M in FY2025), not principal ($2,524M), which
   is why its $25.6bn differs from this file's $24.7bn.
5. **The memory-sourced beliefs (section 3), settled:** Class B ten votes, one-for-one conversion, founder control: **held**
   (charter and 10-K). Two segments with Reality Labs losing $15-20bn a year: **held** ($16.1bn, $17.7bn, $19.2bn FY2023-25;
   $10.2bn and $13.7bn in FY2021-22). The Q3 2025 tax charge: **held** ($15.93bn, OBBBA, partly reversed by an $8.03bn CAMT
   benefit in Q1 2026). Scale AI: **held** ($13.80bn minority stake, measurement alternative). The Louisiana joint venture:
   **held, and off the balance sheet** (20% equity-method interest, unconsolidated VIE, $45.95bn maximum exposure); the name
   "Hyperion" appears in no filing read. 2026 capex far above 2025: **held** ($130-145bn guided against $72.2bn including
   finance-lease principal). The FTC monopolisation case: **decided for Meta** (2025-11-18), FTC appeal filed 2026-01-20; and
   the ground of the decision, that TikTok and YouTube are in Meta's market, decided Q2. EU DMA decisions and fines: **held**
   (EUR 200M, 2025; plus a June 2026 interim measure on WhatsApp). Competitors in the 10-K: **the 10-K names TikTok (once, as a
   cause of reduced engagement), Apple and Google (as platform owners), and no other rival**; Alphabet and Amazon name no
   competitor at all, and Snap, Pinterest and Reddit name Meta.
6. **The brief did not know** about the $349.31bn of commitments and $347bn of signed leases at mid-2026, the RSU grants of
   $47.2bn gross in H1 2026 ($79.79bn unrecognized), the 20 million options at $2,788, the $2.4bn Q2 2026 legal charges, the New
   Mexico $375M verdict, or the $190M derivative settlement; each is in the file.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.sovereign()` served the cached 09/17 row** at 22:03 EDT while the Treasury had published 09/18: the seventh
  reproduction.
- **`sources._chart()` returned `close None` for the day's bar** after the close, as at BX and AEHR.
- **`share_count_shift` and every dei reader miss per-class covers.** A reader of the inline XBRL cover (the raw 10-Q, not
  companyfacts) would find the dimensioned facts; `Screens/cover_shares.py` already does this and correctly refuses to add them.
  The remaining names in this row (DASH, PATH, PUBM, BZFD) should be checked for the same dimensioned-cover pattern first.
- **The screen's capex end subtracts finance-lease ROU additions, not principal paid**, which understates the cash cost of
  finance-leased plant wherever principal exceeds additions (Meta FY2025: $2,524M against $613M).

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**Read the company's own litigating position.** Meta's 10-K says users have substitutes; in court, on a full trial record, Meta
argued its market *"at a minimum includes TikTok and YouTube"*, and won. A company that has proved in court that it has close
substitutes has answered [E3-03]'s second criterion for us.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)**, at Q2. [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** META CLOSES AT Q2 (OUT, ON THE BUSINESS, [E3-03] criterion 2, with [E4-04], [E4-55], [E4-38], [E2-44], [E3-46],
  [E3-51], [E2-59], [E4-23]): the FY2025 10-K says users are *"actively engaging with other products and services similar to, or
  as a substitute for, our products"*, names TikTok, and says marketers spend *"only a relatively small portion of their overall
  advertising budget with us"*; the D.D.C. held on 2025-11-18, on Meta's own argument, that *"YouTube and TikTok belong in the
  product market, and they prevent Meta from holding a monopoly"*; the average price per ad compounds to 0.97 times FY2018's over
  seven filed years while impressions grow; the company describes its business as *"characterized by innovation, rapid change,
  and disruptive technologies"* and holds its position by rebuilding the basis, now at $130-145bn a year of capital spending
  (capex/revenue 15.8% FY2021 to 34.7% FY2025) with $349bn of commitments and $347bn of signed leases, no filing splitting defence
  from replacement; the EU caps the terms in 23% of revenue; founder control recorded. On a five-filer row it is the margin and
  owner-cash leader. Q1 IN (advertising by auction on four apps, 97.6% of revenue; superintelligence, enterprise AI and Reality
  Labs outside the circle). Q3 recorded UNRESEARCHED on the binary (the [E5-22] pattern: the 2012 FTC order, its $5.0bn
  violation settlement in 2019, the 2023 modification proceeding, the 2026 New Mexico $375M jury verdict; work order: that
  verdict record and the FTC Order to Show Cause), with prompts on server-life extensions, a capital-spending guidance ratchet and
  the withdrawn Facebook-app series, a capital-allocation flag on FY2025 buybacks at about $657, pay vesting on nothing the capital
  earns, and 20 million options at $2,788. Q4 recorded UNKNOWABLE: owner earnings five-year FY2021-25 **$24.7bn at the capex end
  (central; the D&A end $50.4bn is INVALID under [E5-20])**, $12.7bn for the twelve months to June 2026, about $3bn in FY2025 with
  SBC at grant value [E3-70]; strength 3 fails; shape #10 THE CAMOUFLAGE with #1 and #2 as features. Price $665.75 x 2,547,506,225
  = $1,696.0bn, headed COMPUTATION — NOT A CLEARANCE: yield 0.75-1.72% at the capex end against 5.34% and a ~10% floor, which would
  need about $170bn a year; Q6 records the reversal condition in words and arms nothing.
- **The skip reason, as it turned out:** a tagging convention, not a missing count. The 10-Q cover carries both class counts
  under `dei:EntityCommonStockSharesOutstanding`, each dimensioned by class of stock, and companyfacts publishes only
  undimensioned facts. The charter makes the classes economically identical, so the count is their sum.
