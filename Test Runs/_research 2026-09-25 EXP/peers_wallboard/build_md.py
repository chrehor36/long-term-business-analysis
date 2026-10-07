# builds Part A of WALLBOARD_AGG_ROW.md; quotes pulled by line number from the saved filing texts (verbatim, no edits)
import statistics as S
def L(f,n): return open(f,encoding='utf-8').read().split('\n')[n-1].strip()
def Q(f,ns,label):
    return "> " + " / ".join(L(f,n) for n in ns) + "\n\n*" + label + "; saved text `" + f + "` line(s) " + ", ".join(map(str,ns)) + "*\n"
A={'USG09':'0000950123-10-011978','USG10':'0000950123-11-012693','USG11':'0001193125-12-059658','USG12':'0000757011-13-000023','USG13':'0000757011-14-000047','USG14':'0000757011-15-000041','USG15':'0000757011-16-000148','USG16':'0000757011-17-000010','USG17':'0000757011-18-000014','USG18':'0000757011-19-000016',
 'CB13':'0001193125-14-118572','CB14':'0001193125-15-062550','CB15':'0001193125-16-473633','CB16':'0001592480-17-000006','CB17':'0001628280-18-002132','CB18':'0001592480-19-000005','CBQ':'0001592480-19-000033','TIN10':'0000731939-11-000015'}
out=[]
w=out.append
w("# Wallboard and aggregates competitor row: EXP peers (research file, 2026-09-25)\n")
w("Fetch-and-compute only. No conclusion on moats is drawn here. Every figure carries its form, fiscal year, filing date and accession. Margins are computed here (profit / revenue) and are labelled COMPUTED; they are not filed figures. Dollar figures in millions unless marked.\n")
w("## PART A. GYPSUM WALLBOARD\n")
w("### A1. USG Corporation (CIK 757011), U.S. gypsum business\n")
w("**Scope of the profit figure changes over the series; read before averaging:**\n")
w("- FY2007-FY2013: the line is **United States Gypsum Company (\"U.S. Gypsum\")**, a reporting unit inside the North American Gypsum segment. U.S. only; excludes CGC (Canada), USG Mexico, ceilings (USG Interiors) and L&W Supply distribution. Includes all U.S. gypsum products (SHEETROCK wallboard, joint compound, DUROCK cement board, FIBEROCK, SECUROCK, plaster), not wallboard alone. FY2013 cross-check: wallboard sales implied by 5.14 bsf x $154.04 = $792M; the filing says non-wallboard sales were $966M of $1,758M, leaving $792M. Agreement.")
w("- FY2014-FY2016: the line is **\"United States\"** within the reportable Gypsum segment; same U.S.-only scope. The FY2016 10-K restated earlier years for the L&W discontinued-operation presentation (2015: $2,041 / $329; 2014: $1,913 / $188), and the FY2014 10-K restated 2013 to $1,765 / $214.")
w("- FY2017-FY2018: new reportable segment **U.S. Wallboard and Surfaces** (wallboard, joint compound, plaster, glass-mat panels). Narrower: it excludes U.S. Performance Materials (Fiberock, Durock, Levelrock, Securock roof board), reported separately. The FY2018 10-K restated for ASU 2017-07 (2017 op. profit $306M; 2016 $328M on $1,778M). The FY2017 10-K on the new basis: 2015 $1,720 / $298; 2016 $1,778 / $334.")
w("- Operating profit is USG's segment or unit operating profit (after unit S&A, before corporate costs and interest). It includes restructuring, impairment and litigation charges (for example 2014 includes a $48M wallboard price-fixing class action settlement and $30M impairments).\n")
w("| FY | Net sales | Op. profit | Margin (COMPUTED) | SHEETROCK wallboard shipped (bsf) | Avg realized wallboard price $/MSF | Industry capacity utilization (USG est.) | USG own wallboard utilization | Source (form, FY, filed, accession) |")
w("|---|---|---|---|---|---|---|---|---|")
rows=[
(2007,2417,30,'9.0','134.93','n/s in file','n/s','10-K FY2009, filed 2010-02-12, '+A['USG09']+' (prior-year column)'),
(2008,1933,-261,'7.16','111.15','~62%','65%','10-K FY2009, filed 2010-02-12, '+A['USG09']+' (prior-year column)'),
(2009,1432,-20,'4.72','117.16','~52%','47%','10-K FY2009, filed 2010-02-12, '+A['USG09']),
(2010,1295,-160,'4.19','111.66','~51%','43%','10-K FY2010, filed 2011-02-11, '+A['USG10']),
(2011,1297,-78,'4.11','111.27','~53%','43%','10-K FY2011, filed 2012-02-14, '+A['USG11']),
(2012,1512,89,'4.72','131.70','~58%','51%','10-K FY2012, filed 2013-02-15, '+A['USG12']),
(2013,1758,216,'5.14','154.04','~64%','55%','10-K FY2013, filed 2014-03-03, '+A['USG13']),
(2014,1920,192,'5.33','not disclosed; filed change +8%','~66%','56%','10-K FY2014, filed 2015-02-12, '+A['USG14']),
(2015,2012,316,'5.44','not disclosed; filed change +2%','~68%','57%','10-K FY2015, filed 2016-02-10, '+A['USG15']),
(2016,2135,375,'5.76','not disclosed; filed change -1%','~75%','61%','10-K FY2016, filed 2017-02-08, '+A['USG16']),
(2017,1916,314,'6.12','not disclosed; price effect -$7M, shown as a dash in the % column','76%','n/s','10-K FY2017, filed 2018-02-14, '+A['USG17']+' (U.S. Wallboard and Surfaces)'),
(2018,1927,248,'5.81','not disclosed; filed change +3%','74%','n/s','10-K FY2018, filed 2019-02-14, '+A['USG18']+' (U.S. Wallboard and Surfaces)'),
]
for y,s,o,v,p,iu,uu,src in rows:
    w(f"| {y} | {s:,} | {o:,} | {100*o/s:.1f}% | {v} | {p} | {iu} | {uu} | {src} |")
