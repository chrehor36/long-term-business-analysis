# Company Run — Criteo S.A. (CRTO) — 2026-09-21
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**VERDICT: Q2 OUT on the business.** Q1 IN. The file closes at Q2 on `[E3-03]` criterion 2.
Q3, Q4, Q5 and Q6 are NOT OPENED. A COMPUTATION block sits below the close, headed as the
protocol requires, carrying no entry language.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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

### 0(a) THE CAP, RE-STRUCK BY HAND [operator rule 4]

`cap = close(anchor) x shares(measurement) x splits AFTER measurement`. `close`, never `adjclose`.

- **Share count, from the cover of the newest periodic filing, verbatim:**
  *"As of July 31, 2026, the registrant had 48,997,559 ordinary shares, nominal value €0.025 per
  share, outstanding."* — Form 10-Q for the quarter ended 2026-06-30, accession
  **`0001576427-26-000092`**, filed 2026-08-05, cover page.
- **One class or more?** **ONE.** The 8-K cover pages of 2026-07-29 and 2026-08-05 each register a
  single class under Section 12(b): *"Ordinary Shares, nominal value €0.025 per share | CRTO |
  Nasdaq Global Select Market"*. No second class, no preferred outstanding.
- **Treasury shares are OUTSIDE the cover count, and they exist.** The 10-Q balance sheet reads
  *"Common shares, € 0.025 par value, 53,728,895 and 55,659,895 shares authorized and issued, and
  48,550,453 and 51,151,866 outstanding at June 30, 2026 and December 31, 2025, respectively."*
  Issued less outstanding at 2026-06-30 = **5,178,442 treasury shares**, held by the company and
  not in the cover figure. The brief's prior — that a European issuer can hold its own shares in
  treasury while they remain issued — is **confirmed on the filed statement**, and the cover figure
  is already net of them, so no adjustment is due.
- **Splits after measurement:** none. `tools/sources.py split_factor_after("CRTO","2026-06-30")`
  returns **1.0**; no split appears anywhere in the twelve-year filed record.
- **The instrument changed on 2026-07-29 and the count is still comparable.** Until that date the
  listed security was an American Depositary Share, *"each representing one ordinary share"*
  (FY2025 10-K cover). The 8-K12B of 2026-07-29 records that *"all ADSs were mandatorily
  surrendered and the holders thereof received one ordinary share of Lux Criteo per ADS"*. **The
  ADS ratio was and remains 1:1, so no ADR ratio enters the cap.**
- **Price:** **$16.70**, close of **2026-09-18**, Nasdaq, USD. Source: Yahoo chart endpoint via
  `tools/sources.py price()` — **AGGREGATOR, used for a live quote only, and flagged as such**
  under operator rule 5.

> **HAND-STRUCK CAP = 48,997,559 x $16.70 x 1.0 = $818,259,235 ≈ $818.3M**

The screen carried **$865M**, which is 48,997,559 x **$17.65**; the closes of 2026-09-03 and
2026-09-04 were $18.17 and $17.62, so the screen's cap is the same share count at an early-September
price. **The screen's share count was right; its price is stale by two weeks and 5.4%.**

### 0(a)(ii) THE `cap_flag`, SETTLED ON ARITHMETIC AND NOT ASSERTED

The flag: *"CAP BELOW FILED PUBLIC FLOAT - cap $865M against a filed float of $1,254M (1.45x) as of
2025-06-30. A cap cannot be smaller than a subset of itself."*

**The float figure is real and I have read it in the filing.** FY2025 10-K, accession
`0001576427-26-000014`, cover page: *"The aggregate market value of voting stock held by
non-affiliates of the registrant as of June 30, 2025, the last business day of the registrant's most
recently completed second fiscal quarter, was $ 1,254 million , based on the closing price of the
American Depositary Shares as reported by the Nasdaq Global Select Market on such date."* The same
sentence appears identically on the 10-K/A cover of 2026-04-28.

**Two hypotheses were live: a date mismatch, or an error in one of the two numbers. The arithmetic
settles it as a DATE MISMATCH, and both numbers are correct at their own dates.**

| | date | shares | price | product |
|---|---|---|---:|---:|
| filed float | 2025-06-30 | 52.34M non-affiliate (derived) | $23.96 | **$1,254M** (filed) |
| hand-struck cap | 2026-09-18 | 48,997,559 outstanding (cover) | $16.70 | **$818.3M** |

Working: $1,254M ÷ $23.96 = **52.34M** non-affiliate shares. The Nasdaq close on 2025-06-30 was
**$23.96**, and the FY2025 10-K states the float is struck on that close. The company's own Q2 2025
weighted-average share count was **52,986,068** (10-Q of 2026-08-05, EPS note), so 52.34M
non-affiliate against about 52.5M outstanding is a 99.7% non-affiliate register — consistent with a
company having no 10% insider holder. **The derived share count reproduces the filed float to within
one-third of one percent, so neither number is wrong.**

The whole gap is then two movements, both filed:
- **price:** $23.96 → $16.70, **−30.3%**
- **shares outstanding:** about 52.5M → 48,997,559, **−6.7%**, and the reduction is documented:
  3,187,498 shares repurchased at a weighted average $32.80 in FY2025 and 3,339,332 at $18.36 in
  H1 2026 (10-Q equity note), with 1,931,000 treasury shares cancelled in H1 2026.
- product: 0.697 x 0.933 = 0.650; $1,254M x 0.650 = **$815M**, against the hand-struck **$818.3M**.
  **The reconciliation closes to 0.4%.**

> **`cap_flag` RESOLVED: DATE MISMATCH. Refuted as an error claim. A float dated 2025-06-30 is not
> a subset of a cap dated 2026-09-18; it is a subset of a cap that no longer exists. Nothing in
> either number is wrong and no figure is discarded.**

### 0(b) THE SOVEREIGN — FOR THE CURRENCY THE BUSINESS EARNS IN [E4-15, E3-32]

**This name is where the question bites, and the brief was right to say so. It had to be argued from
the filings, not assumed.**

**What the filings say.** Three separate facts, and they do not all point the same way:
1. **Reporting currency is the U.S. dollar.** Every statement in the FY2025 10-K and the Q2 2026
   10-Q is presented in USD; `iso4217:USD` is the unit on every financial fact in companyfacts.
2. **The parent's functional currency is the euro.** FY2025 10-K, Item 7A: *"The functional currency
   of the Company is the euro, while our reporting currency is the U.S. dollar."* Restated in Item
   1A: *"Because Criteo S.A.'s functional currency is the euro, while Criteo S.A.'s reporting
   currency is the U.S. dollar, we face exposure to fluctuations in foreign currency exchange
   rates."*
3. **The geographic split, from the revenue footnote, FY2025, "based mainly on the location of
   advertisers' campaigns":**

