p=r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-27 Run - CSCO Cisco Systems.md'
s=open(p,encoding='utf-8').read()
a='The FY2024 cash-flow statement carries *"Acquisitions, net of cash and cash equivalents acquired and divestitures | ( 25,994 )"*.'
b='The FY2026 cash-flow statement carries *"Acquisitions, net of cash and cash equivalents acquired and divestitures | ( 516 ) | ( 291 ) | ( 25,994 )"* (FY2026, FY2025, FY2024).'
assert a in s; s=s.replace(a,b); open(p,'w',encoding='utf-8',newline='\n').write(s)
