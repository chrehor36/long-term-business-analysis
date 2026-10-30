import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfetch import grab
p = grab('1415404', '0001558370-24-002209', 'tmb-20231231x10k.htm', 'ECHO_10K_FY2023.txt')
t = open(p, encoding='utf-8').read()
for m in re.finditer(r'[0-9]\.[0-9]+ million Pay-TV subscribers[^.]*\.', t):
    print(m.group(0))
    break
