import sys,re
sys.stdout.reconfigure(encoding="utf-8")
from _scratch_CHD_lib import *
F={21:"CHD_10K_FY2021_2021-12-31.txt",22:"CHD_10K_FY2022_2022-12-31.txt",23:"CHD_10K_FY2023_2023-12-31.txt",
   24:"CHD_10K_FY2024_2024-12-31.txt",25:"CHD_10K_FY2025_2025-12-31.txt"}
Q="CHD_10Q_2026-06-30.txt"
out=[]
w=out.append
def pct(n,d): return f"{n:,.1f} / {d:,.1f} = {100*n/d:.1f}% (computed)"
def chk(text,*vals):
    for v in vals:
        assert v in text, (v,text)

w("""## Church & Dwight Co., Inc. (CHD)

Transcription only. No judgment is expressed. Line numbers are the 0-based line index printed by `g.py` in the peers folder. CHD's text extraction puts each table cell on its own line; a table-row quote below is the consecutive lines of that row joined with single spaces (whitespace-normalised), and its Source line gives the first line and the last line of the row. Dollar figures are in millions as filed ("Dollars in millions, except share and per share data").

### Documents used

| file | form | fiscal period end | filing date | accession |
|---|---|---|---|---|
| CHD_10K_FY2021_2021-12-31.txt | 10-K | 2021-12-31 | 2022-02-17 | 0001564590-22-005528 |
| CHD_10K_FY2022_2022-12-31.txt | 10-K | 2022-12-31 | 2023-02-16 | 0000950170-23-003066 |
| CHD_10K_FY2023_2023-12-31.txt | 10-K | 2023-12-31 | 2024-02-15 | 0000950170-24-015810 |
| CHD_10K_FY2024_2024-12-31.txt | 10-K | 2024-12-31 | 2025-02-13 | 0000950170-25-019801 |
| CHD_10K_FY2025_2025-12-31.txt | 10-K | 2025-12-31 | 2026-02-12 | 0001193125-26-048139 |
| CHD_10Q_2026-06-30.txt | 10-Q | 2026-06-30 (quarter and six months) | 2026-07-31 | 0001193125-26-327567 |

Source of the table: manifest_list.txt. Fiscal year is the calendar year (December 31 year end).

### 1. Organic sales decomposition

**What CHD files.** None of the five 10-Ks reports an "organic" sales figure. A case-insensitive search for "organic" returns 2 hits in each 10-K, and in every 10-K both are unrelated to sales measurement: one is "a growing demand for natural or organic products and ingredients" (risk factors) and one is "make capital expenditures to support organic growth and gross margin improvements" (MD&A). FY2025 lines:
""")
w(sent(F[25],433,r"a growing demand for natural or organic products and ingredients"))
w(sent(F[25],923,r"make capital expenditures to support organic growth and gross margin improvements"))
w("""
What CHD files instead, in MD&A, is a table of "the components of the net sales increase" (consolidated) and "the components of the net sales change" (each segment), with the rows "Product volumes sold", "Pricing/Product mix", "Foreign exchange rate fluctuations" (in the FY2021 and FY2022 consolidated tables: "Foreign exchange rate fluctuations / Other"), and acquisition or exit rows whose labels change by year. Each 10-K table has a single column, current year versus prior year. The rows are quoted below exactly as filed, for Consolidated, Consumer Domestic, Consumer International and SPD (Specialty Products Division, included so the total can be reconciled).

The 10-Q (six months ended June 30, 2026) uses the words "organic sales growth" and "organic sales volumes" in segment commentary, without a definition or a number:
""")
w(sent(Q,8541,r"In the current year, strong organic sales growth across household and personal care, plus sales volume from the Touchland and Miss Mouth's acquisitions, partially offset by the sales impact from the exited businesses, contributed \$21\.5\."))
w(sent(Q,8662,r"In the current year, the increase is due primarily to the impact of strong organic sales volumes across the portfolio, plus sales volume from the Touchland acquisition of \$15\.1,"))

hdr_sent={21:(1415,r"Net sales for the year ended December 31, 2021 were \$5,190\.1, an increase of \$294\.3, or 6\.0% compared to 2020 net sales\."),
          22:(1055,r"Net sales for the year ended December 31, 2022 were \$5,375\.6, an increase of \$185\.5, or 3\.6% compared to 2021 net sales\."),
          23:(1112,r"Net sales for the year ended December 31, 2023 were \$5,867\.9, an increase of \$492\.3, or 9\.2% compared to 2022 net sales\."),
          24:(1157,r"Net sales for the year ended December 31, 2024 were \$6,107\.1, an increase of \$239\.2, or 4\.1% compared to 2023 net sales\."),
          25:(1171,r"Net sales for the year ended December 31, 2025 were \$6,203\.2, an increase of \$96\.1, or 1\.6% compared to 2024 net sales\.")}
for y in [21,22,23,24,25]:
    f=F[y]; L=lines(f)
    w(f"\n#### FY20{y} (first reported in {f})\n")
    i,p=hdr_sent[y]
    w(sent(f,i,p))
    for k,l in enumerate(L):
        if re.match(r"\s*Net Sales - ",l):
            w("\n"+comp_table(f,k))
w("\nFootnotes and narrative attached to the tables:\n")
w(sent(F[21],1461,r"The volume change reflects increased product sales in the Consumer International and SPD segments, partially offset by slightly decreased sales in the Consumer Domestic segment \."))
w(sent(F[21],1935,r"Includes the TheraBreath and Zicam Acquisitions since the date of acquisition\."))
w(sent(F[22],1101,r"The volume change reflects decreased product unit sales for all three segments\. Price/mix was favorable in all three segments\."))
w(sent(F[23],1147,r"The volume change reflects increased volumes in the Consumer Domestic and Consumer International Segments partially offset by volume declines in SPD\."))
w(sent(F[24],1191,r"\(1\) The volume change reflects increased product unit sales in all three segments\."))
w(sent(F[24],1193,r"\(3\) In the first quarter of 2024, we exited the MEGALAC supplement portion of the SPD Animal Nutrition business\. In the second quarter of 2024 we acquired substantially all of Graphico and sold the Passport food safety business\."))
w(sent(F[25],1212,r"\(1\) The volume change reflects increased product unit sales in the Consumer International and SPD segments\. Volumes were also impacted by a decline in the vitamin business which was sold on December 31, 2025\."))
w(sent(F[25],1213,r"\(2\) Price/mix was unfavorable in the Consumer Domestic segment, partially offset by the SPD and Consumer International segments\."))
w(sent(F[25],900,r"Excluding these items, Consumer International and SPD experienced favorable volumes and pricing/product mix, partially offset by lower price/mix in Consumer Domestic\."))