| region | FY2025 revenue | share | named countries |
|---|---:|---:|---|
| Americas | $836.7M | 43.0% | **United States $753.3M (38.7%)** |
| EMEA | $728.1M | 37.4% | Germany $207.6M (10.7%); France $88.9M (4.6%) |
| Asia-Pacific | $380.2M | 19.5% | Japan $221.1M (11.4%) |
| **Total** | **$1,944.9M** | 100% | |

**THE DECISION, AND ITS GROUND.** **USD.** Three reasons, recorded so a later reader can overturn
them:
- the **largest single-currency block is USD** — the United States alone is 38.7% of revenue, and no
  other single currency reaches half that (Japan 11.4%, Germany 10.7%, France 4.6%). EMEA at 37.4%
  is not a euro block: it contains the United Kingdom, Turkey, the Nordics and the Middle East, and
  the two named euro countries inside it total 15.3%.
- **every number in the owner-earnings construction is a USD number** on the face of the filed
  statement. Pricing a USD cash-flow series against a euro bond would introduce exactly the
  currency mismatch the ATLKY defect was.
- the euro is the **parent holding company's** functional currency, not the currency the operating
  business earns. The redomiciliation to Delaware completing 2027-01-01 (section 0(d)) removes even
  that.

- **rate 5.34 %** · **date 2026-09-18** · **source: U.S. Treasury daily par yield curve, 30-year,
  from the issuing authority.** Raw CSV saved to
  `_research 2026-09-21 CRTO/sovereign_USD_treasury_2026.csv`; the row reads
  `09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34` and the last
  column is the 30-year. **FRED was not used.**
- **The alternative, stated because the decision could go the other way:** ECB SDW
  `YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y` = **3.7502%**, observation date **2026-09-17**, raw CSV saved
  to `sovereign_EUR_ecb_SR30Y.csv`. **Choosing USD is the choice that is harder on the buyer**, by
  159 basis points, so the decision cannot be accused of being made to help the name.
- **FX:** none required. The quote is USD and the reporting currency is USD. ADR ratio: not
  applicable since 2026-07-29 (section 0(a)); it was 1:1 before.
- **The screen's `vs_sovereign 0.0383` is discarded in full**, as instructed and as the arithmetic
  confirms: it is 3.83%, an off-date figure, and it is not the rate struck here.

### 0(c) THE FILING WAS READ — not tagged data [E3-27, E4-14]

- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Documents, dates and accession numbers:**

| document | period | filed | accession |
|---|---|---|---|
| **Form 10-K, FY2025** | 2025-12-31 | 2026-02-26 | **`0001576427-26-000014`** |
| Form 10-K/A (Amendment No. 1) | 2025-12-31 | 2026-04-28 | **`0001576427-26-000033`** |
| Form 10-Q | 2026-06-30 | 2026-08-05 | **`0001576427-26-000092`** |
| Form 8-K12B (redomiciliation completed) | 2026-07-29 | 2026-07-29 | **`0001628280-26-050326`** |
| Form 8-K, Items 2.02/5.02/5.03/7.01/9.01 + EX-99.1 | 2026-08-05 | 2026-08-05 | **`0001628280-26-052913`** |
| Form 8-K, Items 1.01/8.01/9.01 (U.S. Merger) | 2026-08-05 | 2026-08-05 | **`0001628280-26-053414`** |
| Form 10-K FY2024 / FY2021 / FY2018 (for the long series) | — | — | `0001576427-25-000031` / `0001576427-22-000009` / `0001576427-19-000014` |

- **What the 10-K/A amends, read before the original was quoted, as instructed.** Its Explanatory
  Note: *"This Amendment No. 1 on Form 10-K/A (this "Amendment" or "Form 10-K/A") amends our Annual
  Report on Form 10-K for the fiscal year ended December 31, 2025 filed with the Securities and
  Exchange Commission (the "SEC") on February 26, 2026 (the "Original 10-K"), to include the
  information required by Items 10 through 14 of Part III of the Original 10-K."* and *"Because no
  financial statements have been included in this Amendment"* … *"Except for the information
  described above, the Company has not modified or updated disclosures provided in the Original
  10-K in this Amendment."* **It is a Part III-only amendment. No financial statement, no MD&A and
  no footnote is restated, so the Original 10-K's figures stand and may be quoted.**
- **Figure cross-checked against the filed statement:** **operating cash flow, FY2025.** The XBRL tag
  `NetCashProvidedByUsedInOperatingActivities` returns **$311,237** thousand. The filed Consolidated
  Statements of Cash Flows in the FY2025 10-K reads `Net cash provided by operating activities |
  311,237 | 258,161 | 224,246` for 2025, 2024 and 2023. **Match to the dollar, all three years.**
  A second cross-check: the tagged FY2025 revenue of $1,944.9M equals the filed segment table's
  `Total | $ 1,944,901` (Retail Media $263,872 + Performance Media $1,681,029).

### 0(d) THE DEAL — TWO TRACKS, BOTH SETTLED. **NEITHER IS A CHANGE OF CONTROL.**

**The brief named two tracks and missed the event that closes the first one.** See the BRIEF DEFECTS
section at the foot of this file.

**TRACK ONE — France to Luxembourg. COMPLETED 2026-07-29. Not a deal at all; a cross-border
conversion of one legal person.** The S-4 of 2025-11-03 (`0001193125-25-262679`, File No. 333-291227)
and the 425s from 2025-10-29 belong to this track; the shareholder vote of 2026-02-27 approved it.
It completed, and the completion is filed on **Form 8-K12B, accession `0001628280-26-050326`**, whose
Introductory Note reads, verbatim:

> *"On July 29, 2026, Criteo S.A. ("Criteo" or the "Company") completed its previously announced
> corporate redomiciliation from France to Luxembourg via a cross-border conversion (the
> "Conversion")."*

and, in the same note:

> *"the Company converted, without being dissolved, wound up or placed into liquidation, from being
> a public limited liability company ( société anonyme ) governed by the laws of France ("French
> Criteo") to being a public limited liability company ( société anonyme ) governed by the laws of
> the Grand Duchy of Luxembourg ("Lux Criteo")"*

> *"each ordinary share of French Criteo, including shares represented by French Criteo's American
> Depositary Shares ("ADSs"), each of which represented one ordinary share of French Criteo, was
> converted into one ordinary share of Lux Criteo"*

> *"The Conversion did not result in any material change to the Company's business, operations,
> assets, liabilities, obligations, directors or management."*

Rule 12g-3(a) succession is asserted in the same document: *"(i) Lux Criteo is the successor issuer
to French Criteo"*. **One-for-one, same CIK, same Commission file number 001-36153, same directors
and officers, no cash, no premium, no acquirer.**

**AND THE BRIEF'S QUESTION ABOUT WHAT CRITEO WAS BEFORE LUXEMBOURG IS ANSWERED BY THIS SAME
DOCUMENT.** The 8-K12B cover carries *"32 Rue Blanche , Paris , France 75009"* under *"(Former name
or former address, if changed since last report)"*, and the FY2025 10-K cover states the state of
incorporation as **France**. **So the French société anonyme is the whole of the twelve-year filed
record, and the Luxembourg entity is eight weeks old. The continuity of the record is not broken:
the Conversion is expressly "without being dissolved", the registrant is the same legal person, the
CIK never changed, and the 10-Q of 2026-08-05 presents the full comparative history without
re-basing.**

