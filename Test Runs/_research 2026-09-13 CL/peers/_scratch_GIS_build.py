import sys, re
sys.path.insert(0, ".")
from _scratch_GIS_lib import *

F = {21: "GIS_10K_FY2021_2021-05-30.txt", 22: "GIS_10K_FY2022_2022-05-29.txt", 23: "GIS_10K_FY2023_2023-05-28.txt",
     24: "GIS_10K_FY2024_2024-05-26.txt", 25: "GIS_10K_FY2025_2025-05-25.txt", 26: "GIS_10K_FY2026_2026-05-31.txt"}
N = F[26]
out = []
w = out.append

def pct(a, b):
    return f"{a:,.1f} / {b:,.1f} = {100.0 * a / b:.1f}% (computed)"

w("## General Mills, Inc. (GIS)\n")
w("Scope: total company and the pet segment, filed as \"Pet\" (FY2021 to FY2024 10-Ks) and \"North America Pet\" (FY2025 and FY2026 10-Ks). "
  "Fiscal years end on the last Sunday in May. Transcription only; no judgment is expressed.\n")
w("Conventions used in this section: line numbers are the 0-based line indexes printed by `g.py` (add 1 for an editor). "
  "Where the text extraction split one table row or one sentence across several physical lines, the quote joins those lines with a single space "
  "and the Source line is the first physical line. Table cells are separated by \" | \" exactly as extracted (the FY2021 and FY2026 files carry pipe "
  "separators, including empty cells; the FY2022 to FY2025 files carry none). Parentheses in GIS tables denote negative numbers. "
  "Any long dash characters inside quotes are copied from the filings.\n")

w("### Documents used\n")
w("| file | form | fiscal period end | filing date | accession |")
w("|---|---|---|---|---|")
docs = [(F[26], "10-K", "2026-05-31", "2026-07-01", "0001628280-26-046466"), (F[25], "10-K", "2025-05-25", "2025-06-26", "0001193125-25-147079"),
        (F[24], "10-K", "2024-05-26", "2024-06-26", "0001193125-24-168943"), (F[23], "10-K", "2023-05-28", "2023-06-28", "0001193125-23-177500"),
        (F[22], "10-K", "2022-05-29", "2022-06-30", "0001193125-22-185257"), (F[21], "10-K", "2021-05-30", "2021-06-30", "0001193125-21-204830")]
for d in docs:
    w("| " + " | ".join(d) + " |")
w("\nInterim: no 10-Q for any period after the FY2026 10-K (period ended 2026-05-31) is on disk (manifest_list.txt lists only the six 10-Ks for GIS). There is therefore no interim period in this section.\n")

w("Fiscal calendar and 53-week years, as filed:\n")
w(q(F[21], "Fiscal 2021 had 52 weeks compared to 53 weeks in fiscal 2020.", None))
w(q(F[21], "Fiscal years 2021 and 2019 consisted of 52 weeks, while fiscal year 2020 consisted of 53 weeks.", None))
w(q(F[22], "Fiscal years 2022 and 2021 consisted of 52 weeks, while fiscal year 2020 consisted of 53 weeks.", None))
w(q(N, "Fiscal year 2026 consisted of 53 weeks, while fiscal years 2025 and 2024 consisted of 52 weeks.", None))
w(q(N, "Fiscal 2026 had 53 weeks compared to 52 weeks in fiscal 2025 .", None))
w("So FY2021 was a 52-week year lapping a 53-week FY2020 (the assignment note that fiscal 2021 had 53 weeks is not what the filing says), and FY2026 was a 53-week year. "
  "No statement of the week count for FY2023 was found in the FY2023, FY2024 or FY2025 10-Ks (searched \"52 weeks\", \"53 weeks\"); the FY2023 organic table carries no 53rd week row.\n")