w("\n#### Interim: three and six months ended June 30, 2026 (CHD_10Q_2026-06-30.txt)\n")
w(sent(Q,7857,r"Net sales for the six months ended June 30, 2026 were \$2,999\.3, an increase of \$25\.9 or 0\.9% over the comparable six month period of 2025\."))
w("Column header rows above the consolidated table (first numeric column = three months, second = six months):\n")
w(qjoin(Q,7858,7873))
for k in (7874,8464,8564,8684):
    w("\n"+comp_table(Q,k))
w(sent(Q,7961,r"\(1\) For the three and six months ended June 30, 2026, the volume change reflects increased product unit sales in all three segments\."))
w(sent(Q,7962,r"\(2\) For the three and six months ended June 30, 2026, price/mix was favorable in all three segments\."))
w(sent(Q,7963,r"\(3\) In the fourth quarter of 2025, we divested the VMS business\."))

w("""
#### Parsed table

Sign convention: the filing shows negatives in parentheses; below, negatives carry a minus sign. All figures are percent change versus the prior-year period. "Organic" is "nd" throughout because CHD does not file an organic figure in these documents. The column "vol + price/mix" is computed by adding the two filed components; it is NOT a filed organic growth number and is shown only as arithmetic.

| period | scope | reported net sales growth | organic | volume ["Product volumes sold"] | price ["Pricing/Product mix"] | mix (separate) | FX | acq/div | other | vol + price/mix (computed) | label wording used | source line |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2021 | Consolidated | +6.0 | nd | +1.0 | +3.3 | not separate | +0.9 (FX / Other combined) | +0.8 "Volume from acquired product lines (net of divestiture)" | in FX row | +4.3 | "Foreign exchange rate fluctuations / Other" | CHD_10K_FY2021 1416-1456 |
| FY2021 | Consumer Domestic | +4.6 | nd | -0.3 | +3.9 | not separate | no row | +1.0 "Acquired product lines" | none | +3.6 | as filed | CHD_10K_FY2021 1899-1932 |
| FY2021 | Consumer International | +10.1 | nd | +5.3 | -0.3 | not separate | +5.1 | no row | none | +5.0 | "Foreign exchange rate fluctuations" | CHD_10K_FY2021 1943-1975 |
| FY2021 | SPD | +12.0 | nd | +4.6 | +7.4 | not separate | no row | no row | none | +12.0 | as filed | CHD_10K_FY2021 1984-2009 |
| FY2022 | Consolidated | +3.6 | nd | -5.1 | +6.5 | not separate | -1.0 (FX / Other combined) | +3.2 "Acquired product lines" | in FX row | +1.4 | "Foreign exchange rate fluctuations / Other" | CHD_10K_FY2022 1060-1099 |
| FY2022 | Consumer Domestic | +4.8 | nd | -5.9 | +6.8 | not separate | no row | +3.9 "Acquired product lines" | none | +0.9 | as filed | CHD_10K_FY2022 1549-1581 |
| FY2022 | Consumer International | -1.8 | nd | -1.7 | +4.5 | not separate | -5.5 | +0.9 "Acquired product lines" | none | +2.8 | as filed | CHD_10K_FY2022 1592-1631 |
| FY2022 | SPD | +3.7 | nd | -5.1 | +8.8 | not separate | no row | no row | none | +3.7 | as filed | CHD_10K_FY2022 1645-1670 |
| FY2023 | Consolidated | +9.2 | nd | +0.9 | +4.4 | not separate | no row in consolidated table | +3.9 "Acquired product lines" | none | +5.3 | as filed | CHD_10K_FY2023 1113-1145 |
| FY2023 | Consumer Domestic | +10.7 | nd | +1.0 | +4.7 | not separate | no row | +5.0 "Acquired product lines" | none | +5.7 | as filed | CHD_10K_FY2023 1555-1587 |
| FY2023 | Consumer International | +8.9 | nd | +3.4 | +5.1 | not separate | +0.1 | +0.3 "Acquired product lines" | none | +8.5 | as filed | CHD_10K_FY2023 1594-1633 |
| FY2023 | SPD | -7.9 | nd | -7.2 | -0.7 | not separate | no row | no row | none | -7.9 | as filed | CHD_10K_FY2023 1643-1668 |
| FY2024 | Consolidated | +4.1 | nd | +3.3 | +1.3 | not separate | no row in consolidated table | -0.5 "Exit of product lines (net of acquisition)" | none | +4.6 | as filed | CHD_10K_FY2024 1158-1190 |
| FY2024 | Consumer Domestic | +3.5 | nd | +2.8 | +0.7 | not separate | no row | no row | none | +3.5 | as filed | CHD_10K_FY2024 1556-1581 |
| FY2024 | Consumer International | +9.8 | nd | +5.7 | +3.3 | not separate | -0.2 | +1.0 "Acquired product lines" | none | +9.0 | as filed | CHD_10K_FY2024 1587-1626 |
| FY2024 | SPD | -5.5 | nd | +4.0 | +3.1 | not separate | no row | -12.6 "Exit of product lines" | none | +7.1 | as filed | CHD_10K_FY2024 1636-1668 |
| FY2025 | Consolidated | +1.6 | nd | +0.8 | -0.1 | not separate | no row in consolidated table | -1.0 "Exit of product lines"; +1.9 "Acquisitions" | none | +0.7 | as filed | CHD_10K_FY2025 1172-1211 |
| FY2025 | Consumer Domestic | +0.9 | nd | 0.0 | -0.5 | not separate | no row | +2.2 "Acquisitions"; -0.8 "Exit of product lines" | none | -0.5 | as filed | CHD_10K_FY2025 1574-1613 |
| FY2025 | Consumer International | +5.4 | nd | +4.9 | +0.6 | not separate | -0.2 | -0.9 "Exit of product lines"; +1.0 "Acquisitions" | none | +5.5 | as filed | CHD_10K_FY2025 1621-1667 |
| FY2025 | SPD | -1.4 | nd | +0.3 | +2.3 | not separate | +0.3 | -4.3 "Exit of product lines" | none | +2.6 | as filed | CHD_10K_FY2025 1678-1717 |
| H1 2026 (six months) | Consolidated | +0.9 | nd | +4.8 | +0.6 | not separate | +0.7 | -7.6 "Exit of product lines"; +2.4 "Acquisitions" | none | +5.4 | as filed | CHD_10Q 7874-7960 (six-month column) |
| H1 2026 (six months) | Consumer Domestic | -0.5 | nd | +4.6 | +0.7 | not separate | no row | -8.7 "Exit of product lines"; +2.9 "Acquisitions" | none | +5.3 | "Net Sales increase(decrease)" | CHD_10Q 8464-8537 (six-month column) |
| H1 2026 (six months) | Consumer International | +5.9 | nd | +6.4 | +0.1 | not separate | +3.8 | -5.4 "Exit of product lines"; +1.0 "Acquisitions" | none | +6.5 | as filed | CHD_10Q 8564-8657 (six-month column) |
| H1 2026 (six months) | SPD | +2.9 | nd | +1.7 | +1.2 | not separate | no row | no row | none | +2.9 | as filed | CHD_10Q 8684-8735 (six-month column) |
| Q2 2026 (three months) | Consolidated | +1.6 | nd | +4.3 | +1.5 | not separate | +0.4 | -7.4 "Exit of product lines"; +2.8 "Acquisitions" | none | +5.8 | as filed | CHD_10Q 7874-7960 (three-month column) |

Reconciliation note: the FY2023 and FY2024 consolidated tables add to the filed total without any foreign exchange row (FY2023: 0.9 + 4.4 + 3.9 = 9.2; FY2024: 3.3 + 1.3 - 0.5 = 4.1, computed), although the Consumer International tables for those years show foreign exchange rows of +0.1 and -0.2. The FY2025 consolidated components add to 1.6 (0.8 - 0.1 - 1.0 + 1.9 = 1.6, computed) with no foreign exchange row, although the Consumer International and SPD tables show foreign exchange rows. The filings do not say where consolidated foreign exchange effects sit in those years.
""")

