# AAPL — Q3 DISCLOSURE FLAGS (Task 1)
Research file. Gathered 2026-09-06. CIK 0000320193.
Method: full HTML of the primary document downloaded from SEC EDGAR, tag-stripped to text,
case-insensitive literal count. Counts are of the FILED document only, not of exhibits
unless named.

## SOURCES USED (all FILED, all primary)
| doc | accession | file | date |
|---|---|---|---|
| FY2025 10-K (FYE 2025-09-27) | 0000320193-25-000079 | aapl-20250927.htm | filed 2025-10-31 |
| DEF 14A (2026 annual meeting) | 0001308179-26-000008 | aapl014016-def14a.htm | filed 2026-01-08 |
| Q3 FY2026 10-Q (period 2026-06-27) | 0000320193-26-000020 | aapl-20260627.htm | — |
| 8-K Q4 FY2025 earnings, EX-99.1 | 0000320193-25-000077 | a8-kex991q4202509272025.htm | 2025-10-30 |
| 8-K/A CEO transition | 0001140361-26-035325 | ef20081427_8ka.htm | filed 2026-09-01 |
| NT 10-K (option backdating) | 0001104659-06-081617 | a06-25759_1nt10k.htm | 2006-12-15 |

---

## 1A. TERM COUNTS

### FY2025 10-K (aapl-20250927.htm)
| term | count | verdict |
|---|---|---|
| EBITDA | **0** | — |
| non-GAAP | **0** | — |
| pro forma | **0** | — |
| restructuring | **0** | — |
| except for | **0** | — |
| consecutive | **0** | — |
| adjusted | **3** | all three INCIDENTAL — see below |

The three "adjusted" hits in the 10-K:
1. Income-tax note: *"Reserves are **adjusted** considering changing facts and circumstances,
   such as the closing of a tax examination."* — accounting mechanics, not a measure.
2. and 3. The securities table column header **"Adjusted Cost"** (FY2025 and FY2024 columns)
   in the Financial Instruments note. This is the ASC 320 amortized-cost basis. It is a GAAP
   label, not a management-defined measure.

**Result: the FY2025 10-K contains ZERO management-defined non-GAAP measures.** There is no
"adjusted EBITDA", no "adjusted EPS", no "organic growth", no "constant currency" headline in
the 10-K. Same clean sheet as GRMN.

### DEF 14A filed 2026-01-08
| term | count | verdict |
|---|---|---|
| EBITDA | **0** | — |
| non-GAAP | **0** | — |
| pro forma | **0** | — |
| restructuring | **0** | — |
| consecutive | **0** | — |
| adjusted | **3** | all INCIDENTAL |
| except for | **2** | both INCIDENTAL — and one is a POSITIVE governance fact |

The two "except for" hits are both in the Director Plan text, and the first is the anti-repricing
covenant, which cuts in Apple's favour:
> *"**No Repricing** — No adjustment may be made to the plan or any stock option under the
> Director Plan (by amendment, substitution, cancellation and regrant, exchange, or other means)
> that would constitute a repricing of the per-share exercise price of the option **except for**
> an adjustment to reflect a stock split or similar event provided in the Director Plan or any
> repricing that might be approved by shareholders."*

The three "adjusted" hits: (i) deferred-comp account balances "as adjusted for applicable
earnings gains and losses and fees"; (ii) historical director grants "with the number of shares
adjusted for stock splits"; (iii) Dividend Equivalent Rights on RSUs "as such total number may
be adjusted pursuant to Section 7". All mechanical.

**A notable absence: the proxy contains no "adjusted" performance metric because the annual
bonus runs on straight GAAP.** See `q3_proxy_pay.md`.

---

## 1B. THE ONE RUNG OUT — THE 8-K EARNINGS RELEASE

This is where the promotional layer lives, and it is worth stating precisely because it is
NARROW.

**8-K EX-99.1, Q4 FY2025 (filed 2025-10-30):**
| term | count |
|---|---|
| EBITDA | **0** |
| non-GAAP | **12** |
| adjusted | **3** |
| pro forma / restructuring / except for / consecutive | **0** |
| "record" | 7 (5 promotional, 1 "shareholders of record", 1 "recorded a charge") |

The promotional layer is real but thin. Headline and subheads:
> *"Apple reports fourth quarter results — September quarter records for total company revenue,
> iPhone revenue and EPS. Services revenue reaches new all-time high."*
> *"Diluted earnings per share was $1.85, up 13 percent year over year **on an adjusted basis**."*

**What the non-GAAP measure actually is.** ONE adjustment, to the PRIOR-year comparative only:
> *"(b) Non-GAAP adjustments to provision for income taxes and net income to reflect the impact
> of the reversal of the European General Court's State Aid decision recognized during the fourth
> quarter of 2024. On September 10, 2024, the European Court of Justice announced that it had set
> aside the 2020 judgment of the European General Court and confirmed the European Commission's
> 2016 State Aid decision. As a result, during the fourth quarter of 2024 the Company recorded a
> one-time income tax charge of **$10.2 billion, net**, which represented **$15.8 billion payable
> to Ireland** via release of restricted funds held in escrow, partially offset by a U.S. foreign
> tax credit of **$4.8 billion** and a decrease in unrecognized tax benefits of **$823 million**."*

Full reconciliation table is printed in the release. FY2024 as reported: net income $93,736m,
diluted EPS $6.08. As adjusted: $103,982m, $6.75. FY2025 (the current year) is presented
**GAAP-only — no adjustments at all.**

