
---
## THE OUTPUT CONTRACT

**PRICE: US$404.11** (2026-09-17 close; 294,800,000 shares; market capitalisation
**US$119,131.6M**).

**FAIL — the file is closed at Q5, ON PRICE.** Q1 IN · Q2 IN (NARROW, carried by Ratings alone) ·
Q3 IN (qualitative overlay) · Q4 IN · **Q5 FAIL: honest pre-tax expectancy of 8.5% to 9.8%
against the ~10% floor [E4-28], and an owner-earnings yield 1.6 to 2.9 points BELOW the 5.29%
sovereign on every window.** Q6 recorded, and it governs only the conditions for reopening.

**All four business gates cleared. This is a finding about the price, not about the business** —
the ASML, PNR and CL shape.

---
## SELF-AUDIT

- [x] **Questions answered in order; no verdict skipped.** Q5 opened only after Q1-Q4 each showed
      IN, and the file says so at the gate.
- [x] **NO HARD-SEQUENCE VIOLATION, and I audited for one rather than assuming it.** The file was
      searched before folding for valuation language appearing before line 1174 (where Q5 starts).
      Four hits, all inspected: two are the **verbatim text of [E5-44]**, quoted because it is the
      Q3 test for a stock-funded acquisition; one is the **heading of [E5-08]'s second
      condition**, which the template requires at Q3; one is the **humility clause of [E5-08]**
      itself (*"many CEOs never stop believing their stock is cheap"*). **None is an output about
      SPGI's value.** The Q3 buyback paragraph states in terms that it *"rests on our own
      valuation range, which Q5 has not yet produced"*, and compares the repurchase price to
      today's quote — a price-to-price comparison, not a valuation. **No value range, no yield and
      no multiple for this company appears anywhere before Q5.** *(The CL run found two violations
      in a killed session's draft; this session was not killed and none was imported.)*
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2 is IN on
      Ratings, whose competitor row is **complete in units** (nine of ten NRSROs, each from its
      own primary SEC filing). The **PROVISIONAL** legs — Indices and Energy — are named as such
      and are **explicitly excluded from the verdict**, exactly as CL excluded Pet Nutrition.
- [x] **Every UNKNOWABLE names what specifically cannot be known.** Fitch Ratings' income
      statement (Form NRSRO Exhibit 11 is audited financials but Rule 17g-1(i) exempts it from
      publication, and Fitch has taken the exemption); the economics of Kroll, Egan-Jones, A.M.
      Best, JCR, Demotech and HR Ratings (same exemption); Bloomberg Finance L.P. and Solactive AG
      (private, no filing exists); **Argus Media** (private, United Kingdom), which is why Energy
      is PROVISIONAL.
- [x] **Every UNRESEARCHED names the artifact and where it lives.** One only: **LSEG plc's annual
      report**, for FTSE Russell's economics. It is a nameable document on LSEG's investor site
      and it was **not pulled**, because the Indices leg does not carry the verdict. Recorded as
      UNRESEARCHED rather than dressed up as unknowable.
- [x] **Step 0: the filing was read, with accession numbers, and figures were cross-checked.**
      FY2025 10-K `0000064040-26-000013`; OCF $5,651M and capex $195M both matched to the dollar
      against the filed Consolidated Statement of Cash Flows.
- [x] **Owner earnings on a multi-year mean, windows stated, capex band disclosed as a judgment.**
      Three perimeters, never blended; four constructions of (c), two of which land within $156M
      of each other.
- [x] **Competitor row filled.** Nine of ten NRSROs in units; S&P and Moody's in margins on the
      same basis and the same window; MSCI's Index segment for the Indices leg; FactSet and
      Morningstar for Market Intelligence.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated** — USD 5.29%,
      US Treasury daily par yield curve, 09/17/2026, cache deleted and re-fetched this morning.
- [x] **Value stated as a round-number range**, not a point estimate.
- [x] **One bar chosen, not both** (Bar 2, the screamer test; Bar 1's end margin deliberately not
      applied and the reason given). **Windage count: ONE**, stated.
- [x] **Prices dated; the aggregator flagged and used for live quotes only.** SPGI $404.11 at the
      2026-09-17 close; MBGL $19.925 at 2026-09-18, both flagged.
- [x] **Run committed to git**, section by section, with a pathspec on every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record

1. **My own Step 0 error, corrected in a dated note at the head of Q3 rather than by editing**
   (operator rule 6): I wrote that the filing gave "no basis" for treating the 7.2M Markit EBT
   shares as other than treasury-equivalent. The FY2025 balance sheet disproves it — 415M issued
   less **109M of treasury** less 7.2M is exactly the 298.8M on the cover, so the EBT shares are
   **outstanding shares the registrant excludes from its own denominator**, not treasury. The
   headline count and the $2,910M sensitivity both stand; the reasoning behind them is now right.
2. **Fitch Ratings left Item 7A blank in its 2026 Form NRSRO certification** (`0001104659-26-036549`).
   I checked page by page with two different extractors and for form-field values before falling
   back to the 2025 certification, so Fitch's count in the competitor row is **as of 2024-12-31**
   and its share is understated by a year. Said in the row rather than hidden.
3. **HR Ratings LLC's Item 7A did not extract** from its 2026 certification and I did not chase
   it. It is the smallest of the ten and cannot move a 49.4% share. Recorded as incomplete.
4. **The SEC's Annual Report on NRSROs returned HTTP 403** on three plausible paths from this
   harness. Not needed — the per-filer Form NRSRO certifications are the primary source and are
   better.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN

1. **The brief sent me to the wrong documents for the perimeter, and named the right one as
   merely "unread".** It pointed at the May 2026 8.01 filings for a segment recast and at the
   MBGL Form 10-12B/A for the subtraction. **The answer is the 8-K/A of 2026-07-06, accession
   `0001104659-26-080571`**, which carries an **Article 11 unaudited pro forma income statement
   for FY2023, FY2024, FY2025 and Q1 2026, and a pro forma balance sheet** — S&P Global without
   Mobility, filed, five days after the spin. It is also a **better** source than the Form 10,
   because the Form 10's combined statements charge Mobility with allocated corporate overhead
   that stays with S&P Global, while the pro forma's discontinued-operations column is scoped to
   what actually leaves and says so in note (a).
2. **The brief's share-count instruction stopped one step short.** It correctly warned about the
   ERIC trap (issued vs outstanding — present here, and worth 120M shares) and told me to read
   the 10-Q cover. The cover contains a **second** trap running the other way that the brief did
   not name: it excludes **7.2 million shares it itself calls outstanding**, held by an employee
   benefit trust inherited from Markit. Worth $2,910M of market capitalisation.
3. **The brief's framing of the skip reason pointed at the wrong quantity.** "capex unresolved
   [E5-20]: build (c) by hand" is true as far as it goes, and the tag-change hypothesis was right.
   But **plant is not the (c) question at this company** — gross property and equipment is
   $1,139M on $15.3bn of revenue and capex is 1.14x depreciation. The (c) question is whether
   **acquisition** is maintenance, which the [E5-20] label does not describe and which needed a
   different test.
4. **A small factual slip: the brief said `PaymentsToAcquirePropertyPlantAndEquipment` runs
   "FY2007, 2008, 2009 only … then stops" and `PaymentsToAcquireProductiveAssets` runs "FY2008
   through FY2025".** Both true — but the brief then framed this as a possible hole. **The two
   tags OVERLAP in FY2008-FY2009**, so there is no hole anywhere in the nineteen-year series, and
   the union fix reaches every window. Worth stating because the NVDA run's failure mode was
   exactly a hole.
5. **The brief's expectation that Forms 4 would be available to cross-check the quote did not
   hold.** EDGAR, re-queried this morning, shows **nothing filed after 2026-08-04**. The CL
   trick could not be repeated and the limit is recorded instead of worked around.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN

**Form NRSRO is a complete competitor row for an industry with private participants.** Every
nationally recognised statistical rating organisation — including Fitch, which is inside Hearst,
and Kroll, and A.M. Best — files an annual certification on EDGAR carrying **its own count of
credit ratings outstanding by class**. An EDGAR full-text search over form type **NRSRO-CE**
enumerates the whole industry: **exactly ten registrants in 2026.** This is the first name in the
register whose competitor row is complete in units *including the private competitors*, and the
pattern generalises to any SEC-registered-intermediary industry (broker-dealers, transfer agents,
municipal advisors, security-based swap dealers) where registration carries a disclosure exhibit.

---
## REGISTER

- Verdict: **[x] FAIL AT Q5 — about the PRICE.** Not OUT (the business cleared all four gates),
  not UNRESEARCHED, not UNKNOWABLE.
- **One line:** *S&P Global's ratings franchise is real and measurable — 49.4% of every credit
  rating outstanding in the United States regulatory system, a 63.8% segment margin against
  Moody's 60.9%, and a balance sheet that needs no capital because customers prepay — but the
  price asks 31.5 times a three-year mean of owner earnings for a business that has added 1.5% a
  year per share since it issued $43.5 billion of stock, and the expectancy is 9.27% against a
  10% floor and 3.17% against a 5.29% bond.*
- **Not UNRESEARCHED and not UNKNOWABLE:** every number that decides this file is on a filed
  statement, and the one document not pulled (LSEG's annual report) bears on a leg that does not
  carry any verdict.