# ---------------- 2. operating margin
w("\n### 2. GAAP operating margin (and segment margin)\n")
w("""Total company profit line used: **"Income from Operations"**, the caption on the Consolidated Statements of Income (GAAP). Each year is taken from the 10-K that first reports it. The same figures reappear unchanged in the later 10-Ks on disk (FY2021 in the FY2022 and FY2023 10-Ks, FY2022 in the FY2023 and FY2024 10-Ks, FY2023 and FY2024 in the FY2025 10-K). The FY2024 10-K re-presents FY2022 SG&A as $706.0 plus a separate "Flawless Trade name and other asset impairments" line of $411.0, versus $1,117.0 of SG&A in the FY2022 10-K, with Income from Operations unchanged at $597.8.
""")
def is_rows(f,capts):
    s=find(f,r"STATEMENTS OF INCOME"); m=find(f,r"^\s*\(In millions",s)
    ns=find(f,r"^\s*Net Sales\s*$",m)
    res=[qjoin(f,m+1,ns-1)]
    idx={}
    for c in capts:
        k=find(f,r"^\s*"+re.escape(c)+r"\s*$",ns)
        t,a,b=row(f,k); res.append(q(t,f,a,b)); idx[c]=t
    return "".join(res),idx
cap=["Net Sales","Cost of sales","Gross Profit","Marketing expenses","Income from Operations"]
vals={21:(5190.1,2926.6,2263.5,577.7,1079.1),22:(5375.6,3125.6,2250.0,535.2,597.8),23:(5867.9,3279.4,2588.5,641.3,1057.4),
      24:(6107.1,3317.0,2790.1,698.1,807.1),25:(6203.2,3428.4,2774.8,708.9,1077.6)}
for y in [21,22,23,24,25]:
    t,idx=is_rows(F[y],cap)
    for c,v in zip(cap,vals[y]):
        chk(idx[c].split("|")[0]+"|".join(idx[c].split("|")[1:5]),f"{v:,.1f}")
    w(f"\nConsolidated Statements of Income, {F[y]} (columns: FY20{y}, then the two prior years):\n")
    w(t)
t,idx=is_rows(Q,cap)
qv=(2999.3,1624.0,1375.3,304.7,567.4); qv25=(2973.4,1666.8,1306.6,293.7,557.0)
for c,v,v2 in zip(cap,qv,qv25): chk(idx[c],f"{v:,.1f}",f"{v2:,.1f}")
w("\nCondensed Consolidated Statements of Income, CHD_10Q_2026-06-30.txt (columns: three months 2026, three months 2025, six months 2026, six months 2025):\n")
w(t)
w(sent(Q,7973,r"Operating margin increased 20 basis points to 18\.9% for the six months ended June 30, 2026, as compared to 18\.7% in the same period in 2025\."))
w("\n| period | Net Sales | Income from Operations | GAAP operating margin | source line |\n|---|---|---|---|---|\n")
for y in [21,22,23,24,25]:
    n,_,_,_,oi=vals[y]
    w(f"| FY20{y} | {n:,.1f} | {oi:,.1f} | {pct(oi,n)} | {F[y]} income statement rows above |\n")
w(f"| H1 2026 | 2,999.3 | 567.4 | {pct(567.4,2999.3)}; filed 18.9% | CHD_10Q rows 262 and 376; filed at 7973 |\n")
w(f"| H1 2025 | 2,973.4 | 557.0 | {pct(557.0,2973.4)}; filed 18.7% | CHD_10Q rows 262 and 376; filed at 7973 |\n")
w("""
Filed items inside Income from Operations (not adjusted here): FY2022 includes "Flawless Trade name and other asset impairments" of $411.0 (inside SG&A in the FY2022 10-K presentation); FY2024 includes "VMS Trade name and other asset impairments" of $357.1; FY2025 includes charges for exiting the Flawless, Spinbrush and Waterpik showerheads businesses and Touchland transaction costs (MD&A quotes in the segment discussion below).
""")
w("""
**Segment measure.** The segment profit caption in the segment note is **"Income from Operations"** for every year FY2021 to FY2025 and in the 10-Q. The FY2021 to FY2023 segment notes also show a per-segment **"Income Before Income Taxes"** row, and the FY2021 to FY2023 MD&A segment discussion uses "income before income taxes"; from FY2024 the MD&A uses "income from operations". The FY2024 and FY2025 notes state what the chief operating decision maker uses:
""")
w(sent(F[24],9543,r"The CODM considers Operating Income for evaluating performance of each segment"))
w(sent(F[25],9760,r"The CODM considers Income from Operations for evaluating performance of each segment and making decisions about allocating capital and other resources to each segment\."))
w(sent(F[21],1939,r"Consumer Domestic income before income taxes for 2021 was \$861\.4, a \$29\.0 increase as compared to 2020\."))
w(sent(F[25],1617,r"Consumer Domestic income from operations for 2025 was \$920\.8, a \$235\.9 increase as compared to 2024\."))
w(sent(F[25],1617,r"Income from operations was impacted for the year ended 2025 by non-cash charges associated with exiting the Flawless, Spinbrush, and Waterpik showerheads businesses of \$45\.6 and transaction-related costs of \$30\.5 relating to the Touchland Acquisition\."))
w("Production planning and logistics administrative costs sit in cost of sales in the consolidated statement but are moved into segment SG&A:\n")
w(sent(F[24],1673,r"Corporate includes administrative costs of the production, planning and logistics functions which are reported as Cost of Sales in our Consolidated Statements of Income but are allocated to the operating segments in SG&A expenses to determine segment income from operations\."))
w(sent(F[25],10489,r"\(1\) Reflects the a dministrative costs of the production planning and logistics functions which are elements of Cost of Sales in the Company’s Consolidated Statements of Income but are allocated to the operating segments in Selling, General and Administrative expenses to determine operating segment income before income taxes \."))
w("(Extraction artefact in the line above: \"a dministrative\" is split in the text file. The footnote says \"income before income taxes\" while the table row caption is \"Income from Operations\"; both are as filed.)\n")

