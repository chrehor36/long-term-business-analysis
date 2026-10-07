# D1 — SHARES OUTSTANDING AND CHARTER
## ALPHABET INC. (GOOGL / GOOG) · CIK 0001652044
### Stage 0, transcribed by hand off the covers. Research file for the v4.1 run of 2026-09-06.

**Sentinel check.** Every document transcribed below was confirmed to contain the exact
string "Alphabet Inc." before any figure was taken. Occurrence counts in the extracted
text: FY2025 10-K = 132; Q2-2026 10-Q = 35; Q1-2026 10-Q = 29; DEF 14A 2026 = present
throughout. No wrong-registrant contamination.

---

## 1. THE COVER PAGES — THE UNITS QUESTION SETTLED

### 1a. Q2-2026 Form 10-Q · accession 0001652044-26-000071 · `goog-20260630.htm`

Cover sentence, **verbatim**:

> "As of July 15, 2026, there were 5,868 million shares of Alphabet's Class A stock
> outstanding, 835 million shares of Alphabet's Class B stock outstanding, and 5,527
> million shares of Alphabet's Class C stock outstanding."

### 1b. FY2025 Form 10-K · accession 0001652044-26-000018 · `goog-20251231.htm`

Cover sentence, **verbatim** (the OCR/HTML artifact "wer e" is reproduced as filed and is
not smoothed):

> "As of January 28, 2026 , there wer e 5,822 million shares of Alphabet's Class A stock
> outstanding, 837 million shares of Alphabet's Class B stock outstanding, and 5,438
> million shares of the Alphabet's Class C stock outstanding."

### 1c. **THE UNITS — ANSWERED DIRECTLY**

**The cover states the counts IN MILLIONS, in words, on the face of the document.** The
word "million" is printed in the sentence itself. The cover does *not* give a raw
integer. This is unusual — most registrants print the full integer on the cover — and it
is the trap the share-renderer audit flagged.

**The renderer's "millions" reading of the cover is therefore CORRECT as a transcription
and WRONG as a share count if carried through unconverted.** A tool that reads "5,822"
off this cover and treats it as a share count understates Alphabet by a factor of one
million. The number to carry is **5.822 billion**, not 5,822.

**Unambiguous full-integer counts, converted:**

| Class | Ticker | Q2-2026 10-Q (as of 2026-07-15) | FY2025 10-K (as of 2026-01-28) |
|---|---|---|---|
| Class A | GOOGL | **5,868,000,000** | **5,822,000,000** |
| Class B | *(unlisted)* | **835,000,000** | **837,000,000** |
| Class C | GOOG | **5,527,000,000** | **5,438,000,000** |
| **TOTAL** | | **12,230,000,000** | **12,097,000,000** |

**Independent corroboration that the unit is millions, from a document that DOES print
full integers.** The DEF 14A filed 2026 gives the beneficial-ownership denominator to the
single share:

> "Applicable percentage ownership is based on 5,823,665,113 shares of Class A common
> stock and 835,779,041 shares of Class B common stock outstanding at April 6, 2026."

5,823,665,113 ≈ "5,822 million" at the 10-K date and ≈ "5,868 million" at the 10-Q date.
**The unit is confirmed: billions of shares. Units resolved. IN.**

**Balance-sheet cross-check** (operator rule 4 — one figure checked against the filed
statement, not the cover). Q2-2026 10-Q consolidated balance sheet, verbatim:

> "Class A, Class B, and Class C stock and additional paid-in capital, $ 0.001 par value
> per share: 300,000 shares authorized (Class A 180,000 , Class B 60,000 , Class C 60,000
> ); 12,088 (Class A 5,822 , Class B 837 , Class C 5,429 ) and 12,230 (Class A 5,868 ,
> Class B 835 , Class C 5,527 ) shares issued and outstanding"

The balance sheet is stated in millions and its 12,230 total at 2026-06-30 reconciles to
the cover's 2026-07-15 total exactly. Authorized: 180,000M Class A + 60,000M Class B +
60,000M Class C = 300 billion shares authorized against 12.23 billion outstanding.

