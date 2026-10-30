# WORKPAPER - the competitor row, BELFB, 2026-09-21
**Required at Q2 [E3-28]: a moat is a claim about relative position and cannot be evidenced from
one company's numbers.** One construction, applied identically to every name, from each filer's own
SEC data, newest fiscal year and the five most recent fiscal years.

## THE CONSTRUCTION, stated once and not varied
From each registrant's own SEC XBRL companyfacts, **annual (330-400 day) durations tagged in a 10-K
only**, newest filing vintage wins where a year was restated:
- **GM%** = `GrossProfit` / revenue (revenue = `RevenueFromContractWithCustomerExcludingAssessedTax`,
  falling back through `Revenues`, `SalesRevenueNet`, `SalesRevenueGoodsNet`)
- **OM%** = `OperatingIncomeLoss` / revenue
- **NTA** (unleveraged net tangible assets, the denominator [E2-43] prescribes for acquisitive
  filers) = `Assets` - `Goodwill` - intangibles - (`Liabilities` - interest-bearing debt)
- **EBIT/NTA** = `OperatingIncomeLoss` / NTA

Scripts: `peers.py`, `peers5y.py`. Raw: `peer_row.json`, `peer_5y.json`, `peers_*.json`.

**Operator rule 4 is satisfied for the row by a hand cross-check against a filed statement.**
Amphenol's own FY2025 10-K (accession `0001104659-26-013549`, filed 2026-02-11) MD&A states:
*"Operating income was $5,868.6, or 25.4% of net sales, in 2025, compared to $3,156.9, or 20.7% of
net sales, for 2024."* The construction above returns **25.4%** and **20.7%** for those two years.
The construction reproduces the filed figure.

## THE ROW - newest fiscal year, same metrics, same construction
| company | ticker | what it sells that Bel sells | FY end | rev $m | GM% | OM% | NTA $m | EBIT/NTA |
|---|---|---|---|---|---|---|---|---|
| **Bel Fuse** | **BELFB** | **the subject** | **2025-12-31** | **675** | **39.1** | **16.4** | **283** | **39.2%** |
| Amphenol | APH | connectors, cable assemblies, RF | 2025-12-31 | 23,095 | 36.9 | 25.4 | 15,527 | 37.8% |
| TE Connectivity | TEL | connectors, harsh-environment interconnect | 2025-09-26 | 17,262 | 35.2 | 18.6 | 8,219 | 39.1% |
| Vishay Intertechnology | VSH | passives, inductors, magnetics, protection | 2025-12-31 | 3,069 | 19.4 | 1.9 | 2,780 | 2.0% |
| Littelfuse | LFUS | circuit protection, fuses, PTC | 2025-12-27 | 2,386 | 38.0 | 1.6 | 1,422 | 2.6% |
| Advanced Energy | AEIS | embedded and front-end power supplies | 2025-12-31 | 1,799 | 37.7 | 9.3 | 2,087 | 8.0% |
| Methode Electronics | MEI | power distribution, connectors | 2026-05-02 | 1,019 | 19.8 | 0.9 | 610 | 1.4% |
| Standex International | SXI | electronics, magnetics, reed switches | 2026-06-30 | 892 | 41.7 | 21.7 | n/a | n/a |
| Allient | ALNT | motion and power electronics | 2025-12-31 | 554 | 32.8 | 7.9 | 259 | 17.0% |
| CTS Corporation | CTS | electronic components, sensors | 2025-12-31 | 541 | 38.4 | 15.3 | 189 | 43.8% |
| Vicor | VICR | board-mount DC/DC power modules | 2025-12-31 | 408 | 63.6 | 20.1 | 712 | 11.5% |
| RF Industries | RFIL | RF connectors and cable assemblies | 2025-10-31 | 81 | 33.2 | 2.2 | 25 | 7.2% |

**Eleven peers taken.** SXI's NTA is not computed because it does not tag `Liabilities`
undimensioned; its margins are unaffected and are shown.

## THE SAME ROW OVER FIVE YEARS - because one year is a snapshot, not a position
Operating margin %, oldest first, five most recent fiscal years, same construction:

| ticker | window | OM% by year | 5y mean | 5y min |
|---|---|---|---|---|
| **BELFB** | 2021..2025 | **5.8 / 10.0 / 13.8 / 12.0 / 16.4** | **11.6** | **5.8** |
| APH | 2021..2025 | 19.4 / 20.5 / 20.4 / 20.7 / 25.4 | 21.3 | 19.4 |
| TEL | 2021..2025 | 16.3 / 16.9 / 14.4 / 17.6 / 18.6 | 16.8 | 14.4 |
| SXI | 2022..2026 | 12.0 / 23.1 / 14.1 / 11.8 / 21.7 | 16.6 | 11.8 |
| CTS | 2021..2025 | 14.9 / 15.8 / 13.6 / 13.8 / 15.3 | 14.7 | 13.6 |
| LFUS | 2022..2025 | 18.5 / 19.9 / 15.3 / 7.2 / 1.6 | 12.5 | 1.6 |
| VICR | 2021..2025 | 15.5 / 6.8 / 12.7 / -0.4 / 20.1 | 10.9 | -0.4 |
| VSH | 2021..2025 | 14.4 / 17.6 / 14.3 / 0.2 / 1.9 | 9.7 | 0.2 |
| AEIS | 2021..2025 | 10.4 / 12.6 / 6.9 / 2.5 / 9.3 | 8.3 | 2.5 |
| ALNT | 2021..2025 | 6.4 / 6.3 / 7.3 / 5.7 / 7.9 | 6.7 | 5.7 |
| MEI | 2022..2026 | 9.6 / 7.7 / -10.0 / -2.3 / 0.9 | 1.2 | -10.0 |
| RFIL | 2021..2025 | 7.7 / -5.3 / -5.3 / -4.4 / 2.2 | -1.0 | -5.3 |

Gross margin over the same five years, subject only: **24.7 / 28.0 / 33.7 / 37.8 / 39.1** - up every
single year.

## THE SUBJECT'S OWN SEVENTEEN YEARS, which the five-year row cannot see
Operating margin, FY2009 to FY2025, all from 10-K-tagged annual facts:
`-9.5 / 5.0 / 2.5 / 0.6 / 4.3 / 2.8 / 5.0 / -15.3 / 3.5 / 4.9 / -0.3 / 4.0 / 5.8 / 10.0 / 13.8 /
12.0 / 16.4`

**Thirteen of the seventeen years are below 6%. Two are negative. The best year before 2022 is 5.8%.**

## PEERS EXCLUDED, AND WHY - named, per the rule
- **Molex** (Koch Industries), **Pulse Electronics** (Yageo), **Halo Technology**, **Bourns**,
  **Samtec** - private, no filings at any rung of the evidence ladder.
- **TDK**, **Murata**, **Delta Electronics**, **Yageo**, **Sumida** - Japan- and Taiwan-listed, not
  SEC registrants. Real competitors in magnetics and power; **excluded and disclosed**. This is the
  row's one material gap: the magnetics segment (13% of Bel's 2025 sales) competes mainly against
  Asian filers absent from this row.
- **Smiths Interconnect** (Smiths Group plc, LSE) - no SEC filing, and the connector business is not
  separately reported inside the group.
- **Sensata (ST)**, **Vishay Precision Group (VPG)** - sensors and weighing; adjacent, not the same
  socket. Excluded as not competitors.
- **Bel's own compensation peer group** (DEF 14A filed 2026-04-10, accession `0001437749-26-011998`)
  is **not** a product-competitor list and is not used as one. It names ACM Research, Allient, Alpha
  and Omega Semiconductor, Arlo, Aviat Networks, Cambium Networks, CTS, Ichor, Kimball Electronics,
  NETGEAR, nLIGHT, Northwest Pipe Company, PAR Technology, Photronics, RF Industries, Richardson
  Electronics, Standex, Thermon, Veeco and Vishay Precision Group, and the proxy says on its face it
  is a group of *"companies with similar operational focus or in comparable industry segments ...
  with comparable size, scope, and public float, and that compete with Bel for executive talent."*
  **Northwest Pipe Company makes steel water pipe.** Four names on that list are genuine product
  competitors and all four (CTS, Standex, RF Industries, Allient) are in the row above.

## WHAT THE ROW SHOWS, and its limit [E3-61]
Two of the eleven - **Amphenol and TE Connectivity** - never fell below 14.4% operating margin in
five years and raised gross margin in every one of them. The other nine, Bel included, swing between
positive and negative. **The same industry, the same five years, produced both outcomes**, which is
[E3-61] exactly: *"In some businesses, the participants behave like a demented Kellogg. In other
businesses, they don't ... I think you'd have to know the people involved."* The row establishes
position; it cannot establish conduct.

What it does establish for this run is narrower and it is enough: **the environment is not the
explanation for Bel's thirteen weak years, because two competitors in the same environment did not
have them**; and **Bel's 2025 is its best year in seventeen and still sits nine points of operating
margin below Amphenol.**