w("Pet segment reporting-period change affecting the FY2021 comparison:\n")
w(q(F[21], "Fiscal 2020 included 13 months of Pet operating segment results as we changed the Pet operating segment’s reporting period from an April fiscal year end to a May fiscal year end to match our fiscal calendar.", None))
w("Segment naming, as filed:\n")
w(q(F[25], "In the first quarter of fiscal 2025, we renamed the Pet segment to the North America Pet segment", "no impact on our historical segment", 0))
w("Pet acquisitions described in the filings:\n")
w(q(F[22], "During the first quarter of fiscal 2022, we acquired Tyson Foods’ pet treats business for $ 1.2 billion in cash.", None))
w(q(F[22], "We consolidated Tyson Foods’ pet treats business into our Consolidated Balance Sheets", "deductible for tax purposes.", 15000))
w(q(N, "During the third quarter of fiscal 2025 , we acquired NX Pet Holding, Inc.,", "(Whitebridge Pet Brands acquisition).", 3000))
w(q(N, "The consolidated results are reported in our North America Pet operating segment on a one-month lag.", None, 3000))
w(q(N, "During the fourth quarter of fiscal 2024 , we acquired a pet food business in Europe,", "net of cash acquired.", 3000))
w(q(N, "The goodwill is included in the International segment and is not deductible for tax purposes.", None, 3700))
w("(The European pet food business is reported in the International segment, not in North America Pet.)\n")

# ---------------- 1 ----------------
w("### 1. Organic sales decomposition\n")
w("GIS files two tables per scope: a reported table (\"Contributions from volume growth\", \"Net price realization and mix\", \"Foreign currency exchange\") "
  "and an organic table (\"Contributions from organic volume growth\", \"Organic net price realization and mix\", \"Organic net sales growth\", plus reconciling rows). "
  "Volume is footnoted \"(a) Measured in tons based on the stated weight of our product shipments.\" Price and mix are one combined component. Units are percentage points (\"pt\"/\"pts\") or \"Flat\".\n")
w(q(N, "Net price realization. The impact of list and promoted price changes, net of trade and other price promotion costs.", None))
w(q(N, "(a) Measured in tons based on the stated weight of our product shipments.", None, 1000))

w("#### Total company\n")
for y in [21, 22, 23, 24, 25, 26]:
    f = F[y]
    w(f"FY20{y} ({f}):\n")
    w(qf(f, "Consolidated net sales were as follows:", "Note: Table may not foot due to rounding"))
    w(qf(f, "Components of organic net sales growth are shown in the following", "Note: Table may not foot due to rounding"))

w("Parsed (total company; all figures as filed, in percent or percentage points; parentheses negative):\n")
w("| year | scope | reported net sales growth | organic | volume (as labelled) | price (as labelled) | mix (if separate) | FX | acq/div | other | label wording used | source line |")
w("|---|---|---|---|---|---|---|---|---|---|---|---|")
def ln(f, s, after=0):
    return QF(f, s, None, after)[1]
tot = {21: ("3", "4", "2 (organic) / Flat (reported)", "2 (organic) / 2 (reported)", "not separate", "1", "none shown", "53rd week (2)"),
       22: ("5", "6", "(1) (organic) / (5) (reported)", "7 (organic) / 10 (reported)", "not separate", "Flat", "Acquisition and divestitures (1)", "none"),
       23: ("6", "10", "(4) (organic) / (8) (reported)", "14 (organic) / 15 (reported)", "not separate", "(1)", "Acquisitions and divestitures (4)", "none"),
       24: ("(1)", "(1)", "(3) (organic) / (3) (reported)", "2 (organic) / 2 (reported)", "not separate", "Flat", "Acquisitions and divestitures Flat", "none"),
       25: ("(2)", "(2)", "Flat (organic) / (1) (reported)", "(1) (organic) / (1) (reported)", "not separate", "Flat", "Acquisitions and divestiture Flat", "none"),
       26: ("(5)", "(2)", "(1) (organic) / (8) (reported)", "(1) (organic) / 2 (reported)", "not separate", "1", "Divestitures and acquisition (6)", "53rd week 2")}
for y, r in tot.items():
    f = F[y]
    w(f"| FY20{y} | total | {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | \"Contributions from (organic) volume growth\"; \"(Organic) net price realization and mix\"; \"Foreign currency exchange\" | {ln(f, 'Consolidated net sales were as follows:')}, {ln(f, 'Components of organic net sales growth are shown in the following')} |")
w("")