**Note the direction of travel.** Total shares went from 12,088M (2025-12-31) to 12,230M
(2026-06-30) — **an increase of 142 million shares, +1.17%, in a single half-year.** The
cause is documented in section 5 below and in D3: Alphabet issued equity in June 2026 and
repurchased nothing. This is a reversal of a decade-long pattern.

---

## 2. ECONOMIC EQUIVALENCE — VERIFIED FROM THE CHARTER, NOT ASSUMED

Source: **Amended and Restated Certificate of Incorporation of Alphabet Inc.**, effective
June 3, 2022 at 4:01 p.m. EDT, filed as **Exhibit 3.01** to the Form 8-K of June 3, 2022,
executed by Sundar Pichai. Corroborated by the **Description of Securities** exhibit
(Exhibit 4.x to the Form 10-K).

### 2a. Class A and Class B dividends — charter Article, Section 2(b), verbatim

> "**Dividends** . Subject to the preferences applicable to any series of Preferred Stock,
> if any, outstanding at any time, the holders of Class A Common Stock and the holders of
> Class B Common Stock shall be entitled to share equally, on a per share basis, in such
> dividends and other distributions of cash, property or shares of stock of the
> Corporation as may be declared by the Board of Directors from time to time with respect
> to the Common Stock out of assets or funds of the Corporation legally available
> therefor; provided, however, that in the event that such dividend is paid in the form of
> shares of Common Stock or rights to acquire Common Stock, the holders of Class A Common
> Stock shall receive Class A Common Stock or rights to acquire Class A Common Stock, as
> the case may be, and the holders of Class B Common Stock shall receive Class B Common
> Stock or rights to acquire Class B Common Stock, as the case may be."

### 2b. **Class C dividends — the question asked. Charter Section 5(b), verbatim**

> "**Dividends** . Subject to the preferences applicable to any series of Preferred Stock,
> if any, outstanding at any time, the holders of Class C Capital Stock shall be entitled
> to receive, on a per share basis, **the same form and amount of dividends and other
> distributions of cash, property or shares of stock of the Corporation** as may be
> declared by the Board of Directors from time to time with respect to shares of the
> Common Stock out of assets or funds of the Corporation legally available therefor;
> provided , however , that in the event that such dividend is paid in the form of shares
> of Common Stock or rights to acquire Common Stock, the holders of Class C Capital Stock
> shall receive Class C Capital Stock or rights to acquire Class C Capital Stock, as the
> case may be."

**ANSWER: YES. Class C (non-voting, GOOG) receives the same form and the same amount of
dividends as Class A and Class B, per share, as a matter of charter right — not board
discretion.** This is confirmed in practice: the FY2025 10-K states the quarterly dividend
is declared "per share of outstanding Class A, Class B, and Class C shares," and the
Q2-2026 10-Q reports dividends actually paid on all three classes (see D3).

### 2c. The stock-dividend "like class" provision

Present in **all three** sections quoted above. A dividend paid in stock is paid in the
recipient's own class: Class A holders get Class A, Class B holders get Class B, Class C
holders get Class C. **This is the mechanism that preserved the founders' voting control
through the July 2022 20-for-1 split** — the split was executed as a stock dividend, so
Class B holders received Class B and the 10:1 voting ratio was untouched.

### 2d. Liquidation — charter Sections 2(c) and 5(c), verbatim

Class A / Class B:
> "**Liquidation** . Subject to the preferences applicable to any series of Preferred
> Stock, if any outstanding at any time, in the event of the voluntary or involuntary
> liquidation, dissolution, distribution of assets or winding up of the Corporation, the
> holders of Class A Common Stock and the holders of Class B Common Stock shall be
> entitled to share equally, on a per share basis, all assets of the Corporation of
> whatever kind available for distribution to the holders of Common Stock."

Class C — reached by an automatic conversion, not by a parallel entitlement:
> "**Conversion upon Liquidation** . Immediately prior to the earlier of (i) any
> distribution of assets of the Corporation to the holders of the Common Stock in
> connection with a voluntary or involuntary liquidation, dissolution, distribution of
> assets or winding up of the Corporation pursuant to Section 2(c) or (ii) any record date
> established to determine the holders of capital stock of the Corporation entitled to
> receive such distribution of assets, each outstanding share of the Class C Capital Stock
> shall automatically, without any further action, convert into and become one (1) fully
> paid and nonassessable share of Class A Common Stock."