m={y:o/s for y,s,o,*_ in rows}
w("")
w(f"COMPUTED means of annual margins: FY2009-FY2018 (10 yrs, requested window) **{100*S.mean(m[y] for y in range(2009,2019)):.1f}%**; FY2007-FY2018 {100*S.mean(m.values()):.1f}%; FY2012-FY2018 {100*S.mean(m[y] for y in range(2012,2019)):.1f}%. Aggregate (sum of profit / sum of sales) FY2009-FY2018: {100*sum(o for y,s,o,*_ in rows if y>=2009)/sum(s for y,s,o,*_ in rows if y>=2009):.1f}%. The series mixes three scopes (see above); the FY2017-18 rows are on the narrower U.S. Wallboard and Surfaces basis.\n")
w("Price per MSF: USG stated a dollar figure per MSF through FY2013 only. From FY2014 it gives only percentage changes. A COMPUTED chain from the $154.04 FY2013 anchor using the rounded filed percentages (not a filed figure; rounding error up to about 0.5% per link): 2014 ~ $166, 2015 ~ $170, 2016 ~ $168, 2017 ~ $168, 2018 ~ $173. The FY2018 10-K (proxy material in Part III, line 5869) says: \"We do not publicly disclose U.S. Wallboard gross margin or U.S. Surfaces gross margin because that information constitutes confidential commercial and financial information, the disclosure of which would cause us competitive harm.\"\n")
w("Industry capacity and shipments as stated by USG (Gypsum Association data unless noted): capacity ~34.4 bsf (12/31/2009), 32.9 (12/31/2010), 31.9 (1/1/2012), 32.7 (1/1/2013), 32.8 (1/1/2015 and 1/1/2016), 33.4 (1/1/2017), 34.0 (1/1/2018, USG estimate), 34.1 (1/1/2019). Industry shipments of gypsum board: 30.7 bsf 2007, 25.2 2008, 18.4 2009, 17.3 2010, 17.5 2011, 19.3 2012, 20.9 2013, 22.3 2015, 25.0 2016, 25.7 2017, 25.4 2018. USG share of U.S. gypsum board: ~27% 2009, ~24% 2010, ~25% 2011, ~26% 2012-2015, ~25% 2016 (24.6% per the FY2017 10-K), 25.4% 2017, 24.5% 2018.\n")
w("### A2. Continental Building Products (CIK 1592480)\n")
w("Formed 2013-07-26 to buy the Lafarge North America gypsum division (closed 2013-08-30); IPO February 2014; acquired by Saint-Gobain on 2020-02-03 and deregistered (Form 15-12B filed 2020-02-13, accession 0001140361-20-003164). **There is no FY2019 10-K**: the last 10-K is FY2018; the last periodic report is the Q3 2019 10-Q. \"Mill net sales price\" is the company's term, defined as \"average selling price per thousand square feet net of freight and delivery costs.\" USG's realized price is not stated as net of freight, so the two price series may not be on the same basis.\n")
w("| FY | Total net sales ($000) | Operating income ($000) | Margin (COMPUTED) | Wallboard segment sales ($000) | Wallboard segment op. income ($000) | Wallboard seg. margin (COMPUTED) | Wallboard volume (MMSF) | Mill net price $/MSF | Industry utilization (CBPX est.) | Source |")
w("|---|---|---|---|---|---|---|---|---|---|---|")
C=[
('2012 (Predecessor: Lafarge gypsum division carve-out)',311410,-12757,295282,-11814,'1,903','124.02','n/s','10-K FY2014, filed 2015-02-25, '+A['CB14']),
('2013 (Predecessor 1/1-8/30 + Successor 7/26-12/31, summed here)',402314,46405,384914,46861,'2,161 (1,334 + 827)','145.92 (combined; 147.55 pred., 143.28 succ.)','n/s','10-K FY2014, filed 2015-02-25, '+A['CB14']+'; pro forma 2013 operating income is $29,790k'),
('2014',424502,60761,409408,60080,'2,180','154.77','n/s','10-K FY2014, filed 2015-02-25, '+A['CB14']),
('2015',421682,44005,407982,44276,'2,199','153.70','67% (per FY2017 10-K)','10-K FY2015, filed 2016-02-23, '+A['CB15']+'; includes $29,946k LTIP funded by Lone Star (ex-LTIP op. margin COMPUTED 17.5%)'),
('2016',461375,87140,447679,87094,'2,560','143.83','75%','10-K FY2016, filed 2017-02-24, '+A['CB16']),
('2017',489163,89585,474189,90220,'2,666','146.92','76%','10-K FY2017, filed 2018-02-23, '+A['CB17']),
('2018',528060,107314,514374,109266,'2,736','153.83','73%','10-K FY2018, filed 2019-02-22, '+A['CB18']),
]
for y,s,o,ws,wo,v,p,u,src in C:
    w(f"| {y} | {s:,} | {o:,} | {100*o/s:.1f}% | {ws:,} | {wo:,} | {100*wo/ws:.1f}% | {v} | {p} | {u} | {src} |")