w("#### Pet segment (\"Pet\" FY2021 to FY2024; \"North America Pet\" FY2025 and FY2026)\n")
for y in [21, 22, 23, 24, 25, 26]:
    f = F[y]
    pre = "North America Pet" if y >= 25 else "Pet"
    w(f"FY20{y} ({f}):\n")
    w(qf(f, f"{pre} net sales were as follows:", "Note: Table may not foot due to rounding."))
    w(qf(f, f"The components of {pre} organic net sales growth are shown in the following", "Note: Table may not foot due to rounding."))
w("Footnotes (b) to the pet organic tables, as filed:\n")
w(q(F[22], "(b) Acquisition of Tyson Foods’ pet treats business in fiscal 2022.", None, 7000))
w(q(F[23], "(b) Acquisition of Tyson Foods’ pet treats business in fiscal 2022.", None, 7000))
w(q(F[25], "(b) Acquisition of Whitebridge Pet Brands business in fiscal 2025.", None, 7000))
w(q(N, "(b) Acquisition of Whitebridge Pet Brands business in the third quarter of fiscal 2025.", None, 1000))
w("Parsed (pet segment; as filed):\n")
w("| year | scope | reported net sales growth | organic | volume (as labelled) | price (as labelled) | mix (if separate) | FX | acq/div | other | label wording used | source line |")
w("|---|---|---|---|---|---|---|---|---|---|---|---|")
pet = {21: ("2 ($1,732.4m vs $1,694.6m)", "2", "2 (organic) / 2 (reported)", "Flat (organic) / Flat (reported)", "Flat", "none", "none (FY2020 comparative included 13 months of Pet results; no reconciling row is shown for it)"),
       22: ("30 ($2,259.4m vs $1,732.4m)", "18", "8 (organic) / 11 (reported)", "10 (organic) / 19 (reported)", "Flat", "Acquisition (b) 13 (Tyson Foods pet treats)", "none"),
       23: ("9 ($2,473.3m vs $2,259.4m)", "9", "(3) (organic) / (2) (reported)", "11 (organic) / 12 (reported)", "Flat", "Acquisition (b) 1 (Tyson Foods pet treats)", "none"),
       24: ("(4) ($2,375.8m vs $2,473.3m)", "(4)", "(7) (organic) / (7) (reported)", "3 (organic) / 3 (reported)", "Flat", "none", "none"),
       25: ("4 ($2,470.8m vs $2,375.8m)", "Flat", "3 (organic) / 4 (reported)", "(2) (organic) / Flat (reported)", "Flat", "Acquisition (b) 4 (Whitebridge Pet Brands)", "none"),
       26: ("6 ($2,613.3m vs $2,470.8m)", "(3)", "(5) (organic) / Flat (reported)", "2 (organic) / 5 (reported)", "Flat", "Acquisition (b) 6 (Whitebridge Pet Brands)", "53rd week 2")}
for y, r in pet.items():
    f = F[y]
    pre = "North America Pet" if y >= 25 else "Pet"
    w(f"| FY20{y} | {pre} segment | {r[0]} | {r[1]} | {r[2]} | {r[3]} | not separate | {r[4]} | {r[5]} | {r[6]} | same labels as total company | {ln(f, pre + ' net sales were as follows:')}, {ln(f, 'The components of ' + pre + ' organic net sales growth are shown in the following')} |")
w("")
w("Narrative sentences for the pet segment, newest year:\n")
w(q(N, "North America Pet organic net sales decreased 3 percent in fiscal 2026 compared to fiscal 2025 ,", "organic net price realization and mix.", 1400))
w(q(N, "On our priority of accelerating North America Pet growth, we partially achieved our objective.", "driven largely by changes in retailer inventory.", 0))

# ---------------- 2 ----------------
w("### 2. GAAP operating margin (and segment margin)\n")
w("Total company profit line used: \"Operating profit\" from the Consolidated Statements of Earnings (FY2026 10-K: \"Consolidated Statements of (Loss) Earnings\"). This is a GAAP line. Each year is taken from the 10-K that first reports it.\n")
IS = {}
for y in [21, 22, 23, 24, 25, 26]:
    f = F[y]
    blk, t, l = qt(f, P("GENERAL MILLS, INC. AND SUBSIDIARIES (In Millions, Except per Share Data)"), P("Benefit plan non-service income"), 0, True, True)
    w(f"FY20{y} income statement rows ({f}):\n")
    w(blk)