def note_old(y,fy):
    f=F[y]; p=find(f,r"The following table presents selected financial information relating to the Company’s segments")
    ns=find(f,r"^\s*Net sales\s*$",p)
    res=[qjoin(f,p+1,ns-1)]
    got={}
    for c in ["Net sales","Marketing Expenses","Income from Operations","Income Before Income Taxes"]:
        k=find(f,r"^\s*"+re.escape(c)+r"\s*$",p)
        res.append(q(norm(lines(f)[k]),f,k))
        yr=find(f,r"^\s*"+fy+r"\s*$",k)
        t,a,b=row(f,yr,stop_year=True); res.append(q(t,f,a,b)); got[c]=t
    return "".join(res),got
def note_new(y,fy):
    f=F[y]; h=find(f,r"^\s*Year Ended December 31, "+fy+r"\s*$")
    ns=find(f,r"^\s*Net Sales\s*$",h)
    res=[qjoin(f,h,ns-1)]; got={}
    for c in ["Net Sales","Marketing expenses","Income from Operations"]:
        k=find(f,r"^\s*"+re.escape(c)+r"\s*$",h)
        t,a,b=row(f,k); res.append(q(t,f,a,b)); got[c]=t
    return "".join(res),got
segv={21:((3941.9,912.2,336.0),(442.1,131.1,4.5),(908.4,135.3,35.4)),
      22:((4131.0,896.1,348.5),(412.9,117.7,4.6),(499.1,46.2,52.5)),
      23:((4571.2,975.7,321.0),(509.5,127.7,4.1),(929.7,104.2,23.5)),
      24:((4732.3,1071.5,303.3),(538.5,156.9,2.7),(684.9,83.1,39.1)),
      25:((4774.8,1129.4,299.0),(532.7,172.7,3.5),(920.8,116.2,40.6))}
for y in [21,22,23]:
    t,got=note_old(y,f"20{y}")
    ns,mk,oi=segv[y]
    for v in ns: chk(got["Net sales"],f"{v:,.1f}")
    for v in mk: chk(got["Marketing Expenses"],f"{v:,.1f}")
    for v in oi: chk(got["Income from Operations"],f"{v:,.1f}")
    w(f"\nSegment note, {F[y]} (columns: Consumer Domestic, Consumer International, SPD, Corporate, As Reported; each caption row is followed by its FY20{y} row):\n")
    w(t)
for y in [24,25]:
    t,got=note_new(y,f"20{y}")
    ns,mk,oi=segv[y]
    for v in ns: chk(got["Net Sales"],f"{v:,.1f}")
    for v in mk: chk(got["Marketing expenses"],f"{v:,.1f}")
    for v in oi: chk(got["Income from Operations"],f"{v:,.1f}")
    w(f"\nSegment note, {F[y]}, FY20{y} table:\n")
    w(t)
def q_seg(title):
    h=find(Q,r"^\s*"+title+r"\s*$"); ns=find(Q,r"^\s*Net Sales\s*$",h)
    res=[qjoin(Q,h,ns-1)]; got={}
    for c in ["Net Sales","Marketing expenses","Income from Operations"]:
        k=find(Q,r"^\s*"+re.escape(c)+r"\s*$",h); t,a,b=row(Q,k); res.append(q(t,Q,a,b)); got[c]=t
    return "".join(res),got
t26,g26=q_seg("Six Months Ended June 30, 2026"); t25,g25=q_seg("Six Months Ended June 30, 2025")
for v in (2273.5,571.4,154.4): chk(g26["Net Sales"],f"{v:,.1f}")
for v in (463.6,81.5,22.3): chk(g26["Income from Operations"],f"{v:,.1f}")
for v in (225.1,78.4): chk(g26["Marketing expenses"],f"{v:,.1f}")
for v in (2283.9,539.5,150.0): chk(g25["Net Sales"],f"{v:,.1f}")
for v in (462.2,70.1,24.7): chk(g25["Income from Operations"],f"{v:,.1f}")
for v in (225.7,66.3): chk(g25["Marketing expenses"],f"{v:,.1f}")
w("\nSegment note, CHD_10Q_2026-06-30.txt, six months ended June 30, 2026 and six months ended June 30, 2025:\n")
w(t26); w(t25)

w("\n| period | segment | segment Net Sales | segment Income from Operations | segment margin | source |\n|---|---|---|---|---|---|\n")
names=("Consumer Domestic","Consumer International","SPD")
for y in [21,22,23,24,25]:
    ns,mk,oi=segv[y]
    for i,nm in enumerate(names):
        w(f"| FY20{y} | {nm} | {ns[i]:,.1f} | {oi[i]:,.1f} | {pct(oi[i],ns[i])} | {F[y]} segment note rows above |\n")
for lab,nsv,oiv in (("H1 2026",(2273.5,571.4,154.4),(463.6,81.5,22.3)),("H1 2025",(2283.9,539.5,150.0),(462.2,70.1,24.7))):
    for i,nm in enumerate(names):
        w(f"| {lab} | {nm} | {nsv[i]:,.1f} | {oiv[i]:,.1f} | {pct(oiv[i],nsv[i])} | CHD_10Q segment note rows above |\n")