**TRACK TWO — Luxembourg to Delaware. SIGNED 2026-08-05, effective 2027-01-01. Also not a change of
control.** Re-struck by me from accession **`0001628280-26-053414`**, Item 1.01, and the dispatcher's
quotation is **CONFIRMED ACCURATE** where it overlaps. The full filed sentence, with what the brief's
ellipses removed restored:

> *"On August 5, 2026, Criteo S.A., a public limited liability company ( société anonyme )
> incorporated and existing under the laws of the Grand Duchy of Luxembourg ("Lux Criteo"), entered
> into the Agreement and Plan of Merger (the "Merger Agreement") and the Common Draft Terms of
> Cross-Border Merger (the "Draft Terms"), in each case, with Criteo Holdings, Inc., a Delaware
> corporation and wholly owned subsidiary of Lux Criteo ("U.S. Criteo"), pursuant to which, on the
> terms and subject to the conditions set forth therein, Lux Criteo will merge with and into U.S.
> Criteo (the "U.S. Merger"), with U.S. Criteo surviving the U.S. Merger."*

Effective Time, verbatim: *"at 12:00:01 a.m., New York City time, on January 1, 2027"* — **confirmed
as the brief stated it.** Consideration, verbatim from clause (D):

> *"each ordinary share of Lux Criteo issued and outstanding immediately prior to the Effective Time
> (other than any shares held in treasury of Lux Criteo (the "Treasury Shares")) will automatically
> be cancelled, and U.S. Criteo will issue the holder thereof in exchange therefor shares of its
> common stock on a one-to-one basis, in each case without interest and net of any applicable
> withholding taxes"*

and clause (H): *"the directors and officers of Lux Criteo immediately prior to the Effective Time,
from and after the Effective Time, will be the directors and officers of U.S. Criteo"*.

**THE DECISION, WITH CONSEQUENCES, AS THE BRIEF REQUIRED.**

| precedent | does it apply? | why |
|---|---|---|
| **ROKU** — a live deal makes the quote a spread, not an owner-earnings price | **NO** | There is no counterparty, no consideration, no premium and no acquirer on either track. U.S. Criteo is *"a wholly owned subsidiary of Lux Criteo"*; the exchange is one-for-one; the directors and officers continue. Nothing is being bought, so nothing can trade at a spread to a bid. |
| **LEG** — the name no longer exists as a public security | **NO** | The security exists and trades. Track one COMPLETED and the shares kept trading under **CRTO** without interruption: *"Lux Criteo's ordinary shares will begin trading on Nasdaq at the opening of trading on July 29, 2026 and will trade under the symbol "CRTO" in lieu of the ADSs"*. Track two is expected to list on NYSE. |

> **DEAL SETTLED: BOTH TRACKS ARE REDOMICILIATIONS, NOT CHANGES OF CONTROL. THE QUOTE IS AN
> OWNER-EARNINGS PRICE AND IS PRICED NORMALLY.** The `deal_note`'s warning is discharged, and the
> screen's count of *"6 filing(s) since the annual report"* is refuted as a signal: those filings are
> conversion and merger mechanics for the company's own domicile, and the screen could not see the
> 2025 half of track one or the completion on 2026-07-29 at all.

**Two consequences that DO follow, and neither is a spread:**
1. **Track two can be abandoned.** The Merger Agreement says so: *"Lux Criteo and U.S. Criteo may
   mutually decide to terminate the Merger Agreement and abandon the Merger at any time prior to the
   Effective Time."* It is also conditioned on a shareholder vote and on an S-4 becoming effective.
2. **Jurisdiction moved twice in six months and moves again in January.** `[E3-66]` requires a
   non-US run to say where its shareholders stand in the queue. Today the answer is Luxembourg law
   (8-K12B Item 3.03: *"the rights of the shareholders of Lux Criteo are governed by Luxembourg law
   and the Lux Articles"*); from 2027-01-01 it is Delaware. That is a Q4 item and Q4 is not opened.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively
> simple and stable in character. If a business is complex or subject to constant change, we're not
> smart enough to predict future cash flows."* — **[E3-31]**, 1992 letter

### Unit economics, in my own words, without management's language

**Two businesses, filed as two segments, and they are not the same trade.**

**Performance Media ($1,681.0M of FY2025 revenue, 86.4%).** An online retailer wants back a shopper
who looked at a coat and left. Criteo holds a record of what that shopper looked at, buys an
advertising slot somewhere else on the internet in the fraction of a second before a page loads, and
puts the coat in it. **It bills the advertiser the whole price and pays the slot's owner out of the
proceeds. What it keeps is the difference.** The filed name for the amount paid away is traffic
acquisition cost; the filed name for the difference is Contribution ex-TAC. **So each dollar is:
the media bought at wholesale, resold with targeting at retail, less the servers that ran every
auction it bid in, won or lost.**

**Retail Media ($263.9M, 13.6%).** A supermarket has advertising space of its own — the sponsored
slots on its website and app. Criteo runs the software that auctions those slots to the brands whose
products sit on the shelves, and **shares the proceeds with the retailer.** Criteo does not own the
space. The retailer does, and the retailer can run the auction itself or hire someone else.

The margin structure, all filed, FY2025:

| line | FY2025 | source |
|---|---:|---|
| Revenue | $1,944.9M | segment note |
| less traffic acquisition cost | $(770.3)M | derived: revenue minus Contribution ex-TAC |
| **Contribution ex-TAC** | **$1,174.6M** (60.4% of revenue) | non-GAAP reconciliation |
| less other cost of revenue | $(125.2)M | same reconciliation |
| **Gross profit** | **$1,049.4M** | filed income statement |
| **Operating income** | **$202.8M** | filed income statement |
| **Net cash from operating activities** | **$311.2M** | filed cash-flow statement |

**The scarce input this business controls.** Its own filing nominates three: *"Actionable Commerce
Data: We curate one of the largest commerce data sets in the world, normalizing and mapping ove r 5
billion SKUs to brands, merchants, and transactions"*; *"Extensive, Cross-Channel Media Access: We
reach approximately 740 million daily active users through direct"* integrations; and the AI engine.
**On my own reading of the filings, only one of those is genuinely controlled, and only partly:
the code that sits inside retailers' and publishers' own properties under contract.** The data is
other people's data, licensed; the media is other people's inventory, bought; the shoppers are other
people's customers. **The scarce asset is a contract position, and a contract position is renewable
by the counterparty.** That is a Q2 finding and it is recorded there, not here.

**Will the fundamentals look broadly the same in ten years?** **No, and the company says so in
Item 1**, verbatim: *"Our market is complex, rapidly evolving, highly competitive, still fragmented
and yet rapidly consolidating."* The FY2024 10-K carries the risk-factor heading *"We operate in a
rapidly evolving industry, which makes it difficult to evaluate our future prospects and may
increase the risk that we will not be successful."* The FY2021 10-K describes the company as
undergoing *"a significant transformation, partially in response to major changes in the advertising
technology industry"*, of which *"The components of our transformation include diversification of
our services as we shift away from third-party cookies"*.

### THE VERDICT AND WHY IT IS IN AND NOT OUT

**Q1 asks whether I can understand how this makes money. I can, and the paragraphs above do it from
filed figures without management's vocabulary: buy media wholesale, resell it with targeting at
retail, keep the spread; and run other people's on-site auctions for a share.** Both legs are
separately disclosed with their own revenue and their own cost line, the reconciliation to gross
profit is published, and my construction of traffic acquisition cost reproduces the filed figures.

**The instability [E3-31] warns about is real here and I am not going to pretend otherwise — but it
is a claim about the durability of the advantage, which is the question Q2 asks, and the framework
puts it there.** `[E4-04]`'s scope paragraph and the 2026-09-20 verdict-form ruling both locate
rapid-and-continuous-change at Q2. Marking Q1 OUT on it would say I cannot comprehend the business;
that would be false, and it would also hide the finding, because Q1 OUT is permanent while the Q2
analysis below is the one that names the mechanism.

**Recorded and carried forward to Q2, not resolved here:** the ten-year answer is **NO**, on the
company's own words.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its
> customers to have no close substitute and; (3) is not subject to price regulation."* — **[E3-03]**,
> 1991 letter

### The three criteria, one at a time, on filed evidence

**(1) Needed or desired — YES.** Advertisers must acquire customers and retailers must monetise
their own inventory. Criteo's media spend was *"$4.5 billion in the last 12 months"* (EX-99.1,
2026-08-05). The demand for the category is not in question.

