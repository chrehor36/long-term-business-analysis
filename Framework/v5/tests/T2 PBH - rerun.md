# Company Run — Prestige Consumer Healthcare Inc. (NYSE: PBH) — 2026-10-06
**T2 TEST RE-RUN under `Framework/v5/tests/T2 PROTOCOL - the four re-runs of 2026-10-06.md` and
`Framework/v5/tests/RULES UNDER TEST 2026-10-06 - sections D and H.md`. A test record: it binds nothing, enters no register and
changes no verdict of record.** Framework v5 (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`.
The run form is the one fifteen test runs used; the template's header names `Framework/v5/tests/PROTOCOL - running a name under the
v5 drafts.md`, which the T2 protocol's blind rule forbids this analyst to open, so it was not opened. Fill top to bottom; every
judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. Copied from the template before any fetch.

**POSITION NOTE, declared before any verdict:** not checked. The T2 protocol's blind rule forbids opening `PORTFOLIO.md`, any
holding review and any register; whether the operator holds or wants this name is unknown to this analyst and was not sought.

**CONTAMINATION, declared before any verdict.** Seen by accident and not used: (1) the git status shown at the session's start
listed the file names `Framework/v5/tests/T2 ENSG - rerun.md` and `Framework/v5/tests/T2 RYZ - rerun.md` (names only), several
`Test Runs/_research 2026-09-26 <TICKER>/` folder names including one for CHD, a competitor used here (names only, no content);
(2) the recent commit subjects shown there, one of which reads "ABG and PBH re-look alerts", which implies that a prior run of this
name exists with alert levels; nothing of its content was seen; (3) the memory index shown at the start, which says a count of
gate-clearers and "nothing buyable" without naming any company; (4) after the Q2 commit, `git log --oneline -1` returned the
subject of another analyst's parallel test re-run, "T2 ENSG: Q1 closed IN at low precision; the rate path carried to Q2 and Q9",
a verdict on another company, seen and not used. None of these entered any judgment below.

**A defect in the commit instruction, found at the first commit.** The T2 protocol's pathspec names the working folder
`Framework/v5/tests/_work_T2_PBH`, but the repository's `.gitignore` (line 117, `Framework/v5/tests/_work_*/`) ignores every
such folder, so git refuses the path and nothing in it can be committed without `-f`. The run file is committed alone, with its
own pathspec; the working folder's arithmetic (`q7_arith.py`) and check script (`check_run.py`) are reproduced in this file so
that the record does not depend on an ignored folder.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $46.16 (close 2026-10-06; aggregator, Yahoo chart via `tools/sources.py`, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 47,374,522 shares of common stock, par $0.01, one class, as of 2026-07-31
  (Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0001295947-26-000042`; `python Screens/cover_shares.py PBH`
  returned the same count). The charter authorises 5.0 million preferred shares, none issued (same 10-Q, Note 10). The balance-sheet
  issued count is 56.312 million with 8.940 million in treasury at 2026-06-30 (same 10-Q): 56.312 less 8.940 is 47.372 million,
  consistent with the cover. The proxy counts 47,372,166 shares outstanding at 2026-06-10 (DEF 14A filed 2026-06-29, accession
  `0001295947-26-000021`). No 8-K or prospectus after the 10-Q changes the count.
- **Market cap:** $2,186.8M (47.374522M × $46.16).
- **Sovereign for the earnings currency:** USD 5.66%, the US Treasury 30-year par yield, 2026-10-05 (issuing authority;
  `python tools/sources.py`). The earnings currency is USD (the filer reports in USD; 84% of revenue is North American).
