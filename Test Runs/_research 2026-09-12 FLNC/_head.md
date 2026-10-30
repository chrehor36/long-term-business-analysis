# Company Run — FLUENCE ENERGY, INC. (FLNC) — 2026-09-12
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Run opened 2026-09-12 from a brief that told this run to read its row as UNLABELLED: the
tier-3 triage had filed FLNC under "NEGATIVE ON EVERY CONSTRUCTION ... the cheapest in the
queue", and the correction of 2026-09-12 records that label as the defect. Every gate is
open. Sovereign, price and share count are re-struck here per operator rule 5; the screen
row's cap was a hand override **frozen at 2026-09-02** and is not used. Research folder:
`Test Runs/_research 2026-09-12 FLNC/` (filing dumps pattern-ignored; the scripts that
fetched them are kept).*

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 5.35%** · **date 2026-09-11** · source: **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`daily_treasury_yield_curve` CSV, struck 2026-09-12 via
  `tools/sources.py:sovereign("USD")`, which returned `(5.35, '09/11/2026', 'US Treasury daily
  par yield curve')` — the Treasury rung, **not** the FRED fallback). 2026-09-12 is a Saturday,
  so the 09/11 print is the currently observed rate. The brief quoted 5.35% for 09-11; this
  figure was read fresh, not inherited, and it agrees.