**(2) Thought by its customers to have NO CLOSE SUBSTITUTE — NO. This is where the file closes, and
the strongest single piece of evidence is the company's own Item 1.**

> *"We currently compete with large, well-established companies, such as Amazon, Meta Platforms,
> Google, and Microsoft, pure play DSPs, such as The Trade Desk, pure play SSPs such as Magnite or
> PubMatic, and pure play retail SSPs such as Publicis' CitrusAd, that focus on monetizing
> retailers' media, as well as smaller, privately held companies such as Kevel or Koddi."*
> — FY2025 10-K, Item 1, "Competition"

**The PUBM run's quotation is VERIFIED verbatim in Criteo's own filing.** Criteo names **nine**
competitors by name across every position in the chain, and the sentence immediately before them
reads *"Our market is complex, rapidly evolving, highly competitive, still fragmented and yet
rapidly consolidating."* A company that can name nine close substitutes for its customers' money in
one sentence is not describing a franchise; it is describing a market.

**And the filings quantify the substitution, which is what makes this OUT rather than an opinion.**

**(2a) The customers leave, at a published rate, and the count has fallen for four straight years.**
*"In each of 2025 , 2024 and 2023 , our client retention rate was approximately 90%"* (FY2025 10-K).
Ten per cent of live clients stop being live clients every year. The count itself, on the filings:

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Number of clients** | 14,468 | 18,118 | 19,419 | 20,247 | 21,460 | **21,745** | 18,990 | 18,197 | 17,269 | **16,786** |

Source: the "key metrics" table of each year's 10-K (FY2018, FY2021, FY2024 and FY2025 filings).

**THE METHODOLOGY BREAK IS REAL AND I AM NOT SMOOTHING IT.** The FY2024 10-K footnotes the table:
*"In the first quarter of 2023, we streamlined our client count methodology which is now based on
unique billing accounts while the previous methodology included clients from whom Criteo has
received a signed contract or an insertion order during the previous 12 months. The new methodology
led to the consolidation of some clients accounts but does not change the underlying activity or the
overall trends."* **So 21,745 (2021) and 16,786 (2025) are not on one basis and the −22.8% that
crosses the break must not be quoted.** On a single basis the fall is **18,990 → 16,786, −11.6% in
three years, four consecutive annual declines**, and that is the figure this run uses.

**This is the `[E4-55]` shape and the corpus names it:** *"This decline in physical volume is a
serious reverse, not likely to disappear in some ""bounce back'' e&#65533;ect. Nor do we expect another
sharp rise in prices like the approximately 40% rise that recently occurred, holding dollar volume
roughly level despite a precipitous drop in physical volume."*
**OCR ARTIFACTS FLAGGED, NOT SMOOTHED, per PRIME RULE 1:** the ledger row carries doubled opening
quotation marks and two apostrophes for the closing pair around *bounce back*, and a U+FFFD
replacement character in place of the `ff` ligature in *effect*, rendered above as the numeric
entity `&#65533;`. Both are reproduced as the row holds them. Criteo's dollar line was held level —
revenue $1,949.4M (2023), $1,933.3M (2024), $1,944.9M (2025) — while the client series went down
every year. **Where units exist, monitor units.**

**(2b) Two customers moved and took a fifth of the segment that was supposed to be the franchise.**
The Q2 2026 earnings release, EX-99.1 to accession `0001628280-26-052913`:

> *"Retail Media revenue decreased (21)%, or (22)% at constant currency, and Retail Media
> Contribution ex-TAC decreased (21)%, or (22)% at constant currency, reflecting a $21 million
> headwind from previously communicated scope changes with two specific Retail Media clients"*

**Two clients out of roughly 16,800 produced a 21% decline in an entire reporting segment in one
quarter.** That is the [E3-03] criterion-2 test failing in the most direct form the filings permit:
the customers not only have a close substitute, two of them took it, and one quarter's effect is
visible in the consolidated result.

**(2c) The top line has shrunk for seven years while the market grew.** Revenue, filed:
$2,300.3M (2018), $2,261.5M (2019), $2,072.6M (2020), $2,254.2M (2021), $2,017.0M (2022),
$1,949.4M (2023), $1,933.3M (2024), $1,944.9M (2025). **Seven years, −15.4%.**

**(2d) And the measure management itself calls a key profitability metric has now turned down, with
the company guiding it down for the full year.** From the same EX-99.1:

> *"We now expect Contribution ex-TAC to decrease -12% to -10% at constant currency."*

with Q2 2026 Contribution ex-TAC *"decreased (13)% year-over-year, or decreased (12)% at constant
currency, to $255 million (Q2 2025: $292 million)"*, and H1 2026 revenue $853M against $934M, −9%.
The CEO's own words in that release: *"While our second quarter top line performance was
disappointing"*.