w(f"| 9M 2019 (supplementary, not a fiscal year) | 373,677 | 62,455 | {100*62455/373677:.1f}% | n/a | n/a | n/a | 2,032 | 145.13 | n/s | 10-Q Q3 2019, filed 2019-11-12, {A['CBQ']} |")
cm=[o/s for y,s,o,*_ in C]
w("")
w(f"COMPUTED means: total operating margin FY2014-FY2018 (full public-company years) **{100*S.mean(cm[2:]):.1f}%** (17.9% with 2015 ex-LTIP); FY2012-FY2018 incl. predecessor {100*S.mean(cm):.1f}%. Wallboard segment margin FY2014-FY2018 {100*S.mean([wo/ws for y,s,o,ws,wo,*_ in C][2:]):.1f}%. Wallboard is 96.8% to 97.4% of revenue (FY2015-FY2018 per the segment notes). Sales include Canada.\n")
w("Utilization cross-check: CBPX estimated 67% for 2015 against USG's ~68%; CBPX 73% for 2018 against USG's 74%; both 75% (2016) and 76% (2017).\n")
w("### A3. Other SEC-registered U.S. wallboard makers\n")
w("- **Eagle Materials (American Gypsum)**: the subject company; excluded from the peer row.")
w("- **PABCO Gypsum** (division of PABCO Building Products, part of Pacific Coast Building Products): EDGAR company search for \"PABCO\" and \"Pacific Coast Build\" returns no registrant. Not an SEC filer; no figures.")
w("- **National Gypsum**: private; EDGAR shows only 1994-1995 Schedule 13D filings under that name. No 10-K in the period.")
w("- **Georgia-Pacific** (CIK 41077): last 10-K FY2004 (filed 2005-03-01, 0001193125-05-039002), before Koch; outside the window, not fetched.")
w("- **Lafarge North America** (CIK 716783): last 10-K FY2005 (filed 2006-03-01, 0000950133-06-000946); its gypsum division became CBPX. Outside the window, not fetched.")
w("- **CertainTeed / Saint-Gobain, Knauf**: foreign parents, no 10-K.")
w("- **Temple-Inland** (CIK 731939): made wallboard (4 plants, 2,100 MMSF rated capacity) until International Paper bought it in 2012; last 10-K FY2010 (filed 2011-02-22, " + A['TIN10'] + "). Wallboard profit is **not disclosed**: only a Building Products segment result (lumber, particleboard, MDF, fiberboard and wallboard together). Filed wallboard revenue / volume: 2010 $150M / 1,288 MMSF; 2009 $141M / 1,162; 2008 $135M / 1,061. COMPUTED revenue per MSF (the filing's pricing note says pricing includes freight): $116.46, $121.34, $127.24. Filed average wallboard price change: 2010 -4%, 2009 -4%, 2008 -18%. Whole Building Products segment operating income: 2010 $(19)M on $646M; 2009 $(27)M on $576M; 2008 $(40)M on $694M.\n")
open('_partA.md','w',encoding='utf-8').write('\n'.join(out))

