# builds Part B and the limits list, then assembles WALLBOARD_AGG_ROW.md
import statistics as S
out=[]; w=out.append
def tbl(rows, hdr):
    w("| FY | " + " | ".join(hdr) + " | Source (form, FY, filed, accession) |")
    w("|---|" + "---|"*len(hdr) + "---|")
    for r in rows: w("| " + " | ".join(str(x) for x in r) + " |")
def pct(p,r): return f"{100*p/r:.1f}%"
w("## PART B. AGGREGATES AND READYMIX\n")
w("All margins are COMPUTED (profit / revenue). The profit measure is the company's segment or product-line **gross profit** in every case below (none of the three reports an operating profit by product line). Revenue bases differ between companies and within MLM; see the notes under each table.\n")

# ---------------- VMC
w("### B1. Vulcan Materials (CIK 1396009)\n")
V={2019:('0001396009-20-000006','2020-02-26',3990.3,1146.6,395.6,43.2,855.8,63.0),
   2020:('0001396009-21-000009','2021-02-25',3944.3,1159.2,383.6,44.2,792.6,75.2),
   2021:('0001396009-22-000010','2022-02-25',4345.0,1295.7,766.8,54.3,777.8,21.2),
   2022:('0001396009-23-000007','2023-02-24',5272.8,1408.5,1593.9,89.3,990.2,57.3),
   2023:('0001396009-24-000006','2024-02-22',5909.9,1733.6,1249.3,62.1,1140.7,149.6),
   2024:('0001396009-25-000005','2025-02-20',5949.6,1816.7,653.5,12.8,1245.6,170.1),
   2025:('0001628280-26-009546','2026-02-19',6297.2,1964.8,846.6,35.9,1294.4,173.9)}
rows=[]
for y,(acc,fd,ar,ag,cr,cg,sr,sg) in V.items():
    rows.append((y,f"{ar:,.1f}",f"{ag:,.1f}",pct(ag,ar),f"{cr:,.1f}",f"{cg:,.1f}",pct(cg,cr),f"{sr:,.1f}",f"{sg:,.1f}",pct(sg,sr),f"10-K FY{y}, filed {fd}, {acc}"))
tbl(rows,["Aggregates segment revenue ($M)","Aggregates gross profit ($M)","Agg. margin","Concrete (readymix) revenue","Concrete gross profit","Concrete margin","Asphalt revenue","Asphalt gross profit","Asphalt margin"])
am=[v[3]/v[2] for v in V.values()]; cm=[v[5]/v[4] for v in V.values()]
w("")
w(f"COMPUTED means 2019-2025: aggregates gross margin **{100*S.mean(am):.1f}%** (2019-2021 {100*S.mean(am[:3]):.1f}%; 2023-2025 {100*S.mean(am[4:]):.1f}%); concrete {100*S.mean(cm):.1f}%.\n")
w("Notes: figures are from the \"Segment Financial Disclosure\" note in each year's own 10-K (FY2019 filed in thousands, converted to millions here by moving the decimal only). Aggregates segment revenue is before elimination of aggregates intersegment sales and \"Includes product sales, as well as freight & delivery costs that we pass along to our customers, and service revenues\" (FY2025 footnote 1). Calcium was a separate segment through FY2023 and is inside Aggregates from the FY2024 10-K (FY2024 restates 2023 aggregates to $5,918.9 / $1,736.8 and 2022 to $5,280.6 / $1,411.1). Concrete jumps in 2021-2022 on the U.S. Concrete acquisition (August 2021) and falls on the 2022 NJ/NY/PA and 2023 Texas concrete divestitures (FY2024 10-K footnote 3).\n")

# ---------------- MLM
w("### B2. Martin Marietta Materials (CIK 916076)\n")
M={2019:('0001564590-20-005784','2020-02-21',2756.7,807.9,'948.1','78.8',948.1,78.8,'products and services, excl. freight'),
   2020:('0001564590-21-006959','2021-02-19',2769.3,848.5,'952.1','79.6',952.1,79.6,'products and services, excl. freight'),
   2021:('0001564590-22-005965','2022-02-22',3058.5,904.8,'1,145.8','95.6',1145.8,95.6,'products and services, excl. freight'),
   2022:('0000950170-23-004361','2023-02-24',3506.0,980.3,'951.3','69.6',951.3,69.6,'products and services, excl. freight'),
   2023:('0000950170-24-019275','2024-02-23',4301.6,1378.1,'1,009.3','102.0',1009.3,102.0,'total revenues, incl. freight'),
   2024:('0000950170-25-024770','2025-02-21',4514,1449,'n/a separately (cement + RMC combined: 1,083)','n/a (combined: 260)',None,None,'total revenues, incl. freight'),
   2025:('0001193125-26-059193','2026-02-19',5004,1677,'n/a (\"other building materials\" = cement/RMC + asphalt/paving: 992)','n/a (combined: 98)',None,None,'total revenues, incl. freight; continuing ops')}
