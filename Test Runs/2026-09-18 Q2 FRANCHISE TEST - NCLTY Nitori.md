# Q2 FRANCHISE TEST — NITORI HOLDINGS (TSE 9843; unsponsored ADR NCLTY)
**2026-09-18. One gate, not a run.** Q2 only, under `Framework/THE FRAMEWORK v4.md`. Built
because Q2 is the one gate this company has never had: the standing record
(`Test Runs/2026-08-28 RERUN - NCLTY (Nitori) under v4.1.md`) carries **Q2 UNRESEARCHED, moat
class PROVISIONAL, because the competitor row has never been built.**

**Scope lock.** No owner earnings, no price, no value, no entry or exit language, no H1 verdict.
Q5 is out of scope by the brief and by operator protocol rule 2 in reverse: this file produces
the instrument H1 of `Framework/THE HOLDINGS FRAMEWORK.md` needs, and nothing more.

**Pre-registration [E4-26], written before any figure was computed.** The brief's stated prior is
**NARROW at best**, on the category argument that home furnishing has low switching costs and the
customer walks into whichever store is convenient. The test designed to refute it is the yen
pass-through test named below. The operator holds this position and is up on it; that is the
incentive **[E4-27]** and the self-deception **[E3-41]** this gate must be run against, so the
row is built peer-first and the verdict written last.

*(Sections are appended as each closes — write-early protocol.)*

---

# 1. SOURCES AND RUNGS