**(3) Not subject to price regulation — PASSES, narrowly, and the regulation bites the input
instead.** No authority sets Criteo's prices. But the FY2025 10-K carries a CNIL contingency
(contexts dated 2022-08-03 and 2023-06-21 in the filed XBRL), a *"Payment for contingent liability
on regulatory matters"* of **$43.3M** on the FY2023 cash-flow statement, and a standing risk factor
that *"Our ability to generate revenue depends on our collection of significant amounts of data from
various sources, which may be restricted by consumer choice, clients, publishers and retailer
partners, browsers or other software"*. **Criterion 3 is satisfied on its own terms; the regulation
here constrains the scarce input, not the price, and that is a different finding.**

### `[E4-04]` — must the moat be continuously rebuilt?

> *"Our criterion of "enduring" causes us to rule out companies in industries prone to rapid and
> continuous change. Though capitalism's "creative destruction" is highly beneficial for society,
> it precludes investment certainty. A moat that must be continuously rebuilt will eventually be no
> moat at all."* — **[E4-04]**

**The scope test from the framework: does a lapse in spending destroy the structure, or merely narrow
it, and does the spending defend the same advantage or buy its replacement?** On Criteo's own filed
record the spending buys the **replacement**, repeatedly and by name:
- FY2021 10-K: the transformation *"include[s] diversification of our services as we shift away from
  third-party cookies"* — the identifier the retargeting business was built on.
- The IPONWEB acquisition was justified in the FY2021 10-K as *"further reducing our reliance on
  third-party cookies and other identifiers."*
- By 2026 the basis has moved again: *"Criteo became OpenAI's first advertising technology partner
  in March 2026"* (EX-99.1, 2026-08-05).

**Three different bases in five years is the replaced-moat case, not the defended-moat case** —
Mitsui's Rhodes Ridge, not Coca-Cola's advertising.

**But I do not reach a verdict on [E4-04], and the reason matters.** The framework's ruling of
2026-09-20 applies [E4-04] **as a competence limit, never as a fourth franchise criterion**, and it
sends a name that *passes* [E3-03] but whose durability cannot be judged to **UNKNOWABLE at Q2**,
the perimeter close. **Criteo does not pass [E3-03]. Criterion 2 fails on filed evidence, not on my
inability to judge the future, so the verdict is OUT on the business and [E4-04] never becomes
load-bearing.** It is recorded because it is true, not because it decides.

### THE COMPETITOR ROW — REQUIRED **[E3-28]**

> *"I can't be an intelligent owner of a business unless I know what all the other businesses in
> that industry are doing."* — **[E3-28]**

**Metric: each filer's own top line, on its own basis, over one window — FY2021 to FY2025 — taken
from that filer's own annual report.** Revenue *levels* are not comparable across these filers
because some report gross of media cost and some net; **growth of each filer's own series is**,
because each filer's basis is constant within itself. The second pair of columns gives gross profit
where the filer tags it, for the same reason.

| Company | position in the chain | FY2021 revenue | FY2025 revenue | **change** | FY2021 gross profit | FY2025 gross profit | **change** |
|---|---|---:|---:|---:|---:|---:|---:|
| **CRITEO (subject)** | demand side + retail media | **$2,254.2M** | **$1,944.9M** | **−13.7%** | **$781.9M** | **$1,049.4M** | **+34.2%** |
| The Trade Desk | pure-play DSP, named by Criteo | $1,196.5M | $2,896.3M | **+142.1%** | not tagged (revenue is net) | — | — |
| Taboola | demand + supply, native | $1,378.5M | $1,912.0M | **+38.7%** | $441.1M | $569.5M | +29.1% |
| Magnite | pure-play SSP, named by Criteo | $468.4M | $714.0M | **+52.4%** | not tagged | — | — |
| PubMatic | pure-play SSP, named by Criteo | $226.9M | $282.9M | **+24.7%** | $168.6M | $179.8M | +6.6% |
| Digital Turbine | mobile demand + supply | $747.6M (FYE 3/22) | $565.3M (FYE 3/26) | **−24.4%** | $376.9M | $321.6M | −14.7% |
| Alphabet — Google Network | the incumbent Criteo names first | $257,637M (group) | group, unsegmented on this metric | — | — | — | — |

Sources: each filer's own 10-K, read through `companyfacts` at the newest vintage and, for MGNI and
TTD, against the 10-K texts on disk.

- **Peers named: 6 of the 9 competitors Criteo itself names.** The other three — Amazon, Meta and
  Microsoft — file no advertising-intermediary segment that can carry this metric, and CitrusAd
  (Publicis), Kevel and Koddi are private or unsegmented. **Their absence is stated, not hidden**,
  and it does not soften the row: the three unavailable names are the three largest, and the six
  available ones already settle the question. The moat class below is **NONE**, not PROVISIONAL, so
  the unavailability does not convert this into UNRESEARCHED.
- **Source vintage, checked as the brief required:** the MGNI, TTD, TBLA, APPS and GOOGL
  companyfacts files and two peer 10-K texts were fetched by the PUBM run on **2026-09-19** and were
  **copied into this run's folder** rather than read across. PUBM's own companyfacts was fetched
  fresh today, 2026-09-21. **Criteo's own figures are taken from Criteo's filings only, never from
  the peer folder.**

**WHAT THE ROW SAYS.** Over one window, Criteo is **the only filer in the row that sells less than it
did four years ago except Digital Turbine**, and the pure-play DSP it names as its direct
demand-side competitor — The Trade Desk — grew **142%** while Criteo shrank **13.7%**. On the supply
side, the two SSPs Criteo names as substitutes each grew. **A moat is a claim about relative
position, and the relative position moved against the subject on the one metric every filer
publishes.**

**THE ROW'S LIMIT, STATED AS THE FRAMEWORK REQUIRES `[E3-61]`:** *"In some businesses, the
participants behave like a demented Kellogg. In other businesses, they don't. … I think you'd have
to know the people involved to fully understand what was happening."* The row shows position. It
cannot show conduct, and none of it tells me whether these managements will compete rationally from
here.

### THE DISCONFIRMING CASE, PUT AT FULL STRENGTH FIRST **[E4-26, E4-51]**

> *"I feel that I'm not entitled to have an opinion unless I can state the arguments against my
> position better than the people who are in opposition."* — **[E4-51]**

**Four filed facts cut against the OUT, and this is the best version of that case:**
1. **The take went UP, not down, and by a lot.** Contribution ex-TAC as a share of revenue:
   **52.5% (2023) → 58.0% (2024) → 60.4% (2025)**. The PUBM prior — a −66% collapse in revenue per
   million impressions — **does not replicate at Criteo. It is REFUTED on the subject's own
   filings.** The absolute figure grew too: $928.2M (2022), $1,022.6M (2023), $1,121.5M (2024),
   $1,174.6M (2025).
