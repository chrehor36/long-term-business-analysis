import re, html as H
from fetch import get
def strip2(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'\s+',' ',s)
    s=re.sub(r'(?is)<br[^>]*>','\n',s)
    s=re.sub(r'(?is)</(p|div|tr|h1|h2|h3|li|table)>','\n',s)
    s=re.sub(r'(?is)</t[dh]>','|',s)
    s=re.sub(r'(?s)<[^>]+>','',s)
    s=H.unescape(s).replace('​','').replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\|[\s|$]*\|','|',s)   # collapse empty cells
    s=re.sub(r'\|\s*\)', ')', s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
