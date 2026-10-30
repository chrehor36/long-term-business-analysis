import sys,re
t=open(sys.argv[1],encoding='utf-8').read()
i=t.find(sys.argv[2])
seg=t[i-200:i+int(sys.argv[3]) if len(sys.argv)>3 else i+6000]
seg=re.sub(r'\n\s*\|\s*', ' ', seg); seg=re.sub(r'\s+',' ',seg).replace(' | ',' ')
print(seg)
