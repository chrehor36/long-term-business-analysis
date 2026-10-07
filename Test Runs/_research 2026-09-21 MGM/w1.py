# -*- coding: utf-8 -*-
import io, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(BASE, "Test Runs", "2026-09-21 Run - MGM MGM Resorts International.md")
t = io.open(P, encoding="utf-8").read()
t = t.replace(u"[COMPANY] ([TICKER]) — [DATE]",
              u"MGM Resorts International (MGM) — 2026-09-21")

step0 = u'''## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34** % · date **2026-09-18** · source (issuing authority) **US Treasury daily par yield
  curve, 30 Yr column, CY2026 feed from home.treasury.gov. Struck fresh this run on 2026-09-21;
  the Friday 2026-09-18 row is the newest published. FRED DGS30 NOT used: it is the fallback,
  not the source (operator rule 5).**
- FX if the quote and the earnings differ in currency: **none needed for the quote, which is in
  USD. The earnings currency is mixed and that is recorded rather than smoothed: FY2025 net
  revenue was $12,411.6M United States, $4,464.1M China, $662.0M Other (10-K Note 17). The Macau
  pataca is pegged to the Hong Kong dollar, which is pegged to the US dollar, so the USD
  sovereign fits roughly 71% of revenue directly and the Macau leg by peg. The LeoVegas leg,
  3.8% of revenue and loss-making, is the part the USD rate does not fit.**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for FY2025, period ended 2025-12-31, filed
  2026-02-11, accession 0000789570-26-000018, primary document mgm-20251231.htm. Also read:
  Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-29, accession 0000789570-26-000076;
  Form 8-K of 2026-07-29 (Items 2.02, 9.01) accession 0000789570-26-000075 with EX-99.1;
  Form 8-K of 2026-04-07 (Items 1.01, 9.01) accession 0000789570-26-000029; Form 8-K of
  2026-05-14 (Items 1.01, 2.03, 9.01) accession 0001193125-26-224106; DEF 14A filed 2026-03-27,
  accession 0001193125-26-129074; and the FY2021 and FY2022 10-Ks for the pre-window cash flows.**
- figure cross-checked against the filed statement (say which): **three, each read off the filed
  statement rather than the tag. (1) Net cash provided by operating activities FY2025 =
  $2,529,378 thousand on the Consolidated Statements of Cash Flows, matching the tagged
  NetCashProvidedByUsedInOperatingActivities of $2,529.4M. (2) "Operating cash outflows from
  operating leases" FY2025 = $1,867,130 thousand in Note 11, which is the CASH rent, and it sits
  $391.3M BELOW the $2,258,405 thousand of "Triple net lease rent expense" in the Note 17
  reconciliation. Those are not the same number, and the gap is the subject of this run.
  (3) Total operating lease liabilities $25,068,747 thousand against total future minimum lease
  payments of $54,679,646 thousand, Note 11 maturity table.**

**THE PRICE, THE COUNT AND THE CAP — struck fresh, nothing inherited**
- price **$38.59** · date **2026-09-21** · source **Yahoo Finance chart endpoint via
  tools/sources.py price(). AGGREGATOR, and FLAGGED as such: permitted for live quotes only
  (operator rule 5). Intraday Monday quote.**
- share count **251,592,756** common shares, $0.01 par — read off the COVER of the latest
  periodic filing, the Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-29,
  **accession 0000789570-26-000076**, via python Screens/cover_shares.py MGM.
- **ONE class.** The FY2025 balance sheet carries a single line: "Common stock, $0.01 par value:
  authorized 1,000,000,000 shares, issued and outstanding 258,323,143 and 294,374,189 shares".
  There is no second class to sum, so no charter question arises. The count has fallen 6.7M
  shares in the six and a half months between the two dates; that is the buyback, read at Q3.
- **market capitalisation = $38.59 × 251,592,756 = $9,709M.** The screen row of 2026-09-02
  carried $10,273M; the difference is the quote, not the count.
- *No split has occurred in this window, so the split-invariance correction is inert here.*

'''

