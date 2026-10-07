import re,sys,html
for f in ['RMRpeer_BRDG_10K_FY2024','RMRpeer_AINC_10K_FY2024','RMRpeer_OWL_10K_FY2025','RMRpeer_ARES_10K_FY2025','RMRpeer_BAM_10K_FY2025']:
    s=open(f+'.htm',encoding='utf-8',errors='ignore').read()
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)</(td|th)>',' | ',s)
    s=re.sub(r'(?i)</(tr|p|div|h[1-6]|li)>','\n',s)
    s=re.sub(r'(?is)<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    open(f+'.txt','w',encoding='utf-8').write(s)
    print(f, len(s))