ns = {21: 18127.0, 22: 18992.8, 23: 20094.2, 24: 19857.2, 25: 19486.6, 26: 18424.6}
cos = {21: 11678.7, 22: 12590.6, 23: 13548.4, 24: 12925.1, 25: 12753.6, 26: 12228.9}
op = {21: 3144.8, 22: 3475.8, 23: 3433.8, 24: 3431.7, 25: 3304.8, 26: 885.8}
w("| year | net sales ($m) | Operating profit ($m) | operating margin | source line |")
w("|---|---|---|---|---|")
for y in ns:
    w(f"| FY20{y} | {ns[y]:,.1f} | {op[y]:,.1f} | {pct(op[y], ns[y])} | {ln(F[y], 'GENERAL MILLS, INC. AND SUBSIDIARIES (In Millions, Except per Share Data)')} |")
w("")
w("Filed cross-checks (GIS states its own operating profit margin): FY2021 17.3 percent, FY2026 4.8 percent.\n")
w(q(F[21], "Operating profit margin of 17.3 percent was up 50 basis points from year-ago levels", None))
w(q(N, "Operating profit margin of 4.8 percent decreased 1,220 basis points.", None))
w("FY2026 operating profit includes large charges, as filed:\n")
w(q(N, "In fiscal 2026, w e recorded a $1,500 million non-cash goodwill impairment charge related to our North America Pet", "brand intangible assets", 1000))
w("(Extraction artefact: \"w e\" is split in the extracted text.)\n")

w("Segment profit line used: \"Operating profit\" by segment (FY2021 to FY2024 tables, rows under \"Operating profit:\") and \"Segment operating profit\" (FY2025 and FY2026 tables). "
  "This is a segment measure reviewed by management, not a GAAP total; it excludes unallocated corporate items, divestiture gains/losses and restructuring, transformation, impairment and other exit costs:\n")
w(q(N, "Operating profit for these segments excludes unallocated corporate items, gain or loss on divestitures, and restructuring,", "and other exit costs.", 7000))
w(q(N, "Segment operating profit as reviewed by our executive management excludes unallocated corporate items, net gain or loss on", "that are centrally managed.", 1000))
w("The FY2026 goodwill impairment of $1,500 million related to the North America Pet reporting unit is therefore not in the segment operating profit figure below.\n")
for y in [21, 22, 23, 24, 25, 26]:
    f = F[y]
    w(f"FY20{y} segment table ({f}):\n")
    w(qf(f, "Our operating segment results were as follows:", "Unallocated corporate items"))
w("FY2021 10-K segment structure (Europe & Australia, Convenience Stores & Foodservice, Asia & Latin America) was re-presented in the FY2022 10-K (International, North America Foodservice); the Pet rows for FY2021 are identical in both ($1,732.4m net sales, $415.0m operating profit).\n")
sp = {21: (415.0, 1732.4), 22: (470.6, 2259.4), 23: (445.5, 2473.3), 24: (485.9, 2375.8), 25: (501.0, 2470.8), 26: (498.8, 2613.3)}
w("| year | segment | segment profit caption | segment profit ($m) | segment net sales ($m) | segment margin | source line |")
w("|---|---|---|---|---|---|---|")
for y, (a, b) in sp.items():
    cap = "Segment operating profit" if y >= 25 else "Operating profit (segment table)"
    seg = "North America Pet" if y >= 25 else "Pet"
    w(f"| FY20{y} | {seg} | {cap} | {a:,.1f} | {b:,.1f} | {pct(a, b)} | {ln(F[y], 'Our operating segment results were as follows:')} |")
w("")
w("FY2025 and FY2026 segment tables also show pet segment cost of sales and SG&A (FY2026: cost of sales $1,568.6m, SG&A $545.9m; FY2025: $1,476.4m and $493.4m; FY2024 as re-presented in the FY2025 10-K: $1,446.8m and $443.1m). "
  "Pet segment gross margin before SG&A, computed from those rows: FY2026 (2,613.3 - 1,568.6) / 2,613.3 = 40.0% (computed); FY2025 (2,470.8 - 1,476.4) / 2,470.8 = 40.2% (computed); FY2024 (2,375.8 - 1,446.8) / 2,375.8 = 39.1% (computed). Segment cost of sales is not disclosed by segment in the FY2021 to FY2024 10-Ks (searched the segment note).\n")