**Verdict on the ER layer.** Apple does not run its earnings release on adjusted measures. It
made one back-adjustment, to a genuine one-time legally-imposed tax charge, in the prior-year
comparative, and disclosed the full bridge. This is materially cleaner than the WMT pattern (a
standing adjusted layer in the ER that the 10-K does not use). Apple's promotional content is
the word "record" applied to GAAP revenue, which is verifiable.

**Caution flag, not a violation:** the headline number the reader takes away ("EPS up 13 percent")
is the non-GAAP comparison. On straight GAAP the FY2025 Q4 EPS growth is much larger (vs $0.97),
so the adjustment made the growth rate look SMALLER, not larger. The adjustment runs against
management's promotional interest. That is the honest direction.

---

## 1C. AUDITOR

> *"/s/ Ernst & Young LLP — **We have served as the Company's auditor since 2009.** San Jose,
> California, October 31, 2025"*

- **Ernst & Young LLP, PCAOB ID 42, San Jose CA. 17 consecutive years (2009–2025).**
- Predecessor was KPMG (dismissed 2009).
- Two opinions issued: financial statements AND internal control over financial reporting
  (ICFR). Both **unqualified**. Section 404(b) attestation box on the cover is checked.
- **One Critical Audit Matter: uncertain tax positions** (Note 7). The CAM is the only one and
  it is the expected one for a company with Apple's cross-border structure.

## 1D. RESTATEMENTS

**Current:** none. The FY2025 10-K cover-page error-correction box is **UNCHECKED**:
> *"...indicate by check mark whether the financial statements of the registrant included in the
> filing reflect the correction of an error to previously issued financial statements. ☐"*

And the clawback box is also unchecked:
> *"...whether any of those error corrections are restatements that required a recovery analysis
> of incentive-based compensation received by any of the registrant's executive officers during
> the relevant recovery period pursuant to §240.10D-1(b). ☐"*

**Filing history — full amendment scan of the EDGAR submissions JSON (all filings, both pages):**
- **10-K/A: ONE, filed 2010-01-25** (accession 0001193125-10-012091). Retrospective adoption of
  the new software/multiple-element revenue guidance — NOT an error correction.
- **10-Q/A: ONE, filed 2009-04-27** (0001193125-09-087629).
- **NT 10-K: ONE, 2006-12-15.** This is the real one. Verbatim from the filing:
  > *"On October 4, 2006, Apple Computer, Inc. announced that the special committee of its board
  > of directors had reported its findings after a three month investigation into Apple's
  > historical stock option practices. Apple initiated this voluntary independent investigation
  > after a management review discovered irregularities in past stock option grants. ... management
  > has concluded, and the audit committee agrees, that **Apple will need to restate its historical
  > financial statements to record non-cash charges for compensation expense relating to past stock
  > option grants.**"*
  Signed: Peter Oppenheimer, CFO.
- **NT 10-Q: ONE, 2006-08-11** (same matter).
- No 10-K/A, 10-Q/A or NT filing of any kind since 2010. **Sixteen clean years.**

**Judgment note for the run:** the 2006 backdating restatement is a genuine honesty event, but
it is 20 years old, was self-initiated ("voluntary independent investigation ... after a
management review discovered irregularities"), and no member of the implicated management team
remains. Cook became CEO in 2011. Record this as historical, not live.

## 1E. SHARE CLASS STRUCTURE

**SINGLE CLASS. NO super-voting stock. NO dual-class.** From the FY2025 10-K cover:
> *"Common Stock, $0.00001 par value per share — AAPL — The Nasdaq Stock Market LLC"*
> *"**14,776,353,000 shares of common stock were issued and outstanding as of October 17, 2025.**"*

The only other registered securities are seven series of listed notes (0.000% 2025, 1.625% 2026,
2.000% 2027, 1.375% 2029, 3.050% 2029, 0.500% 2031, 3.600% 2042) — Nasdaq-listed euro/foreign
notes, no voting rights.

- Aggregate market value held by non-affiliates at 2025-03-28: **$3,253,431,000,000**.
- State of incorporation: **California** (unusual for a mega-cap; most are Delaware).
- No preferred outstanding.

## 1F. GOVERNANCE EVENT DISCOVERED — CEO TRANSITION (FILED, 2026-09-01)

Not in the brief but material and FILED. Form 8-K/A Amendment No. 1 to the 8-K of 2026-04-20:
> *"Apple Inc. previously announced its Chief Executive Officer transition plan in its Current
> Report on Form 8-K filed on April 20, 2026. This Amendment ... is being filed to disclose
> **John Ternus' new compensation arrangement in connection with his appointment to the role of
> CEO**, and **Tim Cook's new compensation arrangement in connection with his appointment to the
> role of Executive Chair** of Apple's Board of Directors, in each case **effective as of
> September 1, 2026**."*

Terms disclosed:
- **Ternus (CEO):** salary raised to **$3 million** on the transition date; prorated FY2026 RSU
  award target value **$2.5 million**; FY2027 annual equity award target value **$55 million**,
  **75% performance-based RSUs vesting on Apple's TSR relative to the S&P 500**, 25% time-based
  vesting semiannually 12.5% over four years.
- **Cook (Executive Chair):** salary **$2 million** effective 2026-09-26; FY2027 equity award
  target value **$45 million**, **50% TSR-based PSUs / 50% time-based**.

Note the mix shift: the incoming CEO's award is 75% performance-conditioned; the outgoing CEO's
Executive-Chair award is 50%. Also note the transition took effect **five days before this
research date** — the 2026 DEF 14A (filed 2026-01-08) predates the announcement and still
describes Cook as CEO.