w("""
The segment margin uses CHD's segment measure "Income from Operations" (a segment measure; the three segments sum to consolidated GAAP Income from Operations, with zero in the Corporate or Consolidating Reclassification column). It includes each segment's share of the filed impairment charges: FY2022 Flawless $349.3 (Consumer Domestic) and $61.7 (Consumer International); FY2024 VMS $327.4 (Consumer Domestic) and $29.7 (Consumer International), per the FY2024 10-K segment tables.
""")
w(sent(F[25],1674,r"Consumer International income from operations was \$116\.2 in 2025, an increase of \$33\.1 compared to 2024\."))

# ---------------- 3. advertising
w("\n### 3. Advertising\n")
w("""CHD does not disclose a separate "advertising expense" or "advertising costs" dollar amount in any of the five 10-Ks or the 10-Q. Search terms used (case-insensitive): "advertis", "advertising costs", "advertising expense", "marketing", "brand support", "media", "A&P". Every "advertis" hit is risk-factor language, the revenue-recognition policy on cooperative advertising (netted against sales), or the definition of Marketing expenses below; no "advertis" sentence carries a dollar amount (regex "advertis[^.]*\\$|\\$[^.]*advertis": 0 hits in all six files). The filed line is the income-statement caption **"Marketing expenses"**, which the accounting policy says includes advertising:
""")
w(sent(F[25],4839,r"Marketing expenses include costs for advertising \(excluding the costs of cooperative advertising programs, which are reflected in net sales\), costs for coupon insertion \(mainly the cost of printing and distribution\), consumer promotion costs \(such as on-shelf advertisements and floor ads\), public relations, package design expense and market research costs\."))
w(sent(F[21],5164,r"Marketing expenses include costs for advertising \(excluding the costs of cooperative advertising programs, which are reflected in net sales\)"))
w(sent(F[25],4829,r"The Company conducts extensive promotional activities, primarily through the use of off-list discounts, slotting, coupons, cooperative advertising, periodic price reduction arrangements, and end-aisle and other in-store displays\. The costs of such activities are netted against sales and are recorded when the related sale takes place\."))
w("\nMD&A statements of Marketing expenses and the filed percentage of net sales:\n")
w(sent(F[21],1464,r"Marketing expenses for 2021 were \$577\.7, a decrease of \$13\.5 compared to 2020\."))
w(sent(F[21],1464,r"Marketing expenses as a percentage of net sales decreased 100 bps to 11\.1% in 2021 as compared to 2020"))
w(sent(F[22],1105,r"Marketing expenses as a percentage of net sales decreased 110 bps to 10\.0% in 2022 as compared to 2021"))
w(sent(F[23],1151,r"Marketing expenses as a percentage of net sales increased 90 bps to 10\.9% in 2023 as compared to 2022"))
w(sent(F[24],1200,r"Marketing expenses as a percentage of net sales increased 50 bps to 11\.4% in 2024 as compared to 2023"))
w(sent(F[25],1222,r"Marketing expenses for 2025 were \$708\.9, an increase of \$10\.8 compared to 2024\. Marketing expenses as a percentage of net sales was 11\.4% in 2025 and 2024\."))
w(sent(Q,7969,r"Marketing expenses for the six months ended June 30, 2026 were \$304\.7, an increase of \$11\.0 or 3\.7% as compared to the same period in 2025\."))
w(sent(Q,7969,r"Marketing expenses as a percentage of net sales for the first six months of 2026 increased by 30 bps to 10\.2% as compared to 9\.9% in the same period in 2025"))
w("\nThe Marketing expenses and Net Sales rows are quoted in section 2 (income statements and segment notes).\n")
w("\n| period | scope | Marketing expenses | Net Sales | % of net sales | filed % | source |\n|---|---|---|---|---|---|---|\n")
filed={21:"11.1%",22:"10.0%",23:"10.9%",24:"11.4%",25:"11.4%"}
for y in [21,22,23,24,25]:
    n,_,_,mk,_=vals[y]
    w(f"| FY20{y} | Total | {mk:,.1f} | {n:,.1f} | {pct(mk,n)} | {filed[y]} | {F[y]} income statement; MD&A sentence above |\n")
w(f"| H1 2026 | Total | 304.7 | 2,999.3 | {pct(304.7,2999.3)} | 10.2% | CHD_10Q rows 332 and 262; filed at 7969 |\n")
w(f"| H1 2025 | Total | 293.7 | 2,973.4 | {pct(293.7,2973.4)} | 9.9% | CHD_10Q rows 332 and 262; filed at 7969 |\n")
for y in [21,22,23,24,25]:
    ns,mk,oi=segv[y]
    for i,nm in enumerate(names[:2]):
        w(f"| FY20{y} | {nm} | {mk[i]:,.1f} | {ns[i]:,.1f} | {pct(mk[i],ns[i])} | not filed | {F[y]} segment note |\n")
for lab,nsv,mkv in (("H1 2026",(2273.5,571.4),(225.1,78.4)),("H1 2025",(2283.9,539.5),(225.7,66.3))):
    for i,nm in enumerate(names[:2]):
        w(f"| {lab} | {nm} | {mkv[i]:,.1f} | {nsv[i]:,.1f} | {pct(mkv[i],nsv[i])} | not filed | CHD_10Q segment note |\n")
w("\nMarketing expenses is broader than advertising (it also contains coupon insertion, consumer promotion, public relations, package design and market research) and excludes cooperative advertising, which is netted against net sales.\n")

# ---------------- 4. gross margin
w("\n### 4. Gross margin and shipping/handling placement\n")
w("Gross Profit is a caption on the Consolidated Statements of Income (rows quoted in section 2). MD&A statements of gross margin:\n")
w(sent(F[21],1462,r"Gross margin was 43\.6% in 2021 compared to 45\.2% in 2020, a 160 basis points \(“bps”\) decrease\."))
w(sent(F[22],1103,r"Gross margin was 41\.9% in 2022 compared to 43\.6% in 2021, a 170 basis points \(“bps”\) decrease\."))
w(sent(F[23],1149,r"Gross margin was 44\.1% in 2023 compared to 41\.9% in 2022, a 220 basis points \(“bps”\) increase\."))
w(sent(F[24],1195,r"Gross margin was 45\.7% in 2024 compared to 44\.1% in 2023, a 160 basis points \(“bps”\) increase\."))
w(sent(F[25],1220,r"Gross margin was 44\.7% in 2025 compared to 45\.7% in 2024, a 100 basis points \(“bps”\) decrease\."))
w(sent(Q,7967,r"Gross margin increased 200 bps in the first six months of 2026 compared to the same period in 2025\."))
w("\n| period | Gross Profit | Net Sales | gross margin | filed | source |\n|---|---|---|---|---|---|\n")
gfiled={21:"43.6%",22:"41.9%",23:"44.1%",24:"45.7%",25:"44.7%"}
for y in [21,22,23,24,25]:
    n,c,g,_,_=vals[y]
    w(f"| FY20{y} | {g:,.1f} | {n:,.1f} | {pct(g,n)} | {gfiled[y]} | {F[y]} income statement |\n")