# ---------------- 3 ----------------
w("### 3. Advertising\n")
w("GIS discloses \"Advertising and media expense (including production and communication costs)\" in the notes (supplemental information table). Dollar amounts are filed; percentages of net sales are computed. Search terms used: advertis, marketing, media, \"brand support\", \"A&P\".\n")
ad = {21: 736.3, 22: 690.1, 23: 810.0, 24: 824.6, 25: 847.5, 26: 873.6}
for y in [21, 22, 23, 24, 25, 26]:
    w(qf(F[y], "Advertising and media expense (including production and communication costs)", "The components of interest"))
w("| year | advertising and media expense ($m) | net sales ($m) | % of net sales | source line |")
w("|---|---|---|---|---|")
for y in ad:
    w(f"| FY20{y} | {ad[y]:,.1f} | {ns[y]:,.1f} | {pct(ad[y], ns[y])} | {ln(F[y], 'Advertising and media expense (including production and communication costs)')} |")
w("")
w("MD&A sentences referring to media and advertising, newest year:\n")
w(q(N, "SG&A expenses decreased $57 million to $3,388 million in fiscal 2026 compared to fiscal 2025 ,", "media and advertising expenses.", 1000))
w("Pet segment advertising: not disclosed as a dollar figure by segment (searched advertis, media in the segment note and MD&A). Qualitative pet references, as filed:\n")
w(q(F[23], "Pet operating profit decreased 5 percent to $446 million in fiscal 2023,", "favorable net price realization and mix.", 7000))
w(q(F[25], "North America Pet operating profit increased 3 percent to $501 million in fiscal 2025,", "unfavorable net price realization and mix.", 7000))

# ---------------- 4 ----------------
w("### 4. Gross margin and shipping/handling placement\n")
w("GIS has no \"Gross profit\" caption on the income statement; gross margin is computed as (Net sales - Cost of sales) / Net sales from the income statement rows quoted in section 2. GIS uses the term \"Gross margin\" in MD&A for the same difference.\n")
w("| year | net sales ($m) | cost of sales ($m) | gross margin | filed MD&A figure | source line |")
w("|---|---|---|---|---|---|")
filed_gm = {21: "35.6 percent", 22: "33.7 percent", 26: "33.6 percent"}
for y in ns:
    g = ns[y] - cos[y]
    w(f"| FY20{y} | {ns[y]:,.1f} | {cos[y]:,.1f} | {g:,.1f} / {ns[y]:,.1f} = {100*g/ns[y]:.1f}% (computed) | {filed_gm.get(y, 'not transcribed')} | {ln(F[y], 'GENERAL MILLS, INC. AND SUBSIDIARIES (In Millions, Except per Share Data)')} |")
w("")
w(q(F[21], "Gross margin as a percent of net sales increased 80 basis points to 35.6 percent compared to fiscal 2020.", None))
w(q(F[22], "Gross margin as a percent of net sales decreased 190 basis points to 33.7 percent compared to fiscal 2021.", None))
w(q(N, "Gross margin as a percent of net sales of 33.6 percent decreased 100 basis points compared to fiscal 2025 .", None))
w("Shipping and handling placement: GIS records shipping costs to customers in cost of sales (accounting policy, every year):\n")
for y in [21, 26]:
    w(q(F[y], "Shipping costs associated with the distribution of finished product to our customers are recorded as cost of sales", "accepted by the customer.", 0))
w("The same sentence appears in the FY2022 to FY2025 10-Ks (FY2021 wording has a comma after \"cost of sales\"). Shipping and handling billed to customers is in net sales:\n")
w(q(N, "Sales include shipping and handling charges billed to the customer", "prompt pay discounts.", 0))