**Nitori files nothing with the SEC.** Operator rule 5 wants primary filings and rule 4 wants the
filing read, so the rung ladder used here is: **(1) Japanese statutory filing (有価証券報告書,
filed to EDINET, posted by the company) > (2) company English financial statements (a translation
of the filing) > (3) company FACT BOOK / IR disclosure (unaudited by the company's own statement)
> (4) aggregator.** Every figure below carries its rung.

## EDINET — reached, but not through EDINET

**EDINET's own API was NOT reached.** Tested this session:
- `https://api.edinet-fsa.go.jp/api/v2/documents.json?date=2026-06-25&type=2` returned HTTP 200
  carrying `{"StatusCode": 401, "message": "Access denied due to invalid subscription key."}` — the
  v2 API requires a registered key, which confirms the 2026-08-28 file's finding.
- `https://disclosure.edinet-fsa.go.jp/api/v1/documents.json?...` — the v1 endpoint is retired and
  returns an HTML error page, not JSON.

**The route that worked, and it is rung 1, not a workaround: Nitori posts the Japanese annual
securities reports itself**, on its own Japanese IR library page
`https://www.nitorihd.co.jp/ir/library/security.html`. The 2026-08-28 session did not find it
because it searched the *English* library (`/en/ir/library/`), which carries only the translated
financial-statements extract. The PDFs carry the EDINET submission header
`EDINET提出書類 / 株式会社ニトリホールディングス(E03144) / 有価証券報告書` on every page, so these
are the EDINET documents themselves, served from the issuer. **EDINET filer code E03144.**

### Documents read — downloaded to `Test Runs/_research 2026-09-18 NCLTY/docs/`

| Short name | Document | Fiscal year covered | Server Last-Modified | Bytes | URL under `nitorihd.co.jp/ir/items/` |
|---|---|---|---|---:|---|
| YUHO-26 | 有価証券報告書 (54th) | FYE 2026-03-31 | 2026-06-24 | 1,325,355 | `2026_NITORI_houkoku.pdf` |
| YUHO-25 | 有価証券報告書 (53rd) | FYE 2025-03-31 | 2025-06-25 | 1,442,533 | `2025_NITORI_houkoku.pdf` |
| YUHO-24 | 有価証券報告書 (52nd) | FYE 2024-03-31 | 2024-06-21 | 1,112,948 | `2024_NITORI_houkoku.pdf` |
| YUHO-23 | 有価証券報告書 (51st) | FYE 2023-03-31, **13.4 months** | 2023-09-07 | 904,802 | `2023_NITORI_houkoku.pdf` |
| YUHO-22 | 有価証券報告書 (50th) | FYE 2022-02-20 | 2022-05-20 | 828,563 | `2022_NITORI_houkoku_1.pdf` |
| YUHO-21 | 有価証券報告書 (49th) | FYE 2021-02-20 | 2021-05-14 | 809,773 | `2021_NITORI_houkoku.pdf` |
| YUHO-20 | 有価証券報告書 (48th) | FYE 2020-02-20 | 2020-05-15 | 735,629 | `202002_NITORI_houkoku.pdf` |
| YUHO-19 | 有価証券報告書 (47th) | FYE 2019-02-20 | 2019-05-17 | 742,124 | `201902_NITORI_houkoku.pdf` |
| FB-21 … FB-26 | FACT BOOK, 4Q (決算) | FYE 2021-02 through FYE 2026-03 | see `fb/` | — | listed on `/ir/library/factbook.html` |
| MON | 株式会社ニトリ月次国内売上高前年比推移 | FYE 2018-02 … FYE 2027-03 YTD | fetched 2026-09-18 | — | `/ir/performance/sales_YYYY.html` |

**Rung note on the FACT BOOK and the monthly page.** Both are the company's own disclosure and
not part of the audited statements — the FACT BOOK says so on its face:
*"本資料には、監査を受けていない参考数値が含まれます"* ("This material contains both audited and
non-audited information"). They are **rung 3**. Every margin figure below is rung 1; the average
settlement rate and the monthly customer series are rung 3, flagged wherever used. Neither is a
translation, so no translation flag applies. The English "Consolidated Financial Statements" PDFs
relied on by the 2026-08-28 run are a **translation** of Chapter 5 of YUHO-25 and YUHO-26 and are
rung 2; this file does not rely on them.

## Accounting basis, and it changed inside the window

- **J-GAAP through the 52nd period (FYE 2024-03-31).**
- **IFRS from the 53rd period (FYE 2025-03-31)**, transition date **2023-04-01**, so FY2024 exists
  on both bases: J-GAAP as originally filed in YUHO-24, IFRS as the restated comparative in
  YUHO-25. **Both are shown; no series crosses the bases silently.**
- **The 51st period is 13.4 months** (2022-02-21 to 2023-03-31), the fiscal-year-end change from
  February 20 to March 31. Excluded from every length-dependent comparison and flagged wherever it
  appears.

## Rule 4 cross-check

**FY2026 revenue ¥912,248 million** appears in two independently prepared places inside YUHO-26:
the front table 主要な経営指標等の推移 (p.2, 売上収益 row, 54th-period column) and the
連結損益計算書 (Consolidated Statement of Profit or Loss, 売上収益 line, note refs 5/13/26).
**Gross profit ¥485,413** likewise appears in the 連結損益計算書 and independently in FB-26 item 01
at a stated 53.2% share of revenue, which reproduces the computed 485,413 / 912,248 = 53.21%.
Cross-check clears.

---

# 2. THE PERIMETER, WITH EVERY ACQUISITION DATED

From YUHO-26's own 沿革 (corporate history) and the 企業結合等関係 note of YUHO-21. This matters
because a comparable-store or margin series that crosses an acquisition is not one company.

| Date | Event | Effect on the perimeter |
|---|---|---|
| 2017-05 | 株式会社カチタス (Katitas) acquired by share purchase, becoming an **equity-method affiliate**, plus a business-alliance contract | Not consolidated. Sits in 持分法による投資利益: **¥4,258m in FY2026**, ¥3,265m in FY2025, i.e. 3.4% of FY2026 operating profit. The only equity-method investee (YUHO-25: 持分法適用会社１社) |
| 2018-12 | 株式会社Ｎプラス founded, apparel business started | Organic. N Plus peaked at 44 stores (FYE2025) and fell to **30** by FYE2026 on 14 closures and zero openings |
| 2020-03 | NITORI RETAIL (MALAYSIA) SDN.BHD founded | Organic |
| **2020-11-30** | **株式会社島忠 (Shimachu) — deemed acquisition date (みなし取得日)** | — |
| **2021-01-06** | **Shimachu — share-acquisition date; 77.04% of voting rights; consideration ¥165,054m in cash** | **FYE 2021-02-20: balance sheet consolidated only.** YUHO-21 states it plainly: *"当連結会計年度は貸借対照表のみを連結しているため、被取得企業の業績は含まれておりません"* — no Shimachu P&L in the 49th period, and *"当連結会計年度に帰属する設備投資はありません"* |
| 2021-05 | Shimachu additional shares acquired, becoming **wholly owned** | — |
| 2021-09 | NITORI RETAIL SINGAPORE PTE. LTD. founded | Organic |
| 2022-04 | 株式会社エディオン (Edion) capital-and-business-alliance contract | Not consolidated, not equity-method |
| **2023-04** | **United States: stores and the EC site closed; withdrawal from the US business** | A country exited inside the window. FB-26 shows the USA store line at zero |
| 2024-06 to 2024-12 | First stores in the Philippines, Indonesia and India; Nitori Digital Base Vietnam founded | Organic |

**The break that matters.** Consolidated gross margin is **Nitori-only through FYE 2021-02-20** and
**Nitori plus Shimachu from FYE 2022-02-20**. Shimachu is a home-centre chain whose segment margin
runs 1.8% to 6.5%, so the consolidated 57.44% to 52.48% step at FY2022 is contaminated. **Every
franchise judgment below therefore runs on the Nitori segment, not the consolidated figure**; the
consolidated series is shown only to expose the contamination.

---

# 3. THE FILED RECORD

Arithmetic in `Test Runs/_research 2026-09-18 NCLTY/margins.py`, output in `margins_out.txt`;
numerator and denominator shown for every ratio. Yen figures in millions, as printed.

## 3a. Consolidated — and why it cannot be read straight

| FYE | basis | Revenue | Gross profit | GM % | Operating profit | OP % | OP / total assets | filer ROE % |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2019-02-20 (47th) | J-GAAP | 608,131 | 331,421 | **54.50** | 100,779 | 16.57 | 16.27 | 14.5 |
| 2020-02-20 (48th) | J-GAAP | 642,273 | 354,364 | **55.17** | 107,478 | 16.73 | 15.73 | 13.5 |
| 2021-02-20 (49th) | J-GAAP | 716,900 | 411,791 | **57.44** | 137,687 | 19.21 | 14.79 | 15.3 |
| 2022-02-20 (50th) | J-GAAP | 811,581 | 425,897 | 52.48 | 138,270 | 17.04 | 14.05 | 14.1 |
| 2023-03-31 (51st) | J-GAAP | *948,094* | *478,106* | *50.43* | — | — | — | 12.3 |
| 2024-03-31 (52nd) | J-GAAP | 895,799 | 455,949 | 50.90 | 127,725 | 14.26 | 10.31 | 10.1 |
| 2024-03-31 (52nd) | IFRS | 896,667 | 457,403 | 51.01 | — | — | — | 11.3 |
| 2025-03-31 (53rd) | IFRS | 928,828 | 473,923 | 51.02 | 117,665 | 12.67 | 7.69 | 9.5 |
| 2026-03-31 (54th) | IFRS | 912,248 | 485,413 | **53.21** | 125,526 | 13.76 | 7.99 | 9.4 |

*51st period italicised: 13.4 months, not comparable.* Shimachu enters the P&L at the 50th.

## 3b. Nitori segment only — the clean series

| FYE | basis | Segment revenue | Segment profit | Margin % |
|---|---|---:|---:|---:|
| 2022-02 | J-GAAP | 679,252 | 135,274 | **19.92** |
| 2023-03 *(13.4m)* | J-GAAP | *821,782* | *135,329* | *16.47* |
| 2024-03 | J-GAAP | 785,404 | 125,075 | 15.92 |
| 2024-03 | IFRS | 786,306 | 128,638 | 16.36 |
| 2025-03 | IFRS | 820,886 | 118,975 | 14.49 |
| 2026-03 | IFRS | 816,196 | 118,381 | **14.50** |

Shimachu segment for completeness: 2.21 / 3.05 / 1.77 / **−1.08** / 6.54 % — a loss in FY2025,
recovered in FY2026 on private-brand mix and advertising cuts.

**Three facts on the face of it.** Nitori-segment revenue is **lower in FY2026 than in FY2025**
(816,196 against 820,886). Nitori-segment margin has fallen from 19.9% to 14.5% and did **not**
recover in FY2026 even though gross margin did. And **return on capital employed has roughly
halved** — 16.3% of assets in FY2019 to 8.0% in FY2026, filer ROE 15.3% to 9.4% — while the equity
ratio rose to 62.9%, so leverage is not the explanation.

## 3c. The consecutive-growth run, and when it ended

YUHO-21 states it for the 49th period: revenue ¥716.9bn, operating profit ¥137,687m, ordinary
profit ¥138,426m, *"となり34期連続増収増益となりました"* — **34 consecutive periods of rising
revenue and rising profit, through FYE 2021-02-20.** YUHO-21 also records a ¥2 commemorative
dividend for *"30期連続増収増益"*.

**No later report repeats the claim.** The 50th period (FYE 2022-02) would have been the 35th:
revenue rose and consolidated operating profit rose ¥583m to 138,270 — but the **Nitori segment's
own operating profit fell ¥2,412m** to 135,274, and the entire consolidated increase is the newly
consolidated Shimachu's ¥3,032m. **On a same-perimeter basis the run ended at 34.** The company
stopped making the claim at exactly that point, which is to its credit and is the cleanest
available reading of it.

---

# 4. THE YEN PASS-THROUGH TEST — the sharpest instrument this record offers

The setup is the company's own. YUHO-26's risk factor ① states the exposure verbatim:

> 当社グループは、「使う・買う」立場に立って、全ての商品で「お、ねだん以上。」の実現を目指すため、
> **商品の約90％をプライベートブランドとして開発輸入しております。** そのため、外貨建取引について
> 為替予約の実行や、輸入為替レートの平準化を図ることで、仕入コストの安定化を推進しておりますが、
> 各国基軸通貨に対して、米ドル高が急激に進む場合、為替相場の変動が当社グループの業績や財務状況に
> 悪影響を及ぼす可能性があります。

*"About 90% of goods are developed and imported as private brand"* — costs in dollars, revenue in
yen. Risk factor ② adds that *"the majority of the goods sold are produced and imported in China and
other Asian countries."* So **[E2-44]**'s first characteristic — can it raise prices without losing
unit volume — is answerable from the filed record, because the input cost moved violently and the
company's own disclosure separates price from volume.

## 4a. The shock, measured by the company's own settlement rate

FACT BOOK item 07/08, 平均決済レート (average settlement rate), yen per dollar — **rung 3, the
company's own unaudited disclosure, and the right number because it is the rate Nitori actually
settled its imports at, not a market average.**

| Fiscal year | Rate ¥/$ | vs the FY2020 trough |
|---|---:|---:|
| FY2018 (to Feb 2019) | 110.20 | +6.0% |
| FY2019 (to Feb 2020) | 107.46 | +3.4% |
| **FY2020 (to Feb 2021)** | **103.95** | **base** |
| FY2021 (to Feb 2022) | 111.16 | +6.9% |
| FY2022 (to Mar 2023) | 132.23 | +27.2% |
| FY2023 (to Mar 2024) | 146.60 | +41.0% |
| FY2024 (to Mar 2025) | 152.54 | **+46.7%** |
| FY2025 (to Mar 2026) | 148.06 | +42.4% |

**A 47% rise in the yen cost of its own purchases, inside five years.** That is as clean a natural
experiment on pricing power as a filed record is ever going to hand over.

## 4b. What happened to price, and what happened to volume

`株式会社ニトリ月次国内売上高前年比推移`, the 年間 (annual) row, existing stores (既存店), Nitori
Co. domestic including mail order, excluding the corporate and reform businesses — **rung 3**. The
company's FY2026 briefing deck (p.12) reproduces the identical five-year series, which is a
same-issuer confirmation rather than an independent one.

| FYE | rate ¥/$ | existing-store **sales** YoY | existing-store **customers** YoY (買上客数) | existing-store **spend per customer** YoY (客単価) |
|---|---:|---:|---:|---:|
| Feb 2018 | — | 102.9 | 104.8 | 98.2 |
| Feb 2019 | 110.20 | 102.7 | 100.8 | 101.8 |
| Feb 2020 | 107.46 | 102.8 | 101.3 | 101.4 |
| Feb 2021 | 103.95 | 110.4 | 112.8 | 97.9 |
| Feb 2022 | 111.16 | 90.9 | 90.1 | 100.8 |
| Mar 2023 | 132.23 | 101.2 | **94.4** | **107.2** |
| Mar 2024 | 146.60 | 102.9 | **98.7** | **104.2** |
| Mar 2025 | 152.54 | 100.2 | 100.9 | 99.3 |
| Mar 2026 | 148.06 | **95.8** | **92.8** | **103.2** |
| Mar 2027 YTD (5 months) | — | 99.6 | 100.1 | 99.4 |

Chained, existing stores, **base FYE Feb 2020 = 100** (the last clean pre-COVID year):

| FYE | sales | customers | spend per customer |
|---|---:|---:|---:|
| Feb 2021 | 110.4 | 112.8 | 97.9 |
| Feb 2022 | 100.4 | 101.6 | 98.7 |
| Mar 2023 | 101.6 | 95.9 | 105.8 |
| Mar 2024 | 104.5 | 94.7 | 110.2 |
| Mar 2025 | 104.7 | 95.5 | 109.5 |
| **Mar 2026** | **100.3** | **88.7** | **113.0** |

And the same chain from the FY2021 COVID peak: sales 90.9, **customers 78.6**, spend per customer
115.4.

**Store count over the same span: 541 domestic stores at FYE Feb 2020 to 778 at FYE Mar 2026,
+43.8%.** Nitori Co. domestic selling floor grew from 2,246,826 m² (FYE 2024) to 2,383,120 m² (FYE
2026) on the Nitori banner alone, +6.1% in two years.

## 4c. The answer, stated plainly

**Nitori raised prices into the currency shock and lost the customers.** Existing-store spend per
customer is up 13.0% against FY2020 and existing-store footfall is down 11.3% — with the price rises
concentrated exactly in the two years the settlement rate moved most (FY2023 +7.2% spend per
customer against a 27% rate move; FY2024 +4.2% against 41%) and the traffic loss arriving in the
same years and then again, harder, in FY2026. **Existing-store sales are flat against FY2020 while
the store base is 44% larger.** This is **[E4-55]** in its textbook form: *"This decline in physical
volume is a serious reverse, not likely to disappear in some 'bounce back' effect. Nor do we expect
another sharp rise in prices like the approximately 40% rise..."* — Precision Steel's pounds fell
while price rises held dollar revenue level, and Munger called it a serious reverse rather than a
cycle. **The physical series here is the honest one, and it is falling.**

**The company agrees, in the filing, and names the cause as its own product.** YUHO-26's
対処すべき課題 makes *"①安さの実現"* — the realisation of cheapness — the **first** of its five
priority tasks:

> 2026年３月期において、国内ニトリ事業における**既存店の買上客数前年比が92.8％と大きく落ち込む結果
> となりました。** 食品やエネルギー等の価格上昇により生活防衛意識が高まる中で、**消費者の節約志向・
> 低価格指向に充分にお応えできていないことが大きな要因である**と認識しております。 … 原価低減を実現
> し、**売価に還元する**ことで、品質を維持しながら、よりお求めいただきやすい価格を実現し…

And the MD&A on the Nitori segment:

> 国内既存店の客数が前期比92.8%となり、売上が前期比95.8%となりました。足元における客数の減少は、
> **デザインや機能、価格競争力に優れた新たな商品の開発が十分に進まず**、適時に商品提案を行えなかった
> ことにより、お客様の期待に応えられなかったことが要因であると認識しております。

The board's own diagnosis: it failed to respond to consumers' shift to low prices, and its product
development failed on design, function **and price competitiveness**. Its remedy is to cut costs and
**give the saving back in the shelf price**.

**That is [E4-37]'s inverse metric reading against the company.** The test is *"you can almost
measure the strength of a business over time by the agony they go through in determining whether a
price increase can be sustained,"* and *"it's not a great business when you have to have a prayer
session before you raise your prices a penny."* Nitori did not have a prayer session before raising
prices — it raised them. But **the sequel is worse than agony: the increase did not hold, traffic
left, and the board has now committed in a statutory filing to reversing it.** A price rise that
must be given back is a demonstration that it could not be sustained. On [E4-37] the direction is
unambiguously **down**.

## 4d. And the half of [E2-44] that Nitori does pass

**Gross margin recovered while the yen stayed weak, and that is real.** Consolidated gross margin
went 57.44% (FY2021, Nitori-only) → 50.43% (FY2023, the trough) → **53.21% (FY2026)**, and the
FY2026 recovery happened with the settlement rate still 42% above the FY2020 trough and with
Shimachu, a low-margin home centre, inside the denominator. The recovery came from cost work the
filing itself describes: specification changes and product switching, raw-material review, new
supplier development, renegotiated terms with existing suppliers, in-house manufacture from raw
materials, new equipment, and **smaller product packaging to cut transport cost**. The FY2026
briefing deck's FY2027 priority list says it outright: *"円安基調でも荒利益を毀損しない原価設計"* —
cost design that does not damage gross profit even on a weak-yen trend.

**So the currency shock was absorbed — on the cost side.** What was not absorbed is the demand side:
SG&A ran from 35.4% of revenue (FY2021) to **39.9% (FY2026)**, personnel up 9.4% and advertising up
15.3% in FY2026 alone, and the Nitori segment's operating margin sat at 14.50% against 19.92% five
years earlier. **A business that has to spend 4.5 more points of revenue on selling, and cut price,
to hold flat existing-store sales on a 44% larger store base, has absorbed the shock in its cost of
goods and paid for it out of its franchise.**

## 4e. [E2-44]'s second characteristic: dollar volume with only minor additional capital

It fails on the filed record. Total assets went ¥683bn (FYE Feb 2020) to ¥1,571bn (FYE Mar 2026), a
**2.3x** increase, while revenue went ¥642bn to ¥912bn, **1.42x**, and operating profit ¥107.5bn to
¥125.5bn, **1.17x**. Operating profit per yen of assets fell from 15.73% to 7.99%. **[E3-46]** asks
the second question about the business as a number — *"the best businesses, by definition, are going
to be businesses that earn very high returns on capital employed over time"* — and the answer here
is a return on capital employed that has halved while the equity ratio rose, so leverage is not the
explanation. The capital went into owned real estate (PP&E ¥909bn, investment property ¥95bn) and
six own-built distribution centres. It may yet earn out; **on the filed record to date it has
diluted the return, not levered it.**

---

# 5. THE COMPETITOR ROW

> "**I can't be an intelligent owner of a business unless I know what all the other businesses in
> that industry are doing.**" — **[E3-28]**, 1996 meeting

**Eight peers were sought; seven were measured and one was named and not measured.** Buffett's figure
is eight; the listed Japanese home-furnishing set is small because the category consolidated into
Nitori, so the row is extended with the global operators that file audited accounts. Every cell is
computed by me from the peer's own filing, arithmetic in `margins.py`, numerator and denominator in
`margins_out.txt`. Japanese peer documents, accession-equivalents, URLs and server dates are in
`Test Runs/_research 2026-09-18 NCLTY/peers_jp.md`.

## 5a. BASIS WARNING — read before the table

**Gross margin is not comparable across this row, and the filers say so.** WSM's 10-K states it
outright: *"Our classification of costs in gross profit may not be comparable to other public
companies."* Its cost of goods sold includes **occupancy** (rent, property taxes, common-area
maintenance, utilities, depreciation) **and shipping**. RH's does the same. Wayfair's includes
**shipping and fulfilment**. **Nitori's 売上原価 excludes rent (賃借料 ¥15,383m sits in SG&A) and
excludes customer delivery (発送配達費 ¥33,820m sits in SG&A)**, and splits depreciation between the
two lines. Ryohin Keikaku has **no 売上高 line at all** — its captions are 営業収益 / 営業原価 /
営業総利益. DCM prints two denominators (売上高 for goods, 営業収益 = 売上高 + 不動産賃貸収入).

Adjusting Nitori toward the US basis (computed, FY2026):

| adjustment | GM |
|---|---:|
| as reported | **53.21%** |
| less SG&A customer delivery (¥33,820m) | 49.50% |
| less delivery + rent (¥49,203m) | **47.82%** |
| less delivery + rent + *all* SG&A depreciation (¥111,859m) — over-adjusted | 40.95% |

**On a WSM/RH-style basis Nitori's gross margin is between 41% and 48%, against WSM's 46.15% and
RH's 44.07%.** The apparent 7-to-9-point gross-margin lead over the US peers is mostly a
classification artifact. **Operating margin, return on assets and the physical series are the
comparable metrics, and the row below leads with them.**

## 5b. The row — latest completed fiscal year, each filer's own accounts

| Company | Ticker / filer | FYE | Basis | Revenue (own currency) | GM % | **Operating margin %** | **OP / total assets %** | **filer ROE %** | Source |
|---|---|---|---|---|---:|---:|---:|---:|---|
| **Nitori — Nitori segment** | TSE 9843 | 2026-03-31 | IFRS | ¥816,196m | n/d | **14.50** | n/d | 9.4 | YUHO-26 MD&A |
| **Nitori — consolidated** | TSE 9843 | 2026-03-31 | IFRS | ¥912,248m | 53.21† | 13.76 | **7.99** | **9.4** | YUHO-26 |
| Williams-Sonoma | WSM, CIK 719955 | 2026-02-01 | US GAAP | $7,806.8m | 46.15‡ | **18.13** | **26.16** | — | 10-K, accn 0000719955-26-000059 |
| Ryohin Keikaku (MUJI) | TSE 7453 | 2025-08-31 | J-GAAP | ¥784,629m | 51.36§ | 9.41 | **13.12** | **16.3** | yuho filed 2025-11-21 |
| RH | RH, CIK 1528849 | 2026-01-31 | US GAAP | $3,439.5m | 44.07‡ | 11.26 | 8.01 | — | 10-K, accn 0001104659-26-037992 |
| DCM Holdings | TSE 3050 | 2026-02-28 | J-GAAP | ¥542,317m (営業収益) | 34.34¶ | 5.72 | 4.62 | 6.2 | yuho filed 2026-05-27 |
| Ingka Group (IKEA retail) | Ingka Holding B.V. | 2025-08-31 | Dutch Civil Code Bk2 Pt9 | €41,451m | 34.79 | **3.53** | 2.38 | — | audited annual summary, unqualified opinion dated 2025-11-04 |
| Yamada Holdings | TSE 9831 | 2026-03-31 | J-GAAP | ¥1,691,808m | 26.11** | 0.96 | 1.24 | 2.3 | yuho posted 2026-06-26 |
| Wayfair | W, CIK 1616707 | 2025-12-31 | US GAAP | $12,457m | 30.22‡ | 0.14 | 0.49 | neg. equity | 10-K, accn 0001616707-26-000027 |

† Nitori 売上原価 excludes rent and customer delivery — see 5a; comparable range 41–48%.
‡ COGS includes occupancy and/or shipping — the filer's own non-comparability warning applies.
§ 営業総利益 / 営業収益; there is no 売上高 line in this filer.
¶ 売上総利益 / 売上高 (¥533,107m); the operating margin uses 営業収益 because operating profit
includes 不動産賃貸収入.
** FY2026/3 売上原価 carries **+¥1,762m from a change in inventory-writedown estimate**, with gross
and operating profit each reduced by that amount — a material part of the fall from ¥42,821m to
¥16,166m.

## 5c. The row over time — which way each one is going

**[E4-32]**: *"we want the moat widened every year … that does not necessarily mean that the profit
is more this year than last year."* Direction, not level.

**Operating margin, five years each** (Nitori on the Nitori segment; the 13.4-month 51st period
marked \*):

| Company | y-4 | y-3 | y-2 | y-1 | latest |
|---|---:|---:|---:|---:|---:|
| **Nitori segment** | **19.92** | 16.47\* | 15.92 / 16.36 | 14.49 | **14.50** |
| Williams-Sonoma | 17.62 | 17.27 | 16.05 | 18.55 | **18.13** |
| Ryohin Keikaku | 9.36 | 6.61 | 5.70 | 8.48 | **9.41** |
| RH | 24.67 | 20.11 | 12.09 | 10.14 | **11.26** |
| DCM (on 営業収益) | 6.89 | 6.31 | 5.87 | 6.10 | **5.72** |
| Ingka Group | — | — | 4.53 | 2.99 | **3.53** |
| Yamada | 4.06 | 2.75 | 2.61 | 2.63 | **0.96** |
| Wayfair | −0.69 | −11.33 | −6.77 | −3.89 | **0.14** |

**Operating profit per yen/dollar of total assets, five years:**

| Company | y-4 | y-3 | y-2 | y-1 | latest |
|---|---:|---:|---:|---:|---:|
| **Nitori consolidated** | **14.79** | 14.05 | 10.31 | 7.69 | **7.99** |
| Williams-Sonoma | 31.41 | 32.13 | 23.59 | 26.98 | **26.16** |
| Ryohin Keikaku | 10.79 | 8.21 | 7.30 | 11.02 | **13.12** |
| RH | 16.73 | 13.60 | 8.83 | 7.08 | **8.01** |
| DCM | 6.82 | 5.83 | 4.61 | 5.13 | **4.62** |
| Yamada | 5.17 | 3.47 | 3.22 | 3.23 | **1.24** |

**Filer-stated ROE, the Japanese three:**

| Company | y-4 | y-3 | y-2 | y-1 | latest |
|---|---:|---:|---:|---:|---:|
| **Nitori** | **14.1** | 12.3\* | 10.1 / 11.3 | 9.5 | **9.4** |
| Ryohin Keikaku | 17.3 | 10.8 | 8.7 | 14.9 | **16.3** |
| DCM | 7.9 | 7.5 | 8.7 | 6.7 | **6.2** |
| Yamada | 7.9 | 5.0 | 3.9 | 4.3 | **2.3** |

## 5d. The same-basis growth test — [E2-44]'s second characteristic across the row

*"an ability to accommodate large dollar volume increases in business … with only minor additional
investment of capital"* **[E2-44]**. Measured over each filer's own comparable window:

| Company | window | revenue | total assets | operating profit |
|---|---|---:|---:|---:|
| **Nitori** (Shimachu inside both ends) | FYE 2022-02 → 2026-03 | **+12.4%** | **+59.7%** | **−9.2%** |
| Ryohin Keikaku (no acquisition inside) | FY2021/8 → FY2025/8 | **+72.9%** | **+43.1%** | **+74.0%** |
| DCM (營業収益; three acquisitions inside) | FY2022/2 → FY2026/2 | +21.9% | +49.4% | +1.2% |
| Yamada | FY2022/3 → FY2026/3 | +4.5% | +2.5% | −75.4% |

**Ryohin Keikaku grew revenue 73% and operating profit 74% on 43% more capital. Nitori grew revenue
12%, put 60% more capital in, and earned 9% less.** On the corpus's own second characteristic, the
nearest listed Japanese comparator passes and Nitori fails, in the same five years, on each filer's
own audited accounts.

## 5e. The physical series across the row — [E4-55] where units exist

| Company | metric disclosed | latest reading |
|---|---|---|
| **Nitori** | existing-store customers (買上客数), existing-store spend per customer | **customers 92.8% YoY; 88.7 on a FY2020 = 100 chain; spend per customer 113.0** |
| Williams-Sonoma | comparable brand revenue | +22.0 / +6.5 / −9.9 / −1.6 / **+3.5 %**; chained FY2022→FY2025 **−2.3%** |
| Ingka Group (IKEA retail) | **quantities sold, store visits** | **units +1.6%, store visits +1.3%, online visits +4.6%, revenue −0.9%** |
| Wayfair | active customers, orders delivered, average order value | **active customers 22m → 21m → 21m; orders 41m → 40m → 40m; AOV $292 → $300 → $312** |
| RH | none (comps not disclosed) | — |
| Ryohin Keikaku / DCM / Yamada | not disclosed in the 有価証券報告書 | — |

**Two of the four disclosers are doing what Nitori did — price up, units down.** Wayfair's AOV rose
6.8% over two years while orders fell from 41m to 40m and active customers from 22m to 21m. Nitori's
version is larger and longer. **One is doing the opposite on purpose**: Ingka took units up 1.6% and
let revenue fall 0.9%, and its own release frames the year as becoming *more affordable*. **And one
— WSM — has held comps roughly flat while earning the row's highest operating margin and three times
Nitori's return on assets.**

## 5f. Peers named and NOT measured, and why

1. **IKEA Japan K.K. — named, not measured. This is the most important gap in the row.** IKEA is
   Nitori's closest direct competitor in the actual market Nitori sells in, and **Ingka Group
   publishes no country segment.** Its audited annual summary gives FY25 retail sales by region only
   (Europe 73.8%, Americas 17.2%, Asia Pacific 9.0%) and top-selling countries (Germany 15.4%, USA
   12.6%, France 9.0%, UK 6.8%, Italy 5.6%) — **Japan does not appear in either list.** IKEA Japan
   K.K. is a Japanese kabushiki kaisha and files its accounts with the Legal Affairs Bureau rather
   than publishing them; it is not an EDINET filer because it has no listed securities.
   *Resolving document, named:* IKEA Japan K.K.'s 計算書類 obtained from the Legal Affairs Bureau
   (登記所) by paid request, or its 官報 decisory notice if it publishes one. **Not obtained. The
   Japanese-market half of the row is therefore incomplete and the row's own limit is recorded
   here.**
2. **Shimachu — inside the perimeter, so not a peer.** Its pre-2021 standalone accounts exist on
   EDINET (it was a filer until the 2021 squeeze-out) but the EDINET API is key-gated and the
   segment disclosure in YUHO-22 through YUHO-26 already carries it.
3. **Otsuka Kagu (大塚家具) — cannot be measured separately.** Absorbed into ヤマダデンキ effective
   **2022-05-01** and accounted for as a **共通支配下の取引 (common-control transaction)** because it
   was already consolidated from December 2019 (100% from September 2021). It has no separate
   accounts inside the window and it does not break Yamada's consolidated revenue.
4. **Tokyo Interior, Francfranc, Shimachu's private competitors, Nafco and the unlisted
   home-furnishing chains — not measured, because they are not listed and publish no accounts.**
   Nafco was taken private; Tokyo Interior and Francfranc file nothing public. Named so the row's
   coverage is honest rather than complete.
5. **Ryohin Keikaku's FY2026/8 — a completed year with no filed annual accounts.** Its FYE is
   2025-09-01 to 2026-08-31, closed 18 days ago; the latest filing is the **Q3 決算短信 posted
   2026-07-10**, and the annual 短信 and 有価証券報告書 historically arrive in October and late
   November. **Ryohin's window therefore ends one year behind DCM's and Yamada's, and this is stated
   in every table rather than papered over.**

## 5g. The row's limit, stated as the corpus requires — [E3-61]

> "In some businesses, the participants behave like a demented Kellogg. In other businesses, they
> don't. … **I think you'd have to know the people involved to fully understand what was
> happening.**"

The row shows position. It cannot show conduct, and in this industry conduct is decisive in a way
the numbers hide. **Ingka's 3.53% operating margin is not weakness; it is policy.** Ingka Holding
B.V. is owned by a foundation, reinvests 85% of net profit and pays 15% to the INGKA Foundation, and
its own summary says it *"think[s] in decades, not quarters."* It cut prices in FY2025 and accepted a
revenue decline to take units. **A competitor with no share price to defend, that has chosen price as
its weapon, is the demented Kellogg in this row** — and Munger's point is that no model predicts how
far it goes. Nitori's next five years turn substantially on a decision made inside a Dutch
foundation, and the row cannot forecast it.

---

# 6. THE THREE [E3-03] CRITERIA, ANSWERED SEPARATELY

> "An economic franchise arises from a product or service that: (1) is needed or desired; (2) is
> thought by its customers to have no close substitute and; (3) is not subject to price regulation.
> The existence of all three conditions will be demonstrated by a company's ability to regularly
> price its product or service aggressively and thereby to earn high rates of return on capital.
> Moreover, franchises can tolerate mis-management." — **[E3-03]**, 1991 letter

## Criterion 1 — needed or desired: **SATISFIED**

Furniture, bedding, kitchenware and home textiles are needed. The scale of the demand is on the
filed record: **group annual purchasing customers of 149 million** (FYE 2025-03, YUHO-25's
progress-against-2025-targets table), 22.56 million app members at the same date, 1,069 stores at
FYE 2026-03. Nothing in the record puts criterion 1 in doubt.

## Criterion 2 — no close substitute: **NOT SATISFIED.** This is the criterion that carries the weight, and it fails on the company's own evidence.

Four filed facts, all from the issuer:

1. **The company's own description of its competitive environment names no competitor and names the
   opposite of a moat.** YUHO-26's MD&A: *"家具・インテリア業界におきましては … 業種・業態の垣根を
   越えた販売競争の激化"* — intensifying sales competition **across the boundaries of industry and
   business format.** YUHO-20 said the same thing six years earlier: *"業態を越えた販売競争の激化."*
   A company whose product is thought to have no close substitute does not describe its market as one
   where the competition comes from across format boundaries.

2. **The company says its differentiated products are copied quickly.** Integrated report (rung 3,
   posted 2026-08-28), the head of its Product Development Laboratory: *"最新の情報は競合他社も入手
   できることから、独自性のある商品も短期間で模倣されることが少なくありません"* — "because the latest
   information is available to competing companies too, it is not uncommon for even distinctive
   products to be imitated in a short period." *(Extraction note, PRIME RULE 1: the second character
   of the word rendered 模倣 comes out of the PDF as an uncommon variant glyph; the sense — "imitated"
   — is unambiguous.)* The company founded the laboratory in **March 2025** specifically because of
   this, which dates the problem rather than denying it.