**Effect: identical.** Class C becomes Class A one-for-one immediately before any
liquidating distribution, so it participates on exactly the same per-share footing.

### 2e. Anti-dilution — subdivisions must be uniform

Section 2(d): *"If the Corporation in any manner subdivides or combines the outstanding
shares of one class of Common Stock, the outstanding shares of the other class of Common
Stock will be subdivided or combined in the same manner."*

Section 5(d): *"…the outstanding shares of the Class C Capital Stock will be subdivided or
combined in the same manner. The Corporation shall not subdivide or combine the
outstanding shares of the Class C Capital Stock unless a subdivision or combination is
made in the same manner with respect to each class of Common Stock."*

### 2f. The company's own summary of equivalence — FY2014 10-K, verbatim

> "The rights, including the liquidation and dividend rights, of the holders of our Class A
> and Class B common stock and Class C capital stock are identical, except with respect to
> voting. Further, there are a number of safeguards built into our certificate of
> incorporation, as well as Delaware law, which preclude our board of directors from
> declaring or paying unequal per share dividends on our Class A and Class B common stock
> and Class C capital stock. … As the liquidation and dividend rights are identical, the
> undistributed earnings are allocated on a proportionate basis. The net income per share
> amounts are the same for Class A and Class B common stock and Class C capital stock
> because the holders of each class are legally entitled to equal per share distributions
> whether through dividends or in liquidation."

And in the FY2014 note on the Class C creation:
> "Except as expressly provided in the New Charter, shares of Class C capital stock have
> the same rights and privileges and rank equally, share ratably and are identical in all
> other respects to the shares of Class A common stock and Class B common stock as to all
> matters including dividend and distribution rights."

### 2g. **VERDICT ON ECONOMIC EQUIVALENCE**

**IN. All three classes are economically identical per share** — same dividend
entitlement in form and amount, same participation in distributions, same effective
liquidation participation, same subdivision treatment, same EPS. **The ONLY difference is
voting**: Class A = 1 vote, Class B = 10 votes, Class C = 0 votes.

**Consequence for the run: it is correct to value Alphabet on the TOTAL of all three
classes (12.23 billion shares at 2026-07-15), and it is correct to apply a single
per-share price across classes for market cap.** No class-mix adjustment is required. The
economics do not split; only the control does.

### 2h. Conversion features

| Direction | Charter treatment |
|---|---|
| **Class B → Class A** | Convertible at any time at holder's option, **one-for-one**, on written notice to the transfer agent. **Automatic** on any transfer except certain permitted transfers. |
| **Class B on death of holder** | Automatic conversion to Class A of the decedent's shares and those of his permitted entities. Larry or Sergey may transfer voting control to the other on death without triggering conversion, **but those shares convert to Class A nine months after the death of the transferring founder.** |
| **Class B once converted** | *"Once transferred and converted into shares of Class A Common Stock, shares of Class B Common Stock shall not be reissued."* — Class B is a **strictly shrinking class**. |
| **Class A → anything** | *"Shares of Class A Common Stock are not convertible into any other shares of our capital stock."* |
| **Class C → anything** | *"Other than in connection with a liquidation as described above, shares of Class C Capital Stock are not convertible into any other shares of our capital stock."* |

**The nine-month clock is the single most important governance fact in this file.** Class
B cannot be replenished. On the death of both founders (plus nine months), the entire
Class B block converts to Class A and Alphabet becomes a one-share-one-vote company with a
large non-voting Class C float. The dual-class structure has a biological expiry date.

### 2i. The Class C Undertaking — a live 15% trigger

From the Description of Securities, the terms of the 2015 Class C Undertaking (binding
Alphabet to the 2013 *In Re: Google Inc. Class C Shareholder Litigation* settlement)
require the company to:

> "(iv) when the aggregate voting power of Larry and Sergey falls below 15% of the
> cumulative voting power of all our shareholders, have our Board of Directors consider in
> good faith whether it is no longer in our best interests to maintain a class of nonvoting
> stock and, if it so determines, take steps to cause the Class C Capital Stock to convert
> into Class A Common Stock."

