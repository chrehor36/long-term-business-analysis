# COMPETITOR ROW — Polar Electro Oy and Suunto: SEC-registrant status and what exists on the record

**Transcription only. No conclusions. Retrieved 2026-09-06.**

**Bottom line up front, stated plainly: neither Polar Electro nor Suunto is an SEC registrant.
There is no 10-K, 20-F, 40-F, F-1 or S-1 for either. No annual-report figures for either
company are available on the filing rung. This row cannot be built to primary-filing standard;
it is UNRESEARCHED-at-best on any rung above the ones recorded below.**

---

## 1. EDGAR company search — the exact searches run and their results

Method: EDGAR company-name browse endpoint,
`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=<NAME>&type=&dateb=&owner=include&count=100&output=atom`,
with header `User-Agent: BRK-framework-research chrehor36@gmail.com`. The Atom feed returns one
`<entry>` element per matching registrant. Run 2026-09-06, 12:45 ET.

| Search string submitted | `<entry>` elements returned | Result |
|---|---|---|
| `Polar Electro` | **0** | **No registrant. The feed contains a `<title>Company Search Feed</title>` and no entries at all.** |
| `polar electro` (lowercase) | **0** | No registrant. |
| `Suunto` | **0** | **No registrant. Empty feed, no entries.** |
| `polar oy` | **0** | No registrant. |
| `Amer Sports` | 2 | Two registrants returned — see Section 3. |

Verbatim, the complete body of the "Polar Electro" response (the empty result, reproduced in
full so it can be verified in under two minutes):

```
<?xml version="1.0" encoding="ISO-8859-1" ?>
  <feed xmlns="http://www.w3.org/2005/Atom">
    <author>
      <email>webmaster@sec.gov</email>
      <name>Webmaster</name>
    </author>
    <id>https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;company=Polar Electro&amp;owner=include&amp;count=40</id>
    <link href="..." rel="self" type="application/atom+xml" />
    <link href="..." rel="alternate" type="text/html" />
    <title>Company Search Feed</title>
    <updated>2026-09-06T12:45:53-04:00</updated>
  </feed>
```

The "Suunto" response is identical in form, with `company=Suunto` in the `<id>` and an
`<updated>` timestamp of `2026-09-06T12:45:54-04:00`. **Zero entries in both cases.**

Control check that the method works: `company=polar` (the bare word) returns 100 entries —
registrants such as unrelated "Polar"-named entities — so an empty result for `Polar Electro`
is a genuine absence and not a broken query.

---

## 2. EDGAR full-text search — the names appear only as third parties in OTHER filers' documents

Method: `https://efts.sec.gov/LATEST/search-index` with `q="Polar Electro"` and `q="Suunto"`.
EDGAR full-text search covers filings from 2001 forward only.

**"Polar Electro"** — the hits are in filings by *other* registrants. The highest-relevance
hits attributable to the sports-wearables company are **Garmin Ltd's own Form 10-Qs**, where
"Polar Electro, Inc." is named as a **co-defendant in patent litigation**, not as a filer.
Verbatim, Garmin Ltd Form 10-Q filed 2012-05-09 (accession 0001144204-12-027190, primary
document `v308106_10q.htm`), Legal Proceedings:

> "*Avocet Sports Technology, Inc. v. Garmin International, Inc., Implus Footcare, LLC d/b/a
> Highgear, Polar Electro, Inc., Brunton d/b/a Brunton Outdoor Group, and Casio America, Inc.*
> On August 18, 2011, Avocet Sports Technology, Inc. ("Avocet") filed suit in the United States
> District Court for the Northern District of California against five companies, including
> Garmin International, Inc., alleging infringement of U.S. Patent No. 5,058,427 ("the '427
> patent")."

That mention carries **no** financial data about Polar Electro. Other high-scoring full-text
hits (American Software Inc 8-Ks, Structured Asset Securities Corp II 8-Ks) are unrelated
token matches, not the Finnish company.

**"Suunto"** — the substantive hits are in filings by **Amer Sports, Inc.**, Suunto's former
owner. See Section 3.

---

## 3. The one filing-rung disclosure that contains Suunto figures — Amer Sports, Inc. Form 20-F

**This is a real primary-filing source and is recorded as such. It is NOT a Suunto annual
report; it is Suunto reported inside a former parent's discontinued operations, on IFRS, in US
dollars, for a partial period.**

Registrant: **Amer Sports, Inc.**, CIK **0001988894**, ticker **AS**, NYSE, fiscal year end
December 31, incorporated Cayman Islands. (The EDGAR name search also returned a second,
dormant registrant, CIK 0000810038, "Amer" of Hyrylä, Finland, last filing date 2008-12-30 —
recorded for completeness, not used.)

Source document: **Form 20-F for fiscal year ended December 31, 2023, accession
0001104659-24-035553, primary document `as-20231231x20f.htm`, filed 2024-03-18.**

Verbatim, MD&A, "Comparability of Our Results of Operations — Discontinued Operations":
> "During the years ended December 31, 2022 and December 31, 2021, we completed the divestitures
> of our Suunto and Precor businesses, respectively. All income and expenses of each of the
> Precor and Suunto businesses have been reported as discontinued operations for the full years
> 2022 and 2021, while the related assets and liabilities have been classified as assets and
> liabilities held-for-sale as of December 31, 2021 and January 1, 2021, respectively. During
> the year ended December 31, 2021, we recognized impairment charges on the carrying value of
> Suunto's net assets in the amounts of $77.5 million. During the year ended December 31, 2022,
> we recognized a loss on disposal on the sale of our Suunto business in the amount of $5.5
> million, offset by a $4.8 million gain relating to a final purchase price adjustment relating
> to the Precor divestiture."

Verbatim, MD&A:
> "Loss from discontinued operations, net of tax for 2023 decreased by $21.8 million, to nil,
> compared to $21.8 million in 2022. Loss from discontinued operations, net of tax in 2022, only
> included losses generated by Suunto for the period until disposal on May 6, 2022, including a
> loss on disposal of $5.5 million, partially offset by a gain of $4.8 million relating to a
> final purchase price adjustment paid in 2022 relating to the Precor disposal."

Verbatim, Note 29 "DISCONTINUED OPERATIONS AND ASSETS AND LIABILITIES HELD FOR SALE":
> "During June 2021 the Company entered into a term sheet with Dongguan Liesheng Electronic
> Technology Co. Ltd ('Liesheng'), a leading Chinese technology company focusing on the smart &
> sport wearables electronics segment, in regards to the disposal of Suunto. The asset and
> liabilities of the disposal group were classified as held-for-sale and it was concluded that
> the disposal group qualifies as a discontinued operation. On December 28, 2021, an agreement
> was reached with Liesheng to acquire the Suunto business subject to the satisfaction of
> customary closing conditions."
>
> "The closing of the transaction was completed on May 6, 2022. The consolidated cash and
> debt-free sales value amounted to USD 18.3 million (net of transaction costs). The loss on
> disposal upon the sale of the Suunto business amounted to USD 5.5 million and is reported
> under loss from discontinued operations, net of tax. Upon classifying Suunto as held-for-sale,
> an impairment loss in the amount of USD 77.5 million was recognized in accordance with IAS 36
> Impairment of Assets."

Verbatim, the discontinued-operations table. **The table's own heading is "The result of the
Suunto and Precor businesses" — it is a COMBINED line, not Suunto alone. Recorded as printed;
not split.**

| USD million | 2023 | 2022 | 2021 |
|---|---|---|---|
| Revenue | — | 31.3 | 192.0 |
| Cost of goods sold | — | (24.9) | (114.2) |
| Gross profit | — | 6.4 | 77.8 |
| Selling, general and administrative expenses | — | (24.1) | (123.7) |
| Impairment losses on non-financial assets | — | — | (77.5) |
| Profit and loss on sale of divested businesses | — | (5.5) | 116.0 |
| Other operating income | — | 1.1 | 3.1 |
| Operating loss | — | (22.1) | (4.3) |
| Finance income | — | 0.0 | 0.0 |
| Finance expenses | — | 0.5 | (0.3) |
| Net finance cost | — | 0.5 | (0.3) |
| Loss before tax | — | (21.6) | (4.6) |
| Income tax expense | — | (0.2) | 2.8 |
| Profit (loss) for the period | — | (21.8) | (1.8) |

**What can and cannot be said from this table, stated plainly:**
- The **2022 column ($31.3 million revenue)** is stated by the filing's own MD&A to relate only
  to Suunto, for the period from January 1, 2022 to disposal on May 6, 2022 — **roughly four
  months, not a year.** It is **not** a Suunto annual revenue figure.
- The **2021 column ($192.0 million revenue)** is **Suunto and Precor combined.** The 20-F does
  **not** split it. Any Suunto-only 2021 number would be an invention. **Absence recorded.**
- **No Suunto revenue figure for any full year is disclosed in any SEC filing.**
- Amer Sports' 20-F for FY2023 states: "During the fiscal year 2023, the Company neither
  accounted for any discontinued operations nor reported assets or liabilities held-for-sale as
  of December 31, 2023." Suunto disappears from Amer Sports' financials after 2022.
- Suunto's current owner, **Dongguan Liesheng Electronic Technology Co. Ltd**, is named in the
  20-F. Liesheng is not an SEC registrant either (no EDGAR company-name match; not searched
  further because it does not bear on this row).

Amer Sports' 20-F filings on EDGAR: FY2023 (0001104659-24-035553, filed 2024-03-18), FY2024
(0001628280-25-011314, filed 2025-03-07), FY2025 (0001988894-26-000004, filed 2026-02-26). Only
the FY2023 vintage still carries the 2021–2022 Suunto comparatives.

---

## 4. Polar Electro Oy — no filing-rung figures exist at all

- **Not an SEC registrant** (Section 1).
- **Named in SEC filings only as a third party**, and only as a patent-litigation co-defendant
  of Garmin's (Section 2). No revenue, no earnings, no balance-sheet item.
- **No former or current SEC-registrant parent.** Polar Electro Oy is, per its own site, a
  Finnish private company; there is no EDGAR filer that consolidates it and therefore no
  discontinued-operations or segment disclosure anywhere on EDGAR analogous to the Amer
  Sports/Suunto route.
- **Nothing on the filing rung. Recorded plainly as an absence.**

---

## 5. Company-website check — NON-FILING RUNG, and it came back empty

Pages retrieved 2026-09-06 with `curl -L --compressed`:

| URL | HTTP status | Financial figures found |
|---|---|---|
| `https://www.polar.com/en/about_polar` | 200 | **None.** Text scan for "revenue", "turnover", "net sales", "annual report", "EUR", "million" returned **0 matches** in the rendered text. |
| `https://www.polar.com/en/company` | 200 (same document served) | None. |
| `https://www.suunto.com/en-us/About-Suunto/` | 200 | **None.** Same scan, **0 matches**. |
| `https://www.suunto.com/about-suunto/` | 200 | None. |

**No public annual-report figures were found on either company's own site.** Nothing is
recorded here as NON-FILING-RUNG data because nothing was found to record.

**Note on what was deliberately NOT done:** Polar Electro Oy files statutory accounts with the
Finnish Patent and Registration Office (PRH) trade register, and Suunto Oy's Finnish statutory
accounts would be filed the same way. Those are behind a paid national register and were not
retrieved. If the framework needs a Polar or Suunto revenue figure, **the document that would
resolve it is nameable** — the Finnish PRH statutory annual accounts (*tilinpäätös*) for Polar
Electro Oy and for Suunto Oy — which under the operator protocol makes this **UNRESEARCHED, not
UNKNOWABLE.** It has not been researched here because it is off the SEC ladder this pass was
scoped to.

---

## 6. What this row does NOT contain, said once more

- No estimated Polar revenue. No estimated Suunto revenue.
- No market-share figure for either.
- No unit shipments for either.
- No third-party research-house numbers of any kind. Nothing from IDC, Counterpoint, Canalys or
  similar was consulted or recorded, and none of it would be a filing.
- **No estimate anywhere in this file is presented as a filing, because no estimate appears in
  this file.**