3. **The substitution was measured, by the customers, in the filed monthly series.** Section 4 is the
   experiment: Nitori raised spend per existing-store customer 7.2% in FY2023 and 4.2% in FY2024 as
   its import cost rose, and existing-store footfall fell 5.6% and 1.3%. Footfall is now **11.3%
   below FY2020** on a store base 43.8% larger. **A product thought to have no close substitute does
   not shed an eighth of its customers when it raises price by a tenth.** That is what substitution
   looks like when it is metered.

4. **The board's own remedy is the shelf price.** YUHO-26 makes *"①安さの実現"* the first of five
   priority tasks and commits to *"売価に還元する"* — giving the cost saving back in the selling
   price. A business with no close substitute does not have to do that.

**The one serious argument on the other side, and why it does not carry criterion 2.** Nitori is
~90% private brand and vertically integrated, and its reported gross margin (53.21%) is the highest
in the competitor row. At the SKU level there is no substitute for an N-Cool or an N-Inbox — you
cannot buy one anywhere else. But criterion 2 is a claim about **what the customer thinks when they
need the thing**, and the customer needs a sofa, not an N-anything. The filed traffic response shows
where the substitution happens: at the need level, not at the SKU level. **[E2-58]** is the right
home for this: *"In many industries, differentiation simply can't be made meaningful. A few
producers in such industries may consistently do well if they have a cost advantage that is both
wide and sustainable. By definition such exceptions are few."* Nitori looks like that named
exception. **An exception to the commodity rule is not a franchise.**