Also binding: amendments or waivers of the founders' Transfer Restriction Agreements must
be recommended by a committee of two or more independent directors who hold no Class B,
then approved by every board member excluding Larry and Sergey, and **publicly disclosed
on Form 8-K/10-Q/10-K at least 30 days before taking effect.**

**Transfer Restriction Agreements — the B:C ratchet.** Larry, Sergey and Eric Schmidt may
not sell Class C such that they would then hold more Class B than Class C; if they do, the
excess Class B **automatically converts** to Class A to restore parity. The structure
forces the founders to bleed voting stock in step with economic stock.

---

## 3. THE 2014 CLASS C DISTRIBUTION AND THE 2022 20-FOR-1 SPLIT

### 3a. The 2014 Class C distribution ("the Stock Split") — FY2014 10-K, verbatim

> "In April 2012, our board of directors approved amendments to our certificate of
> incorporation that created a new class of non-voting capital stock (Class C capital
> stock). The amendments authorized 3 billion shares of Class C capital stock and also
> increased the authorized shares of Class A common stock from 6 billion to 9 billion .
> The amendments are reflected in our Fourth Amended and Restated Certificate of
> Incorporation (New Charter), the adoption of which was approved by stockholders at our
> 2012 Annual Meeting of Stockholders held on June 21, 2012. **In January 2014, our board
> of directors approved a distribution of shares of the Class C capital stock as a dividend
> to our holders of Class A and Class B common stock (the Stock Split). The Stock Split had
> a record date of March 27, 2014 and a payment date of April 2, 2014.**"

Mechanics: **one share of Class C for each share of Class A and each share of Class B
outstanding on the record date** — an effective 2-for-1 split in which the new half
carries no vote. Class C began trading on NASDAQ **April 3, 2014**.

**Retroactive adjustment confirmed**, verbatim: *"Share and per share amounts disclosed as
of December 31, 2014 and for all other comparative periods have been retroactively
adjusted to reflect the effects of the Stock Split."*

**The litigation settlement and the Possible Adjustment Payment.** The Delaware Court of
Chancery approved a settlement on 2013-10-28, with Order and Final Judgment 2013-11-06,
in *In Re: Google Inc. Class C Shareholder Litigation*, Civil Action No. 7469-CS. Under
it Google could owe holders of Class C a make-whole if Class C traded below Class A on a
VWAP basis over the 365 days from first trade. FY2014 10-K, verbatim:

> "Had we been obligated to make a payment based on the Volume Weighted Average Price
> (VWAP) of the Class A and Class C shares from April 3, 2014 through December 31, 2014,
> the monetary value of the Possible Adjustment Payment would have been approximately $593
> million as of December 31, 2014."

*This is the market's own valuation of the vote: roughly $593 million of measured Class C
discount over nine months. The vote was worth something, and the company had contracted to
pay for it.*

### 3b. The July 2022 20-for-1 split — FY2022 10-K Note 11, verbatim

> "**Stock Split Effected in the Form of a Stock Dividend ("Stock Split")** — On February
> 1, 2022, the company announced that the Board of Directors had approved and declared a
> 20 -for-one stock split in the form of a one-time special stock dividend on each share of
> the company's Class A, Class B, and Class C stock. The Stock Split had a record date of
> July 1, 2022 and an effective date of July 15, 2022. The par value per share of our Class
> A, Class B, and Class C stock remains unchanged at $ 0.001 per share after the Stock
> Split. **All prior period references made to share or per share amounts in the
> accompanying consolidated financial statements and applicable disclosures prior to the
> effective date have been retroactively adjusted to reflect the effects of the Stock
> Split.**"

| | |
|---|---|
| Announced | 2022-02-01 |
| Ratio | 20-for-1 |
| Mechanism | one-time special **stock dividend** (each holder receives 19 additional shares of **their own class**) |
| Record date | 2022-07-01 |
| Effective date | 2022-07-15 |
| Par value | unchanged at $0.001 |
| Prior periods | **retroactively adjusted — confirmed in three separate places in the FY2022 10-K** (MD&A, Note 1, Note 11) |