# ---------------- 6 ----------------
w("### 6. Competition and customer language\n")
w("#### (a) Colgate and Hill search\n")
w("Counts are case-insensitive substring counts on the full extracted text of each annual filing.\n")
w("| file | \"Colgate\" | \"Colegate\" (misspelling check) | \"Hill\" (all) | of which Hill's pet brand | of which other words |")
w("|---|---|---|---|---|---|")
for y in [21, 22, 23, 24, 25, 26]:
    f = F[y]
    hc = raw_count(f, r"hill")
    hb = raw_count(f, r"hill['’]s")
    w(f"| {f} | {raw_count(f, r'colgate')} | {raw_count(f, r'colegate')} | {hc} | {hb} | {hc - hb} (\"Rooty Hill, Australia\", a property listing) |")
w("")
w("No GIS annual filing on disk names Colgate, Colgate-Palmolive or Hill's. The single \"Hill\" hit in each file is a property location:\n")
w(q(N, "• Rooty Hill, Australia", None))

w("#### Competition sentences (newest annual filing, Item 1 and Item 1A)\n")
w(q(N, "The human and pet food categories are highly competitive, with numerous manufacturers of varying sizes in the United States and", "each country includes a unique group of competitors.", 200))
w(q(N, "The human and pet food categories in which we participate are very competitive.", "If we did not do the same, our revenues and market share could be adversely affected.", 400))

w("#### (b) Private label / store brands\n")
w("Search terms: private label, store brand, retailer brand, own label, value brand, generic, economy brand.\n")
w(q(N, "In most product categories, we compete not only with other widely advertised, branded products,", "generally sold at lower prices.", 200))
w(q(N, "If we are unable to build and sustain brand equity by offering", "generic and private label products.", 400))
w(q(N, "large retail customers may seek to use their position to improve their profitability", "increased promotional programs.", 400))
w(q(N, "In periods of economic", "may forego certain purchases altogether.", 600))
w(q(N, "CPW also markets cereal bars in European countries and", "customers in the United Kingdom.", 3000))

w("#### (c) Customer concentration, every year\n")
w("Item 1 sentence each year, plus the Note 8 customer concentration table (which gives a Pet segment column).\n")
for y in [21, 22, 23, 24, 25, 26]:
    f = F[y]
    sp_ = " " if y == 26 else ""
    w(f"FY20{y}:\n")
    w(q(f, f"fiscal 20{y}{sp_}, Walmart Inc. and its affiliates (Walmart) accounted for", "No other customer accounted for 10 percent or more of our consolidated net sales.", 0))
    w(qf(f, "customer concentration was as follows:", "No customer other than Walmart accounted for 10 percent or more of our consolidated net sales."))
w("| year | Walmart % consolidated net sales | Walmart % North America Retail | Walmart % Pet / North America Pet | five largest customers % Pet / North America Pet | source line |")
w("|---|---|---|---|---|---|")
wm = {21: (20, 29, 13, 71), 22: (20, 28, 16, 64), 23: (21, 28, 16, 67), 24: (22, 30, 17, 64), 25: (22, 31, 18, 66), 26: (22, 31, 17, 66)}
for y, r in wm.items():
    w(f"| FY20{y} | {r[0]} | {r[1]} | {r[2]} | {r[3]} | {ln(F[y], 'customer concentration was as follows:')} |")
w("")
w("Column assignment note: in the \"Five largest customers\" and \"Accounts receivable\" rows the Consolidated column is blank. The FY2021 extraction shows the blank as an explicit empty cell (\"Net sales | | | 53 | % ...\"), so the values run from the first segment column; for FY2022 to FY2026 the extracted rows carry one value fewer than the header and are read the same way (last value = pet column). This alignment is an inference from the extraction, flagged.\n")

w("#### (d) Pricing, elasticity, trade-down, promotion (newest MD&A; no interim filing)\n")
w(q(N, "Weak consumer sentiment, heightened uncertainty, and significant volatility weighed on category growth", "than we originally anticipated.", 800))
w(q(N, "With our price investments completed in fiscal 2026, our", "which should", 800))
w(q(N, "Amid a continued challenging macroeconomic backdrop for consumers, we expect category growth to be", "below our long-term growth projections.", 800))
w(q(N, "Organic net sales in fiscal 2026 decreased 2 percent compared to fiscal 2025 , driven by a decrease in contributions from organic", "unfavorable organic net price realization and mix.", 1000))
w(q(N, "North America Retail organic net sales decreased 3 percent in fiscal 2026 compared to fiscal 2025 ,", "a decrease in contributions from organic volume growth.", 1200))
w(q(N, "If our large competitors", "our revenues and market share could be adversely affected.", 400))
w(q(N, "Consumer demand for our products may also be impacted by changes in the level of advertising or promotional support.", None, 400))
w("Search terms used: price investment, elastic, promot, trade spend, trade expense, trade-down, pricing action, price increase, rollback, value-seeking. \"elastic\", \"trade-down\" and \"rollback\" have no hits in the FY2026 10-K.\n")