## Criterion 3 — not subject to price regulation: **SATISFIED**

No price regulation on Japanese home furnishing appears anywhere in the eight securities reports.
The eleven business-risk items of YUHO-26 are FX, overseas sourcing, quality, intellectual property,
human capital, climate, natural disaster, pandemic, information security, M&A/alliances and
compliance. **Price regulation is not among them — and neither is competition.** *(The absence of a
competition risk factor is recorded as a disclosure fact, not read as confidence: the same document's
MD&A says competition is intensifying, so the risk section and the MD&A disagree.)*

## The demonstration test, which the corpus attaches to all three: **FAILS on both halves**

> "The existence of all three conditions will be demonstrated by a company's ability to **regularly
> price its product or service aggressively and thereby to earn high rates of return on capital.**"
> — **[E3-43]**, 1991 letter

- **Aggressive pricing:** attempted FY2023-FY2024, not sustained, and now being reversed by board
  decision. Under **[E4-37]** — *"you can almost measure the strength of a business over time by the
  agony they go through in determining whether a price increase can be sustained"* — a price increase
  that has to be given back is a stronger negative than agony beforehand.
- **High rates of return on capital:** operating profit per yen of assets **16.27% → 7.99%** across
  FY2019 to FY2026; filer ROE **15.3% → 9.4%** with the equity ratio *rising* to 62.9%. **[E3-46]**
  asks this as the second question about the business, and the answer is a return that has halved.