**Retroactive adjustment confirmed for both events.** All FY2015–FY2025 share and
per-share figures as they appear in the *current* filings are already on a post-2022,
post-2014 basis. Figures taken from *original* FY2015–FY2021 filings are NOT, and must be
divided by 20 to compare. This is the split-invariance discipline the CLAUDE.md market-cap
rule exists to enforce.

---

## 4. FOUNDER VOTING CONTROL

### 4a. The proxy table — DEF 14A for the 2026 Annual Meeting, as of the April 6, 2026 Record Date

Denominator, verbatim: *"Applicable percentage ownership is based on 5,823,665,113 shares
of Class A common stock and 835,779,041 shares of Class B common stock outstanding at
April 6, 2026."* Non-voting Class C is excluded from the table.

| Beneficial owner | Class A shares | Class A % | Class B shares | Class B % | **Total voting power %** |
|---|---|---|---|---|---|
| **Larry Page** | — | — | **389,051,160** | 46.5 | **27.4** |
| **Sergey Brin** (1) | 37,469 | * | **358,939,978** | 42.9 | **25.3** |
| Sundar Pichai | 227,560 | * | — | — | * |
| Anat Ashkenazi (CFO) | — | — | — | — | — |
| Ruth M. Porat | 28,060 | * | — | — | * |
| Philipp Schindler | — | — | — | — | — |
| Kent Walker | — | — | — | — | — |
| L. John Doerr | 472,165 | * | 22,348,940 | 2.7 | 1.6 |
| K. Ram Shriram | 1,811,108 | * | — | — | * |
| John L. Hennessy | 20,624 | * | — | — | * |
| Frances H. Arnold | — | — | — | — | — |
| R. Martin "Marty" Chávez | — | — | — | — | — |
| Roger W. Ferguson Jr. | — | — | — | — | — |
| Robin L. Washington | — | — | — | — | — |
| **All officers and directors (14 persons)** | 2,596,986 | * | **770,340,078** | **92.2** | **54.3** |
| BlackRock, Inc. | 356,934,964 | 6.1 | — | — | 2.5 |

(1) Brin's Class B is held via SMB Pacific 2021 Charitable Remainder Unitrust I and II
(172,700 shares each **before** the 2022 split adjustment as printed in the footnote),
of which he is sole trustee.

### **PAGE + BRIN = 27.4% + 25.3% = 52.7% OF TOTAL VOTING POWER.**

**The board and officers as a group hold 54.3%.** Alphabet is a **controlled company by
arithmetic**: two men who hold no executive office can carry any shareholder vote alone.

The proxy's own footnote on the mechanism, verbatim:

> "Percentage total voting power represents voting power with respect to all shares of our
> Class A common stock and Class B common stock, voting together as a single class. Each
> holder of Class B common stock is entitled to ten (10) votes per share of Class B common
> stock, and each holder of Class A common stock is entitled to one (1) vote per share of
> Class A common stock on all matters submitted to our shareholders for a vote. … The Class
> B common stock is convertible at any time by the holder into shares of Class A common
> stock on a share-for-share basis upon written notice to the transfer agent."

And on Class C, verbatim: *"Holders of Class C capital stock have no voting power as to any
items of business that will be voted on at our Annual Meeting."*

### 4b. **A shareholder proposal states the case against the structure** — 2026 proxy, verbatim

> "In Alphabet's multi-class voting structure, Class B stock has 10 times the voting rights
> of Class A. As a result, Mr. Page and Mr. Brin currently control 52% of our company's
> total voting power while owning less than 11% of outstanding voting stock 1 , and will
> continue to retain voting control even though they have stepped down from leading the
> company."

The board **recommends a vote AGAINST** this proposal, as it does against every shareholder
proposal on the 2026 ballot.

### 4c. **The risk factor — FY2025 10-K, verbatim**

The 10-K states the founders hold *"outstanding Class B stock, which represented
approximately 52.7% of the voting power of our outstanding common stock,"* and continues:

> "Through their stock ownership, Larry and Sergey have significant influence over all
> matters requiring stockholder approval, including the election of directors and
> significant corporate transactions, such as a merger or other sale of our company or our
> assets, for the foreseeable future. In addition, because our Class C stock carries no
> voting rights (except as required by applicable law), the issuance of the Class C stock,
> including in future stock-based acquisition transactions and to fund employee equity
> incentive programs, **could continue Larry and Sergey's current relative voting power and
> their ability to elect all of our directors and to determine the outcome of most matters
> submitted to a vote of our stockholders. The share repurchases made pursuant to our
> repurchase program may also affect Larry and Sergey's relative voting power.** This
> concentrated control limits or severely restricts other stockholders' ability to
> influence corporate matters and we may take actions that some of our stockholders do not
> view as beneficial, which could reduce the market price of our Class A stock and our
> Class C stock."

**Read that sentence carefully.** The company states in its own risk factors that the
existence of the non-voting Class C, and the buyback program itself, are instruments that
*maintain* founder voting power. Issuing Class C for acquisitions and employee comp
dilutes economics without diluting control. Repurchasing Class A shrinks the denominator
of the vote. **The capital structure is a control-preservation machine that also happens
to be a capital-allocation machine.** For Q3 (honesty and rationality) this is the fact to
weigh: the disclosure is candid to the point of bluntness, which counts in Alphabet's
favour, while the structure it describes is one Buffett's own writing on the shareholder
franchise would not admire.

Delaware backstop, also disclosed: *"Under Delaware law, a corporation may not engage in a
business combination with any holder of 15% or more of its outstanding voting stock unless
the holder has held the stock for three years or, among other things, the Board of
Directors has approved the transaction. Our Board of Directors could rely on Delaware law
to prevent or delay an acquisition of us."*

---

## 5. **NEW IN JUNE 2026 — THE CAPITAL STRUCTURE CHANGED. FLAG FOR Q3/Q4/Q5.**

The Q2-2026 10-Q (accession 0001652044-26-000071), Note 11 "Stockholders' Equity",
discloses four transactions completed within four days of each other in June 2026. Any
run using a pre-June-2026 mental model of Alphabet's balance sheet is stale.

### 5a. Common stock public offering — 2026-06-04, verbatim

> "On June 4, 2026, the company completed an underwritten public offering of 29 million
> Class A shares at a price of $ 355.1982 per share and 29 million Class C shares at a
> price of $ 351.8018 per share. All shares have a par value of $ 0.001 per share."

### 5b. **PRIVATE PLACEMENT TO BERKSHIRE HATHAWAY — 2026-06-04, verbatim**

> "Concurrently with the public offering, on June 4, 2026, the company completed a private
> placement of 14 million Class A and 14 million Class C shares to **an affiliate of
> Berkshire Hathaway Inc.** (the "private placement"). The shares were issued in a private
> placement pursuant to an exemption from registration under section 4(a)(2) of the
> Securities Act of 1933, as amended."

> "The net proceeds received by the company were $ 20.5 billion from the public offering
> and **$ 10.0 billion from the private placement**, after deducting underwriting
> discounts, commissions, and direct offering expenses which were recorded as a reduction
> to common stock and APIC. These proceeds will be used for general corporate purposes,
> including capital expenditures to scale AI infrastructure and global compute."

**Berkshire Hathaway is a direct, primary-issuance holder of Alphabet as of 2026-06-04, to
the tune of $10.0 billion for 28 million shares (14M Class A + 14M Class C).** Note this
is a *primary* placement — Berkshire bought newly issued stock from the company, not
shares in the market. Berkshire does **not** appear in the 2026 proxy's >5% holder table
(record date 2026-04-06, which predates the placement); 28 million shares against 12.23
billion outstanding is ~0.23%, far below 5%, so no proxy listing would be expected. See
D2 §15.

*Analyst's note under operator rule 9: the framework's own corpus is Buffett and Munger.
The fact that Berkshire took a $10bn primary position is evidence about the security, but
it is exactly the kind of fact that invites the analyst to stop thinking. It is not a
substitute for Q1–Q4. It must not be used as one.*

### 5c. Mandatory convertible preferred stock — 2026-06-05, verbatim

> "On June 5, 2026, the company issued an aggregate amount of 385 million Series A and
> Series B depositary shares, representing 19 million shares of 6.25 % Mandatory
> Convertible Preferred Stock, split evenly into Series A (indexed to Class A stock) and
> Series B (indexed to Class C stock). Each depositary share represents a 1/20th fractional
> interest in a share of preferred stock."