w(f"| H1 2026 | 1,375.3 | 2,999.3 | {pct(1375.3,2999.3)} | level not stated (stated as +200 bps) | CHD_10Q rows 310 and 262 |\n")
w(f"| H1 2025 | 1,306.6 | 2,973.4 | {pct(1306.6,2973.4)} | not stated | CHD_10Q rows 310 and 262 |\n")
w("\n**Shipping and handling placement: cost of sales.** The accounting policy lists freight to customers and warehousing inside cost of sales:\n")
w(sent(F[25],4838,r"Cost of sales include costs related to the manufacture and distribution of the Company’s products, including raw material, inbound freight, import duties and tariffs, direct labor \(including employee compensation benefits\) and indirect plant costs such as plant supervision, receiving, inspection, maintenance labor and materials, depreciation, taxes and insurance, purchasing, production planning, operations management, logistics, freight to customers, warehousing costs, internal transfer freight costs and plant impairment charges\."))
w(sent(F[25],4832,r"The Company accounts for shipping and handling costs as fulfillment activities which are therefore recognized upon shipment of the goods\."))
w(sent(F[21],5163,r"Cost of sales include costs related to the manufacture of the Company’s products, including raw material, inbound freight, direct labor"))
w("""The cost-of-sales sentence including "freight to customers, warehousing costs" appears in the FY2022 (line 4907), FY2023 (4717), FY2024 (4761) and FY2025 (4838) 10-Ks; the FY2021 wording (line 5163) reads "manufacture of" rather than "manufacture and distribution of" and does not list "import duties and tariffs", but it also lists "freight to customers, warehousing costs". The 10-Q does not restate the policy (regex "freight to customers|Cost of sales include|shipping and handling": 0 hits in CHD_10Q_2026-06-30.txt; its only "shipping" hit is the Middle East shipping-routes sentence at line 7473).
""")

# ---------------- 6. competition
w("\n### 6. Competition and customer language\n")
w("""**(a) Colgate and Hill's.** Newest annual filing: CHD_10K_FY2025_2025-12-31.txt. Case-insensitive "Colgate": 3 hits (lines 327, 428, 620). Case-insensitive "Hill": 0 hits (so 0 Hill's pet-brand hits and 0 unrelated hits). "Colgate" hit counts across all CHD annual filings on disk: FY2021 3, FY2022 3, FY2023 3, FY2024 3, FY2025 3 (total 15); "Hill" 0 in every CHD file including the 10-Q; "Colgate" 0 in the 10-Q. Sentences naming Colgate-Palmolive in the FY2025 10-K:
""")
w(sent(F[25],327,r"Our competitors in the Consumer Domestic and Consumer International segments include, among others, Procter & Gamble Company \(“P&G”\), The Clorox Company, Colgate-Palmolive Company, .*?and Peach & Lily\."))
w(sent(F[25],327,r"Many of these companies have greater financial resources than we do and have the capacity to outspend us in their attempts to gain market share\."))
w(sent(F[25],428,r"Many of our competitors are large companies, including, among others, P&G, The Clorox Company, Colgate-Palmolive Company, .*?and Peach & Lily\."))
w(sent(F[25],428,r"Many of these companies have greater financial resources than we do, and these competitors, as well as new market entrants, may therefore, have the capacity to outspend us on advertising and promotional activities"))
w("The third hit is the peer index used for the stock performance graph, not a competitor statement:\n")
w(sent(F[25],620,r"\(1\) S&P 500 Household Products Index consists of the Church & Dwight Co\., Inc\., Clorox Company, Colgate-Palmolive Company, Kimberly-Clark Corporation and Procter & Gamble Company\."))
w("""
**(b) Private label, store brands, value brands** (FY2025 10-K; regex "private label|store brand|retailer.brand|retail-brand|own label|value.brand": 15 hits; the substantive sentences are quoted):
""")
w(sent(F[25],327,r"In addition, the growing number of sales channels and business models, such as niche brands, internet-only brands and retailer co-developed and owned brands, have increased competition in certain product categories, particularly within personal care, and specialty hair and skin care, from less well capitalized competitors\."))
w(sent(F[25],427,r"Most of our products compete with other widely-advertised promoted and merchandised brands within each product category and from retailers, .*?consumers are increasingly seeking lower cost “private label” products\."))
w(sent(F[25],427,r"In addition, an increase in consumers purchasing more “private label” or other lower price brands has increased competition in certain product categories in particular, including diagnostic kits and oral analgesics, and there has been increased consumer shifts to private label products across multiple categories\."))
w(sent(F[25],431,r"In 2025, some of our largest customers launched private label brands that compete with our products and may continue to expand those offerings in the future\."))
w(sent(F[25],449,r"In addition, private label and retail-branded products sold by retail trade chains are typically sold at lower prices than branded products\. .*?\(primarily in the stain fighters, diagnostic kits and oral analgesics categories\)\."))
w(sent(F[25],913,r"Some retail customers have responded to economic conditions by increasing their private label offerings \(primarily in the stain fighters, diagnostic kits and oral analgesics categories\), launching their own brands, and consolidating the product selections they offer to the top few leading brands in each category\."))
w(sent(F[25],444,r"We believe that inflation drove a decline in consumer spending for our Waterpik brand, as a growing number of water flosser consumers switched to competitors' value-branded products\."))
w(sent(F[25],919,r"Our global product portfolio consists of both premium \(66% of total worldwide consumer revenue in 2025\) and value \(34% of total worldwide consumer revenue in 2025\) brands, which we believe enables us to succeed in a range of economic environments\."))