rows=[]
for y,(acc,fd,ar,ag,rr,rg,rrv,rgv,basis) in M.items():
    rows.append((y,f"{ar:,.1f}",f"{ag:,.1f}",pct(ag,ar),basis,rr,rg,pct(rgv,rrv) if rrv else 'n/a',f"10-K FY{y}, filed {fd}, {acc}"))
tbl(rows,["Aggregates product-line revenue ($M)","Aggregates gross profit ($M)","Agg. margin","Revenue basis","Ready mixed concrete revenue","RMC gross profit","RMC margin"])
am=[v[3]/v[2] for v in M.values()]
rm=[v[7]/v[6] for v in M.values() if v[6]]
w("")
w(f"COMPUTED means: aggregates gross margin 2019-2025 as filed **{100*S.mean(am):.1f}%** (mixes the two revenue bases); 2019-2022 excl.-freight basis {100*S.mean(am[:4]):.1f}%; 2023-2025 incl.-freight basis {100*S.mean(am[4:]):.1f}%. On the FY2023 10-K's restated incl.-freight basis, 2021 is $3,344.3 / $907.6 ({pct(907.6,3344.3)}) and 2022 is $3,879.0 / $983.8 ({pct(983.8,3879.0)}); mean 2021-2025 on that one basis: {100*S.mean([907.6/3344.3,983.8/3879.0]+am[4:]):.1f}%. Ready mixed concrete 2019-2023 mean {100*S.mean(rm):.1f}%.\n")
w("Notes: source is Note Q (FY2019-FY2022) or Note P (FY2023-FY2025), \"Revenues and Gross Profit\", in each year's own 10-K. MLM reports no aggregates *segment*: its reportable segments are geographic (East Group, West Group) plus Magnesia Specialties/Specialties; aggregates is a product line of the Building Materials business. Aggregates revenue is before \"interproduct revenues\". The FY2024 10-K combined cement with ready mixed concrete; the FY2025 10-K combined those with asphalt and paving as \"other building materials\" and moved the Midlothian cement plant and Texas ready mixed plants to discontinued operations. The FY2025 note gives the pre-combination 2024 split: \"the cement and ready mixed concrete product line reported revenues of $1.1 billion and gross profit of $260 million\"; readymix alone is not separable from 2024.\n")

# ---------------- KNF
w("### B3. Knife River (CIK 1955520)\n")
w("Spun off from MDU Resources on 2023-05-31. Its first 10-K is FY2023. Product-line revenue and gross profit are disclosed in the MD&A (the reportable segments are geographic and measured on EBITDA).\n")
K=[(2020,406.6,None,15.4,547.0,None,13.6,'30,949','13.14','4,087','133.86','Form 10-12B/A (Amendment 3), Exhibit 99.1 information statement, filed 2023-05-08, 0001140361-23-023310; gross profit $ not shown there, only revenue and margin %'),
   (2021,444.0,60.5,None,584.4,81.5,None,'33,518','13.25','4,267','136.94','10-K FY2023, filed 2024-02-27, 0001955520-24-000007 (prior-year column)'),
   (2022,496.6,69.5,None,609.5,85.9,None,'33,994','14.61','4,015','151.80','10-K FY2023, filed 2024-02-27, 0001955520-24-000007 (prior-year column)'),
   (2023,547.9,109.7,None,653.9,101.2,None,'33,637','16.29','3,837','170.42','10-K FY2023, filed 2024-02-27, 0001955520-24-000007'),
   (2024,556.1,114.3,None,655.5,106.0,None,'31,832','17.47','3,484','188.11','10-K FY2024, filed 2025-02-21, 0001955520-25-000010'),
   (2025,617.1,114.1,None,779.4,133.6,None,'32,494','18.99','3,913','199.17','10-K FY2025, filed 2026-02-20, 0001955520-26-000003')]
rows=[]; am=[]; rm=[]
for y,ar,ag,agm,rr,rg,rgm,t,p,cy,pc,src in K:
    if ag is None:
        a=agm/100; agtxt=f"~{ar*a:.1f} (COMPUTED from filed {agm}%)"; amt=f"{agm}% (filed)"
    else:
        a=ag/ar; agtxt=f"{ag:,.1f}"; amt=pct(ag,ar)
    if rg is None:
        r_=rgm/100; rgtxt=f"~{rr*r_:.1f} (COMPUTED from filed {rgm}%)"; rmt=f"{rgm}% (filed)"
    else:
        r_=rg/rr; rgtxt=f"{rg:,.1f}"; rmt=pct(rg,rr)
    am.append(a); rm.append(r_)
    rows.append((y,f"{ar:,.1f}",agtxt,amt,f"{rr:,.1f}",rgtxt,rmt,t,p,cy,pc,src))
