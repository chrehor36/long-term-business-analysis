## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.35%** · date **2026-09-11** (latest print; 09-12 and 09-13 are a weekend) · source
  **US Treasury daily par yield curve, 30-year** (issuing authority), struck fresh through
  `tools/sources.py:sovereign("USD")` on 2026-09-13. It agrees with the brief's figure; it was
  not inherited from it.
- **Earnings currency — NOT one currency, and stated as such.** The 40-F MD&A (Part 2, *Foreign
  Currency Translation*, p.56): *"As at December 31, 2025, our common equity of $43.8 billion was
  invested in the following currencies: U.S. dollars – 58% (December 31, 2024 – 64%); British
  pounds – 13% … Canadian dollars – 7% … Euro – 5% … Brazilian reais – 4% … Australian dollars –
  4% … and other currencies – 9%"*. Hedge levels on the Brazilian real, Colombian peso and other
  emerging-market currencies *"were low as at December 31, 2025"* (same page). Common dividends
  are declared in USD; the preferreds are declared in CAD; corporate bonds are USD and CAD.
  **The USD sovereign is used, as the reporting and dividend currency and the 58% majority, and
  the choice is disclosed as unresolved** — the open question recorded in `Framework/SECTOR
  METHOD …` FINDING 8 (the WTM run: state the exposure, use the reporting currency's sovereign,
  disclose that the choice is unresolved). No blending rule is invented (PRIME RULE 3).
  Direction of the error: the non-USD 42% includes BRL, COP and INR exposure whose own
  sovereigns sit well above 5.35%, so the USD bond is the *lowest* bar available, not the highest.
- FX: the NYSE line is quoted in USD and the statements are in USD. No ADR.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Form 40-F for FY2025**, filed 2026-03-18, accession `0001001085-26-000006` — cover, Exhibit
  99.1 (Annual Information Form, `a2025-40xfex991aif.htm`) and Exhibit 99.2 (MD&A plus the
  audited IFRS consolidated statements and notes, `bn-20251231_d2.htm`). Read: MD&A Parts 1-4,
  the Glossary with its net-income-to-DE reconciliation, Notes 1 (capital management and the
  audited Corporation-level balance sheet), 16 and 21, and the four primary statements including
  every cash-flow detail line.
- **Form 6-K, Q2 2026 interim report**, dated 2026-08-14, filed 2026-08-17, accession
  `0001001085-26-000021` (Exhibit 99.1, `bn-20260630.htm`).
- **Form 6-K filed 2026-09-04**, accession `0001171843-26-005886` — **NOT an interim report.**
  The brief's pre-check listed it as the latest 6-K "for interims"; it is a press release,
  *"Brookfield Announces Intention to Redeem its Class A Preference Shares, Series 51 and 52"*,
  for cash on November 1, 2026. Recorded at Q4.
- **Brookfield Wealth Solutions Ltd. Form 20-F for FY2025**, filed 2026-03-26, accession
  `0001837429-26-000008` — read for the paired exchangeable-share count (Item 7.A) and the
  class C residual structure (Item 7.B).
- **Figure cross-checked against the filed statement:** corporate borrowings **$14,301M** at
  2025-12-31 appear identically on the audited consolidated balance sheet (Note 16 line), in
  Note 1's audited Corporation-level reconciliation, and in MD&A Part 4. Net income **$3,235M**
  on the audited statement of operations is the opening line of the MD&A's net-income-to-DE
  reconciliation (Glossary, p.136). Both tie.

**Price and share count — read by hand; `cover_shares.py` is not built for a 40-F and was not
used:**
- Price **$38.22**, NYSE close 2026-09-11 (`sources.price("BN")`, Yahoo chart API — **aggregator,
  flagged, live quote only**). The paired BWS exchangeable share (BNT) closed **$38.19** the same
  day, 0.08% below, consistent with its one-for-one exchange right. `split_factor_after("BN",
  "2026-08-13")` = **1.0**; the 3-for-2 split completed **2025-10-09** precedes every count used,
  and every count below is on the post-split basis the filer states.
- **Step 1 — the 40-F cover is an ISSUED count, not an outstanding count.** Cover: *"Class A
  Limited Voting Shares: 2,476,767,072 · Class B Limited Voting Shares: 85,120"* at 2025-12-31.
  Note 21(c) of the same filing: Class A **2,244,618,516** outstanding, *"Net of 183,590,069 Class
  A shares held by the company in respect of long-term compensation agreements."* Walking the
  cover down: 2,476,767,072 − 183,590,069 = 2,293,177,003, which is **48,558,487 more** than Note
  21's outstanding figure. The AIF repeats the pattern at a second date (2,450,703,928 Class A
  issued at 2026-03-10, against 2,237,128,859 outstanding at 2026-03-13 and 167,018,055 held at
  2026-03-31: a residual of ~46.6M). **The filing does not name the ~47-49M residual.** I use the
  filer's outstanding figure, which is the one its per-share figures use, and carry the residual
  as a disclosed sensitivity (~$1.8bn, ~2% of the cap) rather than resolve it by assumption.
- **Step 2 — walk forward to the latest filed count.** Q2 2026 6-K, MD&A Part 4: *"As at August
  13, 2026, the company had 2,232,266,331 Class A shares and 85,120 Class B shares
  outstanding."* (Note 12: 2,233,003,705 at 2026-06-30, net of 169,607,525 held; H1 2026
  repurchases 14,819,781.) Nothing filed after 2026-08-13 carries a count.
- **Step 3 — Class B.** 85,120 shares, *"held in a trust (the "BAM Partnership")"*, beneficial
  interests one-third Bruce Flatt, one-third Jack L. Cockwell, one-third jointly Kingston,
  Lawson, Madon, Pollock and Shah (AIF p.32). Class A and B *"rank on par with each other with
  respect to the payment of dividends and the return of capital"* (Note 21(c)) — **an economic
  common share; included.**
- **Step 4 — the paired exchangeable share is an economic common claim.** BWS 20-F Item 7.B: each
  exchangeable share is *"exchangeable at the option of the holder for one Brookfield Class A
  Share or its cash equivalent"* and receives *"distributions at the same time and in the same
  amounts as dividends on the Brookfield Class A Shares"*; BN is *"the sole holder, directly or
  indirectly, of all of our class C shares, which entitle Brookfield Corporation to all of the
  residual value in our company after payment in full of the amount due to holders of
  exchangeable shares"*. BN's own diluted count includes *"exchangeable shares of affiliate"*.
  **65,327,130** BWS class A exchangeable shares outstanding at 2026-03-23 (Item 7.A; 65,307,416
  at 2025-12-31 on the cover). BN *"currently owns less than 5%"* of them, not quantified.
  **Included in full**; the overstatement from BN's own holding is at most ~3.3M shares (~$0.1bn),
  named, not netted.
- **Step 5 — preferred shares are OUT of the common count.** Twenty-one series of Class A
  Preference Shares, *"entitled to preference over the Class A and Class B Limited Voting
  Shares"*, carrying value **$4,090M** (Note 21(a)); a senior claim, subtracted from value, never
  counted as common. Options (36.5M outstanding, US$21.21 average strike) and the escrowed stock
  plan are dilution, recorded at Q4, not in the basic cap.
- **Count used: 2,232,266,331 + 85,120 + 65,327,130 = 2,297,678,581 economic common shares.**
- **Cap = $38.22 × 2,297,678,581 = $87,817M.** On BN's Class A+B alone: $85,320M. With the
  unexplained cover residual: ~$89.7bn. Fully diluted (Note 21: 2,383.2M at 2025-12-31, including
  exchangeables and share plans): ~$91.1bn.

---
