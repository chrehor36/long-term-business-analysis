import re,sys
y=sys.argv[1]
s=open(f'cache/k{y}.txt',encoding='utf-8').read()
i=s.find('Cash Flows from Operating Activities')
if i<0: i=s.lower().find('cash flows from operating activities:')
j=s.find('Cash and cash equivalents—end of period',i)
if j<0: j=i+6000
t=re.sub(r'[ \t|$]+',' ',s[i-600:j+200]); t=re.sub(r'\n\s*\n+','\n',t)
print(t)