tbl(rows,["Aggregates revenue ($M)","Aggregates gross profit ($M)","Agg. margin","Ready-mix revenue ($M)","Ready-mix gross profit ($M)","Ready-mix margin","Agg. tons (000)","Agg. avg price $/ton","RMC cu yd (000)","RMC avg price $/cu yd"])
w("")
w(f"COMPUTED means 2020-2025: aggregates gross margin **{100*S.mean(am):.1f}%** (2021-2025 {100*S.mean(am[1:]):.1f}%); ready-mix {100*S.mean(rm):.1f}%.\n")
w("Notes: product-line revenues are before the \"Internal sales\" elimination; the average selling price \"includes freight and delivery and other revenues\" (filed footnote). 2019: no Knife River registrant existed. The parent MDU Resources (CIK 67716) 10-K FY2020 (filed 2021-02-19, 0000067716-21-000007) gives only the whole construction materials and contracting segment for 2019: operating revenues $2,190.7M, gross margin $274.0M (COMPUTED 12.5%), aggregates 32,314 thousand tons. No product-line gross profit for 2019 is filed; not invented here.\n")

# ---------------- limits
w("## LIMITS (plain list)\n")
L=[
"USG: the profit figure is never wallboard alone. FY2007-FY2016 it is the whole U.S. gypsum unit (wallboard plus joint compound, cement board, Fiberock, Securock, plaster); FY2017-FY2018 it is the narrower U.S. Wallboard and Surfaces segment. The 10-year mean margin spans a scope change and several restatements (2013, 2014, 2015, 2016, 2017 were each later restated; the table uses the as-first-reported figure of each year's own 10-K).",
"USG disclosed a dollar price per MSF only through FY2013. FY2014-FY2018 prices are percentage changes; the dollar chain in A1 is COMPUTED from rounded percentages and is not a filed number. USG expressly withholds U.S. Wallboard gross margin.",
"USG's own capacity utilization is not stated in FY2017-FY2018. Industry utilization is USG's estimate (FY2017-18: annualized shipments over capacity); 2007 industry utilization was not found in the FY2009 10-K.",
"CBPX has no FY2019 10-K (acquired 2020-02-03; Form 15 filed 2020-02-13). Only 9M 2019 from the Q3 10-Q is shown, and it is not a fiscal year. 2012 and 2013 are Lafarge-division predecessor figures; 2013 is a sum of two stub periods done here, not a filed full-year GAAP figure (a pro forma operating income of $29.8M is also filed). 2015 operating income carries a $29.9M LTIP charge funded by Lone Star.",
"CBPX mill net price is net of freight; USG's realized price is not stated as net of freight; Temple-Inland's revenue per MSF includes freight. The three price series may not be on one basis.",
"No other current SEC filer makes U.S. wallboard besides Eagle. PABCO is not an SEC registrant; National Gypsum has no 10-K in the period; Georgia-Pacific and Lafarge North America stopped filing in 2005-2006 (not fetched); Temple-Inland gives wallboard revenue and volume through FY2010 but no wallboard profit.",
"Knauf (USG's owner since 2019) and Saint-Gobain (CertainTeed, CBPX since 2020) file no U.S. 10-K; no U.S. wallboard figures exist in the SEC record after FY2018 (USG) and Q3 2019 (CBPX).",
"Aggregates: the profit measure is gross profit for all three companies; none reports operating profit by product line, so these margins are not comparable to USG/CBPX operating margins without that adjustment.",
"MLM's aggregates revenue basis changes in the FY2023 10-K (excl. freight through FY2022, incl. freight from FY2023); both bases are shown. MLM readymix cannot be separated after 2023.",
"VMC's aggregates segment absorbed Calcium from FY2024; concrete revenue moves with the 2021 U.S. Concrete acquisition and the 2022-2023 divestitures.",
"Knife River: 2020 gross profit dollars are COMPUTED from the filed margin percentage; 2019 product-line figures do not exist in any filing located (MDU gives only the whole segment).",
"VMC and MLM aggregates volumes and per-ton prices were not extracted in this pass (not requested; the per-ton figures are stated in each MD&A).",
"Text extraction flattens tables to one cell per line or ' | ' joins; every table figure above was read against its row label and column-year header in the saved text files in this folder.",
]
for x in L: w("- " + x)
w("")
w("## FILES IN THIS FOLDER\n")
w("Saved filing texts: USG_10K_FY2009..FY2018.txt, CBPX_10K_FY2013..FY2018.txt, CBPX_10Q_2019Q3.txt, TIN_10K_FY2010.txt, VMC_10K_FY2019..FY2025.txt, MLM_10K_FY2019..FY2025.txt, KNF_10K_FY2023..FY2025.txt, KNF_Form10A_ex99-1_2023-05-08.txt, MDU_10K_FY2020.txt; submissions JSONs sub_*.json; builders build_md.py (Part A) and build_partB.py (Part B and assembly).\n")
partB='\n'.join(out)
A=open('_partA.md',encoding='utf-8').read(); Qa=open('_quotesA.md',encoding='utf-8').read()
open('WALLBOARD_AGG_ROW.md','w',encoding='utf-8').write(A+'\n'+Qa+'\n'+partB)
print('ok')