# ---------------- 7 ----------------
w("### 7. Pet channels and named pet competitors\n")
w("Channel sentences, as filed:\n")
w(q(F[21], "Our Pet operating segment includes pet food products sold primarily in the United States in national pet superstore chains,", "veterinary clinics and hospitals.", 1000))
w(q(N, "Our North America Pet operating segment includes pet food products sold primarily in the United States and Canada in national pet", "hospitals.", 1000))
w(q(N, "Our primary customers are grocery stores, mass merchandisers, membership stores,", "and pet specialty stores.", 0))
w("The FY2026 wording adds \"and Canada\" and \"fresh foods\" relative to FY2021 (compare the two segment-description quotes). \"Food, Drug and Mass\" and \"FDM\" have no hits in any GIS annual filing on disk.\n")
w("Hit counts across all GIS annual filings on disk (case-insensitive substring counts):\n")
w("| file | Purina | Nestl | Mars (substring) | Mars (whole word) | Hill's | Blue Buffalo |")
w("|---|---|---|---|---|---|---|")
for y in [21, 22, 23, 24, 25, 26]:
    f = F[y]
    c_mw = raw_count(f, r"\bmars\b"); c_hb = raw_count(f, r"hill['’]s")
    w(f"| {f} | {raw_count(f, 'purina')} | {raw_count(f, 'nestl')} | {raw_count(f, 'mars')} | {c_mw} | {c_hb} | {raw_count(f, 'blue buffalo')} |")
w("")
w("No GIS annual filing names Purina, Mars or Hill's. Every \"Nestl\" hit concerns the Cereal Partners Worldwide cereal joint venture, trademark licensing, or the exhibit index; none concerns pet food. \"Blue Buffalo\" is GIS's own pet brand. Every hit sentence, per file, deduplicated within each file:\n")
for y in [21, 22, 23, 24, 25, 26]:
    f = F[y]
    w(f"{f}:\n")
    for t, l in hit_quotes(f, r"nestl|blue buffalo|purina|\bmars\b|hill['’]s", width=350):
        w(f"> {t}\nSource: {f} line {l}\n")

# ---------------- summary ----------------
w("### Summary row\n")
w("| FY window used | organic volume by year | price by year | GAAP operating margin by year | advertising % of sales by year | gross margin by year |")
w("|---|---|---|---|---|---|")
def cm(d, fn):
    return " / ".join(f"FY{y} {fn(y)}" for y in d)
w("| FY2021 to FY2026 (years end last Sunday of May; FY2026 = 53 weeks) | Total [Contributions from organic volume growth, tons]: FY21 +2 / FY22 -1 / FY23 -4 / FY24 -3 / FY25 Flat / FY26 -1; Pet [same label]: FY21 +2 / FY22 +8 / FY23 -3 / FY24 -7 / FY25 +3 / FY26 -5 | Total [Organic net price realization and mix]: FY21 +2 / FY22 +7 / FY23 +14 / FY24 +2 / FY25 -1 / FY26 -1; Pet [same label]: FY21 Flat / FY22 +10 / FY23 +11 / FY24 +3 / FY25 -2 / FY26 +2 | "
  + cm(op, lambda y: f"{100*op[y]/ns[y]:.1f}") + "; Pet [segment operating profit, non-GAAP segment measure]: " + cm(sp, lambda y: f"{100*sp[y][0]/sp[y][1]:.1f}") + " | "
  + "[Advertising and media expense] " + cm(ad, lambda y: f"{100*ad[y]/ns[y]:.1f}") + " | "
  + "[(net sales - cost of sales)/net sales; shipping in cost of sales] " + cm(ns, lambda y: f"{100*(ns[y]-cos[y])/ns[y]:.1f}") + " |")