2. **Gross profit grew 34.2% over the window on which revenue fell 13.7%**, and operating income
   went $151.9M (2021) to $202.8M (2025), the highest in the filed record.
3. **Operating cash flow is the best it has ever been**: $311.2M in FY2025 against a twelve-year
   mean of $216.0M, and the FY2025 figure was **not** flattered by working capital — the filed
   detail lines net to **−$13.3M** (trade receivables +$246.0M against trade payables −$265.4M and
   four smaller lines).
4. **The client decline is partly deliberate and the company said so in advance.** FY2021 10-K:
   *"While we intend to put more focus on our Strategic and Core clients and therefore less emphasis
   on the Tail client category"*, and both the FY2018 and FY2025 10-Ks warn that *"changes in client
   count does not necessarily correspond to changes in revenue for a given period."*

**WHY IT DOES NOT SAVE THE GATE, AND THIS IS THE CORE OF THE FINDING.** **The margin gain came from
the price of the input falling, not from the price of the output rising, and Criteo says so in the
MD&A itself:**

> *"The increase in Gross Profit and Contribution ex-TAC was driven by growth in Retail Media and
> lower traffic acquisition costs in Performance Media, related primarily to the decrease of the
> average CPM for inventory purchased."* — FY2025 10-K, and the same sentence for the 2024
> comparison

**`[E3-62]` is the test the corpus supplies for exactly this, and it asks who keeps the saving:**
*"if you own the only newspaper in Oshkosh and they were to invent more efficient ways of composing
the whole newspaper, then when you got rid of the old technology and got new, fancy computers and so
forth, all of the savings would come right through to the bottom line"* — against *"All of the
advantages from great improvements are going to flow through to the customers."* **A cheaper input
kept for four years is not evidence of a moat until the customer cannot take it back; and the FY2026
guidance, −12% to −10% on that very metric, is the customer taking it back.** The advantage lived in
the wave — falling display CPMs — and `[E3-51]` names that class: *"when a surfer gets up and catches
the wave and just stays there, he can go a long, long time. But if he gets off the wave, he becomes
mired in shallows."* **A surfing run is not a moat; the advantage lives in the wave, not the
surfer.**

**And `[E4-32]` decides the direction question.** *"we want the moat widened every year … that does
not necessarily mean that the profit is more this year than last year."* The inverse holds here:
profit was more this year than last for three years while the moat narrowed — clients down four
years running, revenue down seven, two retail-media customers able to remove a fifth of a segment,
and the full-year guide now negative on management's own key metric.

### Untapped pricing power `[E3-33]` — and the agony metric `[E4-37]`

**None found, and the filings say the opposite.** `[E3-33]`'s class is scoped by `[E5-28]` — *"If you
name some business that has incredible pricing power, you're talking about a business that's a
monopoly or a near monopoly"* — and the competitor row above refutes near-monopoly at every position
in the chain. Criteo's own revenue description is *"Generally, our revenue is based on a percentage
of working media spend that runs through our platform"*, a percentage whose level appears nowhere in
any filing I read, and whose direction is set by an auction. **No price increase is announced in the
FY2018, FY2021, FY2024 or FY2025 10-Ks or in the Q2 2026 release.** `[E4-37]`'s inverse metric
therefore cannot even be run: there is no pricing event to observe agony about.

### Class and direction

- Needed or desired [x] · no close substitute [ ] **FAILS** · not price-regulated [x]
- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL
- Direction: **NARROWING**, on four filed series moving the same way — clients (four consecutive
  annual falls, one basis), revenue (seven years), Retail Media Contribution ex-TAC (−21% in Q2
  2026), and management's own full-year guidance (−12% to −10%).

### VERDICT

**Criterion 2 of `[E3-03]` fails on the filings, and it fails on evidence rather than on my
inability to see the future — which is what separates OUT from UNKNOWABLE here.** The customers have
close substitutes; the company names nine of them itself; ten per cent of clients leave every year;
the client count has fallen four years running on a single methodology; two retail-media customers
alone removed a fifth of that segment in a quarter; the top line is 15.4% smaller than seven years
ago while five of six named public peers grew; and the one metric that improved improved because the
input got cheaper, which management states in the MD&A and which the FY2026 guidance is now
reversing.

**Can I name the document that would resolve this?** I can, and I have read it: the FY2025 10-K and
the EX-99.1 of 2026-08-05. **They resolve it against the name.** So this is not UNRESEARCHED. And it
is not UNKNOWABLE, because nothing here waits on the future: the substitution has already happened
and is already filed.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?

**NOT OPENED.** Q2 is OUT and the framework stops at the first verdict that is not IN. Q3 could not
rescue a Q2 failure in any case — **THE GUARDRAIL**: *"a good managerial record (measured by economic
returns) is far more a function of what business boat you get into than it is of how effectively you
row"* **[E2-37]**. A strong Q3 cannot promote a name, repair Q2, or substitute for Q4.

**Three observations are recorded WITHOUT a verdict**, because they were seen while reading for Q1
and Q2 and a later reader should not have to find them again. **None is scored and none is used:**
- `[E4-29]`, the fifth flag, **would have had a live prompt to read.** Adjusted EBITDA is one of the
  three "key metrics" in the 10-K's own table, and Adjusted EBITDA margin is quoted as a percentage
  of a second non-GAAP measure (Contribution ex-TAC) in the Q2 2026 release. The FY2026 guidance is
  given in two non-GAAP measures and in no GAAP measure.
- `[E2-57]`, the except-for flag, **would have had a live prompt to read**: *"Excluding this impact,
  Contribution ex-TAC grew 20% in Q2 across the underlying client base"* (EX-99.1, 2026-08-05).
- **`[E2-49]` metric withdrawal: I checked it, as the brief asked, and it DOES NOT FIRE.** The same
  three key metrics — number of clients, Contribution ex-TAC (called Revenue ex-TAC until the
  gross/net change), Adjusted EBITDA — appear in the FY2018, FY2021, FY2024 and FY2025 10-Ks. **The
  client count has fallen for four years and they have kept publishing it**, and when the definition
  changed in Q1 2023 they footnoted the change and restated the prior year **downward**. That is the
  opposite of *"disposition of the yardstick rather than disposition of the manager"*. **My prior
  therefore stands at six fires and SIX failures** (previously six and five).

- **VERDICT: NOT OPENED — the file closed at Q2.**

## Q4 — WILL IT SURVIVE?  **NOT OPENED — the file closed at Q2.**
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?  **NOT OPENED — the file closed at Q2.**
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?  **NOT OPENED — the file closed at Q2.**

---

# COMPUTATION — NOT A CLEARANCE