q=[]
w=q.append
w("## PART A VERBATIM QUOTES (Item 1 Competition, risk factors, MD&A capacity statements)\n")
w("Quoted exactly from the text extracted by fetch2.py from the filed HTML. Extraction artifacts: table cells are flattened; line breaks inside a quoted block are shown as ' / '. Registered-trademark symbols are as filed.\n")
w("### USG\n")
w(Q('USG_10K_FY2009.txt',[141],'USG 10-K FY2009, Item 1 Competition, filed 2010-02-12, '+A['USG09']))
w(Q('USG_10K_FY2009.txt',[142],'USG 10-K FY2009, Item 1 Competition, '+A['USG09']))
w(Q('USG_10K_FY2009.txt',[201],'USG 10-K FY2009, Item 1A Risk Factors, '+A['USG09']))
w(Q('USG_10K_FY2009.txt',[532],'USG 10-K FY2009, MD&A, '+A['USG09']))
w(Q('USG_10K_FY2010.txt',[531],'USG 10-K FY2010, MD&A, filed 2011-02-11, '+A['USG10']))
w(Q('USG_10K_FY2011.txt',[651],'USG 10-K FY2011, MD&A, filed 2012-02-14, '+A['USG11']))
w(Q('USG_10K_FY2012.txt',[1161],'USG 10-K FY2012, MD&A, filed 2013-02-15, '+A['USG12']))
w(Q('USG_10K_FY2013.txt',[180],'USG 10-K FY2013, Item 1 Competition, filed 2014-03-03, '+A['USG13']))
w(Q('USG_10K_FY2013.txt',[1200],'USG 10-K FY2013, MD&A, '+A['USG13']))
w(Q('USG_10K_FY2014.txt',[903],'USG 10-K FY2014, MD&A, filed 2015-02-12, '+A['USG14']))
w(Q('USG_10K_FY2015.txt',[1006],'USG 10-K FY2015, MD&A, filed 2016-02-10, '+A['USG15']))
w(Q('USG_10K_FY2016.txt',[193],'USG 10-K FY2016, Item 1 Competition, filed 2017-02-08, '+A['USG16']))
w(Q('USG_10K_FY2016.txt',[893],'USG 10-K FY2016, MD&A, '+A['USG16']))
w(Q('USG_10K_FY2016.txt',[1402],'USG 10-K FY2016, MD&A, '+A['USG16']))
w(Q('USG_10K_FY2017.txt',[1021],'USG 10-K FY2017, MD&A, filed 2018-02-14, '+A['USG17']))
w(Q('USG_10K_FY2018.txt',[153],'USG 10-K FY2018, Item 1 Gypsum Business, filed 2019-02-14, '+A['USG18']))
w(Q('USG_10K_FY2018.txt',[184,185],'USG 10-K FY2018, Item 1 Competition, '+A['USG18']))
w(Q('USG_10K_FY2018.txt',list(range(186,211)),'USG 10-K FY2018, Item 1 Competition, competitor table (columns United States / Canada / Mexico); ARTIFACT: the table is flattened and the x marks cannot be assigned to columns from the extracted text, '+A['USG18']))
w(Q('USG_10K_FY2018.txt',[364],'USG 10-K FY2018, Item 1A Risk Factors, '+A['USG18']))
w(Q('USG_10K_FY2018.txt',[996,997],'USG 10-K FY2018, MD&A, '+A['USG18']))
w("Text artifact flagged, not smoothed: the USG FY2017 and FY2018 10-Ks both read \"a 6% increase from 5.76 square feet in 2016\" (the word \"billion\" is missing as filed; FY2018 line 1451, FY2017 line 1438).\n")
w("### Continental Building Products\n")
w(Q('CBPX_10K_FY2014.txt',list(range(106,114)),'CBPX 10-K FY2014, Item 1 Competition, filed 2015-02-25, '+A['CB14']))
w(Q('CBPX_10K_FY2014.txt',[143],'CBPX 10-K FY2014, Item 1A Risk Factors, '+A['CB14']))
w(Q('CBPX_10K_FY2018.txt',list(range(239,251)),'CBPX 10-K FY2018, Item 1 Competition, filed 2019-02-22, '+A['CB18']))
w(Q('CBPX_10K_FY2018.txt',[293],'CBPX 10-K FY2018, Item 1A Risk Factors, '+A['CB18']))
w(Q('CBPX_10K_FY2018.txt',[676],'CBPX 10-K FY2018, MD&A, '+A['CB18']))
w(Q('CBPX_10K_FY2017.txt',[721],'CBPX 10-K FY2017, MD&A, filed 2018-02-23, '+A['CB17']+'. ARTIFACT flagged, as filed: "approximately 76% year ended December 31, 2017, respectively," (missing "for the", stray "respectively")'))
open('_quotesA.md','w',encoding='utf-8').write('\n'.join(q))