w("")

# ---------------- gaps ----------------
w("### Gaps, extraction problems and definition differences\n")
w("- No interim filing after the FY2026 10-K is on disk; no interim data reported.")
w("- Price and mix are not separated: GIS reports one component, \"(Organic) net price realization and mix\". Separate price and mix: not disclosed in any GIS 10-K on disk (searched \"price realization\", \"mix\").")
w("- Volume is measured in tons (\"Measured in tons based on the stated weight of our product shipments\"), not units or cases.")
w("- Pet segment advertising dollars: not disclosed (searched advertis, media in segment note and MD&A). Pet segment cost of sales: disclosed only in the FY2025 and FY2026 10-K segment tables (covering FY2024 to FY2026).")
w("- Fiscal week count for FY2023: not stated in the FY2023, FY2024 or FY2025 10-Ks (searched \"52 weeks\", \"53 weeks\").")
w("- Customer concentration table: the Consolidated column is blank for the \"Five largest customers\" and \"Accounts receivable\" rows; column alignment in the FY2022 to FY2026 extractions is inferred (see 6(c)).")
w("- Extraction artefacts: FY2026 10-K line 457 \"account ed\" and \"North A merica\"; FY2026 line 1097 \"w e\"; FY2021 to FY2025 glossary \"53 rd week\" split; FY2022 to FY2025 files break many sentences into one word per line (quotes above join them with single spaces); the FY2021 file carries many empty \" | \" cells. None of these change a number.")
w("- Segment naming: \"Pet\" through the FY2024 10-K; renamed \"North America Pet\" in the first quarter of fiscal 2025 with no change to composition (quoted above). Pet food results outside North America are in the International segment (including the pet food business in Europe acquired in the fourth quarter of fiscal 2024).")
w("- GIS definition of organic growth, as filed:")
w("")
w(q(N, "Organic net sales growth . Net sales growth adjusted for foreign currency translation, as well as acquisitions, divestitures, and a 53rd", "week impact, when applicable.", 7000))
w(q(N, "We believe that organic net sales growth rates provide useful information to investors because they provide", "have on year-to-year comparability.", 2000))
w("- Differences from Colgate's definition (Colgate: net sales growth excluding foreign exchange, acquisitions and divestments; components \"volume\" and \"net selling price\"):")
w("  - GIS also excludes a 53rd week (FY2021 organic table shows 53rd week (2) pts, lapping 53-week FY2020; FY2026 shows 53rd week +2 pts in total and in North America Pet). Colgate's calendar year has no 53rd-week adjustment.")
w("  - GIS combines price and mix into one component (\"net price realization and mix\"); Colgate reports volume and net selling price separately (Colgate's mix treatment is not addressed in GIS filings).")
w("  - GIS volume is tonnage-based and shown both including (reported table) and excluding (organic table) acquisitions and divestitures; e.g. Pet FY2022 volume 11 pts reported vs 8 pts organic.")
w("  - No hyperinflation exclusion (e.g. Argentina) or price-growth cap is described in the GIS organic definition (searched hyperinflat, Argentina: not part of the definition).")
w("  - Fiscal year ends on the last Sunday in May, not December 31. GIS FY2026 covers roughly June 2025 to May 2026.")
w("  - Net price realization is defined net of trade and other price promotion costs (glossary, quoted in section 1).")
w("- Shipping and handling: GIS records shipping costs to customers in cost of sales. Colgate reports shipping and handling in SG&A, so GIS gross margins (section 4) are not on the same basis as Colgate gross margins.")
w("- Segment operating profit is a management segment measure, not GAAP; it excludes restructuring, impairment (including the FY2026 $1,500 million North America Pet goodwill impairment) and unallocated corporate items.")
w("- Accounting restatements: none of the FY2021 to FY2025 total net sales, cost of sales or operating profit figures differ between the first-reporting 10-K and later 10-Ks on disk (checked FY2021 to FY2025 income statement rows across the overlapping 10-Ks). SG&A and divestiture captions changed wording but not amounts.")

md = "\n".join(out) + "\n"
open("SECTION_GIS.md", "w", encoding="utf-8").write(md)
print("written", len(md))