And **[E3-43]**'s own contrast names the class Nitori belongs to:

> "In contrast, 'a business' earns exceptional profits only if it is **the low-cost operator** or if
> supply of its product or service is tight. … With superior management, a company may maintain its
> status as a low-cost operator for a much longer time, but even then **unceasingly faces the
> possibility of competitive attack.** And a business, unlike a franchise, **can be killed by poor
> management.**"

---

# 7. THE OTHER Q2 TESTS

**[E4-04] durability — the moat is not in the excluded class, and that is a real positive.** The
question the framework sets is *"does a lapse in spending destroy the structure, or merely narrow it
— and does the spending defend the same advantage, or buy its replacement?"* Nitori's spending
defends **the same** advantage: specification changes, raw-material review, new supplier sourcing,
renegotiated terms, in-house manufacture from raw materials, new production equipment, smaller
packaging, six own-built distribution centres. None of that replaces the basis of the advantage the
way a new ore body replaces a depleted one. Home furnishing is not a rapid-change industry;
**[E3-51]**'s competitive destruction does not apply. **[E4-04] does not exclude this business.**

**[E4-23] key-person dependence, and this is a moat defect not a management note.** The company
discloses it itself, in YUHO-26 risk factor ⑤:

> また、**代表取締役似鳥昭雄、白井俊之をはじめとする経営陣は、各担当業務分野において重要な役割を
> 果たしているため、これら役員が業務執行できない事態となった場合には、同様に悪影響を及ぼす可能性が
> あります。**

