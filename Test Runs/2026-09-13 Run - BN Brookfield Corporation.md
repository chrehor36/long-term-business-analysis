# Company Run — Brookfield Corporation (BN) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Write-early protocol: this file was created before any fetch. Sections are appended as they
close. Research files: `Test Runs/_research 2026-09-13 BN/`.*

**PRIORS, recorded before any filing was opened [E4-26]** — to be refuted, not confirmed:
1. The brief's prior (operator): measurement of the owner's share is the hardest in the queue for
   BN, harder than BAM, because IFRS consolidates partly owned funds and businesses. A prior about
   measurability, not a verdict.
2. The queue's 2026-09-02 note held BN "BLOCKED" as an asset manager with fee streams. My prior:
   that label is at least partly wrong for BN post-2022 — BN is a holding company whose economic
   assets are (a) a stake in BAM, (b) an insurance/annuity business, (c) direct stakes in listed
   and unlisted operating affiliates, and (d) carried interest. Unverified until the 40-F is read.
3. The pre-check facts (40-F accession `0001001085-26-000006`, 6-K `0001171843-26-005886`, the
   name history, the share classes) are unverified until opened.
4. My own prior: BN publishes a "distributable earnings" management measure and a
   corporate-level balance sheet; whether a corporate cash-flow statement is filed is unknown.

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
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Stage 0(b) — what kind of company is this? *(the SECTOR METHOD's own first test, answered from the filing)*

**Several kinds at once, and not the kind the 2026-09-02 note said.** BN is not an asset manager.
Its own definition (40-F MD&A, p.25): *"The "Corporation" is comprised of ownership interests in
our Asset Management, Wealth Solutions and Operating Businesses."* It is a **holding company**
whose common share owns:

| component (BN's economic share) | what it is | common equity, 2026-06-30 (6-K Q2, segment table) | FY2025 measure (40-F) | market value where quoted, 2026-09-11 (Yahoo, **aggregator, flagged**) |
|---|---|---|---|---|
| **BAM** — *"74% ownership interest"*, 70% direct + 4% through BWS; 1,193.0M shares (6-K Q2 quoted-value table) | the fee-earning alternative asset manager | Asset Management segment **$14,968M** (includes the direct fund stakes below) | BAM DE at BN's share **$1,891M**; realized carried interest, net **$560M** | 1,193.0M × $47.26 = **~$56.4bn** |
| **Direct fund stakes** — BSREP III/IV/V, Oaktree Opps XI/XII and others | LP interests, mostly flagship real-estate funds | inside the line above ($10,876M at 2025-12-31) | distributions **$876M** | not quoted |
| **BWS** — all class C shares (the residual), **equity accounted** | annuity, pension-risk-transfer, life and P&C insurer; *"total insurance assets … $191 billion"* at 2026-06-30 | Wealth Solutions **$13,139M** | WS DE **$1,671M** — *retained in BWS, not paid to BN* | no separate quote; BNT tracks BN |
| **BIP** — 26% direct (27% with BWS), 207.1M units | listed infrastructure partnership (utilities, transport, midstream, data) | Infrastructure **$2,097M** | FFO at share **$757M**; cash distributions **$356M** | 207.1M × $36.88 = **~$7.6bn** |
| **BEP** — 45% direct (47% with BWS), 309.4M units | listed renewables partnership, plus Westinghouse; plus BN's own energy contract buying ~10% of BEP's generation | Energy **$4,729M** | FFO at share **$584M**; distributions **$485M** | 309.4M × $30.39 = **~$9.4bn** |
| **BBUC** — 27% direct, 69% with BWS (after the April 2026 transfer) | listed private-equity holding company (Clarios, lottery services, dealer software …) | Private Equity **$1,016M** | FFO at share **$455M**; distributions **$24M** | ~142.5M combined units × $26.41 = **~$3.8bn** (units derived by hand from the 40-F footnote: 88.9M direct + 53.6M held by BWS subsidiaries at 2025-12-31) |
| **BPG** — 100% | unlisted real estate: super core, core plus, value add, North American residential | Real Estate **$26,706M** | NOI **$3,144M** *(before property-level interest)*; distributions ~$0.7bn | not quoted (BPY preferred units are, and BPY still files with the SEC, CIK 0001545772) |
| **Corporate** | $14,711M corporate borrowings, $4,088M preferred shares, $230M perpetual notes, $5,636M core liquidity (all 2026-06-30) | Corporate Activities **$(20,172)M** | leverage and corporate costs **$(587)M**; preferred dividends **$(177)M** | — |
| **Total** | | **$42,483M** | DE before realizations **$5,386M**; DE **$6,008M** | cap **$87.8bn** (Step 0) |

**Stage 0(b) float test, asked directly.** BN standalone is **not** float-bearing: the float sits
inside BWS, which BN equity-accounts. **After the pending combination closes (below), New BN will
consolidate an insurer with $191bn of insurance assets against $42.5bn of BN common equity**, and
becomes float-bearing. So the SECTOR METHOD reaches **one component** (BWS) today and, on closing,
the consolidated whole. The rest routes to the ordinary method, component by component, which is
CONVENTION 3 of the SECTOR METHOD (*"where a company is part insurer and part operating business,
the two are valued separately and the reason is recorded"*).

**A caution on double counting, recorded before any arithmetic:** BWS's book equity includes the
65,000,000 BAM shares, 53.6M BBU/BBUC units, 15.2M BEP/BEPC units and 3.3M BIP units BN moved into
it. The 1,193.0M BAM count above already includes BWS's 65M; the BEP and BIP counts do not. Q5
must not add BWS's equity and the listed stakes gross.

### Every perimeter change since the 2022 spin, dated from the filings

| date | event | source |
|---|---|---|
| **2022-12-09** | Special distribution of **25%** of the asset management business through the newly listed BAM Ltd (~410M shares, one per four BN shares); name changed from Brookfield Asset Management Inc. to **Brookfield Corporation** | 40-F FY2022 (`0001001085-23-000007`), notes |
| **2024-05-02** | BWS completed the **AEL** acquisition; BN sold BAM shares to BWS for the stock consideration, booking **$1,000M** of *"disposition gains from principal investments"* inside FY2024 DE | AIF FY2025; 40-F FY2024 (`0001001085-25-000007`) DE table fn.4 |
| 2024-09-17 / 2024-09-26 | 51% of Castlelake's fee-related earnings ($489M); Pinegrove Ventures | AIF FY2025 |
| Q4 2024 | *"BWS acquired a $1 billion economic interest in BBU from the Corporation"* | 40-F FY2025 MD&A fn. |
| **2025-02-04** | The **2025 Arrangement**: BN exchanged its 73% of BAM ULC for BAM Ltd shares one-for-one | AIF FY2025 |
| **2025-06-25** | BN contributed **65,000,000 BAM shares (~$3.3bn)** to BWS for class C shares and a note (note converted to class C 2025-12-31) | AIF FY2025 |
| 2025 (dates not given) | BEP, BEPC, BIP, BBU and BBUC units moved into BWS subsidiaries | 40-F FY2025 segment footnotes |
| **2025-10-09** | 3-for-2 splits of BN and BWS | AIF FY2025 |
| **March 2026** | BBU and BBHC reorganized into one corporation, **BBUC** (AIF: expected 2026-03-27; 6-K Q2: completed in March) | AIF; 6-K Q2 2026 |
| **2026-04-01** | BWS completed **Just Group** (£2.4bn / $3.2bn; *"added $45 billion of insurance assets"*) | BWS 6-K `0001171843-26-002125`; 6-K Q2 2026 |
| **April 2026** | *"we transferred a 16% direct interest in BBUC to our wealth solutions business"* (now 27% direct, 42% via BWS) | 6-K Q2 2026, p.15 fn.2 |
| **2026-08-03** | **Oaktree** acquisition completed (the ~26% not owned; BN's stated investment $1.4bn) | 6-K `0001171843-26-005138`; AIF terms |
| **2026-07-16 → year-end 2026** | Shareholders approved the **BN/BWS combination** into *"Brookfield Corporation Ltd."* (New BN): *"all class A limited voting shares of BN and class A exchangeable limited voting shares of BWS will be exchanged on a one-for-one basis for new shares"*; *"expected to close by year-end, subject to receipt of all applicable regulatory approvals"* | 6-K `0001104659-26-066346` (2026-05-26); 6-K `0001104659-26-084374` (2026-07-17); circular, 6-K `0001104659-26-071025` Ex.99.3 |
| 2026 | segment renamed *"Renewable Power and Transition"* → *"Energy"* | 6-K Q2 2026 |

**Do multi-year figures under this CIK describe one perimeter? No.** FY2021-22 carry ~100% of the
asset manager; FY2023 onward ~75%, then 73%, then 74%; Wealth Solutions DE runs **$30M (2021) →
$388M → $740M → $1,350M (AEL) → $1,671M (2025)**, with Just Group added in 2026. **The five-year
default window [E2-42] spans at least three perimeters, and the post-spin perimeter has three full
filed years (FY2023-25).**

### Can the owner's slice be identified and measured from filed documents? *(the brief's central question)*

**IDENTIFIED — yes, from audited documents, better than the prior expected.**
1. **Note 1 of the audited FY2025 statements** reconciles *"the Corporation's capital"* to the
   consolidated balance sheet in three columns — *"The Corporation | Investments | Elimination"* —
   so the parent-only balance sheet is audited: cash $461M, other financial assets $2,114M,
   investments $58,951M, funded by common equity $43,796M, preferred $4,090M, perpetual notes
   $230M and corporate borrowings $14,301M.
2. **The segment note (Note 3)** reconciles net income to each segment's measure; the MD&A
   Glossary reconciles net income **$3,235M** through FFO **$5,692M** to DE **$6,008M**, line by line.
3. **Cash distributions received are disclosed per affiliate** (BAM, BIP, BEP, BBU, BPG, direct
   investments), with units held and quoted value.
4. **Every component except the direct fund stakes has its own SEC filer with audited
   statements:** BAM (CIK 0001937926), BWS 20-F (0001837429), BIP, BEP/BEPC (0001791863), BBUC
   (0001654795), BPY (0001545772). **The L run's test — subsidiaries that publish their own
   audited statements, so the perimeter problem does not arise — is met.**

**MEASURED AS OWNER EARNINGS — not from BN's own filing, and the reason is specific.** BN files no
parent-only cash-flow statement, and its parent earnings measure cannot stand in for one:
- **DE adds back equity-based compensation** (*"Add back: equity-based compensation costs | 110"*,
  FY2025) — **[E5-06]**.
- **DE counts Wealth Solutions' DE ($1,671M), which BN does not receive**, and which by definition
  excludes *"mark-to-market on investments and derivatives"* (Glossary) — the reserve and asset
  marks of a $191bn insurer.
- **DE counts affiliates' distributions, not their owner earnings.** A distribution can exceed or
  undershoot what the affiliate earns; BBU pays almost nothing, BAM pays almost everything.
- **DE counted a related-party gain as earnings**: FY2024's $1,000M was BN selling BAM shares to
  BWS, its own paired affiliate.
- **The segment measures are the [E4-29] mechanism**: FFO adds back depreciation ($10,379M
  consolidated) without deducting maintenance capex, and BPG's NOI is before property-level
  interest (the Real Estate line of property-specific borrowings is $63.8bn, of which $40.7bn
  belongs to the LP investments).

**So owner earnings at BN's share is buildable only by look-through [E3-04], from each affiliate's
own filing, with maintenance capex and SBC at BN's share.** Those documents exist and are named
above. **This is a measurement task for Q4, not a comprehension failure at Q1**, and it is recorded
here so that no later section treats DE as owner earnings.

### Unit economics, in my own words

- **BAM (the largest piece by market value):** clients commit money for ten years or forever; BAM
  charges a base fee whether or not it performs (base fees $4,896M in 2025 on fee-bearing capital
  that rose from $538.5bn to $602.7bn: about 0.86% of the average), spends about 42% of fees running the firm
  (2025 FRE margin *"58%"*), and pays almost all the rest out. On top, a share of fund profits above
  a hurdle (carry) arrives years later and lumpily. **A slice of its fee base is paid by BN's own
  controlled affiliates** (BEP, BIP, BBUC, BPG pay base fees on their capitalization, plus incentive
  distributions) **and by BWS** (*"we raised a total of $25.2 billion from Brookfield Wealth
  Solutions"*, 2025) — a related-party share of revenue that Q2 must weigh.
- **BWS:** takes retirees' and pension plans' money in exchange for guaranteed payments, credits
  them about 3.8% (2025 life and annuity cost of funds), invests at about 5.0% plus 0.7% of real-asset
  gains, and keeps a gross spread of **2.25%** on ~$113bn of average invested assets. *"BAM acts as the
  investment manager of most of the assets of BWS"*, and 2025's deployment was *"$13 billion into
  Brookfield-managed strategies … at an average yield of 8.5%"*. The P&C book (a 99% combined ratio
  in Q2 2026) lowers the blended cost of funds.
- **BIP and BEP:** own long-lived, mostly contracted or regulated assets financed with asset-level
  debt; pay out a share of cash flow as distributions and fund growth with more debt, asset sales
  and new units. BN is general partner of both and collects distributions as a unitholder.
- **BBUC:** buys industrial and service businesses with borrowed money, improves them, sells them;
  reinvests most of its cash, pays BN $24M.
- **BPG:** collects rent on office, retail and residential property it owns 100% of, carries heavy
  property-level debt, sells mature assets, and writes value-add and opportunistic properties down
  or up each quarter (2025: value add −$477M, opportunistic −$456M).
- **Corporate:** borrows at a fixed 4.8% for an average 15 years and issues perpetual preferreds,
  and uses the cash the pieces send up for buybacks, dividends and new commitments.

**The scarce input the business controls:** at BAM, **fundraising access** — 2,400+ institutional
clients and a thirty-year record that raised $112bn in 2025 and $98bn in H1 2026 — plus **control
of the general partner of every vehicle**, which BN holds through Class B. At BIP, BEP and BPG,
**specific physical assets** (hydro stations on 83 river systems, regulated utilities, gateway
office towers). At BWS, on the corpus's own account, **nothing scarce** [E2-70]: *"Their only
products are promises."* At BBUC, nothing structural.

**Will the fundamentals look broadly the same in ten years?** The pieces, largely yes — contracted
and regulated assets, locked-up fund capital, annuity liabilities that run for decades. **What BN
does with the pieces, by its own written program, no.** The FY2025 letter (annual report filed on
6-K/A `0001001085-26-000011`, letter pages rendered as images and read there): *"Flexibility and
Change are Critical to Long Term Success … The ability to continually adapt is the lifeblood of a
great long-term business … Being trusted by shareholders to continuously adapt an investment model
is a special privilege"*; *"Today, most of our excess capital is going towards digitalization,
decarbonization and deglobalization whereas years ago it was going into property, pipeline
infrastructure and hydro facilities"*; *"50% of the things that we invest in today did not exist as
widely held institutional investments 15 years ago."* And the structure itself changes every year
(the table above), with a combination that consolidates the insurer still to close.

### The case against IN, at full strength [E4-26]

**For Q1 OUT or UNKNOWABLE.** [E3-31] asks for businesses *"relatively simple and stable in
character. If a business is complex or subject to constant change, we're not smart enough to
predict future cash flows."* BN describes itself, in writing, as a business whose edge **is**
constant change. Its perimeter moved in every year since 2022 through transfers between entities
the same people control. The owner's earnings require six filers' statements read through. The
largest cash generator by growth, BWS, invests its sponsor's strategies at marks the sponsor sets.
The forward entity (New BN, consolidating the insurer) is not the filed one. **[E4-46]**: a
business that needs months of study is outside the circle.

**Why it still returns IN — and where the evidence goes instead.**
1. **Understanding, not predictability, is the Q1 test, and each piece is writable in a paragraph
   above** — which is what BRK, L and GHC were each held to. Berkshire's allocator also moves capital
   across industries; Q1 did not fail it for that. What differs at BN is that **the legs themselves
   are designed to turn over** — and that is a claim about the **durability** of the advantage.
   **[E4-04]**'s scope note in the framework puts exactly that class — *"the moat whose basis must be
   periodically replaced"* — and **[E3-51]**'s surfing run and **[E4-36]**'s wave-riding cause at
   **Q2**. The letter's words are carried there, not spent here.
2. **The HHH closure does not transfer.** HHH was UNKNOWABLE because *"the acquisitions are not yet
   chosen"* by an allocator with a *"15 months old"* record. BN's program has a long filed record (the FY2025 letter's own table runs 1995-2025, and every
   filing read names the same chief executive), and the pending combination is **documented** — terms, share
   exchange, court process and conditions are in a filed circular. A documented, approved, one-for-one
   exchange between entities that already share economics is not a future record that does not exist.
3. **No named document is missing for comprehension.** The measurement work (look-through owner
   earnings) has named documents, so it cannot be UNKNOWABLE [E4-19]; it belongs at Q4.
4. **[E3-47]**: a wrongly closed file inside the circle is the error the corpus rates most
   expensive. The honest place to hesitate is here, and the evidence does not require the close.

**What the IN does not say:** that BN's cash flows are predictable, that DE is owner earnings, or
that the structure is simple. Those are Q2, Q3 and Q4 questions and each is taken there.

- **VERDICT: [x] IN** — every component's economics is writable from the filings, the owner's slice
  is identified in an audited parent balance sheet and in each affiliate's own audited filing, and the
  constant-change evidence is a durability question carried to Q2 **[E4-04, E3-51]**.

### Was the 2026-09-02 block right?

**Half.** It was right that BN is *"a different perimeter problem"* from the insurers and that the
SECTOR METHOD alone does not reach it. It was **wrong on the facts** — BN is not *"an asset manager
with fee streams"*; it owns 74% of one — and **wrong in effect**: nothing in the filings makes the
perimeter unmeasurable. The parent balance sheet is audited, every listed stake is quoted, every
affiliate files, and the insurer can be run by the SECTOR METHOD as one component. **"Blocked" was a
scheduling label that sat for eleven days where a verdict belonged.**

### Dated correction to Step 0 and Q1, 2026-09-13 (resume session), recorded beneath rather than edited (operator rule 6)
- **The Oaktree completion date is 2026-07-31, not 2026-08-03.** The Q1 perimeter table dates the
  close to BN's 6-K `0001171843-26-005138`, which is the press release of 2026-08-03 (*"today
  announced that it has completed its acquisition of Oaktree"*). BAM's 8-K Item 2.01 of the same day
  (read in `_research 2026-09-13 BAM/8K_2026-08-03_201.txt`) states the date: *"On July 31, 2026,
  Brookfield Asset Management Ltd. ("BAM") and Brookfield Corporation ("BN" and, together with BAM,
  "Brookfield") completed the previously announced acquisition of Oaktree … Total consideration for the
  transaction was approximately $3.0 billion, consisting of both cash and BN and BAM shares."* **BN
  shares were part of the consideration.** Step 0's count (2,232,266,331 Class A at 2026-08-13) post-dates
  the close, so the issuance is already inside it; the count stands.
- **Re-strike at the resume, 2026-09-13:** `sources.sovereign("USD")` returned **5.35%, 09/11/2026, US
  Treasury daily par yield curve** (unchanged); `sources.price("BN")` **$38.22, 2026-09-11** (Yahoo,
  aggregator, flagged; unchanged); `split_factor_after("BN","2026-08-13")` = 1.0. EDGAR submissions for
  CIK 0001001085 show no 6-K after `0001171843-26-005886` (2026-09-04); the filings since 2026-08-13 are
  two 6-Ks, a Form 4, a 13F-HR and an N-PX, none carrying a share count. Script and output:
  `_research 2026-09-13 BN/r0_restrike.py`.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."*
> **[E3-03]**, 1991 letter

### First, the structural question: is the franchise claim BN's, or its legs'? *(brief prior 1, argued, not assumed)*

**Precedent split two ways.** The BRK run found a moat at the level of the **whole** (the float and
balance-sheet system, *"a funding structure"*) that no single leg carried, and then rowed each leg. The L
run found no whole-level claim and asked the question **where the earnings are** (CNA 70%, Boardwalk 27%).
Neither method is a rule; the filings decide which one BN needs.

**BN makes a whole-level claim in its own words, so the whole is tested first.** 40-F MD&A, *Competitive
Advantages*: *"At the center of our success is the Brookfield Ecosystem, which is based on the fundamental
principle that each group within Brookfield benefits from being part of the broader organization. We have
three distinct competitive advantages"* - *"SIGNIFICANT & PERPETUAL CAPITAL BASE"*, *"GLOBAL REACH"*, and
operating expertise; the Q2 2026 6-K adds *"Because our platform spans real estate, infrastructure, energy
and credit, we can bring together teams from across Brookfield to deliver integrated solutions that few
organizations can replicate."* A whole-level moat has to show up as a filed **relative** advantage in
something a customer or a counterparty pays for. Three are candidates, and each gets a row or a filed test
below: **(i) the cost of the perpetual capital** (the BRK analogue: is BN's money cheaper than its
competitors'?), **(ii) fundraising and GP control** (the fee engine), and **(iii) the manager-plus-insurer
system itself** (can it be copied?).

**Then the legs, weighted three ways, because no single weight is honest for a holding company.**
Arithmetic: `_research 2026-09-13 BN/q2_calc.py` (output `q2_calc_out.txt`).

| leg | (a) segment common equity, 2026-06-30, 6-K Q2 (book) | (b) FY2025 cash measure reaching the Corporation, 40-F reconciliation | (c) quoted stakes at 2026-09-11 market, unlisted at book (aggregator quotes, flagged) |
|---|---|---|---|
| **Fee engine: BAM** (74%) | inside AM $14,968M; BAM stake book ~$4.6bn at YE2025 | distributions $1,891M + realized carry net $560M = **37.1%** | 1,193.0M x $47.26 = $56.4bn = **44.1%** |
| **Direct fund stakes** (LP interests, mostly BSREP real-estate funds) | inside AM; $10,876M at YE2025 | distributions $876M = 13.3% | $10.9bn book = 8.5% |
| **Wealth Solutions: BWS** (class C residual) | $13,139M = **21.0%** | WS DE $1,671M (retained in BWS) = **25.3%** | $13.1bn book = 10.3% |
| **Real estate: BPG** (100%) | $26,706M = **42.6%** | distributions $737M (derived: $1,602M less BIP, BEP, BBU) = 11.2% | $26.7bn book = 20.9% |
| **BEP** (45-47%) | $4,729M = 7.5% | $485M = 7.3% | $9.4bn = 7.4% |
| **BIP** (26-27%) | $2,097M = 3.3% | $356M = 5.4% | $7.6bn = 6.0% |
| **BBUC** (27% direct) | $1,016M = 1.6% | $24M = 0.4% | $3.8bn = 2.9% |
| Corporate | $(20,172)M | leverage and corporate costs $(587)M; preferred $(177)M | not a leg |

*(Shares in (a) are of the $62,655M of positive segments; in (b) of $6,600M including carry; in (c) of a
$127.9bn gross that makes no double-count adjustment for the BAM shares and BBUC units held inside BWS. The
columns are for locating the question, not for valuation.)*

**What the table decides.** On **every** basis, the fee engine plus the insurer plus the real estate carry
**at least 76%** of the positive weight (book 87% with the direct stakes; cash 87%; market 84%). **BIP, BEP
and BBUC together carry 12.5% at book, 13.1% of cash and 16.3% at market.** So a franchise verdict on BN
must pass (1) at the whole level, or (2) at the legs where the money is: BAM, BWS and BPG. Each is rowed
below. BIP, BEP and BBUC are read from the filing and not rowed, and the reason is stated where they are
reached.

### [E3-03], the three criteria, per leg

| leg | needed or desired | **no close substitute** | not price-regulated |
|---|---|---|---|
| **Fee engine (BAM)** | yes | **NO** (nine filed substitutes, row A; BN's own risk factor below) | yes |
| **BWS** | yes | **NO** (*"Their only products are promises"* [E2-70]; row B) | partly (rates free, capital regulated) |
| **BPG** | yes | **NO** (BPY's own words; row C) | yes |
| BIP | yes | partly | **NO** on the regulated and price-ceiling share (filing text below) |
| BEP | yes | **NO** (electricity at a contracted price) | partly |
| BBUC | yes | **NO** (*"highly competitive service industry"*) | yes |

**BN's own filing concedes criterion (2) for the whole, in the risk factor that governs every leg.** 40-F
MD&A Part 6: *"Each of our businesses is subject to competition in varying degrees and our competitors may
have certain competitive advantages over us when pursuing investment opportunities. Some of our competitors
may have higher risk tolerances, different risk assessments, lower return thresholds, **a lower cost of
capital**, or a lower effective tax rate (or no tax rate at all), all of which could allow them to consider a
wider variety of investments and to bid more aggressively than us for investments."* And on the fee engine:
*"Competition from other asset managers for raising public and private capital is intense … as competition and
disintermediation in the asset management industry increases, our Asset Management business may face pressure
to reduce or modify asset management fees, including base management fees and/or carried interest."* **A filer
that says its competitors may have a lower cost of capital has not claimed a funding moat.** That is the BRK
analogue refused by the company itself; row B tests it anyway.

### THE COMPETITOR ROWS - required [E3-28]

> *"I can't be an intelligent owner of a business unless I know what all the other businesses in that industry
> are doing."* **[E3-28]**, 1996 meeting

#### ROW A. The fee engine: BAM against nine SEC-filing managers *(evidence imported from the sibling run, and why it transfers)*

**The row itself is not rebuilt; it is cited.** `Test Runs/2026-09-13 Run - BAM Brookfield Asset
Management.md`, Q2, committed `58c6a60`, one specification (FY2025 management fees ÷ average of YE2024 and
YE2025 fee-earning capital, each from the peer's own FY2025 10-K, each figure checked back to the text;
working in `_research 2026-09-13 BAM/peers/peer_row.md` and `calc.py`): **OWL 145.1bp, TPG 117.3, ARES 108.6,
BX 92.2, BAM 85.8 (ex-BWS 99.1), CG 74.8, KKR 73.5 (segment), APO 53.1 (segment), TROW 39.0, BLK 15.0.** BAM
sits fifth of ten on price, sixth on FEAUM growth (14.8% against OWL 35.2%, ARES 21.1%, APO 19.9%), fifth of
eight on FRE margin, inside the pack on duration. Its rate fell 90.4 → 85.0 → 85.8 → 82.4bp (FY2023 to H1 2026
annualised). **The killed session's draft row (`peers_am/competitor_row_asset_managers.md`) contains only the
BAM subject section; the seven peer sections it names were never written.** Its BAM figures agree with the
committed run (base fees $4,896M; FBC $538,541M → $602,714M; 0.858%), and nothing else in it was used.

**Does BAM Ltd's row describe what BN owns of the engine? (brief prior 3, argued.)** BN's economics differ
from a BAM Class A holder's in three filed ways, and **each makes the franchise case weaker at BN, not stronger:**
1. **BN takes carry that BAM's holder does not** (100% of mature-fund carry; realized carry net $560M in FY2025;
   accumulated unrealized carry at BN's share $9.6bn at 2026-06-30, against *"approximately $2.9 billion in
   associated costs"*, 6-K Q2). Carry is priced in the same fundraising contest as the base fee: BN's own risk
   factor names *"base management fees and/or carried interest"* as what competition pressures. It is the same
   product's price, sold against the same nine substitutes.
2. **The durable leg that the BAM run found "conferred rather than won" is, at BN, partly BN paying itself.**
   BWS, whose residual BN owns entirely, paid *"Investment management fees to Brookfield"* of **$243M / $162M /
   $64M** in 2025 / 2024 / 2023 (BWS 20-F FY2025, Note 26; BAM's 10-K books $234M of FY2025 fee revenue on $108bn
   of BWS capital, the difference unreconciled here). BEP and BIP, in which BN holds 45-47% and 26-27%, pay BAM's
   *"Stable incentive distribution fees"* ($466M in FY2025, BAM 10-K). A fee that one controlled leg pays another
   is a transfer between BN's pockets less the minority leakage on each side. **It cannot be a customer's
   judgment that no close substitute exists, because at BN there is no customer.**
3. **The fastest-growing capital is BN's own.** In H1 2026, $48.6bn of BAM's $87.3bn of gross inflows (55.7%)
   came from BWS at roughly a quarter of the third-party price (BAM run, 10-Q Q2 2026). At BN, that is BN moving
   its insurer's float into its own manager's vehicles; it is growth in intra-group volume, not evidence of
   external demand at an undiminished price.

**So row A transfers as a floor, not a ceiling:** whatever BAM Ltd's holder lacks in criterion (2), BN lacks at
least as much, and the part of the engine the BAM run called durable is, at BN, circular.

#### ROW B. The insurer: BWS against the manager-affiliated and independent annuity writers *(one specification: cost of funds)*

**Which measure the corpus supports (brief prior 4, argued).** The SECTOR METHOD grades an insurer by
**[E3-69]**: *"a comparison of underwriting loss to float developed … it gives a rough indication of the cost of
funds generated by insurance operations. A low cost of funds signifies a good business; a high cost translates
into a poor business."* For a spread writer the underwriting loss **is** the crediting cost: there is no premium
to break even on, only a rate promised to the annuitant. **Cost of funds on invested assets is therefore [E3-69]'s
own quantity for this class, and the four filers that publish a rate call it by that name.** The spread is shown
beside it, because it is the other half of the same arithmetic and because it is where BWS's filed number is
built differently. One specification for ranking: **FY2025 cost of funds ÷ average invested assets, as each filer
states it.**

| Company (segment) | cost of funds, FY2025 | FY2024 | FY2023 | earned rate FY2025 | net spread FY2025 | who manages the assets | source |
|---|---|---|---|---|---|---|---|
| **BWS (subject)**, life & annuity | **3.82%** | not filed as a rate | not filed | NII 5.01% + real-asset gains 0.69% | **2.25%** gross (1.56% without the real-asset gains) | *"BAM acts as the investment manager of most of the assets of BWS"*; $13bn deployed into *"Brookfield-managed strategies"* in 2025 | BN 40-F FY2025 `0001001085-26-000006`, WS spread table |
| **BWS**, effective incl. P&C | **3.45%** ($3,889M ÷ $112,700M) | 3.49% ($2,726M ÷ $78,080M, my arithmetic) | not filed | | | | same; FY2024 dollars from BN 40-F FY2024 `0001001085-25-000007` |
| APO / Athene | **3.69%** | 3.29% | 2.71% | 5.25% (fixed income 5.01%, alternatives 10.01%) | 1.61% | Apollo *"managed or advised $392.2 billion"* for Athene | APO 10-K FY2025 `0001858681-26-000013` |
| CRBG, Individual Retirement | **3.23%** | 2.95% | 2.54% | base yield 5.17% (alternatives excluded) | 1.94% | Blackstone $71.2bn (a 12.5% holder), BlackRock $91.9bn | CRBG 10-K FY2025 `0001889539-26-000022` |
| FG | **3.20%** | 2.96% (recast) | 2.92% (as recast in Q4'24 supp.) | 5.08% (alternatives mark-to-market in) | 1.88% | Blackstone manages *"substantially all"* | FG 8-K EX-99.2 `0001934850-26-000021`; 10-K `0001934850-26-000026` |
| KKR / Global Atlantic | *not filed as a rate*; net cost of insurance $5,229M ÷ average insurance investments $181,077M = 2.89% (my arithmetic, **not comparable**: nets policy fees against benefits) | | | | | KKR is *"the investment adviser"* | KKR 10-K FY2025 `0001404912-26-000007` |

*Every rate for APO, CRBG and FG was re-read in the saved filing text at this resume, not taken from the killed
session's draft; the draft's figures were correct. BN's glossary gives no definition of cost of funds; the
component rates do not add (3.82% and 0.55% cannot sum to 3.45%), and the effective rate equals the dollar line
divided by average invested insurance assets, so the two component rates sit on denominators the filing does not
state. Definitions differ: Athene includes option costs and DAC/DSI/VOBA amortisation; CRBG excludes DSI
amortisation; FG includes other liability costs. These are carried, not smoothed.*

**What row B shows.**
- **On the life and annuity book, BWS has the highest cost of funds of the four filers that publish one: 3.82%
  against 3.69%, 3.23% and 3.20%.** Even after its P&C float is blended in (3.45%), it is above both independent
  writers. **[E3-69]: *"a high cost translates into a poor business."*** The filer's own words for why it holds a
  P&C book are *"lowers the overall cost of funds through underwriting profits in property and casualty"*: a
  lever the others do not need to reach a lower number.
- **BWS's spread leads the row only because of a line the others do not have.** The 2.25% includes **0.69 points of
  *"Realized and unrealized gains on real asset strategies"***: gains, partly unrealized, on assets largely managed
  by BN's own manager in Brookfield strategies, at marks that manager's valuation process produces. Without that
  line BWS's spread is **1.56%, the lowest in the row** (Athene 1.61%, FG 1.88%, CRBG 1.94%). Athene's earned rate includes
  alternative-investment income and its segment measure excludes investment gains; CRBG's base yield excludes
  alternative-investment income entirely.
- **The most recent quarter moves further the same way** (single quarters are *"too heavily based on estimates to be
  much good"*, [E3-69], so this is direction only): Q2 2026 cost of funds $1,562M on $165,855M average invested
  insurance assets, **3.77% annualised against 3.65% a year earlier**; spread with gains 1.78%, without 1.28%.
- **The whole-level claim (iii) meets the attacker's test here, in filings [E2-45].** The model BN describes as
  its ecosystem (an alternative manager, a captive annuity balance sheet invested in the manager's strategies, and
  permanent capital) has **two larger filed copies in this row**: Apollo, which merged with Athene on *"January 1,
  2022"* ($292.4bn of net invested assets), and KKR, which *"acquired a majority controlling interest in Global
  Atlantic on February 1, 2021"* and the remainder on January 2, 2024 ($192.0bn of insurance investments), against
  BWS's $120bn at YE2025. Blackstone runs the same mandate without owning the insurer (CRBG $71.2bn, FG
  substantially all). **A system with at least three competitors running it at equal or greater scale is not a
  system without a close substitute.**
- **The filer's own statement of position:** BWS 20-F FY2025, risk factors: *"The insurance industry is highly
  competitive; competitive pressures may result in lower volumes of policies written, fewer insurance contracts
  underwritten, lower premium rates, increased expense for customer acquisition and retention and less favorable
  policy terms and conditions."* That is **[E2-70]** restated by the subject.
- **Peers named: four with a published rate, plus KKR/GA shown and not ranked.** JXN, EQH and LNC were screened by
  the killed session (EDGAR full-text counts, `peers_ins/fts_out.txt`) and publish no comparable rate; they are
  additional substitutes, not missing evidence. **The row's limit [E3-61]:** it shows position; it cannot show
  conduct, and conduct in this class is the crediting decision made one annuity at a time.

#### ROW C. The real estate: BPG against the landlords a tenant would otherwise lease from

**Which peers (brief prior 2, argued).** The brief doubted BXP, SLG, SPG and VNO as peers for an unlisted,
100%-owned BPG carrying fund-level debt. **Criterion (2) is a customer judgment, so the peer set is chosen by
the tenant's alternative, not by the owner's capital structure.** BPG's super core is *"16 premier office and
ancillary mixed-use complexes"* in *"New York City, London, Toronto, Berlin, and Dubai"* and *"18 irreplaceable
malls"* plus a center *"at the corner of 57 th and Fifth Avenue"* (40-F, Real Estate; the split "57 th" is
the extracted text as filed, not smoothed). A New York office tenant's alternatives are SLG's,
VNO's and BXP's towers; a US mall tenant's is SPG. The capital structure (BPY's *"consolidated debt obligations to
capitalization was 51%"*; *"suspended contractual payment on approximately 3 % of its non-recourse mortgages"*) is
a Q4 fact and is carried there. **Limits stated:** the London, Toronto, Berlin and Dubai competitors (British Land,
Landsec, Canary Wharf Group, Oxford, Cadillac Fairview) do not file with the SEC or are private; BPG itself files
nothing, so the subject line is **BPY's 20-F**, which is the SEC filer inside BPG and carries the super core
figures. Metric: **year-end occupancy as each filer defines it**, the physical series [E4-55], which every filer
publishes; rent per square foot is not filed by BPY on a comparable basis.

| Company (portfolio) | 2023 | 2024 | 2025 | definition | source |
|---|---|---|---|---|---|
| **BPY super core office complexes** | **95.1%** | **94.3%** | **95.3%** | occupied, 16 complexes, ~35M sf | BPY 20-F FY2023-25 (`0001545772-24-000004`, `-25-000008`, `-26-000006`), Office key metrics fn.1 |
| BPY office, total consolidated | 84.1% | 84.9% | 86.0% | occupancy | same |
| SLG, Manhattan office | 89.4% | 92.5% | 93.0% | leased, incl. signed not commenced | SLG 10-K FY2025 `0001628280-26-008669`, historical occupancy table |
| *Midtown Manhattan Class A market (SLG's cited source)* | *78.4%* | *78.0%* | *80.5%* | *occupancy incl. sublease space* | *same table* |
| VNO, New York office at share | 90.7% | 88.8% | 91.2% | occupancy rate | VNO 10-K FY2023-25 (`0000899689-24-000005`, `-25-000004`, `-26-000009`) |
| BXP, CBD portfolio | not located | 90.9% | 89.8% | occupied (total in-service 86.7% at 2025) | BXP 10-K FY2024-25 (`0001656423-25-000009`, `0001037540-26-000006`) |
| **BPY super core malls** | **97.3%** | **97.5%** | **97.7%** | occupied, 18-19 centers, ~24M sf | BPY 20-F, Retail key metrics fn.1 |
| BPY retail, total consolidated | 93.7% | 94.0% | 93.0% | leased | same |
| SPG, US Malls and Premium Outlets | 95.7% | 96.5% | 96.4% | ending occupancy, consolidated | SPG 10-K FY2023-25 (`0001558370-24-001532`, `-25-001271`, `0001104659-26-019419`) |

**What row C shows, both directions [E4-26].**
- **For BPG: the super core leads every row it is in.** 95.3% office against 89.8-93.0% for the New York and CBD
  peers; 97.7% malls against SPG's 96.4%. That is a filed relative position, in the portfolio BN calls
  *"irreplaceable"*, and it is the strongest evidence for a moat anywhere in this Q2.
- **Against: the position is in a product whose sellers, BPY included, describe price competition from the
  substitute.** BPY 20-F FY2025: *"Numerous other developers, managers and owners of commercial properties compete
  with us in seeking tenants … Some of the properties of our competitors may be newer, better located or better
  capitalized. These competing properties may have vacancy rates higher than our properties, which may result in
  their owners being willing to make space available at lower prices than the space in our properties, particularly
  if there is an oversupply of space available in the market."* SLG's own table puts the Class A market at 80.5%
  occupied: one fifth of the substitute stands empty. **High occupancy in a building is being the preferred
  seller of a substitutable product, the [E2-37] shape ("a remarkable textile company - but not a remarkable
  business"), not a customer's judgment that no substitute exists.** And [E2-58]'s *"persistent over-capacity"*
  is the filed condition of the office market in every one of these 10-Ks.
- **Against: the super core is a minority of BPG and is being sold down to the insurer.** Super core is 44.8% of
  BPG's FY2025 NOI ($1,407M of $3,144M) and 31.4% of positive segment book equity. BPG NOI fell $3,397M → $3,144M
  (−7.4%); super core NOI fell $1,490M → $1,407M, which the filer attributes to *"the sales of partial interests in
  six super core retail assets"*, and *"Over the year, we transferred partial interests in six super core assets to
  our Wealth Solutions business."* The remainder of BPG (value add *"not considered dominant irreplaceable centers"*,
  opportunistic, residential development, and $(9,141)M of "Corporate and Other") has no position claim at all, and
  the total consolidated office line sits at 86.0%, **below** every peer.
- **Peers named: four** of the SEC-filing landlords a US tenant would call; the non-US gateway-city landlords are
  named above and unpulled. **They are additional substitutes and cannot reverse a no-close-substitute failure.**
  Were BPG's super core the only question and heading for IN, their filings would be required first.

### The legs not rowed, and why that does not make the class PROVISIONAL

**BIP, BEP and BBUC carry 12.5% (book), 13.1% (cash) and 16.3% (market) of the weight.** A row establishes
*relative* position inside a class; it cannot move a leg out of the class its own parent's filing places it in,
and on the weights above it cannot carry BN. From the 40-F:
- **BIP, criterion (3):** *"This includes businesses with price ceilings as a result of regulation, such as our rail
  and toll road operations"*; utilities *"generate long-term returns on a regulated or contractual asset base"*;
  *"Approximately 85% of FFO is supported by regulated or long-term contracted revenues."* **[E2-59]**: *"the moat
  belongs to the regime."* The Loews run's Boardwalk leg (27% of earnings, rate-capped, NARROW) did not make Loews a
  franchise; a leg of 3-6% cannot make BN one.
- **BEP, criterion (2):** *"Revenues in our Renewable Power and Transition segment are 91% contracted with an average
  contract term of 13 years"*; the uncontracted remainder is *"merchant pricing"*, and the contracts are for
  electricity, [E2-58]'s undifferentiated product, won at the price the contract fixes. BN's own energy contract with
  BEP steps down *"by $3 per megawatt hour … followed by a $5/MWh reduction in 2026"* (40-F FY2024): a price that falls
  by agreement between the two parties BN controls.
- **BBUC, criterion (2):** *"We have several companies that operate in the highly competitive service industry"*, and
  BBUC's model is buy, improve, sell, which **[E4-04]** excludes by construction (the basis is replaced every holding
  period).

**This does not hold the class PROVISIONAL, and the reason is directional, as the BAM run's was:** a completed row
for each of the three could only place it higher or lower among regulated utilities, contracted generators or
private-equity owners. It cannot create a no-close-substitute finding for a leg its parent describes as regulated,
contracted or highly competitive, and even a WIDE finding on all three would sit on at most 16% of the weight.
**Were BN's Q2 heading for IN, BIP's, BEP's and BBUC's own 20-Fs and a row for each would be required first;** it is
not, so they are named as the work order for any reversal.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04, E4-23]**

> *"A moat that must be **continuously rebuilt** will eventually be no moat at all. Additionally, this criterion
> eliminates the business whose success depends on having a great manager."* **[E4-04]**, 2007 letter

**The framework's test: does a lapse in spending destroy the structure or merely narrow it, and does the spending
defend the same advantage or buy its replacement?** At the whole level **BN answers it in writing, and the answer is
replacement.** FY2025 letter (6-K/A `0001001085-26-000011`, quoted at Q1): *"The ability to continually adapt is the
lifeblood of a great long-term business"*; *"Today, most of our excess capital is going towards digitalization,
decarbonization and deglobalization whereas years ago it was going into property, pipeline infrastructure and hydro
facilities"*; *"50% of the things that we invest in today did not exist as widely held institutional investments 15
years ago."* That is the excluded class in the filer's own description: the basis of the program is **periodically
replaced**, and the record comes from catching each reallocation, **[E3-51]**'s surfing run and **[E4-36]**'s
wave-riding (institutional money moving to private markets; higher rates making fixed annuities saleable). At the
legs: BAM's closed-end fee base depletes by design (56.4% replaced or redeemable, BAM run); BBUC sells what it buys;
BWS re-underwrites its cost of funds one sale at a time. **Only BPG's super core and BIP's regulated assets are
defended rather than replaced**, and those are the two legs that fail on other criteria (substitutable space;
regulated price).

**Key-person dependence, recorded here as a moat defect, not at Q3 as a compliment [E4-23].** Bruce Flatt has been
BN's chief executive since 2002 (AIF), Chair of BAM, and holds one-third of the beneficial interest in the trust that
owns the Class B shares. BN's own risk factor says the whole-level claim rests on people: *"Our senior management team
possesses substantial experience and expertise and has strong business relationships with investors in managed
entities … the loss of these personnel could jeopardize our relationships with investors in managed entities … and
result in the reduction of our AUM or fewer investment opportunities"*, and fund *"key person" provisions … are
typically tied to multiple individuals"*, with *"we do not maintain any key person insurance."* **The mitigant is
filed and fair: the dependence is on a team, not one person, and BAM's CEO changed on 2026-02-03 with no disclosed
capital consequence.** The defect that remains is structural rather than personal: **the thing BN says is its edge
(adapting the program to the next wave) is a judgment exercised by people, which is the knight, not the castle
[E4-33].** A moat that exists only while the allocators keep choosing the right wave is the business *"whose success
depends on having a great manager."*

### Primary moat metric at the whole level, and its direction [E4-32]

**The whole-level metric is the cost of BN's permanent capital against its competitors'** (row B is the filed half),
and **the business-level number is [E3-46]'s return on capital employed.** Both point the same way.
- **Return on common equity, IFRS** (net income attributable to shareholders less preferred dividends ÷ average common
  equity, 40-F FY2023-25; my arithmetic in `q2_calc.py`): **FY2023 2.37% · FY2024 1.13% · FY2025 2.66%** (FY2022, a
  different perimeter, 4.66%). BN's own DE ÷ average common equity would read ~15.0% and ~14.0%; Q1 recorded why DE
  is not an earnings figure (equity compensation added back, WS DE not received, distributions counted, a $1,000M
  related-party gain in FY2024), so it is shown and not used. **Caveat carried, not smoothed:** IFRS fair-values
  investment property into equity and runs $10.4bn of consolidated depreciation through income, so the IFRS return
  understates the cash yield of the real-asset legs; it is still the only audited return on BN's equity, and
  *"the best businesses … earn very high returns on capital employed over time"* **[E3-46]** is not a description of
  1-3%.
- **Direction:** fee rate down (90.4 → 82.4bp, row A); BWS cost of funds up (3.49% → 3.45% → 3.77% annualised in Q2
  2026) with the peers also rising, and BWS's spread without real-asset gains falling (1.56% FY2025 → 1.28% Q2 2026
  annualised); BPG NOI down 7.4% on dispositions while super core occupancy rose a point. **Nothing in the filings
  shows a moat widening every year.**

### The remaining Q2 tests, each answered

- **[E2-44], the two-characteristic test.** *(a) Raise prices when demand is flat?* No leg shows it: the fee rate
  falls in a record fundraising period; BWS prices its annuities against three larger writers; BPY's own risk factor
  describes landlords with vacancy undercutting it. *(b) Grow dollar volume with minor additional capital?* **No.**
  BN's growth is capital-hungry by design: BWS required $3.3bn of BAM shares (2025-06-25), a $1bn BBU interest (Q4
  2024) and ~$1bn of BAM shares for AEL (2024) as contributed capital, and Just Group cost £2.4bn; BPG's equity rose on
  *"capital contribution to opportunistically repay debt and fund various investments."*
- **[E2-53], the dominance class.** No. No leg sets its own price: nine managers, four annuity writers with a
  published rate (two of them larger), and a landlord market one-fifth empty.
- **[E2-45], the attacker's test.** Answered by filings at both whole-level candidates: Apollo-Athene and KKR-Global
  Atlantic built the manager-plus-insurer system (row B); Blue Owl built a manager to $187.7bn of fee-paying AUM
  growing 35.2% a year (row A, from the BAM run). **Capital and people have already replicated the ecosystem at
  larger scale.**
- **[E4-37], the inverse metric.** The filed pricing language is defensive at every leg: *"pressure to reduce or modify
  asset management fees"*; *"competitive pressures may result in … lower premium rates"*; competitors *"willing to make
  space available at lower prices."* No price increase is contemplated in any document read.
- **Untapped pricing power [E3-33]?** **No, and refused.** **[E5-28]** makes the claim a claim of near-monopoly; the
  rows show nine, four and four competitors. The one place a higher price is available on paper is the related-party
  fee on BWS's capital, and **BN would be raising a price on itself.**

### THE CASE FOR IN, BUILT AT FULL STRENGTH AND REJECTED **[E4-26, E4-51]**

**The strongest case.** BN is the Berkshire of real assets: permanent capital that never has to be returned, a
general-partner position no limited partner can remove, a thirty-year record that fills funds of $10bn+, an insurer
whose float is invested in the group's own higher-yielding strategies at *"an average yield of 8.5%"*, super core
towers and malls that lead every occupancy row, regulated and contracted cash flows under 85-91% of the operating legs'
FFO and revenues, and the operating depth (*"integrated solutions that few organizations can replicate"*) to write
cheques competitors cannot. Every leg supports every other: BWS supplies capital to BAM, BAM supplies assets to BWS,
BPG transfers super core interests to BWS, and the whole compounds at the Corporation. A holding company can be a
franchise where its legs are not, and BRK was.

**Why it does not carry, one line each:**
1. **BRK's whole-level moat was a filed cost advantage** (a negative cost of float, −3.6% over five years, against
   peers that pay). **BN's whole-level funding is the most expensive in its row** on the life and annuity book (3.82%),
   and its filing says competitors may have *"a lower cost of capital."* The analogy fails on the one number it rests on.
2. **The ecosystem's mutual support is transfers between BN's own pockets** (fees BWS pays BAM, IDRs BEP and BIP pay
   BAM, super core interests moved to BWS, BAM shares contributed to BWS, a $1,000M gain booked on selling BAM shares to
   BWS). Transfers inside a controlled group are not a customer's judgment about substitutes; criterion (2) is about
   customers.
3. **The system has been copied at larger scale** by Apollo-Athene and KKR-Global Atlantic, and the manager half by nine
   filers [E2-45].
4. **The basis is replaced by the filer's own program** [E4-04], and the replacement is chosen by people [E4-23, E4-33].
5. **The best-positioned asset (super core) is a leader in an over-supplied, substitutable product** [E2-58, E2-37],
   and it is 31% of the book weight and being sold down to the insurer.
6. **[E3-46]'s number is 1-3% on the audited equity**, and no direction in the filings points up [E4-32].

**A conclusion that required fighting for it is worth less, not more [E4-18].** This one did not: BN's own risk factors
concede competition at the whole and at each leg, and the three rows put each rowed leg inside its pack or at its
expensive end.

- Needed or desired **[x]** · no close substitute **[ ] NO, at the whole and at every leg carrying weight** · not
  price-regulated **[x] at BN's level; [ ] at BIP's regulated and price-ceiling assets**
- Peers named: **row A nine** (every SEC-filing alternative manager of scale; four non-SEC managers named, unpulled);
  **row B four with a published rate plus one shown** (three more screened, no rate filed); **row C four** (non-US
  landlords named, unpulled). BIP, BEP and BBUC not rowed, for the reason above.
- **Untapped pricing power [E3-33]:** no.
- Class: [ ] WIDE  [ ] NARROW  [x] **NONE at the BN level** *(NARROW on position at BPG's super core alone, 31% of book
  weight, being sold down; NARROW and conferred at BAM's perpetual leg, which at BN is partly circular)*  [ ] PROVISIONAL
  *(not PROVISIONAL: the three legs carrying 84-87% of the weight are rowed from primary filings on one specification
  each, and every unpulled filer is an additional substitute or sits on a leg that cannot carry the verdict)*
- **Direction: NOT WIDENING.** Fee rate down, BWS cost of funds up and its ex-gains spread down, BPG NOI down.
- **VERDICT: [ ] IN  [x] OUT - ON THE BUSINESS. Permanent.  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  BN is a well-built group of good businesses and it is not a franchise. **Criterion (2) of [E3-03] fails at the
  whole** (BN's own filing: competitors *"may have … a lower cost of capital"*; the manager-plus-insurer system is
  filed by two larger competitors) **and at each leg carrying the weight** (the fee engine against nine managers; the
  insurer at the high-cost end of four writers, its leading spread made by 0.69 points of gains on its sponsor's own
  strategies; the real estate a leader in a market one-fifth empty). **The basis is replaced by design [E4-04]**,
  chosen by people **[E4-23]**, and the audited return on equity is 1-3% **[E3-46]**.
  *Not UNRESEARCHED: every leg carrying weight is rowed from primary filings, and the named unpulled documents
  (EQT, Partners Group, Antin, Tikehau; British Land, Landsec and the private Toronto and London landlords; BIP, BEP and
  BBUC 20-Fs and rows) are shown to be unable to reverse it. Can I name the document that would resolve this? The
  documents that exist are named and none of them can turn a filed substitute into no substitute. Not UNKNOWABLE: the
  evidence is in, and it decides.*

**⛔ THE FILE CLOSES HERE. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING** - written because the queue's output
contract requires a price and a refutation record on every name, and because a read discarded at the closing gate has to
be bought again. **The price carries the heading `COMPUTATION — NOT A CLEARANCE` (operator rule 3) and no entry language
appears anywhere below.**

**ADDENDUM TO Q2, written after the Q2 commit (`ca71599`) in the same session, recorded beneath rather than edited
(operator rule 6): a moat claim in a leg that Q2 did not name.** The Q2 2026 letter (6-K `0001001085-26-000021`) claims one
explicitly, for Westinghouse: *"Its technology is used by over half of the world's operating nuclear reactors (yes — over half
of all in the world). The company also services roughly half of the global reactor fleet … Few businesses in the world today have
such significant structural tailwinds for growth, and a moat which is unassailable."* The claim is the strongest [E3-03]
candidate in the group (installed-base services on a regulated fleet; the substitutes are few and mostly not SEC filers).
**Its weight at BN:** the AIF states *"BEP, together with institutional partners, own an aggregate 51% interest with Cameco owning
49%"*, and a contingent U.S. Government interest *"entitled to receive 20% of any cash distributions in excess of $17.5 billion"*.
BN holds 45-47% of BEP, and BEP's own share of the 51% is not stated in the documents read, so **BN's look-through interest in
Westinghouse is below 24% (47% x 51%) by an unstated amount**, inside a leg that carries 7-8% of BN's weight on every basis. **It
cannot change the Q2 verdict on BN, and it is not tested here.** Work order for anyone who wants the Westinghouse question on
its own: Cameco's 40-F (Westinghouse is equity-accounted there with summarized financials), BEP's FY2025 20-F segment note, and a
row against Framatome (EDF, not an SEC filer). *Found by reading the letter for Q3's projections flag; the Q2 draft had read the
MD&A and the risk factors but not the letter, which is the order this addendum corrects.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? - **RECORDED, NOT GOVERNING**
*The file closed at Q2 (OUT, on the business). This section decides nothing; it is kept so the read is not bought
twice. Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Companion rule applied: the furnished earnings
releases were pulled and read before the [E4-29] and [E4-22] flags were scored (Q3 2025 6-K `0001171843-25-007252`,
Q4 2025 6-K `0001171843-26-000765`, Q1 2026 6-K `0001171843-26-003394`, Q2 2026 6-K `0001171843-26-005474`; texts in
`_research 2026-09-13 BN/6K_*release.txt`).*

**STEP 1 - THE WEIGHT CASE.**
- [x] **Leverage [E3-29].** Corporate borrowings $14,711M, preferred shares $4,088M and perpetual notes $230M stand ahead
  of $42,483M of common equity at the Corporation (2026-06-30); beneath it, *"Total consolidated debt to capitalization
  ratio of 50%"* (40-F), BPY's *"consolidated debt obligations to capitalization was 51%"* with payment suspended on
  about 3% of its non-recourse mortgages, BBU's $42,424M of subsidiary borrowings at a 7.3% weighted rate, and an insurer
  carrying $191bn of insurance assets. Small asset errors reach the common equity through several layers at once.
- [x] **Daily execution [E3-38, E2-70].** The insurer re-prices its promises one annuity at a time and invests them in
  the sponsor's strategies; the fee engine is re-won vintage by vintage.
- [ ] **Control [E1-16]** in the corpus's sense, no: a holder can sell. **Recorded:** the Class A holders elect *"one-half
  of the Board"* (AIF); the other half is elected through the 85,120 Class B shares held in a trust whose beneficial
  interests are one-third Bruce Flatt, one-third Jack L. Cockwell, one-third jointly five other executives (Step 0). An
  outside holder cannot change the allocators.
- **Case declared: Q3 would be a BINARY GATE** on leverage and daily execution, and, Q2 having found no franchise, on
  **[E3-43]**'s original form: *"a business, unlike a franchise, can be killed by poor management."* No price compensates
  where that case holds **[E1-16, E3-29, E5-35]**.

**Honesty - binary, filings-based [E5-16].** **No integrity disqualifier found in the documents read.** Deloitte LLP gave
an unqualified opinion on the FY2025 statements and on internal control (40-F); no restatement of BN's statements was
found; the risk-factor text on litigation describes ordinary-course *"legal actions"*; no enforcement matter, consent
order or cease-trade order surfaced in a sweep of the 40-F, AIF, Q2 6-K and BWS 20-F for those terms. **Scope stated: this
is a keyword sweep of four documents, not a litigation search.** *A Q3 pass is the absence of found disqualifiers, not a
finding that the managers are honest [E5-17].*

**STEP 2 - THE FLAGS.** *Each a prompt to read, never a verdict.*
- [x] **Adjusted-earnings promotion [E4-29, E5-06] - FIRES, and it is the headline.** Q2 2026 release title: *"Brookfield
  Corporation Reports 15% Increase in Earnings"*; the President's quote: *"15% growth in earnings per share."* The "earnings"
  are **DE before realizations per share** ($0.61 against $0.53). In the same table, *"Net income of consolidated
  business"* fell **$1,055M → $703M (−33%)**, while net income attributable to shareholders rose $272M → $364M and diluted EPS
  $0.10 → $0.14. The headline direction happens to agree with the attributable line this quarter; **the flag is the word,
  not the direction**: DE adds back equity-based compensation ($110M in FY2025) against a gross share-based payment expense of
  **$317M** (*"Total expense arising from share-based payment transactions"*, $513M in 2024) that reaches income only as
  **$123M** after an *"Effect of hedging program"* of $(194)M (40-F note); FFO adds back $10,379M of depreciation
  [E5-41]; and Q1 recorded the $1,000M related-party gain counted in FY2024 DE. **[E3-70]: where SBC is material, the
  reported charge is the floor of the subtraction.**
- [x] **Metric perimeter switch [E2-49] - FIRES as a prompt.** The insurer's yield and spread were published on the **whole
  business** through FY2025: Q3 2025 release, *"Our investment portfolio generated an average yield of 5.7%, maintaining strong
  spread earnings"*; FY2025 40-F, the whole-business spread table (gross spread 2.25%). The Q1 2026 release gave no spread. **The
  Q2 2026 release, the first full quarter with Just Group inside, moved both figures to a sub-perimeter:** *"an average net
  investment income yield of 5.7% for the quarter"* and *"a gross spread of 2.2% for the quarter in our North American
  business"*, and the Q2 6-K MD&A carries the dollars but no percentage table. **From those filed dollars the whole business
  earned 5.04% NII and a 1.78% spread (1.28% without real-asset gains) annualised** (`q2_calc.py`). *The candor reading, stated
  at full strength:* Just Group is a UK pension-risk-transfer book with different economics, and showing the continuing business
  separately is a defensible presentation. **What would make it the candor case is the whole-business figure printed beside the
  sub-perimeter one; it is not.** The document that settles it: the Investor Day materials of 2026-09-17 or the Q3 2026 release.
- [x] **A published yardstick falling, then absent [E2-49] - a weak prompt.** BN printed its own *"view of intrinsic value"*
  per share in consecutive releases: **$69** (Q3 2025), **$68** (Q4 2025), **$66** (Q1 2026). The Q2 2026 release and letter
  print none (the letter speaks of *"higher intrinsic value per share over the longer term"*). One quarter of absence after three
  of decline is a prompt, not a finding; the same two documents settle it.
- [x] **Trumpeted projections [E4-22] - FIRES.** *"We expect to leverage our resources and reputation to continue to seek
  opportunities that will provide total returns of over 15%+ a year over the long-term"* (40-F); *"BWS seeks to generate a 15%+
  annual return on equity over the long term"* (6-K Q2); the Q1 2026 release moved from *"an average yield of 8.5%"* (FY2025
  realised deployment) to *"an average target yield of 10%"*. **[E4-35]'s base rate applies**: fewer than 10 of the 200 most
  profitable companies of 2000 were expected to attain 15% annual EPS growth over twenty years. **Against the record the filings
  show:** IFRS return on common equity 2.37% / 1.13% / 2.66% (FY2023-25, Q2).
- [x] **Earnings made between entities under common control [E2-50] - FIRES as a prompt.** *"Where 'earnings' can be created by
  the stroke of a pen, the dishonest will gather."* The pattern in the filings: $1,000M of *"disposition gains from principal
  investments"* booked in FY2024 DE on BAM shares sold to BWS; partial interests in six super core assets transferred to BWS in
  2025; 16% of BBUC transferred to BWS in April 2026; $3.3bn of BAM shares contributed to BWS for class C shares; Westinghouse sold
  by BBU to *"a strategic consortium led by Cameco and BEP"* in November 2023, with BN's private equity segment FFO for that year *"including a disposition gain of $1.1 billion earned on the sale of Westinghouse"* (AIF FY2025, three-year history). **Each is
  disclosed and quantified separately, which is the [E2-26] disclosure standard met; the prompt is that the headline measure
  counts them.** Not a venality finding [E5-38].
- [ ] **Serial share issuance [E5-15] - does not fire.** Class A outstanding 2,244.6M (2025-12-31) → 2,232.3M (2026-08-13) through
  repurchases, after BN shares were used as part of the Oaktree consideration; the BWS exchangeables are a paired economic claim
  counted at Step 0.
- [ ] **Cash-tax tell [E4-30] - does not fire.** Consolidated income taxes paid $1,079M / $1,677M / $2,674M / $2,225M against pretax
  income (net income plus tax expense) of $6,664M / $6,116M / $2,835M / $4,370M, FY2022-25: 16% / 27% / 94% / 51%. Not a falling series.
- [ ] **Dividends needing the capital replaced [E2-52] - does not fire at the Corporation.** Common dividends $552M (FY2025) against
  repurchases above $1bn in the same year. *(At the legs it is live: BPY paid $800M to redeemable/exchangeable and special LP
  holders in FY2025 against operating cash of $(595)M; carried to Q4.)*
- [ ] **Adjusted Equity redefinition at BWS - read, not fired.** BWS changed its return-on-equity denominator in Q2 2025 *"to exclude
  non-controlling interest and the accumulated after tax impact of certain investment and insurance reserve gains and losses"*, gave
  the reason (*"comparability with peers"*) and *"restated all applicable comparative information"* (BWS 20-F FY2025). Announced with
  reasons and restated: the [E2-49] candor case.

**STEP 3 - THE PRIMARY TEST [E2-01].** Net income attributable to shareholders less preferred dividends ÷ average common equity,
IFRS: **FY2022 4.66% (pre-spin perimeter) · FY2023 2.37% · FY2024 1.13% · FY2025 2.66%.** With undue leverage present (Step 1),
the [E2-43] unleveraged-net-tangible-assets denominator would be the right one for the operators; it was not built. BN's own DE
yardstick would read ~14-15% on the same equity and is not the test [E2-01] names.

**The half-owner test [E2-26]:** **mixed.** Every related-party gain and transfer above is quantified separately in a footnote,
the audited parent balance sheet is in Note 1, and the filer publishes its own intrinsic-value figure with its buyback prices.
Against that, the headline "earnings" word is used for a measure that adds back equity compensation, and the insurer's spread
moved to a sub-perimeter in the quarter its largest acquisition entered.

**The institutional imperative [E2-30]:**
- [ ] resists change: the reverse; the stated program is continuous change.
- [x] funds soak up projects: *"with over $200 billion of deployable capital we are well positioned to invest at scale"*; Just Group
  (£2.4bn), Oaktree (~$3.0bn total consideration), $25bn Bloom framework, all in one half-year.
- [ ] staff studies justify the craving: not observable from filings.
- [x] peer imitation: the manager-plus-captive-insurer model runs at Apollo (Athene, 2022) and KKR (Global Atlantic, 2021/2024);
  BN's reinsurance vehicle dates from 2021, so the order does not establish imitation. **Weak prompt.**

**Capital allocation - the buyback conditions [E5-08, E4-31]:**
- (1) ample funds: yes at the Corporation (core liquidity $5,636M at 2026-06-30; *"no maturities in 2026"*).
- (2) material discount to conservatively calculated IV: **BN says yes in its own numbers** (FY2025 repurchases *"at an average
  price of $36, which represents an approximate 50% discount to our view of intrinsic value at quarter end of $68"*; Q1 2026 *"$41
  … an approximate 40% discount to our view of intrinsic value at quarter end of $66"*; H1 2026 ~$580M at $42). **This run's own
  computation below does not support a material discount on an owner-earnings basis** (the look-through range sits well below the
  quote) while a parts-at-their-own-marks computation sits above it. **CAPITAL ALLOCATION FLAG, stated with the humility clause
  [E4-13]:** *"They also know a whole lot more about them than I do"*, and the corpus's *"infractions, even serious ones, are
  innocent; many CEOs never stop believing their stock is cheap"* **[E5-08]**. Binds position size, never the discount rate.
- (3) [E4-31], owners supplied the information to estimate value: partly. The IV figure is printed; its method is not in the
  documents read (the 6-K/A letter pages were read at Q1 and no plan-value table was quoted there).

**THE GUARDRAIL.**
- [x] Nothing here promotes the name; a strong Q3 cannot repair Q2 [E2-37, E2-38, E3-39].
- [x] Key-person dependence is recorded at Q2 as a moat defect [E4-23], not here.
- [x] Great manager as the reason to act? Not applicable: there is no intact franchise to excise damage from [E2-35, E2-36].

- **VERDICT (recorded, not governing): IN on honesty as the absence of found disqualifiers, under a binary-gate weight case, with
  FIVE live prompts converging on one surface (the adjusted-earnings headline, the spread perimeter switch, the vanished IV figure,
  the 15%+ projections, gains booked between commonly controlled entities) [E4-52], and a live capital-allocation flag.**
  *IN never promotes. The file is closed at Q2.*

## Q4 — WILL IT SURVIVE? - **RECORDED, NOT GOVERNING**
*The file closed at Q2. Written because the queue's contract requires a price, and a price needs owner earnings. It decides
nothing.*

### Owner earnings — the one number **[E2-23]**, by look-through **[E3-04]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its long-term competitive position
> and its unit volume. (… the working capital **increment also should be included in (c)**.)" … "**(c) must be a guess**."

**Not DE, not FFO, not a net-income proxy.** Each leg is built from **its own filed consolidated cash-flow statement**, taken
at BN's economic share, then the Corporation's own costs are charged. Script and output: `_research 2026-09-13 BN/q4_oe.py`,
`q4_oe_out.txt`. Leg filings: BIP 20-F FY2025 `0001406234-26-000002`; BEP 20-F FY2025 `0001533232-26-000011`; BBU 20-F FY2025
(filed under Brookfield Business Corp's CIK 0001654795) `0001628280-26-022148`; BPY 20-F FY2025 `0001545772-26-000006`; each
carries FY2023-25. BAM from the committed BAM run (Q4, `a4c3ca4`), built from BAM's own cash-flow statements.

**CONVENTION (confessed, operator rule 3): the share of a partnership's consolidated owner earnings that belongs to its common
holders is taken as the common group's share of total equity at YE2025** (limited partners + general partner + redeemable,
exchangeable and special LP units, against total equity including the *"interests of others in operating subsidiaries"*,
preferreds and perpetual notes). *Rationale: the consolidated operating cash includes the institutional co-investors' share of
every asset, and the filings give no cash-flow attribution; capital share is reproducible in two minutes from each balance sheet.
It is not the only defensible key: net-income attribution would give BIP a larger share, and the NCI distributions actually paid
(BIP $2,476M, BEP $2,933M, BBU $4,153M, BPY $1,527M in FY2025) run well above capital share, which would give a smaller one.*

| leg (filing) | OCF as filed FY2023 / 24 / 25 | D&A | total capex line | common-group share x BN economic % | leg OE at 100%, 3-yr mean: (c)=D&A · (c)=total capex | **at BN's share** |
|---|---|---|---|---|---|---|
| **BIP** | 4,078 / 4,653 / 5,971 | 2,739 / 3,644 / 4,024 | *"Purchase of long lived assets"* 2,487 / 4,975 / 6,024 | 23.7% x 27% = 6.4% | +1,432 (**INVALID end**, [E5-20]: utilities, transport, midstream, data) · **+405** | +92 invalid · **+26** |
| **BEP** | 1,865 / 1,274 / 1,147 | 1,852 / 2,010 / 2,425 | *"Investment in property, plant and equipment"* 2,809 / 3,733 / 6,587 | 25.4% x 47% = 11.9% | **−667** even at the INVALID end · **−2,948** | **−80 · −352** |
| **BBU** | 2,130 / 3,281 / 3,230 | 3,592 / 3,204 / 3,030 | PP&E and intangibles 2,288 / 2,520 / 2,060; *filer's maintenance capex 833 / 853 / 868* | 35.6% x 68% = 24.2% | **−395** · +591 · +2,029 at the filer's maintenance figure | **−96** · +143 · +491 |
| **BPY** | **−670 / 1,018 / −595** | 440 / 418 / 269 (hotels and PP&E only; investment property is fair-valued, not depreciated) | PP&E 529 / 403 / 758; investment-property spending sits inside *"Investment properties"* acquisitions (4,807 / 9,053 / 4,078) and is not separable | 54.5% x ~100% (BPY's LP units were taken private; BN's share not re-verified here) | **−458** · −646; **−82 at (c)=0**, which no real estate owner can run | **−250** · −352 · −45 |
| **BAM** (74.69%: 1,193.0M of 1,597.25M) | BAM run: OE $1,670M-$1,792M (3-yr), $1,862M-$2,024M (2-yr), on the Predecessor-restated perimeter | | | 74.69% | | **+1,247 to +1,338** (3-yr) · +1,391 to +1,512 (2-yr) |
| **BN's own carry** | *"Realized carried interest, net"* 570 / 403 / 560 (after *"employee expenses and cash taxes"*) | | | 100% | | +403 lowest year · +511 mean |
| **Corporation** | FFO of corporate cash and other +131 / +44 / +155; corporate borrowings −596 / −727 / −742; preferred dividends −176 / −176 / −177; equity-based compensation −108 / −109 / −110 | | | | | **−864** (3-yr mean) |

**Two components are NOT owner-earnings streams and are valued as investments instead (SECTOR METHOD, component 1 [E5-46];
CONVENTION 3, part insurer and part operating business valued separately):** **BWS**, whose DE is retained in BWS and whose
float is the funding of its portfolio rather than an earnings stream (its cost of funds was graded at Q2, row B, as the
diagnostic [E3-69]), carried at BN's IFRS book of $13,139M less the 65.0M BAM shares and 53.6M BBUC units it holds that are already
inside the BAM and BBU lines ($3,072M and $1,416M at 2026-09-11 quotes) = **$8,651M**; and **the direct fund stakes** (BSREP
III-V, Oaktree Opportunities XI-XII and others) at **$10,876M** (YE2025 IFRS fair value; the 2026-06-30 figure was not separated).
Their cash distributions ($876M in FY2025) are not counted as owner earnings.

**The windows [E2-42, E4-25, E4-38].** **No five-year window on one perimeter exists** and none is spliced: FY2022 is the spin
year, and every leg changed perimeter inside FY2023-25 (BIP's $10,032M and $10,747M acquisition years; BBU's $4,686M of 2023
disposition gains and the healthcare operation's receivership in May 2025; BPY's BSREP IV deconsolidation; BWS's AEL). Every
window available is shown.
- **3-yr FY2023-25:** conservative **$12M** · judged top **$900M** · display ceiling $1,443M (INVALID ends)
- **2-yr FY2024-25:** conservative **$222M** · judged top **$1,097M** · display ceiling $1,742M (INVALID ends)
- *(Conservative: BAM conservative, carry at the window's lowest year, BIP and BEP at total capex, BBU at D&A, BPY at total capex.
  Judged top: BAM generous, carry at the window mean, BIP and BEP still at total capex because their D&A end is INVALID, BBU at the
  filer's own maintenance capex, BPY at D&A, which still flatters a fair-valued property book. Display ceiling: BIP and BEP at D&A,
  BPY at (c)=0; shown, never used.)*
- **Combined range: about $0 to $1.1bn a year. The bottom is NIL ($12M).** In words: **on the conservative end of the longest
  window, the operating legs and the Corporation together earn nothing for BN's owners.** On the judged top, $1.1bn.
- **Is the range too wide for a conclusion [E4-25]?** In ratio, yes (the top is ninety times the bottom). **Against the question
  Q5 asks, no:** every point of it, including the display ceiling, is a yield of **0.01% to 1.98% on the $87.8bn cap**, below a
  5.35% bond at every end. The width is real and it does not reach the bond.

**Maintenance capex, a disclosed judgment.** BIP, BEP and BPY are the [E5-20] class (utilities, transport, midstream, renewables,
real estate): the D&A end is INVALID and shown only. **BEP's operating cash was below its depreciation in FY2024 and FY2025
($1,274M against $2,010M; $1,147M against $2,425M)**, so BEP's owner earnings are negative before any capex judgment is made.
BBU is not the capital-intensive class; its D&A includes amortisation of acquired intangibles, so D&A overstates renewal, and the
filer's own maintenance figure ($833-868M) sits far below it; **the band is carried whole, from D&A to the filer's figure, and it
moves BN's share by $587M a year** (the largest single width in the table). *If the capex band changes a verdict, UNKNOWABLE*: it
changes none here, because no (c) end reaches the bond.

**Stock compensation [E5-06, E3-70] - resolves at BAM and at the Corporation; DOES NOT RESOLVE at BIP, BEP, BBU or BPY.** BAM: the
Note 12 total is subtracted (BAM run). The Corporation: the $110M DE add-back is charged; BN's consolidated note shows **$317M of
share-based payment expense before an *"Effect of hedging program"* of $(194)M**, of which BAM's $247M is already inside BAM's
figure, so the remainder is covered. **The four partnership 20-Fs contain no share-based compensation expense line in a text
search** ("share-based", "stock-based", "equity-based compensation"): they are externally managed, their managers are paid in cash
base fees that sit inside operating cash, and the operating companies' own equity plans are not disclosed. **Named, not netted;
the direction is that the leg figures above are overstated by an unknown amount.**

**Distorted years, named [E5-11, E4-41]:** BPY's FY2024 operating cash of +$1,018M includes a +$1,850M working-capital swing, so
its only positive year is a working-capital year; BBU's FY2023 carries $4,686M of disposition gains outside operating cash; BIP's
FY2025 carries a $10,032M acquisition year; BN's FY2024 DE carried the $1,000M related-party gain (excluded here by construction,
because only cash statements are used). **Favourable exogenous breaks:** carry depends on exits in open markets; the conservative
end takes the window's lowest year.

### Great, good, or gruesome? **[E4-20]**
- [x] **great - at BAM**, on BAM's own record (BAM run).
- [x] **good - at BIP**: operating cash above depreciation in every year; capex above operating cash in FY2024 and FY2025.
- [x] **gruesome - at BEP and BPY, on their own cash statements.** BEP spent $6,587M on property, plant and equipment in FY2025
  against $1,147M of operating cash, **5.7 times**, funded by $15,954M of non-recourse borrowings, $3,125M of co-investor capital and
  $6,723M of *"Inflows from related party"*; its operating cash fell in each of the three years while depreciation rose. BPY
  generated negative operating cash in two of three years and paid **$800M** to its redeemable, exchangeable and special LP
  holders and **$1,527M** to its co-investors in FY2025 out of financing. *"requires you to keep adding money at those disappointing
  returns."* **[E4-43]'s scope applied:** capital-hungry growth passes where *"the cash they consume gets to earn a reasonable
  return"*; the filings show the return as fair-value marks, not as cash.
- **At BN as a whole:** IFRS return on common equity 2.37% / 1.13% / 2.66% while the group deploys *"$100 billion into large-scale
  opportunities"* in a half-year. **The gruesome shape, unless the marks are right.**

### Staying power - score all three **[E5-11]**
- **(1) a large and reliable stream of earnings: NO** on owner earnings ($0-1.1bn). The cash BN actually receives is larger and is
  distributions, not earnings: BAM $1,891M, direct investments $876M, operating businesses $1,602M, carry $560M in FY2025, against
  look-through owner earnings of $0-1.1bn. **[E2-60] fires at the legs: restricted earnings are being distributed**, visibly at
  BPY ($800M paid against negative operating cash) and BEP (distributions to unitholders $1,140M against operating cash of $1,147M
  before $6,587M of capex).
- **(2) massive liquid assets: PARTLY.** Core liquidity $5,943M at YE2025 (*"Cash and financial assets, net"* $2,712M, undrawn
  committed facilities $3,231M) and $5,636M at 2026-06-30, against $14,301M of recourse corporate borrowings. **The facilities are
  the kindness of strangers [E5-39]**: without them, $2.7bn. For the insurer, read net worth and reserves, never cash [E2-61]: BWS
  IFRS capital $12.7bn against $191bn of insurance assets; US subsidiaries' capital *"exceeded 300% of their respective Authorized
  Control Levels"*, no numeric ratio filed.
- **(3) no significant near-term cash requirements: NO.** *"The recourse obligations, those amounts that have recourse to the
  Corporation, which are due in less than one year totaled $3.8 billion (2024 – $2.1 billion)"*; unfunded commitments to BAM's
  funds of **$3,950M** ($10,796M committed, $6,846M funded); a **$2.0bn** undrawn equity commitment to BWS; consolidated
  *"Commitments of $9.5 billion (2024 – $6.3 billion)"*; and **$46,648M of property-specific borrowings due inside a year**, *"expected
  to be primarily addressed through refinancings, repayments, and extensions"* (non-recourse to the Corporation, but not to the
  equity BN owns in those assets). The Series 51 and 52 redemption on 2026-11-01 is small (3,320,486 and 1,177,580 shares at C$22.44
  and C$22.00, about C$100M).
- **Score: ONE of three at most (a partial 2).** Leverage named and quantified [E4-16, E3-29]: corporate $14,301M plus $4,090M of
  preferred and $230M of perpetual notes ahead of $43,796M of common equity (YE2025); consolidated *"debt to capitalization ratio of
  50%"*; BBU subsidiary borrowings $42,424M at 7.3%. **The terms are the mitigant [E3-52]:** corporate term debt has *"an average term
  to maturity of 15 years"* and the property and fund debt is non-recourse.
- **Coverage [E2-54]:** interest on corporate borrowings (FFO line) $688M (3-yr mean). Covered **1.3x (3-yr conservative) to 2.6x
  (3-yr judged top)** by look-through owner earnings before corporate interest and preferred dividends; **6.6x** by the FY2025 cash
  distributions and carry actually received ($4,929M against $742M). **The comfortable number is the distribution number, and
  [E2-54]'s test is cash flow "net of ample capital expenditures"; the owner-earnings number is the one that meets that definition.**
- **Jurisdiction [E3-66]:** BN is an Ontario corporation; the circular states *"BWS and New BN are exempted companies existing under
  Bermuda law."* After the combination the common holder sits in a Bermuda company whose half-board is elected by a Class B trust.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism: the internal funding loop runs in reverse.** BN's growth is a loop of commonly controlled entities: BWS's
  policyholder money buys Brookfield-managed assets and Brookfield real estate interests; BAM earns fees and marks those assets;
  the marks lift BWS's capital and BPG's book; BN transfers more assets and shares into BWS at those values. **Exposure, not
  experience [E4-40]:** the loop has not been tested by a year in which real-asset marks and refinancing both break at once.
- **Quantified from filed figures.** BWS holds *"investments in related parties of $ 13.4 billion"* (ex equity method), *"partial
  interests in Brookfield real estate investments totaling $ 6.0 billion"* and $1.0bn of BBU: **$20.4bn of Brookfield-related assets
  against $12.7bn of BWS IFRS capital. A 25% mark-down on those assets is $5.1bn, 40% of BWS's capital**, and BN's $2.0bn equity
  commitment is the first call. **BPY's commercial properties are $54,672M against $23,206M of common equity: a 10% fall is $5.5bn,
  24% of the common equity BN owns there**, on a book that already suspended payment on ~3% of its non-recourse mortgages and faces
  $46.6bn of consolidated property-specific maturities inside a year. **Together, about $10.6bn: 25% of BN's $42.5bn of common equity
  and 12% of the market cap**, before any effect on BAM's fundraising from the same marks.
- **Strongest statement of the opposing case, as its holders would put it [E4-51]:** the recourse debt is $14.3bn with a 15-year
  average term and no 2026 maturity left; everything else is ring-fenced non-recourse; the super core is 95-98% occupied; BAM's
  fee base is 87% long-dated or perpetual; BN has bought back stock through 2025-26 at prices it calls a 40-50% discount; and the
  group raised $98bn and monetized $40bn in H1 2026, which is a loop running forwards, not backwards.
- **Likelihood:** [ ] likely  [x] **a real possibility** that a correlated real-asset and refinancing year impairs a quarter of BN's
  common equity  ·  [x] **a low-level possibility** that the Corporation itself fails to meet recourse obligations, given the terms.

- **VERDICT (recorded, not governing): would be IN on the survival of the Corporation (a low-level possibility of failure, on the
  terms of its recourse debt) and OUT on the economics the survival would preserve: look-through owner earnings of about $0 to
  $1.1bn a year, a nil bottom, gruesome cash shapes at BEP and BPY, staying power one of three, and restricted earnings distributed
  at the legs [E2-60].**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 returned OUT. What follows is arithmetic under the operator-rule-3 heading.

---
## Q5 — COMPUTATION — NOT A CLEARANCE
*No entry language appears below. The price is recorded because the queue's output contract requires one. Q5 did not open.*

**THE FLOOR, before anything else [E4-28].** On the owner-earnings construction above, the honest pre-tax expectancy at $38.22 is
**well below 10%**: the yield on the whole cap is **0.01% to 1.25%** (1.98% at the display ceiling). **Reaching ~10% needs perpetual
growth of about 8.3% to 10.0% a year** on the stream (Gordon arithmetic on the cap less the investments component), which
**[E4-35]** prices as a fewer-than-one-in-twenty event among the best businesses. **Quit on, not ranked.**

**1. THE YIELD.** Owner earnings **$12M to $1,097M** (judged; display ceiling $1,742M) ÷ cap **$87,817M** = **0.01% to 1.25%** ·
sovereign **5.35%** (US Treasury par curve, 30-yr, 2026-09-11, re-struck). **4.1 to 5.3 points BELOW the bond before growth.** On the
cap less the $19.5bn investments component, 0.02% to 1.61%.

**2. WHAT THE PRICE ALREADY ASSUMES.** With the investments component at book, the remaining $68.3bn of cap needs the stream to grow
at **about 3.7% to 5.3% a year forever at the bond rate**, and **8.3% to 10.0% at the floor**. What the business has done: BN's own
DE before realizations per share rose 7% LTM (release), which is not an owner-earnings series; IFRS ROE 1-3%.

**3. WHAT YOU ARE PAID.** At zero growth, **4.1 to 5.3 points below the sovereign.**

**Where certainty is priced [E3-42]:** the bare 5.35%; no premium. Certainty is not re-spent here; it failed at Q2.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** *(the one book: owner earnings against the bond, plus the investments component at
book; a DCF casts no vote)*:
- **At the sovereign, zero growth:** OE capitalised ($0.2bn to $20.5bn) plus investments $19.5bn = **about $9 to $17 a share**
  (display ceiling ~$23).
- **At the ~10% floor, zero growth:** **about $9 to $13 a share.**
- **Cross-check, casting no vote:** the parts at their own marks (BAM, BIP, BEP, BBUC at 2026-09-11 quotes; BWS ex double count,
  BPG and the direct stakes at IFRS book; less the Corporate segment's $(20,172)M) = **$103.2bn, about $45 a share.** BN's own printed
  view of intrinsic value was **$66** (Q1 2026).
- **Current price $38.22** (NYSE close 2026-09-11, Yahoo, aggregator, flagged).

**What the gap means, stated rather than resolved:** the quote sits **between** the owner-earnings construction ($9-17) and the
parts-at-their-marks construction ($45). The difference between them is almost entirely **BAM at its market price ($56.4bn,
against a BAM run that priced BAM's own owner earnings at ~$20-40 a share) and BPG at IFRS book ($26.7bn on a property book that
produced nil operating cash over three years)**. The marks and the cash disagree by a factor of three, and the corpus's measure is the
cash [E2-23].

**WHICH BAR.** [ ] Normal method · [x] **Screamer test [E4-01]:** the price is **above the whole owner-earnings range** at the
sovereign and at the floor → **no**. It is inside the range only if the marks are accepted as value, which is a second book, and
the framework keeps one. **Windage count: ONE** (the conservative end of each leg's (c) band); the common-group CONVENTION is
disclosed with its two alternative keys and is not a windage choice. **No margin was added on top.**

**Deal-shaped facts, read [the ROKU lesson]:** the BN/BWS combination is a one-for-one exchange between two securities that already
carry the same economics (BNT closed $38.19 against BN's $38.22, 0.08% apart); there is no cash offer pinning BN's quote, so **the
quote is an owner-earnings price, not a merger spread.** The Series 51/52 redemption (~C$100M) changes no common count. The
Oaktree consideration included BN shares, issued before the 2026-08-13 count used at Step 0.

- **VERDICT: Q5 did not open (Q2 OUT). Recorded computation: below the floor; not ranked.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? - **RECORDED, NOT GOVERNING**
*Nothing is owned and nothing is armed. These are the conditions under which the Q2 verdict should be reopened, pre-committed in
writing [E1-02].*

**What would prove the Q2 OUT wrong (a reopening requires ALL of the first three, and the fourth):**
1. **Row B reverses:** BWS's life and annuity cost of funds, on a filed whole-business basis, falls **below** Athene's, Corebridge's
   and F&G's for three consecutive years, **with** the spread leading the row **without** the real-asset gains line.
2. **Row A reverses at BN:** BAM's third-party (ex-BWS, ex-affiliate) fee rate rises for three consecutive years while five or more of
   the nine peers' rates fall on the same specification (the BAM run's reversal condition), **and** the share of BAM's gross inflows
   supplied by BN's own insurer falls below a quarter.
3. **The whole-level claim shows up in cash:** look-through owner earnings at BN's share, built as above from the legs' own
   cash-flow statements, exceed the Corporation's interest and preferred dividends by more than 3x on a three-year mean, and BEP's
   and BPY's operating cash exceeds their depreciation in each of those years.
4. **The work orders are pulled:** BIP, BEP and BBUC rows; the non-SEC gateway landlords; EQT, Partners Group, Antin and Tikehau;
   Cameco's 40-F for Westinghouse.

**The monitoring question [E3-30]** for anyone holding it anyway: is the fall in BAM's fee rate and the rise in BWS's cost of funds an
aberrational cycle, or has the group's funding loop slipped in a way that permanently reduces intrinsic value? **Next dated
documents:** Investor Day **2026-09-17** (the whole-business spread and the intrinsic-value figure, both Q3 prompts); the combination
closing *"by year-end"*; the Q3 2026 6-K.

**Position size:** none. No alert band, no PORTFOLIO row: the name failed on the business, and a price alert would be a category error
(the QLYS ruling).

- **VERDICT (recorded): no thesis to monitor; reopening conditions recorded above.**

---
## SELF-AUDIT
*Ticked by the session that resumed and finished the run, 2026-09-13. Qualified ticks say what qualifies them.*

- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 OUT → file closed.** Q3, Q4 and Q6 are written beneath
      RECORDED, NOT GOVERNING banners; Q5 carries the literal heading `COMPUTATION — NOT A CLEARANCE` and no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN (committed before this session) was
      re-read; its one dated error (the Oaktree completion date) is corrected beneath it and does not touch the verdict. The only IN
      written this session is Q3's recorded honesty IN, stated as the absence of found disqualifiers with the scope of the sweep named.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives. **None was issued.** The live place was Q2's moat class,
      where BIP, BEP and BBUC were not rowed and several non-SEC peers were not pulled. **The run states why the class is not
      PROVISIONAL** (the unrowed legs carry 12-16% of the weight and their own parent's filing places them in regulated, contracted or
      highly competitive classes; every unpulled peer is an additional substitute) **and names each document as the work order for a
      reversal.** Had Q2 been heading for IN, those rows would have had to exist first.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known. **None was issued.**
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (corporate borrowings $14,301M across the
      balance sheet, Note 1 and MD&A; net income $3,235M into the DE reconciliation). This session re-struck price and sovereign and
      checked EDGAR for later 6-Ks.
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment. **Qualified:** built by look-through
      from four partnership cash-flow statements plus the BAM run, on two windows (FY2023-25, FY2024-25) and both (c) ends; the
      five-year default cannot be met on one perimeter and is not spliced; **SBC does not resolve at the four partnerships** and the
      direction (overstatement) is stated; the common-group attribution key is a confessed CONVENTION with its two alternatives named.
- [x] Competitor row filled. **Three rows**, one specification each: fee rate (nine managers, imported from the committed BAM run with
      the reason it transfers); cost of funds (four filers with a published rate plus KKR shown and not ranked, every rate re-read in the
      saved filing); occupancy (four US landlords, three years, each from its own 10-K).
- [x] Sovereign is for the earnings currency, from the issuing authority, dated: **USD 5.35%, 2026-09-11, US Treasury par curve**,
      re-struck at the resume. The multi-currency exposure (42% non-USD) was disclosed at Step 0 and does not move any conclusion: no
      Q5 number reaches even the lowest bar available.
- [x] Value stated as a round-number range: ~$9-17 at the sovereign, ~$9-13 at the floor.
- [x] One bar chosen, not both; windage count stated: **screamer test; windage ONE.**
- [x] Prices dated; aggregator used for live quotes only and flagged: $38.22 (BN), $38.19 (BNT), $47.26 (BAM), $36.88 (BIP), $30.39
      (BEP), $26.41 (BBUC), all 2026-09-11 closes, Yahoo, flagged; share count by hand from the filings.
- [x] Run committed to git, **after Q2 (`ca71599`), Q3 (`cd8da9e`) and Q4-Q6 (`09f4445`), each with a pathspec**, and again at the fold.

**Checks not on the template, recorded because this was a resumed run.**
- **The killed session's three draft rows were verified before use, and what was wrong or missing is recorded:** the asset-manager
  draft contained only its BAM subject section (no peer section was ever written; the committed BAM run's row was used instead);
  the annuity-insurer draft's rates for APO, CRBG and FG were re-read in the filing text and were correct, but it presented BN's
  0.55% P&C cost of funds as a leg of the 3.45% effective rate, and **the components do not add**; the real-estate draft had only
  the BPY section, whose figures were re-read and were correct, and the four landlord rows were built here. **No draft line
  presupposed a Q2 outcome** (the drafts were facts-only research files); the brief's warning was checked, not assumed.
- **Found by reading the letter after Q2 was committed:** the Westinghouse moat claim, recorded in an addendum beneath Q2 with its
  weight, rather than edited into the committed section.

## BRIEF ERRORS FOUND *(the brief said to assume at least one)*
1. **The Oaktree completion date.** The brief (and Q1's perimeter table, which the brief summarised) date the close 2026-08-03. BAM's
   8-K Item 2.01 says *"On July 31, 2026"*; 2026-08-03 is the press release. The same 8-K records that **BN shares were part of the
   consideration**, which the brief did not mention; the Step 0 count post-dates the close, so no number changes.
2. **"the peer sections may be incomplete; check"** understated the asset-manager draft: **there were no peer sections at all**, only
   the BAM subject section and the saved 10-K texts.
3. **"eleven 2026 6-K exhibits"**: the folder holds thirteen 2026 6-K exhibit texts (two covers besides). Immaterial; recorded because
   the brief asked for every error.
4. **Not an error in the brief but a standing document the brief did not flag:** `Framework/SECTOR METHOD …` still says BAM and BN
   *"remain blocked"* as *"asset managers with fee streams"*. Both runs have now tested that and found it wrong on the facts for BN
   (a holding company) and wrong in effect for both. This session is forbidden to edit `Framework/`; it is carried to the fold for the
   operator.

## REGISTER
- Verdict: [ ] IN  **[x] OUT (about the business)**  [ ] UNRESEARCHED (about my diligence)  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT - a well-built group of good businesses and not a franchise: BN's own filing concedes competitors may
  have "a lower cost of capital"; its manager-plus-insurer system is filed by Apollo-Athene and KKR-Global Atlantic at larger scale;
  and each leg carrying the weight fails criterion (2) on a filed row (the fee engine mid-pack among nine managers with a falling
  rate; the insurer with the highest life and annuity cost of funds of four writers, its leading spread made by 0.69 points of gains
  on its sponsor's own strategies; the real estate a leader in an office market one-fifth empty). The basis is replaced by the
  filer's own program [E4-04], chosen by people [E4-23], and the audited return on equity is 1-3% [E3-46]. Q3, Q4, Q5 and Q6
  recorded, not governing.**
- **If UNRESEARCHED - THE WORK ORDER:** not applicable. *(Reversal work order, named at Q2 and Q6: BIP, BEP and BBUC rows from their
  20-Fs; EQT, Partners Group, Antin and Tikehau annual reports; British Land, Landsec and the private Toronto and London landlords;
  Cameco's 40-F for Westinghouse.)*
- **If UNKNOWABLE:** not applicable.
- **Price, for the register only (COMPUTATION — NOT A CLEARANCE):** look-through owner earnings about $0 to $1.1bn a year against an
  $87.8bn cap, a 0.01-1.25% yield against a 5.35% sovereign, below the ~10% floor on every construction; about $9-17 a share at the
  sovereign against a $38.22 quote. **The business verdict and the price computation agree.**