q1 = u'''## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **MGM sells time and space inside
  buildings it no longer owns. Four things are sold and the filed statement separates them: a
  house edge on wagers ($9,450.9M of casino revenue in FY2025, 53.9% of the total), hotel
  room-nights ($3,377.4M), food and drink ($3,046.0M), and entertainment, retail and other
  ($1,663.4M) — Consolidated Statements of Operations, FY2025 10-K. The casino take sets the
  rest: rooms and restaurants are priced off the traffic the gaming floor and the convention
  calendar bring, which is why Item 1 says "Our operating results are highly dependent on the
  volume of customers at our properties, which in turn affects the price we can charge for our
  hotel rooms and other amenities."**

  **Against that revenue sit four cost blocks a reader can name from the filed statements.
  Payroll: approximately 44,000 full-time and 18,000 part-time U.S. employees plus 16,000
  internationally, with collective bargaining agreements covering about 37,000 U.S. employees
  (Item 1). Gaming taxes: $3,119.9M across the four segments in FY2025 (Note 17), of which
  $1,969.0M is MGM China alone, where the concession carries a special gaming tax of 35% of gross
  gaming revenue plus a levy of up to 5% (Note 12). Depreciation and amortization: $1,017.8M.
  And RENT: $2,258.4M of triple net lease rent expense (Note 17 reconciliation), of which
  $1,867.1M was paid in cash in FY2025 (Note 11). The rent block is what makes this registrant a
  different animal from the company it was ten years ago, and it is a contractual, escalating,
  23-year-weighted-average obligation, not an operating cost management can flex.**

  **The structure the money passes through, from Note 1 and Note 2. MGM Resorts International is
  a Delaware holding company. It CONSOLIDATES (a) sixteen domestic casino resorts, (b)
  approximately 56% of MGM China Holdings Limited, separately listed in Hong Kong, whose
  subsidiary MGM Grand Paradise holds one of the six Macau gaming concessions, and (c) LeoVegas,
  the European online gaming subsidiary. It does NOT consolidate (d) BetMGM, the 50% North
  American online venture, because "the Company has joint control", (e) MGM Osaka, 50%, a VIE of
  which it is not the primary beneficiary, or (f) the Bellagio REIT Venture — its own landlord,
  in which it holds 5% and which is likewise a VIE it does not consolidate. So the reported
  revenue line contains Macau and LeoVegas in full and contains BetMGM and Osaka not at all;
  those two enter only through the single line "Income (loss) from unconsolidated affiliates",
  $69,982 thousand in FY2025 against $(90,653) thousand in FY2024. That answers the brief
  directly: the equity-method venture and the European online subsidiary sit INSIDE the reported
  numbers in one case and OUTSIDE them in the other, and the filing says which is which.**

- The scarce input this business controls: **the licence and the customer file — and NOT the
  land. This is the sharpest thing Q1 has to say about MGM, and it is a change of kind, not of
  degree. A gaming licence is scarce by statute: Macau has exactly six concessionaires (Item 1),
  and a Maryland, Massachusetts, Michigan, New Jersey, New York, Ohio or Mississippi licence is
  legislatively rationed. The customer file behind MGM Rewards is a real asset. But Las Vegas
  Strip frontage and every domestic regional site — the input that cannot be reproduced at any
  price — is now RENTED: "We lease the real estate assets of our domestic properties pursuant
  to triple net lease agreements" (Item 1, repeated in Note 1). The registrant sold the scarce
  input and signed a lease back on it. Item 1 calls this "an asset-light business model"; the
  balance sheet calls it a $25,068,747 thousand operating lease liability standing against
  $6,305,614 thousand of property and equipment, net.**

- Will the fundamentals look broadly the same in ten years? **Broadly yes, and this is the part
  that passes. People will still gamble, still hold conventions in Las Vegas, and still travel to
  Macau; the filing’s own description of the revenue engine would have been recognisable in 2005
  and is likely to be recognisable in 2035. Two dated edges are named in the documents rather
  than assumed: the Macau gaming concession EXPIRES in December 2032 (Note 12, with the Item 1
  risk list carrying the government’s rights to terminate without compensation in certain
  circumstances, to redeem from the eighth year on one year’s notice, or to refuse an extension),
  and the domestic master leases run 23 years on a weighted average with renewal options at the
  Company’s election (Note 11). Neither makes the business unintelligible. Both are read again at
  Q2 and Q4.**

- **The complexity is recorded, not waved through.** Four segments; a separately listed 56%
  subsidiary that took $315,010 thousand of FY2025 net income as noncontrolling interests against
  $205,862 thousand attributable to MGM’s own shareholders; two 50% ventures outside the
  consolidation; five master leases; and a $3.01 billion shortfall guarantee of the DEBT OF ITS
  OWN LANDLORD (Note 12). That is a complicated holding company. But **[E3-31]** asks whether the
  business is "relatively simple and stable in character" in how it makes money, and the
  money-making is simple: house edge, room nights, and a rent bill. The complexity is a
  MEASUREMENT problem — whose dollars are whose — and it is settled at Q4 where owner earnings
  are built. It is not dodged here.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

'''

a = t.index(u"## STEP 0")
c = t.index(u"## Q2 — IS IT A FRANCHISE?")
t = t[:a] + step0 + u"---\n" + q1 + t[c:]
io.open(P, "w", encoding="utf-8").write(t)
print("ok", len(t))