And the officer table shows how concentrated it is. **Akio Nitori, born 1944-03-05, is Representative
Director, Chairman and CEO of the holding company** — and simultaneously, per the same table,
**代表取締役会長兼社長 (Representative Director, Chairman and President) of 株式会社ニトリ itself since
February 2024**, of ニトリファニチャー since December 2023, of 島忠 since May 2025, and Chairman of
Ｎプラス, ニトリパブリック, オールリンク, ニトリリアルエステート, NITORI FURNITURE VIETNAM and SIAM
NITORI. He holds 17,052 thousand shares. **At 82 he has taken back the presidency of the main
operating company.** [E4-23] is explicit: *"if a business requires a superstar to produce great
results, the business itself cannot be deemed great. … The partnership's moat will go when the
surgeon goes."* And [E3-03] says franchises *"can tolerate mis-management"* — a business whose
founder must hold seven operating presidencies at 82 has not demonstrated that tolerance.

**[E4-32] direction outranks existence.** *"we want the moat widened every year … that does not
necessarily mean that the profit is more this year than last year."* The monitoring metric is the
moat's width, and where units exist the corpus says monitor units **[E4-55]**. Existing-store
footfall: **112.8 → 101.6 → 95.9 → 94.7 → 95.5 → 88.7** on a FY2020 = 100 base. **The direction is
down in four of the last five years, and 2026 is the worst of them.** There is one bright five-month
reading: FYE Mar 2027 to August, existing-store customers **100.1%**, sales 99.6%, spend per customer
99.4% — the bleeding has stopped at a level, but the level is the low one.

**[E2-53] dominance class — NOT CLAIMED.** *"Once dominant, the newspaper itself, not the
marketplace, determines just how good or how bad the paper will be. Good or bad, it will prosper."*
The evidence required is a market share and **Nitori discloses none** — the word シェア appears in
eight securities reports and one integrated report only in the phrase "performance share unit."
*Resolving document, named:* METI's 商業動態統計 (Current Survey of Commerce) furniture-retail series
would allow a share to be computed against Nitori's domestic segment revenue. **It is not fetched
here, and it would not rescue criterion 2**: a dominant share alongside an 11% footfall loss on a
44% larger store base would describe a shrinking dominance, which [E4-32] already reads as the moat
narrowing. This sub-item is therefore recorded as **not claimed**, not as an open UNRESEARCHED that
blocks the gate.

**[E3-33] / [E5-28] untapped pricing power — NOT AVAILABLE.** *"If you name some business that has
incredible pricing power, you're talking about a business that's a monopoly or a near monopoly"*
**[E5-28]**. Nitori is not near a monopoly, and the record runs the other way: it used the pricing
power it had and the customers left.

**[E2-45] the attacker's test.** *"One question I always ask myself in appraising a business is how I
would like, assuming I had ample capital and skilled personnel, to compete with it."* The honest
answer is that **an attacker is already doing it and the filed record shows it working.** IKEA's
retail owner cut prices in FY2025, took units up 1.6% and store visits up 1.3%, and let revenue fall
0.9% to do it — the exact move Nitori's board has now committed to copying. And Nitori's own
laboratory head says its distinctive products get imitated in a short period. **A business I would
not want to attack does not read like this.**

**[E4-36] the four causes, and [E3-51] the wave.** Nitori's 34-period run of rising revenue and
profit is real and rare. Ask which of the four causes produced it. Extreme maximisation of one or two
variables — the vertically integrated private-brand cost position at retail gross margins — is
clearly one of them. But there is a wave underneath it that the settlement-rate series makes
visible: **an importer that buys in dollars and sells in yen, growing through four decades of a
strengthening yen, and the FY2018-FY2021 settlement rates of 104 to 110 are the tail of that
tailwind.** The wave has reversed, and the reversal is exactly when the record broke.
**[E3-51]**: *"when a surfer gets up and catches the wave and just stays there, he can go a long,
long time. But if he gets off the wave, he becomes mired in shallows."* The framework's own gloss:
**a surfing run is not a moat; the advantage lives in the wave, not the surfer.** How much of the 34
years was the wave cannot be decomposed from the filed record — but the cost position survived a 47%
reversal, which is evidence that **some** of it is the surfer.

**[E3-61] the row's limit, and here it is the biggest single uncertainty.** *"In some businesses, the
participants behave like a demented Kellogg. In other businesses, they don't. … I think you'd have to
know the people involved to fully understand what was happening."* The row below shows position. It
cannot show conduct, and the conduct that will set Nitori's next five years belongs to **a
foundation-owned competitor whose stated policy is to cut prices and take units**, and which is not
answerable to a share price for doing it. **Ingka's 3.53% operating margin is not a measure of
weakness; it is a measure of choice**, and no row can predict how far that choice goes.

---

# 8. VERDICT

## **Q2 — IS IT A FRANCHISE? VERDICT: OUT.**

**Not UNRESEARCHED.** The competitor row that was missing has been built, from seven peers' own
filings, on the same metrics over the same windows, with the basis differences exposed rather than
averaged away. **Not UNKNOWABLE.** The question was answerable and the record answered it. **And not
IN at any width** — neither WIDE nor NARROW — because the criterion that carries the weight fails,
and it fails on evidence the company put in its own statutory filing.

