import requests,re,html,sys,time
h={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
base='https://www.sec.gov/Archives/edgar/data/2012219/'
docs={'20F_2026':('000119312526282941','omse-20260331.htm'),
'20F_2025':('000095017025098559','omse-20250331.htm'),
'424B4':('000121390025042797','ea0200016-30.htm'),
'6K_2026_06':('000119312526283046','oms_2026_earnings_releas.htm'),
'6K_2026_02':('000121390026010531','ea0273592-6k_omsenergy.htm'),
'6K_2025_11':('000119312525290488','oms_1h_2026_financial_re.htm'),
'6K_2025_07':('000095017025098129','oms_2025_earnings_releas.htm'),
}
def totext(s):
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>',"\n",s)
    s=re.sub(r'(?i)</td>|</th>'," | ",s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
for k,(acc,doc) in docs.items():
    r=requests.get(base+acc+'/'+doc,headers=h); time.sleep(0.3)
    open(k+'.htm','w',encoding='utf-8').write(r.text)
    open(k+'.txt','w',encoding='utf-8').write(totext(r.text))
    print(k,r.status_code,len(r.text))