> "The mandatory convertible preferred stock has a par value of $ 0.001 per share and
> liquidation preference of $ 1,000 per share ($ 50 per depositary share). **Aggregate net
> proceeds were $ 19.0 billion** which will be used for general corporate purposes,
> including capital expenditures to scale AI infrastructure and global compute."

> "Dividends are cumulative at an annual rate of 6.25 % on the liquidation preference of $
> 1,000 per share of mandatory convertible preferred stock and may be paid in cash, shares
> of common stock, or a combination of cash and shares of common stock, at the company's
> election. Dividends that are declared will be payable quarterly on February 15, May 15,
> August 15, and November 15 of each year, commencing on August 15, 2026 and ending on, and
> including May 15, 2029 with the record date being the first of the respective month."

> "Unless earlier converted, each outstanding share will automatically convert on the
> mandatory conversion date, which is on or about May 15, 2029. **The conversion rate for
> each share of our Series A mandatory convertible preferred stock will be between 2.2520
> and 2.8160 shares of Class A stock, and Series B mandatory convertible preferred stock
> will convert into between 2.2740 and 2.8420 shares of Class C stock**, depending on the
> applicable market value of our Class A and Class C stock upon conversion and subject to
> certain anti-dilution adjustments. The applicable market value will be determined based
> on the average volume-weighted average price per share over the 20 consecutive trading
> day final averaging period ending immediately prior to the mandatory conversion date."

> "The mandatory convertible preferred stock is not redeemable at the company's election
> before the mandatory conversion date. **Holders of the mandatory convertible preferred
> stock will not have any voting rights**, with limited exceptions."

Balance-sheet line, Q2-2026, verbatim: *"Series A and Series B preferred stock and
additional paid-in capital, $ 0.001 par value per share, 100 shares authorized; 6.25 %
mandatory convertible preferred stock, 0 and 19 shares issued and outstanding allocated
equally between each series with a liquidation preference of $ 1,000 per share"* — i.e.
zero at 2025-12-31, 19 million shares at 2026-06-30.

**Dilution arithmetic to carry into Q5.** 19 million preferred shares × between 2.252 and
2.842 common shares each = **between 42.8 million and 54.0 million additional common
shares by May 2029**, plus a cumulative 6.25% dividend (≈ $1.19 billion a year on a
$19 billion liquidation preference) which ranks ahead of the common dividend and is
deducted from net income available to common. The 10-Q confirms the mechanism: *"Net
income available to common stockholders is calculated by adjusting net income to deduct
accumulated and declared dividends on the mandatory convertible preferred stock."*

### 5d. Capped calls — verbatim

> "In connection with the issuance of the 385 million Series A and Series B depositary
> shares, representing 19 million shares of mandatory convertible preferred stock, the
> company entered into privately negotiated capped call transactions with certain
> financial institutions."

> "The company paid an aggregate premium of $ 1.0 billion for these capped call
> transactions, which was recorded as a reduction to preferred stock and APIC. The capped
> call transactions provide the company with the option to receive shares of Class A and
> Class C stock upon conversion of the mandatory convertible preferred stock. The
> transactions have an initial cap price of $ 532.6704 per share for the Class A and $
> 527.7974 per share for Class C, each representing a premium of 50.0 % over their
> respective public offering prices."

> "These transactions are intended to reduce the potential dilution to the company's common
> stock upon conversion of the mandatory convertible preferred stock. As the transactions
> are indexed to the company's own stock and meet certain accounting criteria, the capped
> call options are recorded as a reduction of stockholders' equity and are not accounted
> for as derivatives."

**$1.0 billion of real cash spent to buy back part of the dilution the company had just
sold.** The economic reference prices are useful: public offering priced at $355.1982
(Class A) / $351.8018 (Class C) on 2026-06-04, and the cap is 50% above that.

### 5e. **$40 BILLION AT-THE-MARKET EQUITY PROGRAM — 2026-06-01, verbatim**

