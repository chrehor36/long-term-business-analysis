# Writes the sections after Q1 into the run file (drafting helper; the text is the run file's own).
import sys
p = "Test Runs/2026-10-12 Run - MTSUY Mitsubishi Corporation.md"
t = open(p, encoding='utf-8').read()
add = ''' The company has itself sorted these earnings apart: its 2018 results split net income into a "Business-related
sector" and a "Market-related sector", the latter defined to include "Mineral resources in the Metals segment" and
North American shale gas and E&P (correction notice of 2018-05-17 to the results of 2018-05-08, the company's own
document, read through the www2.infomart.co.jp mirror).'''
if 'Market-related sector' not in t:
    t = t.replace("in both directions.\n\n**The tests.**", "in both directions." + add + "\n\n**The tests.**")
rest = open(sys.argv[1], encoding='utf-8').read()
t = t[:t.index('## Q2')] + rest
open(p, 'w', encoding='utf-8').write(t)
print('ok')