- **Filings read** (operator rule 4): Form 10-K for the fiscal year ended 2026-03-31, filed 2026-05-14, accession
  `0001295947-26-000016` (the "FY2026 10-K"); Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession
  `0001295947-26-000042`; DEF 14A filed 2026-06-29, accession `0001295947-26-000021`; the 8-Ks of 2026-03-20 (the Breathe Right
  agreement and press release, `0001104659-26-032332`), 2026-06-16 (closing and the term loan, `0001104659-26-074259`), 2026-07-06
  (LaCorium and the notes offering, `0001295947-26-000029`), 2026-07-15 (the 6.25% notes indenture, `0001104659-26-083872`) and
  2026-08-14 (an officer's retirement, `0001295947-26-000049`); the 8-K/A of 2026-06-30 with the audited statements of the acquired
  business and the pro forma (`0001295947-26-000025`, exhibits 99.1 and 99.3) and the 8-K/A of 2026-07-09 (`0001295947-26-000032`);
  the fourth-quarter earnings release furnished with the 8-K of 2026-05-13 (`0001295947-26-000013`, exhibit 99.1); and, for the span,
  the 10-Ks for FY2024 (`0001295947-24-000017`), FY2022 (`0001295947-22-000015`), FY2020 (`0001295947-20-000018`), FY2018
  (`0001295947-18-000013`) and FY2016 (`0001295947-16-000051`). Fiscal years end March 31; "FY2026" is the year ended 2026-03-31.
  **One figure cross-checked against the filed statement:** net cash provided by operating activities for FY2026, $257,627 thousand
  on the filed Consolidated Statement of Cash Flows (FY2026 10-K), against the XBRL fact of $257.6M that `tools/run.py` printed:
  they agree. A second: total revenues FY2026 $1,088,705 thousand on the filed Consolidated Statement of Income, against the
  XBRL $1,088.7M: they agree.
- `python tools/run.py PBH` arithmetic lines only (USD millions, as filed; its yield, growth and "owner earnings" lines are v4
  rule lines and were not used, per Part VII): OCF FY2024 248.9, FY2025 251.5, FY2026 257.6; SBC 14.0, 11.2, 10.8; D&A 30.7, 30.2,
  31.3; capex 9.6, 8.2, 11.2; finance-lease principal 2.8, 4.5, 2.5 (financing section). Its ten-year balance-sheet table is read
  at Q4. The five-year window this run uses (FY2022 to FY2026) was completed from the FY2024 10-K (FY2022 SBC $9,039 thousand,
  FY2022 and FY2023 OCF and capex on its cash-flow statement) and the XBRL facts (finance-lease principal FY2022 2.6, FY2023 2.8;
  interest paid FY2022 61.4, FY2023 54.2, FY2024 63.2, FY2025 47.8, FY2026 43.8, the last three also on the FY2026 10-K's
  supplemental cash-flow line "Interest paid").
- **The business, in the filer's words** (FY2026 10-K, Item 1): the development, manufacturing, marketing, sales and distribution
  of brand-name OTC health and personal care products to mass merchandisers, drug, food, dollar, convenience and club stores and
  e-commerce, in North America, Australia and other international markets; two reportable segments, North American OTC Healthcare
  (83.9% of FY2026 revenue) and International OTC Healthcare (16.1%). Third-party manufacturers "fulfill most of our manufacturing
  needs"; 95 of them at 2026-03-31, 18 under long-term contract producing items that were about 60% of gross sales; one privately
  owned pharmaceutical manufacturer produced products that were about 21% of gross revenues in each of FY2026 and FY2025 (and 20% in
  FY2024); three owned plants (United States, Canada, Australia) make about 21% of gross revenues. Walmart was about 20%, 19% and 20%
  of gross revenues in FY2026, FY2025 and FY2024 and Amazon about 15%, 14% and 11%; at 2026-03-31 about 18% of receivables were owed
  by the two. The five top-selling brands were about 38% of gross revenues in FY2026 (Note 19). About 890 employees.
- **What happened after the fiscal year.** On 2026-06-12 the company bought Breathe Right and other brands (Dimetapp, Anbesol;
  the "OTC Wellness Business") from Foundation Consumer Brands for $1,045.0M in cash, funded entirely by a new $1,045.0M term loan
  at Term SOFR plus 2.00% due 2033-06-12 (10-Q Notes 2 and 8; 8-K of 2026-06-16). On 2026-07-01 it bought LaCorium Health
  (Australian skin-care brands) for about $150.0M, with a further $95.0M drawn on the term loan and cash on hand (10-Q Note 18).
  On 2026-07-15 it issued $400.0M of 6.25% senior notes due 2034 and redeemed the $400.0M 5.125% notes due 2028 (10-Q Note 18;
  8-K of 2026-07-15). Debt went from $1,000.0M face at 2026-03-31 to about $2,140M face after these events; the run values the
  company as it stands today, with these deals and this debt (Q7, rule under test, sections D(c) and H).

## THE FOUNDATIONS (not a gate)
Three foundations bear. **A share is a business**: the question is whether I would be content to own this if the market closed
for years **[M1997-109]**, and the answer turns on what the brands will earn, not on the quotation; the stock has fallen from
$85.97 at 2025-03-31 to $46.16 (aggregator closes, flagged), and the rows say appreciation or its reverse "is never a reason to buy
it" **[L2013-007]**. **The market serves**: a price that has halved tells me only the price **[M2006-077]**; the facts and reasoning
come from the filings. **Who is paid to tell you**: the rows refuse the seller's projection of what he sells **[M2011-083]**, and every figure the
company features beside GAAP (adjusted EPS, adjusted EBITDA, its "organic" revenue, the deal multiple it quotes) is read as such. No macro
view enters; the tariff and energy-cost paragraphs of the 10-K are read only as properties of the business **[M2000-094]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) revenue fell 4.3% in FY2026 to $1,088.7M, the North American
segment 4.8%, mostly a Clear Eyes supply failure the filer says will continue (FY2026 10-K, MD&A; earnings release); (2) over ten
fiscal years the company has written down brands it bought by about $713M in total (FY2018 $99.9M Beano and Comet; FY2019 $229.5M
Fleet, DenTek, Efferdent/Effergrip and others; FY2022 $1.1M; FY2023 $370.2M Summer's Eve, DenTek, TheraTears and goodwill; FY2025
$12.5M; the FY2018, FY2020, FY2024 and FY2026 10-Ks); (3) Walmart and Amazon are 35% of gross revenues and Amazon's share has
risen from 11% to 15% in two years; (4) the company has just borrowed $1,140M at floating rates to buy brands at the top of its
own ten-year price history for brands, with net debt now about equal to its market value; (5) owner cash before interest has not
grown over the five-year window (Q7's table).

## THE STANDING RULE
The buyer's own conduct, not the target's: nothing here would be bought on borrowed money or sized so that a fall could force a sale
**[L2014-005]**, **[M2012-081]**; the target's own leverage, which is large after June 2026, is the business's risk and is weighed at
Q9 and priced at Q7 on the all-equity basis (rule under test, section H), not treated as the buyer's **[L2017-004]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it, applied to the filings.** Understanding means "a reasonable fix on about what the earning
  power and competitive position will look like in five or 10 years" **[M2012-065]**, and the forecast here is about customers,
  not technology **[M2017-019]**: whether people will keep asking for Monistat, Dramamine, BC and Goody's, Fleet, Chloraseptic,
  Compound W, Debrox, Summer's Eve, Clear Eyes and TheraTears by name at Walmart, Amazon and the drug chains, and whether the
  retailers will keep giving the brands the shelf. The products are ordinary (eye drops, enemas, lice treatment, headache powders,
  motion-sickness tablets, feminine washes), the regulation is the FDA monograph system "initially established in 1972" (FY2026
  10-K, Item 1), and the operating model is simple: the company owns trademarks, buys finished goods from 95 contract manufacturers
  and three small plants, ships from one third-party warehouse, and spends 13.7% of revenue on advertising (FY2026: $148.8M on
  $1,088.7M). The key variables **[M1998-044]**: (a) the brands' hold on the consumer against private label and the retailer's own
  pressure, the filer naming "private label" products of the major chains as continued competition and the customers' demands for
  "lower pricing, better terms, additional trade spend" (Item 1A); (b) the share of sales that moves to e-commerce, where
  "platform policies, fee structures, fulfillment requirements, and algorithmic changes" are "outside of our control" (Item 1A);
  (c) the third-party supply chain, which failed in eye care in FY2025 and FY2026; (d) the price paid for the next brand, since the
  company "has a history of growth through acquisitions" (Item 1). The past statements do tell me what the future ones will look
  like **[M2008-033]**: ten years of the same gross margin band (57.9% in FY2016, 54.7% in FY2026), the same advertising ratio, the
  same tiny capital spending, and a revenue line that moves with acquisitions and divestitures and little else.
- **How far off could I be** **[M2011-084]**: the ten-year economics of a basket of small #1 OTC brands can be pictured within a
  band, and the band's edges are the retailer and the platform. That is the forecast the Kraft Heinz row warns about, "what the
  retailer is" **[M2019-041]**, and it is carried to Q2 as the castle question, not as a reason the business cannot be read. The
  insiders would write this forecast down: the filer itself writes a "long-term organic sales growth target of 2-3%" (press release
  of 2026-03-20) and a three-year outlook (earnings release of 2026-05-13), which is the opposite of the technology case where "That's
  too hard" **[M2000-105]**. The doubt test **[M2002-092]** is applied: I have no doubt that this is a consumer-brands business
  inside the circle a reader of consumer filings can draw; the doubt I have is about the castle, which is Q2's.
- **Routing.** Not an industry that changes fast; not a bank; not a holding company. A business of parts: the two segments sell
  the same kinds of brands through the same kinds of retailers and the International segment is 16% of revenue; both are read under
  the same forecast (the parts table is at Q2).
- **VERDICT: IN.** The filings let me foresee the shape of the economics ten years out for a business whose product is plain and
  whose variables are customers and retailers **[M2000-037]**, **[M2017-019]**; "unless it's going to be in a business that I think
  I can understand, there's no sense looking at it" **[M1995-051]**, and this one can be understood. Filing facts: Item 1 and Item
  1A of the FY2026 10-K (`0001295947-26-000016`).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question starts from the attacker **[M1995-038]**: these are small brands in small categories, and the reason the castle
still stands is that the categories are too small for the attacker with money to bother with and the brands have been there
longest. The tests, each with its filing fact (the FY2026 10-K, `0001295947-26-000016`, unless another is named):

- **The attacker with money** **[M2011-015]**. Twelve of the seventeen major brands hold the #1 position in their IRI segment
  (analgesic powders, medicated sore-throat liquids, wart removal, ear-wax removal, motion sickness, adult enemas, upset-stomach
  remedies, vaginal anti-fungal, lice treatment, feminine hygiene; Fess and Hydralyte in Australia), and brands with a #1 position
  were 63.7% of revenue in FY2026, up from 58.6% in FY2024 (Item 1). The categories are tiny: Analgesics $108M, Oral Care $87M,
  Cough & Cold $77M of North American revenue. Munger's row names exactly this shape, "very small markets that aren't really too
  attractive to anybody with any sense to enter" **[M2011-017]**; a competitor with $1B could build a national brand of ear-wax
  drops but would not earn its money back on a $30M category. The 10-K's own list of branded competitors is the giants (Haleon,
  Kenvue, Bayer, P&G, Reckitt, Unilever), who compete in the large categories and not, on the evidence of the market positions, in
  these. *Against:* the attacker that does bother is the retailer's own label, which the 10-K names as "continued competition
  from 'private label' products introduced by major retail chains" and expects to increase "during an economic downturn or periods
  of high inflation" (Item 1, Competition).
- **Pricing power and the agony before a rise** **[M2005-020]**. Through the inflation of FY2022 to FY2025 gross margin held in a
  band: 57.1% (FY2022), 55.5% (FY2023), 55.5% (FY2024), 55.8% (FY2025), 54.7% (FY2026), the last year's drop attributed by the filer
  to lower revenue and the costs of the acquired Canadian plant (FY2024 and FY2026 10-Ks, MD&A). The 10-K says prices to customers
  were raised to offset input costs (Item 7, Inflation) and reports supplier price increases "frequent" in inflationary periods
  (Item 1). The margin held while input costs rose is the row's test passed, "over time the businesses with strong competitive
  positions manage to pass through increases in raw material costs" **[M2005-017]**. *Against:* the North American contribution
  margin (gross profit less advertising) is 41.6%, down from 42.4% in FY2022 (FY2022 10-K segment note: $410.0M on $967.9M), and
  FY2026's price held partly by cutting advertising from $155.7M to $148.8M.
- **Unit volume and share of mind** **[M1999-054]**. The filer discloses no unit volumes; the category revenues of the deciding
  segment over the window (the FY2022, FY2024, FY2025 and FY2026 10-Ks, MD&A, USD millions, FY2021 to FY2026): Women's Health
  252.5, 249.1, 231.8, 217.1, 216.3, 205.1; Analgesics 117.8, 117.9, 116.6, 112.0, 112.2, 108.3; Cough & Cold 56.2, 86.9, 100.2,
  93.6, 82.5, 76.9; Oral Care 88.9, 85.2, 85.5, 83.2, 81.9, 87.0; Dermatologicals 104.0, 117.2, 119.8, 123.3, 120.8, 116.6;
  Gastrointestinal 124.8, 152.2, 157.0, 160.9, 174.9, 179.3; Eye & Ear 99.8, 149.5 (TheraTears bought 2021-07-01), 151.9, 156.6,
  158.9, 126.1 (the Clear Eyes supply failure). North American total 849.3, 967.9, 973.8, 958.3, 960.0, 913.6. With prices
  raised through the period, the largest category (Women's Health: Summer's Eve, Monistat) has lost 19% of revenue in five
  years and so more of its units; Analgesics and Cough & Cold are losing units; Gastrointestinal (Fleet, Dramamine, Gaviscon) is
  the one growing castle. The volume test is the one this castle fails in its largest room: "we want a lot more unit cases sold"
  **[M1999-054]**; what the rows allow is the Duracell case, unit declines in a business that still does fine **[M2015-066]**,
  and that is where this evidence sits, slow decline with the price held, not the newspaper's collapse **[L2006-009]**.
- **The low-cost position** **[M2018-043]**. Not claimed on the evidence: the company buys finished goods from contract
  manufacturers and its "low-cost operating model" (Item 1) is low overhead (890 employees, capex 1% of sales), not a cost
  advantage in the product. Its competitive strength is the brand, not the cost.
