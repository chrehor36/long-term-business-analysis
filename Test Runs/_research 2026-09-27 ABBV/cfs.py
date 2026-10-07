import sys,re
sys.stdout.reconfigure(encoding='utf-8')
s=open(sys.argv[1],encoding='utf-8').read()
idx=[m.start() for m in re.finditer(r'Cash Flows from Operating Activities',s)]
for i in idx:
    seg=s[i:i+200]
    if 'Net income' in s[i:i+400] or 'Net Income' in s[i:i+400]:
        print(s[i-400:i+5200]); break