- **Earnings currency: USD, with a real non-USD exposure that does not change the answer.**
  Fluence reports in US dollars and its centralized procurement entity's functional currency
  is the dollar (10-Q Q3 FY2026, Note 18: *"the functional currency of the centralized
  procurement legal entity is the U.S. dollar"*). Revenue by customer location for the nine
  months to 2026-06-30 was **Americas $890.9M (56.0%), APAC $470.0M (29.6%), EMEA $229.0M
  (14.4%)** (Note 4). The non-dollar revenue is hedged back to dollars with forwards
  (notional $263.0M at 2026-06-30, Note 18). **No FX conversion is applied and no ADR ratio
  exists** — FLNC is a Delaware corporation listed on Nasdaq.
- **FX note, not a conversion:** the exposure is an exposure; the quote, the statements and
  the sovereign are all dollars.

**THE SHARE COUNT — THIS IS AN UP-C, AND THE ECONOMIC COUNT IS 184,596,369.**

*Read off the cover, then reasoned from the charter and the LLC agreement as the filings
describe them. `Screens/cover_shares.py` refuses to sum classes on purpose; the summing
below is a judgment and is justified in words.*

- **The cover** of the **Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-05,
  accession `0001868941-26-000029`**: *"As of July 31, 2026, the registrant had
  **143,163,588 shares of Class A common stock** outstanding and **41,432,781 shares of Class
  B-1 common stock** outstanding."*
- **What each class is, in the filing's words.** Fluence Energy, Inc. *"is a holding company
  whose sole material assets are the limited liability company interests (the "LLC
  Interests") in Fluence Energy, LLC. All of our business is conducted through Fluence
  Energy, LLC"* (Note 1). **Class B-1 carries votes and no economics:** *"Shares of our Class
  B-1 common stock are not entitled to receive any distributions or dividends"* (Note 3), and
  *"the shares of our Class B-1 common stock held by AES entitle them to **five votes per
  share**"* (FY2025 10-K, Item 1A). **Each B-1 share is paired with one LLC Interest held by
  AES, redeemable one-for-one:** the LLC Agreement grants the Founders the right *"to have
  their LLC Interests redeemed … [for] newly-issued shares of our Class A common stock on a
  **one-for-one basis** or a cash payment … equal to a volume weighted average market price of
  one share of Class A common stock for each LLC Interest so redeemed"*, and on redemption
  *"such Founder will be required to surrender a share of Class B-1 common stock … which we
  will cancel for no consideration"* (FY2025 10-K Item 1A; 10-Q Note 3). Class B-2: 0 shares
  issued (balance sheet). Preferred: none issued.
- **The charter-level rule, verbatim:** the LLC Agreement *"requires that Fluence Energy, LLC at all times
  maintains (a) a one-to-one ratio between the number of shares of Class A common stock issued and
  outstanding and the number of LLC Interests owned by us and (b) a one-to-one ratio between the aggregate
  number of shares of Class B-1 and Class B-2 common stock issued and outstanding and the number of LLC
  Interests owned by the Founders"* (DEF 14A filed 2026-01-26, `0001140361-26-002380`).
- **So the economic count is Class A + the LLC Interests held outside Fluence, Inc.** — which
  equal the B-1 count one-for-one: **143,163,588 + 41,432,781 = 184,596,369.** That is the
  number of equal economic claims on the operating LLC's equity. **The filing states the
  ratio directly:** *"Controlling Interest Ownership 77.55% · Non-Controlling Interest
  Ownership (AES) 22.45%"* at 2026-06-30 (Note 2), and 143,136,891 ÷ (143,136,891 +
  41,432,781) = **77.55%** on the balance-sheet counts — the arithmetic reproduces the filed
  percentage to the hundredth, which is the check that B-1 maps to LLC units one-for-one.
- **The count moved inside the window this run reads.** On 2026-05-15 AES redeemed
  **10,066,414** LLC Interests for new Class A shares (8-K filed 2026-05-15, accession
  `0001104659-26-062654`, Item 3.02), taking Fluence, Inc.'s interest from 71.81% to 77.55%.
  **The economic total did not change** (51,499,195 + 131,164,365 at 2025-09-30 was
  182,663,560; the rise to 184.6M is option exercises and RSU vesting). An Up-C redemption
  moves a claim from one column to the other; it is not dilution, and it is correctly
  invisible to the economic count.
- **Potential dilution not in the count, named:** 18,738,880 shares underlying the 2030
  Convertible Senior Notes (conversion price ~$21.35, capped call to $28.74, **far out of
  the money at $9.93**); 1,205,058 pre-IPO options at $2.45; 1,649,622 RSUs; 964,545 PSUs;
  623,653 NQSOs (Note 3). In-the-money dilution at this price is the $2.45 options and the
  RSUs/PSUs, about **3.8M shares, 2.1%** — noted, not added, because the SBC subtraction in
  owner earnings is the charge for exactly this class and adding the shares too would count
  it twice.
- **THE TOOL READ THE WRONG CLASS.** `tools/run.py FLNC` printed `shares 51.5M · market cap
  0.51B · share basis: dei cover-page count as of 2025-09-30` — **51,499,195 is the Class B-1
  count**, the non-economic class. The tool's cover-count reader returned the B-1 figure and
  priced Fluence at **28% of its economic count**, a cap 3.6x too low. The hand override on
  the screen row existed because of this; the tool was never fixed. **Recorded as a tooling
  defect**, carried to the fold.

**PRICE AND CAP.**
- **Price $9.93**, close of **2026-09-11** (aggregator via `tools/sources.py:price`,
  **flagged**, operator rule 5 — aggregators for live quotes only).
- **Cap = 184,596,369 × $9.93 = $1,833.0M** (economic, whole-LLC basis).
- **The screen row carried `cap_m 1949`** = the same count at **$10.56 frozen at 2026-09-02**.
  The price fell **6.0% in nine days** and the queue's cap is **$116M (6.3%) high**. The count
  the override used was right; only the price was stale.
- **Context for the quote, not a valuation input:** the aggregator's one-year series runs
  **$7.00 (2025-09-12) → $32.23 (2026-02-03) → $9.69 (2026-09-10)**, and the Founders sold 23.0M
  shares at **$21.00** on 2026-05-12 (8-K Item 8.01). A 4.6x range in five months on a business
  whose owner earnings are the subject of this file. **[E5-29]**: volatility is not risk; it is
  recorded so that no reader mistakes any one print for a considered price.

**THE DEAL NOTE — OPENED. The "2 Item 1.01 filings" are ONE agreement filed twice.**
- **8-K filed 2026-04-03, accession `0001104659-26-039628`**, Item 1.01: *"Amendment Number
  Four to Syndicated Facility Agreement"* — the $500M revolver. It *"(i) extends the 'Trigger
  Date' … from December 31, 2025 to December 31, 2026, (ii) extends the minimum liquidity
  covenant of $150.0 million through December 31, 2026, and (iii) moves the initial test date
  of the 3.50:1.00 consolidated leverage ratio covenant from January 1, 2026 to January 1,
  2027"*; adds a $50.0M cash-collateral requirement above $450.0M of extensions of credit and a
  $150.0M cap on certain investments.
- **8-K/A filed 2026-04-06, accession `0001868941-26-000012`**: *"being filed to correct a
  clerical error in Item 1.01"* — the original read *"a $150.0 aggregate cap"*; the amendment
  reads *"$150.0 million"*. **Same agreement.**
- **What it is:** not a merger, not a share sale. **It is covenant relief** — the second
  consecutive deferral of the leverage-ratio test. That makes it a Q4 fact (staying power,
  strength 3), and it is scored there.
- **No deal-form filing exists** (no DEFM14A, S-4, 425, SC TO-T in the submissions index since
  the 10-K). The 2026-08-05 non-GAAP table does disclose *"$3.8 million for legal and
  consulting fees related to potential strategic transactions"* in the nine months — **a
  prompt, not a deal**; nothing has been filed that makes the quote a spread. Carried to Q6.
- **What the deal note CANNOT see, found by reading the index:** a Form S-3ASR (2026-05-12,
  `0001104659-26-059052`) registering **94,666,665 more Class A shares for resale by selling
  stockholders**, a secondary of 23.0M shares at $21.00 by AES, SPT Holding (Siemens pension
  trust) and Qatar Holding, and two Schedule 13D filings on 2026-05-18/19. **The sponsors are
  sellers.** Scored at Q3.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Anchor annual: Form 10-K, FY ended 2025-09-30, filed 2025-11-25, accession
  `0001868941-25-000081`** (`flnc-20250930.htm`). Read: Item 1 (business, products, supply
  chain, customers, IRA/OBBBA), Item 1A (including the organizational-structure, TRA, Founder
  and controlled-company risks), Item 7 MD&A and key operating metrics, the four statements,
  and the notes on revenue, inventory, debt, commitments and contingencies, related parties,
  SBC, supply chain financing and income taxes.
- **The 10-K series FY2021 → FY2025**, so every owner-earnings year rests on a filed statement:
  FY2021 `0001868941-21-000012` (2021-12-14, the LLC-era 10-K) · FY2022 `0001868941-22-000120`
  (2022-12-14) · FY2023 `0001868941-23-000085` (2023-11-29) · FY2024 `0001868941-24-000070`
  (2024-11-29) and its **10-K/A** `0001104659-25-036111` (2025-04-18) · FY2025 as above.
- **The current perimeter document: Form 10-Q, quarter ended 2026-06-30 (Q3 FY2026), filed
  2026-08-05, accession `0001868941-26-000029`** — read in full: statements, all 20 notes,
  MD&A, Part II. Also fetched for the quarterly walk (each is cited where it is used): 10-Qs for 2026-03-31
  `0001104659-26-056304`, 2025-12-31 `0001868941-26-000005`, 2025-06-30
  `0001868941-25-000076`, 2025-03-31 `0001868941-25-000060`, 2024-12-31
  `0001868941-25-000015`, 2024-06-30 `0001868941-24-000059`, 2024-03-31
  `0001868941-24-000045`, 2023-12-31 `0001868941-24-000014`.
- **Six 8-K EX-99.1 earnings releases** (FY23 Q4, FY24 Q4, FY25 Q4, FY26 Q1, Q2, Q3), fetched
  **before** scoring `[E4-29]` and `[E4-22]`'s third flag, per the standing CGNX instruction.
- **DEF 14A filed 2026-01-26, accession `0001140361-26-002380`**, fetched for related-person
  transactions and pay metrics. **8-K 2026-09-01** (`0001868941-26-000037`, Siemens director
  designation). **8-K 2026-05-15** (AES redemption and secondary). **S-3ASR 2026-05-12.**
- **Figure cross-checked against the filed statement:** *Net cash (used in) provided by
  operating activities*, FY2025 Consolidated Statements of Cash Flows, **$(145,538) thousand**
  — agrees with XBRL `NetCashProvidedByUsedInOperatingActivities` −145.5M. Checked at four more
  lines in the same filed statement: *Stock-based compensation* **$19,540** (XBRL 19.5),
  *Depreciation and amortization* **$29,343** (XBRL 29.3), *Accounts payable* **$(119,228)**
  (XBRL −119.2), *Deferred revenue* **$361,903**. And FY2024's *Accounts payable* **$370,124**
  against *Net cash provided by operating activities* **$79,685** — 464.5%, which **reproduces
  the screen's `wc_note` of 464%** and names its year: **FY2024**.
- *No ladder rung was blocked. Everything above is SEC EDGAR rung 2; the only aggregator
  input in the file is the live quote, flagged above.*