- **The brand in the customer's mind, and against the retailer** **[M2015-038]**, **[M2001-090]**. The brands carry a 55%
  gross margin on products whose ingredients are commodity (monograph drugs, saline, powders), which is the premium a name earns
  over the store's own label; eleven of the trademarks are over a century old or near it (BC and Goody's over 90 years, Fleet
  since 1869, Luden's over 130 years, Item 1). *Against:* the retailer's hand is the strongest fact in the file. Walmart 20% and
  Amazon 15% of gross revenues, Amazon up from 11% in two years; the 10-K says customers "have sought to obtain lower pricing,
  better terms, additional trade spend"; e-commerce platform positioning is "outside of our control" (Item 1A). This is the
  Kraft Heinz lesson, underestimating "what the retailer is" **[M2019-041]**; it does not fail the test today (the margin holds)
  but it is the direction of the threat.
- **Would the customer still choose it over the low bid** **[M2017-009]**. For the products the customer buys in discomfort or
  for a child (Monistat, Dramamine, Debrox, Nix, Fleet, Boudreaux's Butt Paste), the evidence of a held premium says yes; for
  washes, cough drops and eye drops the private label sits beside the brand on the same shelf, and the category declines above
  say some customers take the lower bid. Mixed, and the deciding part's margin says the majority still choose the name.
- **Ask the competitors** **[M1999-130]**. Scuttlebutt is not on the public record; what the rivals' filings say is below.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Narrowing at the edges. The ten-year record of brands bought and
  written down (foundations, item 2) is the record of castles that were smaller than the buyer thought: Fleet, DenTek and
  Efferdent in FY2019; Summer's Eve, DenTek and TheraTears in FY2023, Summer's Eve on "our reassessment of the long-term sales
  projections of this brand" (FY2024 10-K, MD&A). Against that, the share of revenue from #1 brands has risen, GI grows, and the
  margin holds. The notch the newspaper rows describe **[L1995-023]** has been taken in Women's Health; it has not been taken in
  the business as a whole.
- **What could destroy it, five to fifteen years out** **[M2000-014]**. The platform: if Amazon's share keeps rising and its
  own labels and search placement take the brand's shelf, the margin follows the volume. The supply chain: 79% of product is made
  by third parties, one of them 21% of revenue, and eye care supply failed for two years and cost about $33M of revenue in FY2026
  alone (MD&A), with the filer buying the supplier to mend it. Regulation: the monograph framework can change by FDA order
  (Item 1). Would the business be started today **[L2006-008]**? Yes: OTC brands are still being bought and sold at eleven times
  EBITDA by informed buyers, including this one.

**The competitor row** (same metric, operating margin and the ten-year shape, from the rivals' own filings; USD millions unless
stated; XBRL first-filed vintages read against the filings named): **Church & Dwight (CHD)**, operating margin 2016 to 2025:
20.7%, 19.4%, 19.1%, 19.3%, 21.0%, 20.8%, 11.1% (2022, an impairment year), 18.0%, 13.2%, 17.4%; 2025 operating income $1,077.6M
on revenue $6,203.2M, equity $4,002.2M and long-term debt $2,205.1M (10-K for 2025, `0001193125-26-048139`; 2016 `0001564590-17-002326`;
2020 `0001564590-21-006669`). **Kenvue (KVUE)**, operating margin 2022 to 2025: 17.9%, 16.3%, 11.9% (2024, with a $479M intangible
impairment), 16.0% (10-K for 2025, `0001944048-26-000030`; 2023 `0001944048-24-000057`); a 2023 spin-off, so no cycle of its
own. **Perrigo (PRGO)**, the store-brand maker, operating margin 2016 to 2025: a loss of $2.0B on $5.3B of revenue (2016), then
12.1%, 5.0%, 4.2%, 2.3%, 9.9%, 1.8%, 3.3%, 2.6%, and a loss of $1.1B in 2025 with a $1.3B goodwill impairment; net losses in
seven of the ten years (10-K for 2025, `0001585364-26-000009`; 2016 `0001585364-17-000071`; 2020 `0001585364-21-000012`).
**Haleon (HLN)**: files a Form 20-F, not a 10-K, in IFRS and pounds sterling, flagged; operating margin 2021 to 2025: 17.2%,
16.8%, 17.7%, 19.6%, 21.9%; 2025 operating profit £2,412M on revenue £11,030M, equity £16,484M and borrowings £8,609M (20-F for
2025, `0001104659-26-027443`; 2021 in the 20-F `0001558370-23-004167`). **Reckitt** is not an SEC filer and is not compared.
**PBH** on the same metric, FY2017 to FY2026: 23.3%, 20.7%, 6.9% (FY2019 impairments), 30.2%, 31.5%, 30.4%, a loss of $22.4M
(FY2023 impairments), 30.4%, 29.6%, 28.4%; ten-year operating income $2,174M on revenue $10,344M, 21.0% with every impairment
charged. Read together: the branded OTC owners (CHD, Haleon, Kenvue, PBH) earn 16% to 30% operating margins through a full
cycle and all of them write down brands they bought; the store-brand maker earns almost nothing. The field is the
"Buy commodities, sell brands" formula **[L2011-008]**, and the low bid's side of it is a poor business.

**The parts table** (five-year contribution margin, the filer's segment measure, FY2022 to FY2026, from the FY2024 and FY2026
10-Ks' segment notes): North American OTC Healthcare $410.0M, $408.0M, $397.4M, $401.7M, $380.0M, total $1,997M, 85% of the
five-year total; International OTC Healthcare $53.3M, $72.2M, $73.7M, $77.0M, $66.8M, total $343M, 15%. The North American
segment decides (more than half; section B). Its castle: standing, narrowing at the edges, as the tests above read it. The
International part (Hydralyte, Fess, Australia) does not decide; its castle is the same kind and is read the same way.

**The field's returns over the last full cycle, judged in words** (section C). The capital the business needs is small: at
2026-03-31 PBH's property, plant and equipment, inventory and receivables together are about $0.42B against operating income of
$309M (FY2026 10-K balance sheet), so the return on the tangible capital actually needed **[M2010-090]** is far above ordinary;
the rivals' filings show the same shape, Church & Dwight earning $1.08B of operating income on $6.2B of revenue with capex of
$122M. What is ordinary is the return on the price paid for the brands: PBH's FY2026 operating income of $309M on equity plus
debt of $2.88B is 10.7% before tax; Haleon's is 9.6% on the same measure; CHD's 17.4%. The rows say to forget purchased goodwill
when judging the business and to include it when judging the capital allocation, "because we paid for it" **[M2011-060]**, so
the field's castle protects excellent returns on the capital inside the castle, and the ordinary return on the goodwill is a
question for Q6 and Q7, not an OUT here.

- **The routing.** A castle shown open closes OUT; one whose future cannot be judged closes TOO HARD **[M2000-019]**. Neither
  applies on the evidence: the future can be judged (slow volume decline in the older categories, growth in the gastrointestinal
  one, a price held through inflation, a retailer whose weight grows), and it is not shown open, since the margin that measures
  the brand's premium has not moved. What the evidence does say is that the castle will not grow by itself, which Q7 carries as
  the growth shown (rule under test, section D(b)), and that the price must compensate for the notch.
- **VERDICT: IN**, with the narrowing written down. The castles of the deciding part stand on small-category leadership that
  "anybody with any sense" would not pay to attack **[M2011-017]**, on a premium held through an inflation **[M2005-017]**, and
  on names the customer has asked for across generations **[L1996-028]**; the evidence against is the slow loss of units in the
  largest category, the retailer's rising hand **[M2019-041]**, and the ten-year record of brands written down, carried forward
  as contrary evidence **[M1997-127]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed.** The capital inside the business is working capital and three small plants: at
  2026-03-31 receivables $191.9M, inventory $159.1M, property, plant and equipment about $70M (the FY2026 10-K balance sheet;
  `tools/run.py`'s ten-year table), about $0.42B before payables, against FY2026 operating income of $309.4M and the window's
  operating income of $297M to $342M in the four unimpaired years. Measured as the rows measure it, on tangible assets
  **[M2011-060]**, **[M2014-007]**, the return is far above any ordinary figure, and the window's figures carry no cyclical peak
  and no leverage inside them **[L1994-009]** (the leverage is in the capital structure, Q9). Read with care: the equity on which
  "return on equity" would be computed is itself the price paid for brands, $2.88B of goodwill and intangibles against $1.89B of
  equity, so the business's own return and the acquirer's return are two different numbers **[M2010-090]**.
- **Reinvestment to stand still.** Almost none. Capital spending was $9.6M, $7.8M, $9.6M, $8.2M and $11.2M in FY2022 to FY2026
  against depreciation of $8.0M, $7.7M, $8.2M, $9.7M and $10.1M (the FY2024 and FY2026 10-K cash-flow statements and
  depreciation notes; XBRL `Depreciation`); the rest of D&A ($18M to $22M a year) is amortization of purchased tradenames and
  customer relationships. The 10-K gives no maintenance split; the filing therefore does not allow the maintenance guess the rows
  entitle an owner to **[M2000-144]**, and the all-spending case is the only case (rule under test, section D(e), applied at Q7).
  The cash does come out: operating cash flow of $230M to $260M a year against capex near $10M is the business "which drowns in
  cash" **[M2008-036]**, not the one whose profit "just sits there" in the yard. Working capital grew with the inventory build
  of FY2023 (inventory $120M to $162M as supply tightened, FY2024 10-K) and has held near 14% of revenue since; the increase is
  inside operating cash flow and is treated as capital spending there (rule under test, section D(d)).
- **Reinvestment to grow, and what it earns.** This is where the capital goes: the company has bought brands for about $3.5B
  since FY2015 (Insight $745.9M in 2014, DenTek $226.9M in 2016, Fleet $823.7M in 2017, the Akorn consumer brands $228.9M in 2021,
  Hydralyte rights, Pillar5 and smaller purchases, and now Breathe Right $1,045.0M and LaCorium about $150M; the FY2016, FY2018,
  FY2020 and FY2024 10-Ks and the 10-Q `0001295947-26-000042`) and has written down about $713M of what it bought. The return
  on the latest dollar is stated by the filer's own figures: $1,045.0M for a business whose audited year to 2025-12-31 earned
  $60.3M of income from operations before any tax, $89.8M before the seller's amortization (8-K/A `0001295947-26-000025`,
  exhibit 99.1), which is 8.6% before tax on the price, about 6.5% after tax at the filer's 24% blended rate before the tax
  deductibility of the purchase price; and LaCorium at about $150M for a business with about $40M of trailing revenue and a
  profit the filer gives only as a projection "including the benefits from anticipated synergies" (earnings release of
  2026-05-13), which the rows refuse to use **[M1995-050]**. That is the second-best business of the 1998 passage **[M1998-081]**
  at best, growth that "takes more money", and whether the rate is "very satisfactory" the figures above answer: it is a fair
  rate on purchased goodwill, not a rich one, in a world of 5.66% long bonds. Growth without acquisitions has not come: the
  North American segment's revenue was $967.9M in FY2022 and $913.6M in FY2026 (Q2's table), so the organic business is the
  See's case without See's growth, a castle that "can't rationally be expanded very much" in its own categories, which the
  rows accept as a limit and warn against talking oneself out of **[M1997-072]**.
- **The growth arithmetic and its caps.** The owner-cash series of the window carries a growth shown of −1.7% a year on the
  all-equity basis (Q7's table), so no cap is reached: no rate above the discount rate is carried **[M1997-095]** and nothing
  traces to an absurdity **[M1999-067]** (rule under test, section D(f)). The filer's own three-year outlook of "an approximately
  10% annual CAGR for revenue growth" (earnings release of 2026-05-13) is acquisition growth bought with $1.2B of new debt and is
  not credited: "we're not earning a higher rate of return on capital than we were when we started. We just put way more capital
  into the business" **[M2023-081]** (rule under test, section D(c)).
- **WEIGHS FOR on the capital the business needs, and AGAINST on what the added capital earns**, in one sentence: the business
  itself is the first kind, giving "more and more money every year without putting up anything to get it, or very little"
  **[M1998-081]** in the cash it throws off against $10M of capex, but every dollar it has reinvested has gone into brands at
  prices that earn a fair return before write-downs and an ordinary one after them, so the added capital earns the second-best
  rate at best **[L2009-012]**, **[M2003-120]**, and the growth Q7 may credit is the growth shown, which is none. (The "little or
  no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (fiscal year-ends 2017 to 2026, USD millions, `tools/run.py`'s
  table from the first-filed XBRL of the ten 10-Ks `0001295947-17-000018` to `0001295947-26-000016`, read against the filed
  statements of FY2024 and FY2026):

  | FY end | assets | equity | cash | receivables | inventory | goodwill | intangibles | debt | retained |
  |---|---|---|---|---|---|---|---|---|---|
  | 2017 | 3,911 | 823 | 42 | 137 | 116 | 615 | 2,904 | 2,194 | 397 |
  | 2018 | 3,761 | 1,179 | 33 | 141 | 119 | 620 | 2,781 | 1,993 | 736 |
  | 2019 | 3,441 | 1,096 | 28 | 149 | 120 | 579 | 2,507 | 1,799 | 702 |
  | 2020 | 3,514 | 1,171 | 95 | 151 | 116 | 575 | 2,479 | 1,730 | 844 |
  | 2021 | 3,429 | 1,358 | 32 | 115 | 115 | 578 | 2,476 | 1,480 | 1,009 |
  | 2022 | 3,671 | 1,578 | 27 | 139 | 120 | 579 | 2,697 | 1,477 | 1,214 |
  | 2023 | 3,354 | 1,447 | 58 | 167 | 162 | 528 | 2,342 | 1,346 | 1,132 |
  | 2024 | 3,318 | 1,655 | 46 | 177 | 139 | 528 | 2,321 | 1,126 | 1,341 |
  | 2025 | 3,402 | 1,835 | 98 | 194 | 148 | 527 | 2,295 | 992 | 1,556 |
  | 2026 | 3,494 | 1,888 | 64 | 192 | 159 | 581 | 2,300 | 994 | 1,746 |

  What moved and why. **Equity against goodwill and intangibles**: the two intangible lines were $3,519M in 2017, four times the
  equity, and $2,881M in 2026, 1.5 times it; every dollar of tangible equity is negative throughout (equity less intangibles is
  about −$1.0B in 2026). The intangibles fell by write-downs ($713M over the decade, Q2) and amortization, and rose with each
  purchase (2022: TheraTears; 2026: Pillar5); the 2018 jump in equity is the Tax Act's $232.5M deferred-tax benefit on
  indefinite-lived brands (XBRL `IncomeTaxExpenseBenefit` −$232.5M; the FY2018 10-K), not earnings. **Retained earnings** grew
  from $397M to $1,746M, $1,349M kept in nine years, net of the two impairment years in which the line fell (2019, 2023).
  **Debt** was paid down from $2,194M to $992M over eight years out of that cash, then at 2026-06-30 jumped to $2,045M face and
  after July 2026 to about $2,140M (10-Q `0001295947-26-000042`, Notes 8 and 18); the balance sheet of 2026-06-30 shows intangibles
  of $3,243M and goodwill of $651M, $3,894M together against $1,917M of equity, back to the 2017 shape. **Cash** is kept small,
  $27M to $98M. **Receivables against sales**: 15.5% of revenue in 2017, 17.6% in 2026, a slow rise, with FY2026's general and
  administrative line carrying "an increase in our allowance for doubtful accounts pertaining to one specific customer" (FY2026
  10-K, MD&A) and the write-off of a $10.3M loan to a supplier that had been carried inside receivables (MD&A, Other expense).
  **Inventory against sales**: 13.1% in 2017, 14.6% in 2026, with the FY2023 build to $162M (14.4%) when supply tightened. Both
  rises are modest and explained; neither is the suspicious build the rows name **[M1995-064]**. What the figures say: a
  company that borrows to buy brands, pays the debt down from the brands' cash, writes off part of what it bought, and has just
  started the cycle again at twice the scale. What they do not say: whether the brands it has just bought will hold; what they
  cannot say: what the next write-down will be.
- **The real costs.** *Depreciation* is $8M to $10M a year, about equal to capex, a true cost taken **[L2015-004]**.
  *Amortization* of purchased tradenames and customer relationships, $18M to $23M a year, is the kind the rows often add back
  **[M1997-015]**, and this run adds it back at Q7 because the cash to buy the brands is deducted there instead (rule under test,
  section D(c)); the impairments are the evidence that some of these brands do deplete **[L2012-003]**, and they are charged
  through the acquisition deduction, not twice. *Stock pay* is $9.0M to $14.0M a year, 1% of revenue, deducted in full
  **[L2015-003]**; dilution is offset by buybacks, which is a use of cash, not a cost avoided. *Restructurings and "one-time"*
  items: tradename impairments in six of ten years (Q2), acquisition costs in most years, the supplier-loan write-off, "costs
  related to the acquisition of our Canadian manufacturing facility" in cost of sales, all of which the filer's adjusted figures
  remove; the rows do not ask us to forget them **[M1999-023]**, and this run keeps every one. *Taxes*: the effective rate was
  26.1% (FY2026) and 24.5% (FY2025); cash taxes paid $59.6M, $52.1M and $45.9M in FY2024 to FY2026 (FY2026 10-K, supplemental
  cash-flow line), near the provision. *Pensions*: none ("We have no applicable qualified pension", DEF 14A). *Leases*: finance
  leases $20.6M and operating leases $27.9M at 2026-06-30, small.
- **EBITDA in the filer's own mouth.** The company does not use EBITDA in its 10-K, but it features it where it speaks to
  investors: the deal release prices Breathe Right at "11.0x EBITDA" and "9.5x EBITDA net of anticipated tax benefits" and
  speaks of "bank-defined net leverage" (8-K of 2026-03-20, exhibit 99.2); the earnings release defines Non-GAAP EBITDA and
  Adjusted EBITDA and reports Adjusted Diluted EPS of $4.38 against GAAP $3.91 (8-K of 2026-05-13, exhibit 99.1); the annual
  bonus and the three-year performance units pay half on "Adjusted AIP EBITDA" (DEF 14A, Compensation Discussion). The rows'
  answer to the figure is "does management think the tooth fairy pays for capital expenditures?" **[L2000-036]**; here capex is
  1% of sales, so EBITDA overstates the cash less than usual, but the figure as featured leaves out the $1.2B just paid for the
  cash it counts and the $713M written off, and that is where the tooth fairy sits for a buyer of brands. Coverage is read on
  pretax earnings against interest **[L2012-002]**: pro forma FY2026 operating income $358.8M against pro forma interest of
  $104.5M, 3.4 times (8-K/A `0001295947-26-000025`, exhibit 99.3).
- **The featured adjusted figure, guidance and targets (section A of the gaps case).** Adjusted EPS is featured in the release
  and in the proxy's performance summary ("Adjusted EPS of $4.38"); "organic revenue" is defined by the filer as GAAP revenue
  "excluding the impact of foreign currency exchange rates" only (earnings release, Non-GAAP definitions), so the word organic
  does not strip acquired brands, which makes the "long-term organic sales growth target of 2-3%" (deal release) a figure that
  acquisitions can satisfy; guidance is given each year (Fiscal 2027 outlook: adjusted diluted EPS of $4.42 to $4.51, free cash
  flow of $250 million or more) and a three-year target (revenue CAGR about 10%, EPS CAGR about 8%). These are the habits the
  rows condemn, the adjusted figure "makes us nervous" **[L2016-006]** and predictions of growth rates are "both deceptive and
  dangerous" **[L2000-037]**; they weigh against here as a WEIGHING **[M1994-018]** and are carried to Q5 as evidence on the
  people. The targets were missed in FY2026 (95% of net sales, 93% of adjusted EBITDA; payout 68% of target, DEF 14A), which the
  rows read as a point in favour against the "consistently reach their declared targets" tell **[L2002-041]**.
- **What the accounts say of management's character.** Clear statements, two segments reported plainly, every impairment named
  by brand and amount, the supply failure, the customer allowance and the supplier loan all disclosed in the MD&A in plain words;
  the FY2024 segment table labels a $342.4M operating income "Operating loss" (FY2026 10-K, Note 19), a slip. The FY2023
  impairment of $370.2M is explained as "primarily a result of increased discount rates due to macroeconomic conditions" (FY2024
  10-K, MD&A), which puts the write-down on the interest rate rather than on the price paid, a way of talking about a mistake
  that is carried to Q5 **[L2024-003]**. No tell of confusion **[M2003-029]**; no reserve that moves, no prepaid build, no
  profit that may not exist.
- **VERDICT on the accounts: WEIGHS AGAINST, no STOP.** The accounts are clear and the real costs can be found and charged, so
  there is no confusion to stop on **[M1995-063]** and no suspicion in the statements themselves **[M1995-065]**; the featured
  adjusted figure, the EBITDA pricing of the deal and the guidance are the make-the-numbers habits weighed against here and
  judged at Q5 **[L2016-006]**, **[L2019-006]**. **The recast earnings that feed Q7** (USD millions, FY2022 to FY2026): operating
  cash flow 259.9, 229.7, 248.9, 251.5, 257.6; less stock pay 9.0, 12.4, 14.0, 11.2, 10.8; less capital spending 9.6, 7.8, 9.6,
  8.2, 11.2; less finance-lease principal 2.6, 2.8, 2.8, 4.5, 2.5; gives owner cash after interest of 238.7, 206.7, 222.5, 227.6,
  233.1 (average 225.7); add back interest paid of 61.4, 54.2, 63.2, 47.8, 43.8 less its tax effect at the filer's 24% blended
  statutory rate (8-K/A exhibit 99.3, note 4e), gives owner cash before interest and after the company's tax of 285.4, 247.9,
  270.5, 263.9, 266.4 (average 266.8), the all-equity figure rule under test, section H, asks for; cash paid for businesses, net,
  247.0, 0.0, 10.6, 8.2, 123.7 (average 77.9), the capital spending rule under test, section D(c), deducts in its default pair.
  All from the FY2024 and FY2026 10-K cash-flow statements and the XBRL facts named at Step 0.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Ronald M. Lombardi, 62, President and Chief Executive Officer since June 2015, Chair of the Board since May 2017,
  Chief Financial Officer of the company from December 2010 to November 2015, before that a chief financial officer at a
  contract medical-device maker, a specialty chemical business and Cannondale (DEF 14A `0001295947-26-000021`, director
  biographies). Christine Sacco, Chief Financial Officer and Chief Operating Officer, signs the 8-Ks. The Senior Vice President,
  Operations, retired on 2026-08-14, two months after the largest acquisition in the company's history and in the middle of an
  eye-care supply remediation (8-K `0001295947-26-000049`); the filing gives no reason. The CEO owns 376,501 shares, about 0.8%
  of the company, worth about $17M at the price; all directors and officers together own 1.5% (DEF 14A, beneficial ownership
  table). The largest holders are BlackRock 15.9%, Ariel 8.7%, Dimensional 6.1% and two Vanguard entities 11.2% (same table).
- **The first yardstick, the record against the hand dealt** **[M1994-008]**. The hand dealt in 2015: a company of $806M
  revenue (FY2016) with $1.6B of debt from the Insight and DenTek purchases. What was done with it: Fleet bought for $823.7M in
  January 2017 on a $740M incremental term loan (FY2018 10-K `0001295947-18-000013`); the household-cleaning brands and six
  non-core OTC brands sold for about $190M in 2016 to 2018 at a net loss (the FY2018 and FY2020 10-Ks record a pre-tax loss of
  $51.8M on the 2016 divestitures); debt paid down from $2,194M (FY2017) to $992M (FY2025) out of operating cash; the Akorn
  consumer brands bought for $228.9M in 2021; shares reduced from 53.4M diluted (FY2017) to 47.4M (2026) by buybacks; $713M of
  purchased brands written down in FY2018, FY2019, FY2023 and FY2025; organic revenue in the deciding segment flat to down
  (Q2's table); and in June and July 2026 $1,195M of brands bought on $1,140M of new floating-rate debt. The competitors'
  accomplishments over the same span (Q2's row): Church & Dwight grew revenue from $3.5B to $6.2B with margins held; Haleon
  and Kenvue held margins in the high teens; Perrigo destroyed capital. The record is that of a capable buyer and integrator of
  small brands who has not grown the brands he owns, and whose purchases have been written down at a rate of about a fifth.
  "How well that they treat their owners" **[M1994-008]** is Q6's half; the capital allocation is judged there.
- **The second yardstick, the proxy** **[M1994-009]**. Pay in FY2026: salary $1,003,564, stock awards $4,099,959, annual cash
  incentive $850,000, other $51,024, total $6,004,547 (DEF 14A, Summary Compensation Table). The annual incentive pays half on
  net sales and half on "Adjusted AIP EBITDA"; the three-year performance units (75% of the CEO's long-term grant) pay on the
  same two measures over three years; FY2026 paid 68% of target and the FY2024 to FY2026 units 70% (DEF 14A, Executive
  Summary). Pay sits on figures the person controls **[M2003-019]**, and the plan did not pay out on a missed year; but a
  buyer of brands paid on EBITDA with no charge for the capital he spends is paid on "a phony batting average" **[M1995-010]**,
  and this plan has that flaw at the moment the company has doubled its debt to buy EBITDA. An independent consultant (CAP) is
  engaged and a peer group referenced (DEF 14A, Role of Independent Consultant), the ratchet the rows name **[M2004-016]**.
  Say-on-pay passed with about 97% (DEF 14A). The CEO is also Chair, with a Lead Independent Director; the rows say a mediocre
  chief executive is hardest to replace when "also Chairman" **[L2014-026]**, a weight, not a finding of mediocrity. Directors
  receive $95,000 cash and $155,000 in restricted units a year (DEF 14A, Director Compensation), and own between 2,757 and
  49,500 shares each; the rows ask whether the fees are "a very important part of a director's wellbeing" **[M2009-086]**, and
  nothing in the proxy answers it.
- **The tells of dishonesty, hunted.** *Too good to be true* **[M2002-028]**: nothing; the deal release's "9.5x EBITDA net of
  anticipated tax benefits" is salesmanship, not a claim that cannot be. *Reports that dance* **[M1995-111]**: the FY2023
  write-down of $370.2M explained "primarily" by discount rates (Q4), which is the one place the reports put the cause outside
  the room; against it, the Clear Eyes supply failure is stated bluntly in every filing, the customer allowance and the supplier
  loan write-off are named, and Summer's Eve's lower long-term projections are admitted (FY2024 10-K). *Fixed on the stock
  price* **[M2004-067]**: the proxy's first page leads with free cash flow and leverage, not the share price; the 10-K's
  performance graph is the required one. *Taking credit* **[M1998-167]**: the proxy's claim of the largest capital deployment in the company's
  history is a claim of action, not of result. *Owners as patsies* **[L2001-002]**: no related-person transaction is
  disclosed, hedging is prohibited and pledging limited, a clawback policy is in place, and no shares were issued in any deal
  in the decade (every purchase paid in cash). *Professed, not held* **[M2010-069]**: the 10-K's "Trust is foundational"
  paragraph is boilerplate and is given no weight either way. *Serial issuance* **[L2014-015]**: none; the share count has fallen.
- **The habits carried from Q4, read with the integrity record.** Guidance each year, adjusted EPS featured, EBITDA multiples
  in the deal talk, three-year growth targets, and an "organic" definition that strips only currency. These are "things that
  they do in public in relation to their investors and the promises they make" **[M2004-067]**, and in this company they are
  the ordinary habits of a listed consumer company, disclosed and reconciled; the targets were missed and the plan paid less,
  which is the opposite of the fudging the rows fear **[L2002-041]**. Doubt is the test **[M2013-088]**: read with the plain
  disclosure of bad news, the cash-only deals, the absence of any reserve game or issuance, these habits do not raise a doubt
  about honesty; they raise one about judgment, which is ability's column.
- **Love of the business, the same after being paid** **[M2000-098]**. A hired executive, not a seller; eleven years in the
  chair, pay about $6M a year against a $17M holding, so the money is the larger half of the relationship. What the proxy
  shows him wanting is scale: "the largest acquisition in Company history" and "the most significant capital deployment in our
  history" (DEF 14A). The rows' question "What would you be doing differently if you owned it all yourself?" **[M2017-029]**
  gets, from the record, the answer that an owner of these cash flows would have kept paying the debt down and would not have
  borrowed $1.1B at floating rates to buy a nasal-strip brand at eleven times EBITDA in a year when the company's own revenue
  fell; that is a judgment about ability and about Q6, not about honesty.
- **VERDICT on integrity: IN.** No tell of dishonesty is found in the proxy, the letters or the accounts; the bad news is told
  plainly and the deals are paid in cash; the make-the-numbers habits are present, weighed, and leave no doubt about honesty
  when read with the rest **[M2013-088]**, **[M2004-067]**. **Ability WEIGHS AGAINST**: the record is the record of a capable
  integrator and debt-payer who has not grown what he owns and has written off a fifth of what he bought, which the rows read as
  "how our record is achieved" **[M2012-089]** and as a question of focus **[L1996-033]**; the business is one the rows say does
  not need a superstar **[M1996-037]**, and it has not had one, so the weight on value is moderate and goes to Q7 through the
  growth credited, which is none.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**, over the five years 2021-03-31 to 2026-03-31. Kept: retained
  earnings rose from $1,008.8M to $1,746.1M, $737M kept, and the company paid no dividend (it never has: FY2026 10-K, Item 5)
  while buying back $282.8M of stock (cash-flow lines: FY2022 nil, FY2023 $50.0M, FY2024 $25.0M, FY2025 $51.5M, FY2026
  $156.3M). Where the cash went: debt reduced from $1,479.7M to $994.0M, $486M; businesses bought for $389.5M (TheraTears, Pillar5
  and smaller rights); the buybacks. *The market leg*: the stock closed at $44.08 on 2021-03-31 and $59.27 on 2026-03-31
  (aggregator closes, flagged), so on about 50.6M and 47.4M shares the market value went from about $2.23B to $2.81B, up about
  $0.58B for $737M kept and $283M bought in; at today's $46.16 the market value is $2.19B, below where it began. The test is
  failed on the market leg at today's price and barely met at the fiscal year-end. *The intrinsic leg* **[R2009-002]**: owner
  cash after interest, before stock pay, per diluted share went from $4.19 (FY2021: $235.6M less $22.2M capex less $1.4M
  lease principal on 50.6M shares; FY2022 10-K) to $5.01 (FY2026: $257.6M less $11.2M less $2.5M on 48.7M), up 20%, with
  $486M of debt retired besides; so a dollar kept became about a dollar of intrinsic value, mostly by paying lenders. Then the
  forward question **[M2010-097]**, whether the capital can keep being used effectively: the answer the company gave in June
  2026 is $1.2B of brands at 8.6% pre-tax on price (Q3), which is a fair use and not a compounding one.
- **Buybacks** **[L1999-023]**, **[L2016-002]**. A $300.0M authorization of May 2024 names no price above which buying stops;
  $92.2M remained at 2026-06-30 (10-Q Note 10). Prices paid, from the equity statements (treasury shares and cost, FY2026
  10-K): FY2024 515 thousand shares for $30.5M, about $59.2 a share; FY2025 821 thousand for $57.6M, about $70.1; FY2026 2,391
  thousand for $162.1M, about $67.8, including $66.79 and $60.49 in February and March 2026 (Item 5). In the June 2026 quarter,
  with the term loan drawn, only 48 thousand shares were taken for tax withholding (10-Q equity statement). The rule reads the
  prices paid against the bottom of the Q7 range: on the central all-equity basis the bottom is $42.44 a share (Q7, computed
  below and recorded back here), and every year's average price sits above it; on the basis that leaves acquisitions out the
  bottom is $67.84, which FY2024 and FY2026 sit at or below and FY2025 sits above. The stated-price test is failed and the
  prices-paid test is failed on the central basis, so the programme weighs against: "what is smart at one price is dumb at
  another" **[L2011-003]**, and the $162M spent at $68 in the year before a $1.1B borrowing is money the business then had to
  borrow back at SOFR plus 2.00%.
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**. No stock has been issued for any purchase in the decade; every deal
  was cash and debt, so the one STOP in Part A, the all-stock deal by an undervalued acquirer **[L2009-019]**, does not arise.
  Value given against value got, on the latest and largest: $1,045.0M given for a business that earned $60.3M of income from
  operations in its audited year, $89.8M before the seller's amortization, plus a tax deduction on the price worth, by this run's
  arithmetic, about $17M a year for fifteen years (Q7); the deal "will usually boost per-share earnings if it is debt-financed"
  **[L2017-004]** and this one is priced in the release on exactly that footing ("accretive to EPS"), which is the footing the
  rows refuse; on the all-equity basis the return is fair, about 6.5% after tax before the deduction and about 8% with it, against
  a 5.66% long bond. The post-mortem test **[L2014-013]**: the FY2023 write-down of three purchased brands was attributed
  "primarily" to the discount rate (Q4), which is not the honest comparison of reality to the original projections the rows ask
  for. The record of deals bought and written down (Q2, Q3) is the base rate the rows name, "a lot of dumb deals" from the forces
  that push toward deals **[M2014-076]**; the proxy's own words make the deal the year's achievement.
- **Dividends and the use of cash.** None ever paid; the policy is stated and consistent **[L2012-015]** (Item 5: earnings
  "will be used in our operations, to facilitate strategic acquisitions, to repurchase our common stock, or to pay down
  indebtedness"). The rows say a company that cannot employ its cash at more than a dollar should pay it out **[M2004-089]**;
  this company has chosen instead to employ it in brands at a fair return and in its own shares above the bottom of the range,
  and cash is not held as a residual: it is spent as it comes and borrowed when it is not enough.
- **Part A WEIGHS AGAINST**, in one sentence: a dollar kept has become about a dollar by paying down debt and less than a dollar
  in the market at today's price **[R1995-009]**, the buybacks were made with no stated price at prices above the bottom of the
  central range **[L2016-002]**, and the growth bought with $1.2B of new debt earns a fair return that the rows would value on an
  all-equity basis and the company priced on an accretion basis **[L2017-004]**.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**: net sales and adjusted EBITDA, both under management's hand; but
  no capital charge in a company whose capital decisions are the whole game, the flaw of **[M1995-010]**, and EBITDA as the
  profit measure, the figure the rows call "bullshit earnings" **[M2003-109]**. The three-year units make the "lottery ticket"
  **[L1996-018]** smaller: they pay on operating measures, not the share price; 60% to 75% of long-term pay is performance units
  (DEF 14A). Pay fell when the targets were missed (68% and 70% payouts), which is a partner in both directions **[L1994-020]**.
  Designed with an independent consultant against a peer group **[M2004-016]**, **[L2005-015]**; the proxy's pay section runs
  to tens of pages, well short of the hundred the rows mock **[M2009-087]**.
- **The board** **[M2007-120]**: seven directors besides the Chair, all independent by the proxy's test, a Lead Independent
  Director, a combined Chair and CEO since 2017 **[L2014-026]**; directors paid $250,000 a year in cash and units, holdings of
  2,757 to 49,500 shares, none disclosed as bought with their own savings **[L2019-008]**; the board approved the largest deal in
  the company's history on seven-year floating debt at four times EBITDA, which is the "independent judgment in on major
  acquisitions" the rows ask of a board **[M2007-120]**, exercised in favour.
- **The owners as partners** **[L1994-023]**: the bad news (supply, the customer, the write-offs) is told in the filings; one
  class of stock, one vote, no splits, no related-party dealings, hedging prohibited; against that, annual guidance and a
  quarterly "number" to hit, which the rows say Berkshire has never had **[L2018-003]** and call "silly" **[M2016-002]**.
- **Part B WEIGHS AGAINST, mildly**, in one sentence: the plan pays on controllable measures and did not pay out on a missed
  year, but it charges nothing for the capital the chief executive spends and measures profit by EBITDA, with a consultant's
  peer group behind it, and the owners are given guidance rather than the information "we would wish you to give us if our
  positions were reversed" **[L1994-023]**.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, with the fourth question of 2014 asked first:
"are you going to have to put more cash into after you buy it?" **[M2014-068]**. The company gets credit "for whatever net cash
is left every year" **[M1998-080]**, and the construction is the CONVENTION of Part VI (five-year average of owner cash after
every real cost, the growth shown, ten years then no growth, at 5.66%, the no-growth and shown-growth cases as the two ends).

**The basis** (rule under test, section H). The central figure is built on the all-equity basis: owner cash before interest and
after the company's tax, against the market value of the shares plus net debt as the filings state it. Net debt today: at
2026-06-30 borrowings of $2,045.0M face plus finance leases of $20.6M less cash of $89.1M (10-Q `0001295947-26-000042`, balance
sheet and Note 8), $1,976.5M; plus the two filed subsequent events of Note 18, the further $95.0M term-loan draw and the about
$55.0M of cash on hand paid with it for LaCorium ($150.0M in all), $2,126.5M; the $400.0M 6.25% notes replaced the $400.0M
5.125% notes face for face. Operating leases of $27.9M are left out and said so. Market value $2,186.8M (Step 0); the whole
business's price is therefore $4,313.3M. The equity-only figure, owner cash after interest against the market value, is shown
beside it and never decides alone; after June 2026 the interest is not the window's: at the pro forma's 5.63% on the $1,140.0M
term loan, 3.75% on $600.0M and 6.25% on $400.0M (8-K/A exhibit 99.3 note 4d; the 10-Q Note 8; the 8-K of 2026-07-15) interest is
about $111.7M a year before tax, $84.9M after tax at 24%, against the window's average of $41.1M after tax, so the equity-only
series is reduced by the $43.8M difference.

**The cash, and the six specifics of section D (rule under test).**
- *(a) Cycles.* Neither end year of the window is a cyclical peak or trough: the business is "generally not seasonal" (FY2026
  10-K, Item 1) and OTC healthcare has no cycle in these filings; FY2026 is depressed by the eye-care supply failure, which the
  filer says will continue, and FY2022 by nothing. No cycle average is taken and the literal window is the only window; rule under
  test, section D(a), was tested and does not bear **[L2005-003]**.
- *(b) Decline.* The all-equity owner-cash series (Q4) runs 285.4, 247.9, 270.5, 263.9, 266.4 (FY2022 to FY2026), a compound
  rate between the end years of −1.71% a year; between the halves (the first two years against the last two) −0.18% a year. The
  series does not change sign and the end-year rate is not meaningless, so the shown growth of −1.71% is carried as negative and
  makes the bottom of the range, and the no-growth case is the top; the halves' rate is shown beside it: rule under test, section
  D(b), bears **[M2006-058]**, **[M2006-059]**. The equity-only series runs 238.7, 206.7, 222.5, 227.6, 233.1, −0.59% a year.
- *(c) Acquisitions.* Cash paid for businesses, net, was 247.0, 0.0, 10.6, 8.2, 123.7 in the window, average $77.9M a year, and
  nothing was sold. The default pair is applied, acquisitions deducted and the total growth credited, which is the −1.71% shown:
  rule under test, section D(c), bears **[M1998-080]**, **[M2023-081]**. The second pair, acquisitions left out and only organic
  growth as the filer reports it, is shown beside: the filer's "organic" measure strips only currency (Q4), so it cannot separate
  acquired growth and reports −4.5% for FY2026 and 1.1% for FY2025 (the earnings releases); this run credits the second pair the
  same −1.71% the series shows, which is at least as generous as the filer's own organic figure, and says so. The deals since the
  window closed were financed by debt and are valued as if paid with equity, unlevered owner cash less today's net debt (rule
  under test, section D(c)) **[L2017-004]**: Breathe Right's cash enters on its own audited record, the year to 2025-12-31 (8-K/A
  `0001295947-26-000025`, exhibit 99.1): net sales $194.9M, income from operations $60.3M, amortization $29.5M, no property or
  equipment on its balance sheet and so no capital spending, giving $89.8M before tax and $68.2M after tax at 24%; LaCorium's
  cash enters at nothing in the central case, since no statement of its earnings is filed and the rows have "never looked at a projection" **[M1995-050]**; the
  filer's figure, "approximately $12 million in EBITDA including the benefits from anticipated synergies" (earnings release of
  2026-05-13), is a projection and is shown beside as the filer's. The combined business is valued on its own averages with the deals' financing deducted through net debt.
- *(d) Working capital.* The window's working-capital movements are inside operating cash flow and are so treated as capital
  spending; the FY2023 inventory build was tied by the filer to supply constraints across products, not to one contract, so no
  year is aberrational on that ground: rule under test, section D(d), tested, does not change a figure **[M2008-036]**.
- *(e) Growth spending.* The filing gives no maintenance figure and depreciation ($8M to $10M) about equals capital spending
  ($8M to $11M), so the filing does not allow the maintenance guess and the all-spending case is the central and only case;
  nothing is charged twice: rule under test, section D(e), tested, does not bear **[M2000-144]**.
- *(f) The cap.* The shown growth is negative; no rate above the discount rate is carried and nothing traces to an absurdity:
  rule under test, section D(f), tested, does not bite **[M1997-095]**, **[M1999-067]**.
- *The tax shelter (section E, applied by analogy).* The purchase price of Breathe Right is deductible for tax (10-Q Note 2:
  "Goodwill is deductible for income tax purposes"; the deal release values the "future tax savings" at $150 million). Section
  E prices a shelter that runs out inside ten years separately; this one runs fifteen, and the same method is applied because it
  is the cleanest: owner cash is computed at the 24% statutory rate (above) and the shelter's present value is added, $1,045.0M
  over fifteen years at 24% is $16.7M a year, worth $166M at 5.66% (the filer's own figure, $150M, is beside it) and $127M at the
  floor. CONVENTION of this run, in those words; rationale: section E's method, extended to a shelter longer than ten years.

**The arithmetic** (reproduced from the working folder's `q7_arith.py`, which the repository ignores; USD millions; shares
47.374522M; r = 5.66%; the ten-year term then no growth; the shelter's present value added to the whole-business value):

| case | owner cash, all-equity | growth | whole business | less net debt | per share | equity-only cash | equity-only per share |
|---|---|---|---|---|---|---|---|
| default D(c): acquisitions deducted, total growth credited; top (no growth) | 257.1 (266.8 − 77.9 + 68.2) | 0 | 4,709 | 2,583 | **$54.51** | 172.3 | $67.75 |
| same, bottom (shown growth) | 257.1 | −1.71% | 4,137 | 2,011 | **$42.44** | 172.3 | $59.66 |
| beside: acquisitions left out; top | 335.0 (266.8 + 68.2) | 0 | 6,085 | 3,959 | $83.56 | 250.2 | $96.80 |
| beside: acquisitions left out; bottom | 335.0 | −1.71% | 5,340 | 3,214 | $67.84 | 250.2 | $85.05 |

Adding LaCorium at the filer's projected $12M of EBITDA less tax, $9.1M, would add about $160M to each whole-business figure,
$3.40 a share; it is not in the central case.

- **Value range:** **$42 to $55 a share** (the central, all-equity basis, acquisitions deducted) **against $46.16**; the
  whole-cycle variant is the same, there being no cycle; beside it, $68 to $84 a share with acquisitions left out; on the
  equity-only basis $60 to $68 (central) and $85 to $97 (beside). The width of every range is 1.14 to one, far inside the
  three-to-one that would send the file to TOO HARD, so the range is narrow and a conclusion can be drawn **[L2000-024]**.
- **The floor** (CONVENTION, about ten percent pre-tax, applied to owner cash after the company's own tax, no conversion;
  section E). The expected return at the price, the cash yield plus the shown growth, on the all-equity basis: central case
  $257.1M on $4,313.3M is 6.0%, less 1.7% of shown decline, about 4.3%; the beside case $335.0M on $4,313.3M is 7.8%, about 6.1%
  with the decline. Both are below the floor the speakers named, "we don't want to buy equities where our real expectancy is
  below 10 percent" **[M2003-149]**, and below the point at which "we drop out of the game" **[M2003-149]**. On the equity-only
  basis the yields are 7.9% (central) and 11.4% (beside), the second above the floor: this is the flattery of the per-share
  figure that section H names, the lenders taking the first dollar at a coupon below the floor, and it does not decide.
- **Closes:** **OUT.** The price sits inside the central range ($46.16 between $42 and $55), the case the rows call too close,
  "if you have to carry it out to three decimal places, it's not a good idea" **[M2008-068]**; and the expected return at the
  price does not clear the floor on the all-equity basis on either pair, which is the second way the file closes here. Nothing
  screams **[M2009-005]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** the price at which the midpoint of the range earns the floor,
  computed as the present value of the midpoint stream (the mean of the no-growth and shown-growth streams, with the shelter) at
  the floor rate instead of the sovereign; tax treatment: owner cash after the company's 24% blended statutory rate, the shelter
  added separately, no holder's tax. **On equity plus net debt (the central basis): $9.14 a share** (whole business $2,559M less
  net debt $2,126.5M); on equity alone: $37.08 a share. With acquisitions left out: $24.69 on equity plus net debt, $52.63 on
  equity alone. The two bases differ by four times on the central case because net debt is 97% of the market value; that gap is
  the point of the rule under test, section H, and the equity-only figure "never decides alone". No cheap price is reported.
- **VERDICT: OUT.** Valued, and the price does not clear the floor **[M2003-149]**; valued, and the price sits inside a narrow
  range, a case that needs the pencil **[M2008-068]**, **[M1996-084]**. The box is OUT, not TOO HARD: the range is narrow and
  the cash stream can be pictured from ten years of filings, so the stop for a stream that cannot be pictured at all
  **[M1994-077]** does not apply. "You can turn any investment into a bad
  deal by paying too much" **[M2019-015]**, and the company did so in June 2026 on the owners' behalf, which is why a share that
  looks cheap on the equity-only yield is not cheap on the business.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** The file closed at Q7. The bond comparison is recorded under AFTER THE STOP as a fact, not weighed.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** The debt facts found are recorded under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** The newspaper-test fact is recorded under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7.** The value range on the all-equity basis (rule under test, section H), with acquisitions deducted and the shown
decline carried (rule under test, sections D(c) and D(b)), is **$42 to $55 a share against $46.16**; the price sits inside it,
and the expected return at the price, about 4.3% on the central case and about 6.1% with acquisitions left out, is below the
floor of about ten percent **[M2003-149]**, **[M2008-068]**. Beside it: $68 to $84 with acquisitions left out; $60 to $68 and
$85 to $97 on the equity-only basis, which never decides alone. Fair price (a reporting figure): $9.14 on equity plus net debt,
$37.08 on equity alone; $24.69 and $52.63 with acquisitions left out. Q1 IN, Q2 IN with the moat narrowing written down, Q3
for on the capital needed and against on what the added capital earns, Q4 weighs against on the featured figures, Q5 integrity
IN and ability against, Q6 against in both parts. Integrity facts recorded, not judged: none beyond those judged at Q5, which
was reached. A test record under the T2 protocol: it binds nothing and enters no register.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on the questions not reached, each with its source, written down and not weighed* **[M1997-127]**.
- **Q8, the bond.** The 30-year Treasury yields 5.66% (US Treasury, 2026-10-05). The expected return at the price on the
  central all-equity case is about 4.3% and on the beside case about 6.1% (Q7); on the equity-only basis 7.9% and 11.4%. The
  rows take the bond over a stock "in at least 80 percent of the cases" **[M1997-090]**. Not weighed.
- **Q9, the debt.** Borrowings after July 2026 about $2,140M face: a $1,140.0M term loan at Term SOFR plus 2.00% due
  2033-06-12 with 0.25% quarterly amortization and an excess-cash-flow sweep from the fiscal year ending 2028-03-31 when first
  lien net leverage exceeds 2.75 to 1.00, secured on substantially all assets (8-K of 2026-06-16); $600.0M of 3.75% notes due
  2031-04-01; $400.0M of 6.25% notes due 2034-07-15 (8-K of 2026-07-15); a $225.0M asset-based revolver to 2031-06-12 with a
  fixed-charge covenant of 1.0 to 1.0 (FY2026 10-K, Debt Covenants; 10-Q Note 8). Floating share: $1,140.0M of $2,140M, 53%; the
  pro forma says a 12.5 basis-point move is about $1.3M a year (8-K/A exhibit 99.3, note 4d). Maturities inside five years:
  none of size after the 2028 notes were refinanced; the first wall is 2031. Net debt about $2,126.5M against market value
  $2,186.8M; the deal release expected bank-defined net leverage of about 4.0 times at closing (8-K of 2026-03-20, exhibit
  99.2). Coverage on pretax earnings, pro forma FY2026: operating income $358.8M against interest $104.5M, 3.4 times
  (8-K/A exhibit 99.3) **[L2012-002]**. Sudden demands: the change-of-control put at 101% on the notes (FY2026 10-K); no
  collateral calls or cash-out features found. Counterparties and concentrations: Walmart 20% and Amazon 15% of gross revenues;
  one third-party manufacturer 21% of gross revenues; one third-party warehouse for the continental United States (FY2026 10-K,
  Item 1); product liability allocated to manufacturers by contract for the long-term agreements and no negotiated allocation
  of risk for purchase-order suppliers (Item 1). The acquisition criteria's "little or no debt" **[R1997-001]** is
  stated for whole businesses and not for part-interests; recorded, not applied. The standing rule's "no significant near-term
  cash requirements" **[L2014-023]**: the term loan's sweep and amortization are the near-term requirements found. Not weighed.
- **Q10, the pitch.** The range is narrow and the price inside it; nothing in the file is the pitch the rows wait for
  **[M2003-070]**. Not weighed.
- **Q12, the newspaper test.** OTC medicines, feminine care, eye drops and nasal strips sold at retail under FDA monographs; no
  business named by the rows (casinos, tobacco, loading schemes) is present **[M2008-011]**. The FY2026 10-K reports no material
  legal proceedings (Item 3). Not weighed.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each: Q1 (`5a7792be`), Q2
      (`da33f796`), Q3 (`66c8861c`), Q4 (`41275b61`), Q5 (`8398fe96`, corrected in `c45c0d9b`), Q6 (`d651d7c1`), Q7 (`08a5fbfa`),
      and this close. Two corrections were needed before the close: the Q5 commit went through although the check script had
      failed, because the pipe to `tail` masked its exit status; the fragment (a proxy quotation beside a ledger id) was moved
      and committed as a correction, and the chain was mended with `pipefail`. The check script's own quote pairing drifted once
      and was mended (fragments may not contain a bracket), after which it found one real case at Q7, corrected before that commit.
- [x] Dispatched to an analyst under the T2 protocol, which grants the per-question commits and says these runs enter no
      register. The lock: the T2 protocol does not mention it and this analyst did not write one; whether the dispatching
      session held it is not known to this analyst (operator rule ten, (b)).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is declared
      at the head of this file (file names in a git status, three commit subjects including one other re-run's verdict, a memory
      index line) and was not used.
- [x] Every v5 id resolves: the check script `check_run.py` in the working folder (ignored by the repository's `.gitignore`;
      its method: every bold id of the form M, L or R, year and number, looked up in `principle_ledger_v5.csv`, any E-id flagged,
      and every quoted fragment that sits directly before an id tested as a substring of that row's own words after normalising
      quotation marks, dashes and whitespace) reports no E-ids, every id present, and every fragment beside an id in its row; the
      acceptance test `python tools/check_framework.py` PASSed before every commit. Every filing fact carries its accession; the
      aggregator closes used for the price and the retention test are flagged.
- [x] The order was kept; the first STOP that failed, Q7, closed the run; nothing after it is a clearance, and Q8 to Q12 are
      NOT REACHED with their facts under AFTER THE STOP.
- [x] Owner cash after every real cost, never a net-income proxy: operating cash flow less stock pay, capital spending and
      finance-lease principal, with interest added back after tax for the all-equity basis and acquisitions deducted under rule
      under test, section D(c); the sovereign from the issuing authority; aggregator quotes flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations, Q2, Q4, Q5); the facts for the later questions
      are under AFTER THE STOP; no integrity facts beyond those judged at Q5.
- [x] Not a point-in-time run; no row dated after today exists to bar.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield, growth and three-year owner-earnings lines were ignored.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. **(1) The working folder cannot be committed.** The T2 protocol's pathspec names `Framework/v5/tests/_work_T2_<TICKER>`,
and the repository's `.gitignore` ignores every `Framework/v5/tests/_work_*/` folder, so git rejects the path and the commits
carry the run file alone; the arithmetic and the check script's method were reproduced in this file so that the record does not
sit in an ignored folder. **(2) The template cites a file the blind rule forbids.** The template's header names
`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md` as the run form, and the T2 protocol forbids opening any
other file under `Framework/v5/tests/`; the template was followed as written and the named file was not opened. **(3) EBITDA
talk is both a stated count and a weighing.** Q4's list of what it rules out still names EBITDA as earnings and the managements
that talk it, with the row that counts such purchases at "about zero" **[M2002-026]**, while the section A convention of
2026-10-06 makes a featured adjusted figure a WEIGHING carried to Q5; this run followed the convention as the later and more
specific text, and weighed the deal release's EBITDA pricing and the EBITDA-based pay rather than closing on them, which a
reader of the list alone would not have done. **(4) Rule under test, section D(c), is silent on a debt-financed deal that closes
after the window and before the run.** The text handles a merger inside the window and a deal financed by debt in general; here
the two largest deals in the company's history closed after the fiscal year and before the run, and today's net debt carries
their cost while the window's cash does not carry their earnings. This run valued the combined business on each part's own filed
record (the window for the company, the audited year for Breathe Right, nothing for LaCorium) less today's net debt, and said so
at each step; the text should say whether a deal after the window is valued that way or the window is rolled forward to a
four-quarter basis that includes the pro forma, which here would have moved the central range by a few dollars a share and the
verdict not at all. **(5) The fair price's definition.** The text defines the fair price as the price at which the midpoint of
the range earns the floor without saying how a stream with a shown decline earns a rate; this run computed it as the present
value of the midpoint stream at the floor rate, which is the one reading that makes the fair price equal the range's midpoint
when the floor equals the sovereign, and confessed the choice. A sixth, smaller: the section E shelter convention names credits
that run out inside ten years and gives no instruction for a longer one; the method was applied by analogy to a fifteen-year
deduction.
