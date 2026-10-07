import os,json,io
D=os.path.dirname(os.path.abspath(__file__))
r=json.load(open(os.path.join(D,'final.json')))
labs=json.load(open(os.path.join(D,'labels.json')))
ACC={'q1fy17':('0000104169-16-000083','2016-05-19'),'q2fy17':('0000104169-16-000116','2016-08-18'),
'q3fy17':('0000104169-16-000134','2016-11-17'),'q4fy17':('0000104169-17-000013','2017-02-21'),
'q1fy18':('0000104169-17-000025','2017-05-18'),'q2fy18':('0000104169-17-000052','2017-08-17'),
'q3fy18':('0000104169-17-000075','2017-11-16'),'q4fy18':('0000104169-18-000020','2018-02-20'),
'q1fy19':('0000104169-18-000047','2018-05-17'),'q2fy19':('0000104169-18-000081','2018-08-16'),
'q3fy19':('0000104169-18-000103','2018-11-15'),'q4fy19':('0000104169-19-000011','2019-02-19'),
'q1fy20':('0000104169-19-000021','2019-05-16'),'q2fy20':('0000104169-19-000058','2019-08-15'),
'q3fy20':('0000104169-19-000081','2019-11-14'),'q4fy20':('0000104169-20-000007','2020-02-18'),
'q1fy21':('0000104169-20-000016','2020-05-19'),'q2fy21':('0000104169-20-000037','2020-08-18'),
'q3fy21':('0000104169-20-000073','2020-11-17'),'q4fy21':('0000104169-21-000022','2021-02-18'),
'q1fy22':('0000104169-21-000037','2021-05-18'),'q2fy22':('0000104169-21-000054','2021-08-17'),
'q3fy22':('0000104169-21-000063','2021-11-16'),'q4fy22':('0000104169-22-000009','2022-02-17'),
'q1fy23':('0000104169-22-000024','2022-05-17'),'q2fy23':('0000104169-22-000065','2022-08-16'),
'q3fy23':('0000104169-22-000077','2022-11-15'),'q4fy23':('0000104169-23-000010','2023-02-21'),
'q1fy24':('0000104169-23-000043','2023-05-18'),'q2fy24':('0000104169-23-000088','2023-08-17'),
'q3fy24':('0000104169-23-000124','2023-11-16'),'q4fy24':('0000104169-24-000019','2024-02-20'),
'q1fy25':('0000104169-24-000088','2024-05-16'),'q2fy25':('0000104169-24-000131','2024-08-15'),
'q3fy25':('0000104169-24-000170','2024-11-19'),'q4fy25':('0000104169-25-000010','2025-02-20'),
'q1fy26':('0000104169-25-000069','2025-05-15'),'q2fy26':('0000104169-25-000120','2025-08-21'),
'q3fy26':('0000104169-25-000177','2025-11-20'),'q4fy26':('0000104169-26-000032','2026-02-19'),
'q1fy27':('0000104169-26-000095','2026-05-21'),'q2fy27':('0000104169-26-000145','2026-08-20')}
OI={'q1fy22':('26.8%','16.4%'),'q2fy22':('20.4%','11.5%'),'q3fy22':('5.9%','10.2%'),'q4fy22':('0.3%','41.1%'),
'q1fy23':('-18.2%','-20.0%'),'q2fy23':('-6.7%','-35.3%'),'q3fy23':('4.8%','18.3%'),'q4fy23':('3.8%','-6.2%'),
'q1fy24':('11.7%','-0.4%'),'q2fy24':('7.6%','22.0%'),'q3fy24':('-2.2%','5.5%'),'q4fy24':('12.9%','20.4%'),
'q1fy25':('7.0%','34.3%'),'q2fy25':('7.8%','11.5%'),'q3fy25':('9.1%','6.9%'),'q4fy25':('7.4%','(7.4%)'),
'q1fy26':('7.0%','11.5%'),'q2fy26':('2.0%','(15.8%)'),'q3fy26':('6.3%','5.8%'),'q4fy26':('6.6%','3.8%'),
'q1fy27':('3.5%','1.2%'),'q2fy27':('20.6%','44.3%')}
def pretty(q):
    return 'Q'+q[1]+' FY'+q[4:]
def cell(b,k,n=0):
    if not b or not b.get(k) or len(b[k])<=n: return '--'
    return b[k][n].replace(' %','%')
o=io.open(os.path.join(D,'quarterly-transactions.md'),'w',encoding='utf-8')
w=o.write
w("# Walmart quarterly comp decomposition, from the 8-K earnings releases (ex-99.1)\n\n")
w("TRANSCRIPTION ONLY. Figures are exactly as filed. No interpolation, no smoothing, no derived values.\n")
w("Every row is the **as-first-reported** current-quarter column of that quarter's own earnings release.\n")
w("CIK 0000104169. All documents fetched from SEC EDGAR and saved in this directory as `8k-<qtr>-ex991.htm` / `.txt`.\n\n")
w("**Key finding on availability:** the 10-K carries no numeric transactions/ticket split. The quarterly\n")
w("earnings release (8-K, Item 2.02, exhibit 99.1) does. The numeric split in a **segment table** runs from\n")
w("**Q1 FY2017 (release dated 2016-05-19)** forward, uninterrupted, 42 consecutive quarters to Q2 FY2027.\n")
w("Earlier disclosure exists in weaker forms; see Absence and earliest-disclosure findings below.\n\n")
w("## Walmart U.S.\n\n")
w("| Quarter | Comp sales ex-fuel % | Transactions % | Avg ticket % | eComm contribution to comp | Segment op income growth | Source accession | Release date |\n")
w("|---|---|---|---|---|---|---|---|\n")
for q in r:
    b=r[q][0] if r[q] else None
    acc,dt=ACC[q]
    oi=OI.get(q,('--','--'))[0]
    w(f"| {pretty(q)} | {cell(b,'comp')} | {cell(b,'tran')} | {cell(b,'tick')} | {cell(b,'ecom')} | {oi} | {acc} | {dt} |\n")
w("\n## Sam's Club U.S.\n\n")
w("| Quarter | Comp sales ex-fuel % | Transactions % | Avg ticket % | eComm contribution to comp | Segment op income growth | Source accession | Release date |\n")
w("|---|---|---|---|---|---|---|---|\n")
for q in r:
    b=r[q][1] if len(r[q])>1 else None
    acc,dt=ACC[q]
    oi=OI.get(q,('--','--'))[1]
    w(f"| {pretty(q)} | {cell(b,'comp')} | {cell(b,'tran')} | {cell(b,'tick')} | {cell(b,'ecom')} | {oi} | {acc} | {dt} |\n")
w("\n## Metric label as printed, by vintage (transcribed, not normalised)\n\n")
w("| First quarter using it | Transactions row | Ticket row | eCommerce row |\n|---|---|---|---|\n")
prev=None
for q,v in labs.items():
    cur=(v.get('tran'),v.get('tick'),v.get('ecom'))
    if cur!=prev: w(f"| {pretty(q)} | {cur[0]} | {cur[1]} | {cur[2]} |\n")
    prev=cur
o.close()
print("written")