w("\n**(c) Customer concentration (Walmart), each 10-K:**\n")
w(sent(F[21],376,r"In each of the years ended December 31, 2021, 2020 and 2019, net sales to our largest customer, Walmart Inc\. and its affiliates \( “ Walmart ” \), were 24%, 23% and 24% respectively, of our consolidated net sales\."))
w(sent(F[21],469,r"Our top three customers accounted for approximately 37% of net sales in 2021 and 36% of net sales each year in 2020 and 2019\."))
w(sent(F[22],382,r"In the years ended December 31, 2022, 2021 and 2020, net sales to our largest customer, Walmart Inc\. and its affiliates \(“Walmart”\), were 24%, 24% and 23% respectively, of our consolidated net sales\."))
w(sent(F[22],462,r"Our top four customers accounted for approximately 42% of net sales in 2022 and our top three customers accounted for approximately 37% and 36% of net sales in 2021 and 2020, respectively\."))
w(sent(F[23],353,r"In the years ended December 31, 2023, 2022 and 2021, net sales to our largest customer, Walmart Inc\. and its affiliates \(“Walmart”\), were 23%, 24% and 24% respectively, of our consolidated net sales\."))
w(sent(F[24],341,r"In the years ended December 31, 2024, 2023 and 2022, net sales to our largest customer, Walmart Inc\. and its affiliates \(“Walmart”\), were 23%, 23% and 24% respectively, of our consolidated net sales\."))
w(sent(F[25],345,r"In each of the years ended December 31, 2025, 2024 and 2023, net sales to our largest customer, Walmart Inc\. and its affiliates \(“Walmart”\), were approximately 23% of our consolidated net sales\."))
w(sent(F[25],439,r"Our top four customers accounted for approximately 44%, 43%, and 44% of net sales in 2025, 2024, and 2023, respectively\."))
w("""
| year | Walmart % of consolidated net sales | top customers | source |
|---|---|---|---|
| FY2021 | 24% | top three 37% | CHD_10K_FY2021 376, 469 |
| FY2022 | 24% | top four 42% | CHD_10K_FY2022 382, 462 |
| FY2023 | 23% | top four 44% | CHD_10K_FY2023 353; CHD_10K_FY2025 439 |
| FY2024 | 23% | top four 43% | CHD_10K_FY2024 341; CHD_10K_FY2025 439 |
| FY2025 | approximately 23% | top four 44% | CHD_10K_FY2025 345, 439 |
| H1 2026 | not disclosed in CHD_10Q_2026-06-30.txt (search "walmart": 0 hits) | nd | |
""")
w("\n**(d) Pricing, elasticity, trade-down, promotion and price investment language.** FY2025 10-K MD&A:\n")
w(sent(F[25],874,r"potentially increasing prices, adjusting inventories, lobbying and seeking exemptions with respect to tariffs\."))
w(sent(F[25],874,r"We believe our existing tariff cost exposure will be mitigated through the above-mentioned actions, future additional supply chain efforts and surgical pricing\."))
w(sent(F[25],921,r"Historically, we have been able to mitigate the effects of cost increases including tariffs primarily by implementing cost reduction programs and, to a lesser extent, by passing along cost increases to customers\."))
w(sent(F[25],919,r"We continue to evaluate and vigorously address pressures on this business through, among other things, new product introductions and increased marketing and trade spending\."))
w(sent(F[25],923,r"Our focus is to maintain competitive marketing and trade spending, manage our cost structure, continue to develop and launch new and differentiated products, while pursuing strategic acquisitions\."))
w(sent(F[25],1617,r"Excluding these non-cash charges, Consumer Domestic income from operations decreased by \$15\.4 driven by higher manufacturing and distribution expenses of \$130\.3, and unfavorable price/mix of \$24\.8, partially offset by the benefit of productivity programs of \$89\.1, higher sales volumes of \$39\.5, lower marketing expenses of \$5\.8, and lower SG&A expenses of \$5\.3\."))
w(sent(F[25],1674,r"Excluding the non-cash impairment charges, Consumer International income from operations increased \$7\.2 and was driven by higher sales volumes of \$19\.1, favorable price/mix of \$17\.0, and lower manufacturing and commodity costs of \$6\.3, partially offset by higher SG&A expenses of \$16\.8, higher marketing expenses of \$15\.6, and unfavorable foreign exchange rates of \$2\.8\."))
w(sent(F[25],942,r"Our global WATERPIK business is experiencing customer distribution losses and a decline in consumer demand, mainly due to lower consumer spending and more customers choosing value brands amid inflation\."))
w("Item 1 and Item 1A (FY2025 10-K):\n")
w(sent(F[25],325,r"Consumer products, particularly laundry, are subject to significant price competition\. As a result, we, from time to time, may need to reduce the prices for some of our products to respond to competitive and customer pressures and to maintain market share\."))
w(sent(F[25],325,r"Product introductions typically involve heavy marketing and trade spending in the year of launch"))
w(sent(F[25],326,r"Because of the competitive retail environment, we face pricing pressure from our retail customers and customers selling through other channels, particularly high-volume retail customers including, internet-based retailers, who have increasingly sought to obtain pricing concessions or better trade terms that could reduce our margins\."))
w(sent(F[25],429,r"Increases to our prices, because of inflationary pressures or otherwise, could cause declining sales of products whose prices we have increased\. In response to inflationary pressures and other factors, we have raised prices on many of our products across our global portfolio of brands in recent years\."))
w(sent(F[25],442,r"We have implemented price increases and may implement additional price increases in the future, including to account for increased costs, which may slow sales growth or create volume declines in the short term as customers and consumers adjust to these price increases\."))
w(sent(F[25],427,r"The use of evolving technology to develop more complex pricing models by retailers has led and may continue to lead to pricing pressures in some categories\."))
w("\nInterim (CHD_10Q_2026-06-30.txt):\n")
w(sent(Q,7471,r"including exiting certain business lines, shifting production and relocating manufacturing operations, finding alternative sources of supply, selectively increasing prices, adjusting inventories, seeking exemptions with respect to tariffs"))
w(sent(Q,7471,r"We believe our existing tariff cost exposure will be mitigated through the above-mentioned actions, future additional supply chain efforts and surgical pricing \."))
w(sent(Q,7962,r"\(2\) For the three and six months ended June 30, 2026, price/mix was favorable in all three segments\."))
w(sent(Q,8541,r"Consumer Domestic also realized the benefit of productivity programs of \$19\.5 and favorable price/mix of \$14\.5\."))
w(sent(Q,8661,r"Consumer International also experienced favorable price/mix of \$8\.9 and favorable foreign exchange rates of \$1\.9\."))
w(sent(Q,4718,r"The Company’s global WATERPIK business is experiencing customer distribution losses and a decline in consumer demand, mainly due to lower consumer spending and more customers choosing value brands amid inflation\."))
w("""
Searches with no hits in the FY2025 10-K or the 10-Q: regex "elastic|trade.down|rollback|price investment|price give" (0 hits in each file).
""")

