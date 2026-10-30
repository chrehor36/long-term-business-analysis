# post the MAS SGS benchmark form for the 30-year yield, daily, Oct 2026
import re, urllib.request, urllib.parse, http.cookiejar, html, sys
url="https://eservices.mas.gov.sg/statistics/fdanet/BenchmarkPricesAndYields.aspx"
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders=[("User-Agent","Mozilla/5.0")]
t=op.open(url,timeout=60).read().decode('utf-8','replace')
def hid(n): return re.search(r'name="'+re.escape(n)+r'"[^>]*value="([^"]*)"',t).group(1)
P='ctl00$ContentPlaceHolder1$'
data={'__EVENTTARGET':'','__EVENTARGUMENT':'','__LASTFOCUS':'','__VIEWSTATE':hid('__VIEWSTATE'),'__VIEWSTATEGENERATOR':hid('__VIEWSTATEGENERATOR'),'__EVENTVALIDATION':hid('__EVENTVALIDATION'),
P+'StartYearDropDownList':'2026',P+'StartMonthDropDownList':'9',P+'EndYearDropDownList':'2026',P+'EndMonthDropDownList':'10',P+'FrequencyDropDownList':'D',
P+'ThirtyYearBondYieldCheckBox':'on',P+'TenYearBondYieldCheckBox':'on',P+'DisplayButton':'Display'}
# discover option values
for sel in ['StartMonthDropDownList','FrequencyDropDownList']:
    m=re.search(r'name="'+re.escape(P+sel)+r'".*?</select>',t,re.S); print(sel, re.findall(r'<option[^>]*value="([^"]*)"[^>]*>([^<]*)',m.group(0))[:14])
r=op.open(url,urllib.parse.urlencode(data).encode(),timeout=60).read().decode('utf-8','replace')
open('cache/mas_out.htm','w',encoding='utf-8').write(r)
s=re.sub(r'<[^>]+>',' | ',r); s=html.unescape(s); s=re.sub(r'(\s*\|\s*)+',' | ',s)
i=s.find('30-Year Bond Yield',s.find('Display'))
print(s[-4000:])