**The reasoning, in one paragraph.** [E3-03] needs all three conditions. Criterion 1 (needed or
desired) and criterion 3 (no price regulation) are satisfied. **Criterion 2 — thought by its
customers to have no close substitute — is not**, and the proof is metered: when Nitori passed a 47%
rise in its own import cost through to the shelf, spend per existing-store customer rose 13% and
existing-store footfall fell to **88.7** on a FY2020 = 100 chain, on a store base 44% larger; the
company's own board now names *"the realisation of cheapness"* as its first priority and commits to
giving cost savings back in the selling price; and its own product-development head says distinctive
products *"are imitated in a short period."* **[E3-43]**'s demonstration test then fails on both
halves — the aggressive pricing was not sustained and is being reversed, and returns on capital
employed halved from 16.27% to 7.99% with the equity ratio rising. **[E4-32]** reads the direction as
down in four of the last five years on the physical series, **[E4-37]** reads a price increase that
had to be given back as worse than agony before raising it, **[E2-45]**'s attacker is already in the
market and winning on units, and **[E4-23]** is disclosed by the issuer itself in risk factor ⑤.

## What it is instead, named from the corpus

**Nitori is [E3-43]'s "a business", not [E3-03]'s franchise — specifically, a low-cost operator, and
a good one.** The corpus draws exactly this line:

> "In contrast, 'a business' earns exceptional profits only if it is **the low-cost operator** or if
> supply of its product or service is tight. … With superior management, a company may maintain its
> status as a low-cost operator for a much longer time, but even then **unceasingly faces the
> possibility of competitive attack.** And a business, unlike a franchise, can be killed by poor
> management." — **[E3-43]**

And **[E2-58]** puts the same name on it from the other side: *"A few producers in such industries may
consistently do well if they have a cost advantage that is both wide and sustainable. **By definition
such exceptions are few**, and, in many industries, are non-existent."* Nitori looks like that
exception. The cost advantage is real, it is documented, and **it survived a 47% currency reversal** —
gross margin 57.44% → 50.43% → **53.21%** while the settlement rate went 103.95 → 132.23 → 148.06.
The wide-and-sustainable cost advantage is the finding of this gate. **An exception to the commodity
rule is not a franchise, and the corpus is explicit that it faces competitive attack unceasingly.**

## The four-verdict test, applied aloud

**"Can I name the document that would resolve this?"** — asked on every gap:

| Gap | Document nameable? | Would it change the verdict? |
|---|---|---|
| **IKEA Japan K.K.'s accounts** — the one direct Japanese competitor not measured | **YES** — its 計算書類 from the Legal Affairs Bureau (登記所), by paid request; Ingka publishes no Japan segment and Japan appears in neither its regional nor its top-country list | **No.** It would size the pressure on Nitori's home market. It cannot create "no close substitute"; it can only make criterion 2 worse or leave it as found. The row's incompleteness is recorded in 5f as its own limit. |
| **Market share, for the [E2-53] dominance reading** | **YES** — METI 商業動態統計, furniture-retail series, against Nitori's domestic segment revenue | **No.** [E2-53]'s claim is that *position, not execution*, sets the economics — *"Good or bad, it will prosper."* Nitori's own filing says the opposite about itself: footfall fell because **its product and price** failed. Execution is visibly setting the economics, so the dominance reading is refuted by the record whatever the share number is. The sub-item is recorded as **not claimed**, and it does not block the gate. |
| **Overseas profit by country** (Taiwan, mainland China, ASEAN, Korea) | **NO** — the securities report is the most granular filing and presents one Nitori segment covering domestic and overseas; only YoY *point changes* appear, in the rung-3 briefing deck (mainland China operating margin +12.8pt, gross margin +2.3pt, SG&A ratio −7.4pt; Taiwan broke even in its fifth year from opening) | **No**, and it is immaterial: overseas is **7.6%** of Nitori-segment revenue. Recorded as an **UNKNOWABLE sub-item on the filed record**, not as an open work order. |
| **Decomposition of the 34-year run into wave and surfer [E3-51], [E4-36]** | **NO.** No filed document apportions a growth record between a four-decade currency tailwind and a cost position | Recorded as **UNKNOWABLE**. It does not need to be resolved: the cost position's survival of the reversal is direct evidence that some of it is the surfer, and the verdict already credits that. |

**No gap is UNRESEARCHED in a way that blocks this gate.** The two nameable documents are named and
would not move the verdict; the two unnameable ones are closed as UNKNOWABLE, and both are
immaterial to the criterion that decided it.

## What would widen the class, and what would break it further

*Recorded for the next review's monitoring list, not as a forecast.*

**Would move it toward a franchise:**
- **Existing-store customer counts rising for four consecutive quarters while spend per customer does
  not fall.** That is the one series that decided this gate, it is published monthly, and it is free.
  The five months of FYE Mar 2027 to August read customers **100.1%**, sales 99.6%, spend per customer
  99.4% — stabilised, at the low level.
- Return on capital employed recovering back through 12% of total assets as the six own-built
  distribution centres and the ¥1,004bn of owned property and investment property start to earn.
- A price increase that holds — spend per existing-store customer up with footfall flat or rising, in
  the same year.

**Would break it further:**
- The committed price reduction arriving in gross margin without the footfall returning: gross margin
  back below 50% while existing-store customers stay under 100%. That is the losing combination and it
  is directly observable.
- Ingka continuing to cut price and take units in Japan while Nitori's footfall falls again.
- The founder's departure or incapacity, which the company itself names as a risk (⑤), landing while
  he holds seven operating presidencies.
- Nitori-segment revenue falling for a third consecutive year. It has now fallen once
  (¥820,886m → ¥816,196m), and FY2027 Q1 revenue is **−2.3%** against a full-year guide of **+4.9%**.

---

# 9. WHAT THIS MEANS FOR H1

*Stated as evidence for H1, not as H1's verdict, and with no hold, sell or add language — that
belongs to a holding review.*

**Was the business judged a franchise when it was bought? No — it was never judged at all.** The
2026-07-15 entry run and the 2026-08-26 v3.1 run both returned **Gate 2 / Q2 UNRESEARCHED** with the
moat class **PROVISIONAL** and an open work order for the competitor row; the 2026-08-28 re-run
recorded the same thing unchanged. The purchase rested on the vertical-integration cost argument and
on the 53.9% gross margin, explicitly *"plausible"* and never tested against a peer. **So H1's
comparison is not "franchise then, not now."** Under the holdings framework's own split, this is the
second case: *the business was never judged a franchise, and was held for its economics* — and H1
then asks only whether the economics relied on still hold.

**The economics relied on were the cost position, and the cost position holds; the returns it
produces do not.** The 53.9% gross margin cited at purchase is **53.21%** today and survived a 47%
currency reversal, so the specific thing the purchase relied on is intact and is this gate's
strongest positive finding. **What has changed is everything the cost position was supposed to
deliver**: return on capital employed 14.79% → 7.99%, filer ROE 14.1% → 9.4%, Nitori-segment
operating margin 19.92% → 14.50%, existing-store footfall 11.3% below FY2020 on a 44% larger store
base, and the nearest listed Japanese comparator growing revenue 73% and operating profit 74% on 43%
more capital over the same five years while Nitori grew revenue 12% on 60% more capital and earned 9%
less. **[E3-30]** is therefore the live question for the reviewer and this gate does not settle it:
*"whether this erosion is just part of an aberrational cycle … or whether the business has slipped in
a way that permanently reduces intrinsic business values."* The five-month FY2027 stabilisation is the
only evidence for the aberrational reading, and five months is not an answer. **The view is weaker
than at purchase, and the weakness is in the returns rather than in the cost position.**

---

# 10. SELF-AUDIT

## Did the operator's prior hold?