**Operator rule 3.** Q1 through Q4 do not all show IN, so nothing below is a clearance, a valuation,
or a reason to act. **No entry language appears here and none may be read into it.** It exists
because the brief asked four arithmetic questions the screen could not answer, and because the
arithmetic is worth writing down even for a name that failed at Q2.

### (i) THE OWNER-EARNINGS SPREAD, REBUILT ON A LONGER WINDOW **[E4-25]**

The `spread_caveat` said the screen's four-construction width *"CANNOT see variation older than the
5-year window"*, and `years_filed 12` said there was more. **There is: operating cash flow is filed
for twelve consecutive years, 2014 through 2025.**

| FY | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Operating cash flow ($M) | 116.3 | 137.2 | 153.5 | 245.5 | 260.7 | 222.8 | 185.4 | 220.9 | 256.0 | 224.2 | 258.2 | **311.2** |
| Share-based compensation ($M) | 19.6 | 24.0 | 43.3 | 71.6 | 66.6 | 41.0 | 28.8 | 44.5 | 65.0 | 97.2 | 102.6 | 57.8 |
| Capex, intangibles + PP&E ($M) | — | — | 85.1 | 122.2 | 117.0 | 82.7 | 67.3 | 55.0 | 63.8 | 116.1 | 78.1 | 102.7 |

Sources: FY2025, FY2024, FY2021 and FY2018 10-K cash-flow statements, cross-checked against
companyfacts at the newest vintage.

**Owner earnings** on the framework's CONVENTION (operating cash flow, less SBC in full **[E5-06]**,
less the (c) guess):

| window | OCF mean | SBC mean | (c) = capex mean | (c) = D&A | **OE range** |
|---|---:|---:|---:|---:|---:|
| **5 years, 2021-2025** (the corpus default **[E2-42]**) | $254.1M | $73.4M | $83.1M gives **$97.6M** | about $107M gives **$73.7M** | **$74M to $98M** |
| **8 years, 2018-2025** | $242.4M | $62.9M | $85.3M gives **$94.2M** | not built | **about $94M** |

- **The (c) judgment, disclosed as `[E2-23]` requires it to be** — *"(c) must be a guess"*. **D&A is
  the corpus default `[E3-44, E2-41]`** and this is not the capital-intensive exception class
  `[E5-20]` (no railroad, no airline, no utility; the filing nowhere says depreciation understates
  renewal). **Here the default is the CONSERVATIVE end, not the optimistic one**, because D&A
  ($122.3M in FY2025, $101.2M in FY2024, $99.7M in FY2023, from the Adjusted EBITDA reconciliation)
  runs **above** capex in two of the last three years. Both ends are shown and neither is preferred.
- **Stock compensation subtracted in full `[E5-06]`.** It **resolves for every one of the twelve
  years** against the RESUME STATE item 3F check; CRTO is not an SBC-unresolved name. SBC over
  operating cash flow is **28.9%** on the five-year means and its worst single year is **43.4%**
  (2023), so it stays under the 50% threshold that would send this run to the grant table by hand
  `[E3-70]`. **The grant-date measure is therefore not built, and that limit is stated rather than
  concealed: the reported charge is the floor of the subtraction, not the measure.**
- **The working-capital increment is inside the number**, which is why the CONVENTION uses operating
  cash flow. **The empty `wc_note` was checked rather than trusted**, as the brief required. It is
  not clean: FY2025 carries **+$246.0M on trade receivables against −$265.4M on trade payables** on
  the filed detail lines, each about 80% of a year's operating cash flow on its own. **They very
  nearly offset — the six working-capital lines net to −$13.3M — so the FY2025 figure is not
  distorted; but the gross swings are an order of magnitude larger than the flag's 30% trigger and
  the annual-facts flag never saw them.** Receivables alone were $800.9M at 2024-12-31, 41% of that
  year's revenue, which is the ad-intermediary shape the brief predicted.
- **`level_shift 1.14 "no step"` and `best_year_dep 0.035 "no single-year dependence"` were computed
  on the short window and are checked here on twelve years.** The twelve-year mean of $216.0M against
  the five-year $254.1M is a ratio of **1.18**; the FY2025 high of $311.2M is 1.22x the five-year
  mean and 1.44x the twelve-year mean. **No single year carries the series and no step is visible —
  the screen's two verdicts survive the longer window.** That is the rare case of a screen flag
  confirmed rather than refuted, and it is recorded as such.

### (ii) THE YIELD, AND WHAT THE PRICE ASSUMES — arithmetic only

- **$97.6M ÷ $818.3M = 11.9%** at the capex end of (c); **$73.7M ÷ $818.3M = 9.0%** at the D&A end.
  Sovereign **5.34%**.
- **These are trailing means and the business is not earning them now.** H1 2026 operating cash flow
  was **$69M** (against $61M in H1 2025), trailing-twelve-month free cash flow as the company reports
  it was **$180M**, and Contribution ex-TAC is guided **−12% to −10%** for FY2026. **A multi-year
  mean that includes 2024 and 2025 is pricing a level the company has told the market it will not
  repeat this year.** `[E4-41]`'s instruction is to normalise the mean **down** for favourable
  exogenous breaks inside the window, and the falling display CPM identified in the MD&A is exactly
  such a break.
- **The screen's `growth_required 0.0082` is rebuilt and discarded.** It was computed on an $865M cap
  and a $79M bottom; on the hand-struck $818.3M cap the arithmetic moves, and in any case it is a
  figure about a price, and this file closed on the business.

### (iii) THE ACQUISITION PERIMETER, READ BY HAND — and it is a SEVENTH understatement

The `acq_note` said *"acquisitions are $156M, 18% of cap, inside the window"*. **Read by hand from
the filings, as the RESUME STATE section-5 limit requires, the true number is more than twice that.**

- The cash line reproduces the screen: `PaymentsToAcquireBusinessesNetOfCashAcquired` = $10.4M
  (2021) + **$138.0M (2022)** + $6.8M (2023) + $0.5M (2024) + $0.0M (2025) = **$155.7M**.
- **The FY2021 10-K states the price of the one acquisition that matters, verbatim:** *"In December
  2021, we executed a purchase agreement to acquire the business of IPONWEB Holding Limited
  ("IPONWEB"), a market-leading AdTech company with world-class media trading capabilities, for $380
  million comprised of a mix of cash and treasury shares of the Company, subject to certain
  adjustments including for working capital, other current assets and current liabilities and net
  indebtedness, with the transaction expected to close in the first quarter of 2022"*.
- **Two further cash legs sit outside the investing line entirely**: *"Cash payment for contingent
  consideration"* of **$22.0M (2023)** and **$52.0M (2024)** on the FINANCING section of the FY2025
  cash-flow statement, against a contingent entitlement the 10-K describes as *"contingent
  consideration of a maximum of $100.0 million"*.