# ---------------- summary
w("\n### Summary row\n")
w("""
| FY window used | organic volume by year | price by year | GAAP operating margin by year | advertising % of sales by year | gross margin by year |
|---|---|---|---|---|---|
| FY2021 to FY2025 (Dec year end) plus H1 2026 (10-Q) | [organic nd; "Product volumes sold", consolidated] FY21 +1.0 / FY22 -5.1 / FY23 +0.9 / FY24 +3.3 / FY25 +0.8 / H1-26 +4.8; [same, Consumer Domestic] FY21 -0.3 / FY22 -5.9 / FY23 +1.0 / FY24 +2.8 / FY25 0.0 / H1-26 +4.6 | ["Pricing/Product mix", consolidated] FY21 +3.3 / FY22 +6.5 / FY23 +4.4 / FY24 +1.3 / FY25 -0.1 / H1-26 +0.6; [same, Consumer Domestic] FY21 +3.9 / FY22 +6.8 / FY23 +4.7 / FY24 +0.7 / FY25 -0.5 / H1-26 +0.7 | ["Income from Operations" / Net Sales] FY21 20.8 / FY22 11.1 / FY23 18.0 / FY24 13.2 / FY25 17.4 / H1-26 18.9 | [advertising alone nd; "Marketing expenses", which includes advertising] FY21 11.1 / FY22 10.0 / FY23 10.9 / FY24 11.4 / FY25 11.4 / H1-26 10.2 | [Gross Profit / Net Sales; freight to customers in cost of sales] FY21 43.6 / FY22 41.9 / FY23 44.1 / FY24 45.7 / FY25 44.7 / H1-26 45.9 |
""")

# ---------------- gaps
w("\n### Gaps, extraction problems and definition differences\n")
w("""
- **Organic sales growth: not disclosed in any CHD document on disk.** Search "organic" (case-insensitive): 2 unrelated hits per 10-K (quoted in section 1) and 4 hits in the 10-Q, which use "organic growth", "organic sales growth" and "organic sales volumes" without a definition or a number. No CHD definition of organic growth can therefore be quoted from these documents; the comparison with Colgate can only be made on the filed components. (An organic measure, if CHD publishes one, would be in earnings releases, which are not on disk; nothing was fetched.)
- **Advertising expense alone: not disclosed** (search terms "advertis", "advertising costs", "advertising expense", "brand support", "media", "A&P"). Only "Marketing expenses" is filed; it includes advertising plus coupon insertion, consumer promotion, public relations, package design and market research, and excludes cooperative advertising (netted against sales).
- **Walmart % in the 10-Q: not disclosed** (search "walmart": 0 hits).
- **Definition differences versus Colgate** (Colgate: organic = net sales growth excluding foreign exchange, acquisitions and divestments; components "volume" and "net selling price"):
  - CHD combines price and mix in one component, "Pricing/Product mix"; there is no separate price row and no separate mix row. Colgate separates volume and net selling price.
  - CHD's "Product volumes sold" excludes acquired volume, which has its own row ("Volume from acquired product lines (net of divestiture)" in the FY2021 consolidated table; "Acquired product lines" FY2021 to FY2024; "Acquisitions" in FY2025 and 2026), and from FY2024 excludes exited lines, which also have their own row ("Exit of product lines").
  - Foreign exchange: the FY2021 and FY2022 consolidated tables combine "Foreign exchange rate fluctuations / Other" in one row; the FY2023, FY2024 and FY2025 consolidated tables have no foreign exchange row, although segment tables do (reconciliation note in section 1).
  - No hyperinflation or price-growth exclusion is described: regex "hyperinflat|argentin" returned 0 hits in all six CHD files.
  - Fiscal year: calendar year ending December 31, the same as Colgate. Regex "53.week|52.week" returned 0 hits in all six CHD files.
  - Segment basis: Consumer Domestic (U.S. consumer), Consumer International, and SPD (specialty products); not product-category segments.
- **Shipping and handling placement:** CHD puts "freight to customers, warehousing costs" in cost of sales (section 4). Colgate reports shipping and handling in SG&A, so CHD's gross margin is not comparable to Colgate's gross margin without adjustment. No CHD shipping or freight dollar amount is disclosed (search "shipping", "handling", "freight", "distribution cost", "transportation": policy and narrative hits only, no amount).
- **Segment margin comparability:** production planning and logistics administrative costs are in consolidated cost of sales but in segment SG&A (quotes in section 2). Segment Income from Operations includes the FY2022 and FY2024 impairment charges and FY2025 exit costs.
- **Presentation changes:** from the FY2024 10-K, R&D is a separate segment expense row and impairments are separate income-statement lines; earlier 10-Ks include these in SG&A. The FY2024 10-K re-presents FY2022 SG&A (706.0 plus 411.0 impairments) versus the FY2022 10-K (1,117.0); Income from Operations is unchanged. The FY2025 10-K relabels the "Corporate" column "Consolidating Reclassification".
- **Extraction artefacts (flagged, not fixed):** every table cell is on its own line (quotes are whitespace-joined rows); negatives are split across cells as "(5.1 | %)", and in the 10-Q as "(0.5 | )%"; segment-note negatives appear as "( 47.1 | )"; "CONSOL IDATED STATEMENTS OF INCOME" in the FY2022 to FY2025 10-Ks; "a dministrative" in CHD_10K_FY2025 line 10489; "20 2 1 were $ 606.7 , a n increase" in CHD_10K_FY2021 line 1468; "approximat ely" and "approximatel y" in the 10-Q (lines 6171 and 4506); stray spaces before punctuation in several sentences (for example "surgical pricing ." at 10-Q line 7471 and "segment ." at FY2021 line 1461), reproduced as they appear; in the 10-Q the six-months-2025 segment "Income from Operations" row ends with "| | 21" (line 7128), which appears to be a page number glued onto the table row by the extraction, not a figure.
- **Interim period:** only the quarter and six months to June 30, 2026 are available. They include the effects of the 2025 business exits and the VMS divestiture ("Exit of product lines" -7.6% consolidated for the six months).
""")
open("SECTION_CHD.md","w",encoding="utf-8").write("".join(out))
print("written", sum(len(x) for x in out))