**The prior was "NARROW at best." It did not hold — the record is worse than the prior, and for a
different reason than the prior gave.** The brief's reasoning was category switching costs: "a
customer walks into whichever store is convenient." **That is right about the outcome and wrong about
the mechanism.** The filed record shows the customers did not walk to a more convenient store; they
**stopped buying**, or bought cheaper — existing-store footfall fell 11.3% while Nitori itself added
44% more stores, i.e. convenience increased and traffic still fell, and in the same window the
nearest listed Japanese comparator grew 73%. Convenience is not the binding constraint. **Price and
product are**, which is what the company's own board says in its statutory filing. So: the prior's
verdict direction was too generous (OUT, not NARROW) and its stated mechanism is not the one the
record supports.

**And the brief invited exactly the refutation it should have:** it named the consecutive-profit-growth
run as the evidence that would refute a category prior, and that evidence was hunted hardest
**[E4-26]**. It is real — **34 consecutive periods**, stated verbatim in YUHO-21 — and it is the reason
this file spent as long on [E4-36] and [E3-51] as on the failure. The run did not survive the test:
it ended at 34 on a same-perimeter basis, at exactly the point the currency tailwind reversed, and
the company stopped claiming it at that point.

## The strongest single fact against my own verdict

**Gross margin recovered to 53.21% while the settlement rate stayed 42% above its trough.** A
business that absorbs a 47% rise in the yen cost of ~90% of its goods, and comes out with a higher
gross margin than it had at the bottom of the shock, has demonstrated a cost advantage that is both
wide and sustainable in [E2-58]'s exact words — and it did it while carrying a low-margin home-centre
acquisition inside the denominator. **If I am wrong, this is where the error is:** I have read the
margin recovery as a cost achievement and the traffic loss as a franchise verdict, when they could
instead be read as one business deliberately trading volume for margin through a shock it survived
better than anyone else in the row, with the volume recoverable now that the price reduction is
funded. The FY2027 five-month reading — customers **100.1%**, gross margin in Q1 **53.63%** against
53.43% a year earlier — is consistent with that reading. **Five months is not a cycle, and I have not
treated it as one; but it is the fact that would start to overturn this verdict, and it is pointing
the wrong way for me.**

The second-strongest: **Nitori's operating margin is still the second highest of the eight peers
measured**, ahead of Ryohin Keikaku (9.41%), RH (11.26%), DCM (5.72%), Ingka (3.53%), Yamada (0.96%)
and Wayfair (0.14%), and behind only Williams-Sonoma (18.13%). An OUT verdict on a business with the
row's second-best margin needs the direction and the return-on-capital evidence to carry it, and it
does carry it — but the level is a real argument on the other side and is recorded as such.

## Protocol check

- [x] **Q2 only.** No owner earnings, no price, no value, no multiple, no band, no entry or exit
      language, no H1 verdict, no hold/sell/add recommendation.
- [x] **Competitor row built and computed by me**, same metrics, each cell sourced, basis differences
      exposed (5a) rather than averaged. Seven peers measured, five named and not measured with the
      reason for each (5f). Row's limit stated per **[E3-61]** (5g).
- [x] **Every judgment carries a ledger id, and every id was checked against `principle_ledger.csv`
      before citing.** Ids used: E3-03, E3-43, E2-44, E2-45, E2-53, E2-58, E3-28, E3-30, E3-33,
      E3-46, E3-51, E3-61, E4-04, E4-23, E4-26, E4-27, E4-32, E4-36, E4-37, E4-55, E5-28, E3-41.
      Each was read from the ledger this session; none is cited from memory. **[E4-52] was not used**
      — it is the lollapalooza row, not a pay row, per the brief's own warning.
- [x] **Rungs stated for every figure**; rung-3 items (settlement rate, monthly customer series,
      briefing-deck overseas point changes, integrated-report quote) flagged as rung 3 at every use.
      Nothing rung-1 is presented as rung 3 or the reverse.
- [x] **Accounting-basis change handled**: J-GAAP and IFRS both shown for FY2024; the 13.4-month 51st
      period excluded from length-dependent comparisons and flagged wherever it appears; the two
      peer revenue-recognition discontinuities (Ryohin at FY2022/8, DCM at FY2023/2) recorded in
      `peers_jp.md` and the affected earliest columns not used for any single-year claim.
- [x] **Perimeter dated** (section 2) and the Shimachu contamination of consolidated gross margin
      isolated by running every franchise judgment on the Nitori segment.
- [x] **Rule 4 cross-check** performed on Nitori (FY2026 revenue and gross profit in two
      independently prepared places) and on each Japanese peer (every overlapping year agreed across
      two separate filings).
- [x] **Pre-registration written before any figure was computed** (head of file), and the test was
      framed to refute the operator's prior rather than to confirm it.
- [x] **PRIME RULE 1**: one extraction artifact flagged (the glyph for "imitated" in the integrated
      report), not smoothed.

## Defects in the brief, and in the tooling

1. **The brief's [E3-03] emphasis was right and its candidate peer list was half wrong.** It offered
   "Sekisui House interiors or other listed home-furnishing lines if the filings name them" — **no
   Japanese peer is named in any of Nitori's eight securities reports.** The filings name no
   competitor at all; they describe the environment as *"競争の激化 across the boundaries of industry
   and business format."* Sekisui House was not pursued because it is a housebuilder, not a
   home-furnishing retailer, and would have been a category error in the row. The brief's Ryohin
   Keikaku / DCM / Yamada were correct and were measured.
2. **The brief asked for peers "Nitori's own filings name as a competitor." The answer is none**, and
   that absence is itself Q2 evidence: YUHO-26 lists **eleven** business risks and **competition is
   not among them**, while the same document's MD&A says competition is intensifying. The risk
   section and the MD&A disagree, and the brief had no slot for that finding.
3. **The 2026-08-28 file's EDINET problem was solved from the wrong end, and the earlier session's
   note should be corrected in the record.** It named three routes (a browser session on the IR
   library, a free API key, the EDINET full-text viewer). **The actual route needed none of them: the
   Japanese IR library page `/ir/library/security.html` serves all eight annual securities reports as
   plain static links.** The earlier session searched `/en/ir/library/`, which carries only the
   translated financial-statements extract. The lesson generalises to every Japanese name: **check
   the Japanese IR tree before concluding the filing is unreachable.** The subagent found the same
   pattern for Ryohin Keikaku and DCM behind the eir-parts (Pronexus) widget, whose document index is
   a plain JSONP file (`announcement_NN.js`) listing every filing back to 1996 with direct PDF URLs.
4. **The standing Q4 work order from 2026-08-28 is now answerable, and the answer is no.** That run
   named *"the Japanese securities report's capex-by-purpose disclosure (EDINET)"* as the document
   that would split maintenance from growth capex. **The document has now been fetched and read.
   YUHO-26 §第３ 1【設備投資等の概要】gives capex by segment only — Nitori segment ¥43,490m of a
   ¥43,844m total — and describes the purpose qualitatively: *"主に店舗や物流センターの新設、来期以降の
   出店に係るもの"* (mainly NEW stores and NEW distribution centres, and items relating to openings from
   next year onwards). There is no quantified maintenance/growth split.** The named document does not
   resolve the item, so it moves from UNRESEARCHED toward UNKNOWABLE on the filed record. **This is
   recorded as a correction to the standing work order and nothing more — the capex split is a Q4
   input and is out of this gate's scope, and no owner-earnings consequence is drawn here.**
5. **Tooling gap, no fix attempted:** `tools/run.py` and `tools/screen.py` are built on SEC XBRL and
   have no path for a non-SEC filer. Every figure in this file was fetched by hand or by scripts
   written in `_research 2026-09-18 NCLTY/`. That is a friction observation, not a request — a tool
   that fetched Japanese filings would get the same numbers sooner, but it would also be the first
   tool in the kit that has to parse Japanese, and it adds no number.
6. **One brief instruction could not be honoured as written.** It asked for "the last five years" of
   peer data on a common window. **Ryohin Keikaku's FYE 2026-08-31 closed 18 days ago and nothing is
   filed** — the annual 短信 historically arrives in October and the 有価証券報告書 in late November.
   Its window therefore ends one year behind DCM's and Yamada's, and that mismatch is printed in
   every table rather than hidden by relabelling.