- **And the stock leg is partly buried in compensation**: *"LUS were issued to the Iponweb seller as
  partial consideration for the Iponweb Acquisition"* — Lock-Up Shares, expensed through
  share-based compensation, which is part of why SBC jumps from $65.0M (2022) to $97.2M (2023) and
  $102.6M (2024).
- **`BusinessCombinationConsiderationTransferred1` is ABSENT from CRTO's companyfacts**, exactly as
  the RESUME STATE records for CRM, CERT, MRVL and AVGO. **This is the seventh consecutive perimeter
  understatement and it confirms the limit as a SOURCE limit rather than a rule defect.**

> **Perimeter, hand-built: $380M announced against a hand-struck cap of $818.3M = 46% of the cap,
> not 18%.** `[E5-44]` would have governed the stock leg had Q3 been reached — *"The intrinsic value
> of the shares you give in an acquisition must not be greater than the intrinsic value of the
> business you receive"* — and the shares were given at 2021-2022 prices. Not scored; recorded.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, Q3-Q6 NOT OPENED and labelled.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's ten-year
      finding is stated as a NO and carried into Q2, not used to soften Q1's IN.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives — **none was issued.**
- [x] Every UNKNOWABLE verdict states what specifically cannot be known — **none was issued.**
- [x] Step 0: the filing was read, with accession numbers; FY2025 operating cash flow of $311,237
      thousand was cross-checked from XBRL to the filed Consolidated Statements of Cash Flows, and
      total revenue of $1,944,901 thousand to the filed segment table.
- [x] Owner earnings on a multi-year mean; two windows stated; capex band disclosed as a judgment.
      **Inside a COMPUTATION block, not a clearance.**
- [x] Competitor row filled — 6 named filers of the 9 competitors Criteo itself names; the three
      absent are named with the reason. Moat class **NONE**, not PROVISIONAL.
- [x] Sovereign is for the earnings currency, argued from the filings, from the issuing authority,
      dated, with the alternative stated and both raw downloads saved.
- [x] Value stated as a round-number range, not a point estimate — **no value was stated; Q5 was
      not opened.**
- [x] One bar chosen, not both; windage count stated — **no bar was used; Q5 was not opened.**
- [x] Prices dated; aggregator used for live quotes only and flagged.
- [x] Run committed to git.
- [x] Every ledger id used was verified to exist in `principle_ledger.csv` and its quotation checked
      against the row it cites.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** **Q2 OUT on `[E3-03]` criterion 2 — Criteo names nine close substitutes for its
  customers' money in one sentence of its own Item 1, loses about 10% of clients a year, has posted
  four consecutive annual falls in client count on a single methodology, has a top line 15.4%
  smaller than seven years ago while five of six named public peers grew, saw two Retail Media
  clients remove 21% of that segment in one quarter, and improved its margin only because the media
  it buys got cheaper, which it says in its own MD&A and is now guiding away at −12% to −10% for
  FY2026.**

---

# DEFECTS FOUND IN THE DISPATCHER'S BRIEF

**Reported explicitly, as the brief required, because several past briefs have been wrong.**

1. **THE BRIEF MISSED THE 8-K12B OF 2026-07-29 — the single most consequential filing on this name,
   and the one that closes its own "track one".** The brief listed six deal filings and described
   track one as ending at *"a shareholder vote reported in the 8-K of 2026-02-27, Item 5.07"*.
   **Track one COMPLETED on 2026-07-29** under accession `0001628280-26-050326`, Form **8-K12B**,
   Items 1.02/3.01/3.03/5.03/8.01/9.01. That filing is where the registrant's jurisdiction changed,
   where **the ADS structure was terminated and the Deposit Agreement cancelled**, where the listed
   instrument changed from an American Depositary Share to an ordinary share, and where Rule 12g-3
   succession is asserted. **A run that took the brief's list as complete would have struck a cap on
   the wrong instrument and would have had no document for what "Lux Criteo" is.**
2. **The brief presented the pre-Luxembourg question as open research** (*"Also check what Criteo was
   BEFORE Luxembourg"*) **when the answer is on the face of the same 8-K12B it missed**, in the
   "former name or former address" box (*"32 Rue Blanche , Paris , France 75009"*) and in the
   Introductory Note. The brief's premise was correct; its framing implied the answer was not on
   disk in one document.
3. **The brief's quotation of the 2026-08-05 Item 1.01 is ACCURATE.** Re-struck word for word
   against the accession, including the Effective Time *"at 12:00:01 a.m., New York City time, on
   January 1, 2027"*. **No correction is owed.** Recorded because the brief asked to be checked.
4. **Both tracks were framed as candidates for the ROKU spread case. Neither can be.** There is no
   counterparty on either track — U.S. Criteo is *"a wholly owned subsidiary of Lux Criteo"* and the
   exchange is one-for-one — so the spread question had no purchase from the start. The screen's
   *"first 425 on 2026-02-27"* is an artifact of its own cut-off, as the brief correctly said.
5. **`acq_note` understates the perimeter by more than the brief anticipated.** The brief warned of
   *"stock consideration"* not resolving. The stock is one of **three** missing legs: the stock, the
   **$74.0M of contingent consideration paid through the FINANCING section** in 2023 and 2024, and
   the Lock-Up Shares expensed through **share-based compensation**. $155.7M counted against an
   announced **$380M**.
6. **The brief's PUBM-derived prior about take-rate collapse is REFUTED at Criteo**, and the brief
   was right to frame it as a prior rather than a finding. Criteo's take went from 52.5% to 60.4% of
   revenue over 2023-2025.
7. **The brief's `[E2-49]` prior does not fire here**, and the check found the opposite: Criteo has
   kept publishing a falling unit series for four years and restated it downward when it changed the
   definition. The prior now stands at six fires and six failures.
8. **The GOOGL antitrust remedy question the brief posed is answerable and is NOT load-bearing for
   this file.** Criteo names Google as a competitor and as a browser gatekeeper, and its
   third-party-cookie dependence is disclosed in its own words; but the file closes on Criteo's own
   client series, its own competitor list and its own guidance, none of which depends on the remedy.
   **Inside the circle `[E3-31]` as a fact about the industry's structure; outside it as a predictor,
   and it was not used as one.**
9. **The brief repeats `CLAUDE.md`'s stale ledger count of 267 rows. The file holds 311.** Read
   today with `csv.DictReader`: **311 rows, 311 distinct ids, no duplicates**, and every one of the
   62 ids this run considered resolves. **This is NOT a new finding and I am not reporting it as
   one** — the reading list records it as *"Thirteenth consecutive fold to record it"* at the MNRO
   fold of 2026-09-21, with `CLAUDE.md` deliberately left unedited under PRIME RULE 5. **It is
   recorded here only because the brief passed the stale number through**, and the instruction in
   `CLAUDE.md` itself — *"Count the file, never the pointer"* — is what I followed. This fold makes
   it the fourteenth.