> "On June 1, 2026, the company entered into an equity distribution agreement with certain
> sales agents party thereto, pursuant to which we may sell both our Class A and Class C
> stock having aggregate sales proceeds of up to $ 40.0 billion from time to time through
> an at-the-market offering program (the "ATM Program")."

> "Subject to the terms and conditions of the agreement, the company may sell shares of
> Class A and Class C stock through the sales agents listed in the agreement in amounts and
> at times to be determined by the company. In addition, we may elect to sell, through the
> sales agents or through others (whether acting as agent or principal), shares of our
> stock for forward settlement. We are not obligated to sell any of our shares under the
> ATM Program."

> "**The proceeds from offerings under the ATM Program, if any, are primarily intended to be
> used to meet tax obligations associated with employee equity grants.** As of June 30,
> 2026, we have not sold any shares under the ATM Program, and the full $ 40.0 billion
> remains available for future issuance."

**This sentence deserves a hard look at Q3.** A $40 billion authorised share-issuance
program whose stated primary purpose is *funding the tax bill on employee stock
compensation.* Historically Alphabet funded that by withholding shares and paying the
taxing authorities in cash from operations (see D3 §8). An ATM sized at $40 billion says
management would rather issue equity than spend cash to settle SBC taxes. Nothing has been
drawn yet — but the authority exists and it is the single largest standing dilution
authority in the file.

### 5f. Total June-2026 capital raised

| Instrument | Date | Net proceeds |
|---|---|---|
| Common stock public offering (29M A + 29M C) | 2026-06-04 | $20.5bn |
| Private placement to Berkshire affiliate (14M A + 14M C) | 2026-06-04 | $10.0bn |
| 6.25% mandatory convertible preferred (19M shares) | 2026-06-05 | $19.0bn |
| **Total raised** | | **$49.5bn** |
| *less* capped call premium paid | 2026-06 | *($1.0bn)* |
| **Net** | | **$48.5bn** |
| ATM authority created, undrawn | 2026-06-01 | *$40.0bn available* |

Long-term debt also moved: total outstanding long-term debt carrying value went from
$48.5bn at 2025-12-31 (senior unsecured notes) to **$98.2 billion at 2026-06-30**, with
notes fair value rising from ~$45.6bn to ~$94.9bn. Alphabet also drew $1.3bn on credit
facilities (SOFR + 1.5%–2.25%), against $11.7bn of facilities expiring through April 2030,
having had **no** facility borrowings at 2025-12-31.

**Summary of the change in one line: in a single month Alphabet raised roughly $48.5
billion of equity and equity-linked capital, roughly doubled its long-term debt, drew on
its revolver for the first time, created a $40 billion ATM authority, and stopped buying
back stock — all stated to be for "capital expenditures to scale AI infrastructure and
global compute."** That is the Q4 survival question and the Q1 owner-earnings question
arriving together. It is documented further in D3.

---

## SOURCES — ACCESSION REGISTER FOR D1

| Document | Accession | Primary file | Used for |
|---|---|---|---|
| FY2025 Form 10-K | 0001652044-26-000018 | `goog-20251231.htm` | cover counts, risk factor, balance sheet |
| Q2-2026 Form 10-Q | 0001652044-26-000071 | `goog-20260630.htm` | cover counts, Note 11 stockholders' equity |
| Q1-2026 Form 10-Q | 0001652044-26-000048 | `goog-20260331.htm` | sentinel confirmed |
| FY2022 Form 10-K | 0001652044-23-000016 | `goog-20221231.htm` | 20-for-1 split, Note 1 / Note 11 |
| FY2014 Form 10-K (Google Inc.) | — | FY2014 annual report | Class C distribution, equivalence language |
| Amended & Restated Certificate of Incorporation | filed as Ex-3.01 to 8-K of 2022-06-03 | `d294315dex301.htm` | charter Sections 2 and 5 |
| Description of Securities | Ex-4.x to Form 10-K | — | dividends, liquidation, conversion, Class C Undertaking |
| DEF 14A, 2026 Annual Meeting | — | record date 2026-04-06 | beneficial ownership, voting power |

Base path: `https://www.sec.gov/Archives/edgar/data/1652044/<accession-no-dashes>/<doc>`

---
*D1 complete. Written 2026-09-06.*
