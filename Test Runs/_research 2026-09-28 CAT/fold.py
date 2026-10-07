import re, json, sys
sys.stdout.reconfigure(encoding='utf-8')
R = 'Test Runs/_research 2026-09-28 CAT/'
def rd(p):
    raw = open(p, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in raw else '\n'
    return raw, nl
# ---- 1. register entry, by LINE ----
p = 'Screens/WATCHLIST RUN QUEUE.md'
raw, nl = rd(p); L = raw.split(nl)
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(h) == 1, h
def count(L):
    h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE'][0]
    w = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')][0]
    ent = [l for l in L[h + 1:w] if re.match(r'^- \*\*', l)]
    return len(ent), ent[0][:30], sum(1 for l in ent if l.startswith('- **CAT ('))
before = count(L)
assert before[0] == 230 and before[1].startswith('- **ATR') and before[2] == 0, before
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h[0] + 1] + entry + L[h[0] + 1:]
open(p, 'w', encoding='utf-8', newline='').write(nl.join(L))
after = count(open(p, encoding='utf-8', newline='').read().split(nl))
assert after[0] == 231 and after[1].startswith('- **CAT') and after[2] == 1, after
print('register: heading line', h[0] + 1, 'before', before, 'after', after)
# ---- 2. done file ----
p = 'Screens/_daily/_wave7_done.txt'
raw, nl = rd(p)
assert raw.endswith(nl) and 'CAT' not in raw.split(nl)
open(p, 'w', encoding='utf-8', newline='').write(raw + 'CAT' + nl)
D = open(p, encoding='utf-8', newline='').read().split(nl)[:-1]
print('done file', len(D), 'lines, last', D[-1])
# ---- 3. reading list ----
p = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
raw, nl = rd(p)
note = open(R + 'fold_note.md', encoding='utf-8').read().strip('\n').split('\n')
add = nl + nl.join(note) + nl
if not raw.endswith(nl): add = nl + add
open(p, 'w', encoding='utf-8', newline='').write(raw + add)
print('reading list appended', len(note), 'lines; ends:', open(p, encoding='utf-8').read().rstrip()[-40:])
# ---- 4a. alerts ----
p = 'tools/alerts.json'
d = json.load(open(p, encoding='utf-8'))
assert not any(a['id'].startswith('CAT-') for a in d['alerts'])
src = 'Source: Test Runs/2026-09-28 Run - CAT Caterpillar.md.'
d['alerts'].append({"id": "CAT-floor-band", "ticker": "CAT", "currency": "USD", "op": "<=", "threshold": 222.42, "active": True,
 "label": "CAT at/below $222.42: the E4-28 floor is met at g = 2.4% (MP&E sales 2007-2025) on the five-year capex-end MP&E owner earnings of $7,800M and 459,674,889 cover shares. Q1-Q4 all IN on 2026-09-28 (Q2 NARROW through the E2-58 wide-and-sustainable exception: Construction Industries' margin above Deere C&F's in all fifteen years 2011-2025; price realization positive in 19 of 23 filed years; criterion (2) not met as a belief); Q5 quit on at $821.58 (yield 2.07-2.21% five-year against a 5.49% sovereign, expectancy 4.4-8.6%). Prompt for a FULL v4.1 re-run, not a purchase, sized DOWN if it clears (capital-allocation flag live: 2026 buybacks at about $880 against the run's values; the lender rolls $12.6bn a year). VOID if any Q2 falsifier has fired: Construction Industries' margin at or below Deere C&F's in any fiscal year, or below Komatsu's whole-company margin two consecutive years; consolidated price realization negative two consecutive years, or negative in a year of rising volume twice within five years (2025 is the first); the manufacturing margin below 5% outside a year in which sales fell 20% or more; Financial Products past dues above 6%, covenant leverage above 9 to 1, or any payment under the support agreement; an acquisition above $5bn or goodwill impairments above $1bn in a year. " + src})
d['alerts'].append({"id": "CAT-rerun-band", "ticker": "CAT", "currency": "USD", "op": "<=", "threshold": 598.07, "active": True,
 "label": "CAT at/below $598.07: the E4-28 floor is met only if the 5% perpetual-growth ceiling (the JKHY convention under E4-44) is granted on the TTM depreciation-end MP&E owner earnings ($13,746M to 2026-06-30, carrying $3,233M of customer prepayments), above the record's 2.4% sales growth and at the top of the cycle. Prompt for a FULL v4.1 re-run in which the level, the growth and the (c) end are re-tested before any is spent. Re-derive both CAT bands on the 2026 10-K (about mid-February 2027); VOID if any falsifier in CAT-floor-band has fired. " + src})
txt = json.dumps(d, ensure_ascii=False, indent=1) + '\n'
json.loads(txt)
open(p, 'w', encoding='utf-8', newline='\n').write(txt)
print('alerts', len(d['alerts']))
# ---- 4b. PORTFOLIO row after ATR ----
p = 'PORTFOLIO.md'
raw, nl = rd(p); L = raw.split(nl)
i = [k for k, l in enumerate(L) if l.startswith('| - | ATR |')]
assert len(i) == 1 and not any(l.startswith('| - | CAT |') for l in L)
row = ("| - | CAT | 2.07–2.21 % (5-yr, 2026-09-28; 1.21–2.84 % across every window of 1-19 years; 3.27–3.64 % TTM with $3,233M of customer prepayments) | 5.49 % USD | "
       "**below the sovereign on every window and both (c) ends, −3.42 to −3.28 points (5-yr)** | **RUN DONE** (`Test Runs/2026-09-28 Run - CAT Caterpillar.md`, wave 7 name 89): "
       "**Q1–Q4 all IN; Q2 NARROW, through [E2-58]'s wide-and-sustainable exception** (owner earnings and the record measured on the manufacturer as the filer separates it, Cat Financial entering through its dividends; "
       "Construction Industries' margin above Deere C&F's in all fifteen years 2011-2025 and above Komatsu's and CNH's in every year rowed; price realization positive in 19 of 23 filed years including 2009; "
       "the filer's own *\"we compete on the basis of product performance, customer service, quality and price\"* with *\"price discounting\"*, the 2016 and 2025 give-backs and the 1.5-2.1 % trough margins recorded as the strongest evidence against; criterion (2) not met as a belief, the reading named for the operator); "
       "**Q3 IN at binary-gate weight** (no disqualifier; EBITDA absent from every document read; [E2-57] fires in the proxy, the 2025 bonus lifted from 98 % to 107 % by a partial tariff exclusion; capital-allocation flag, 2026 buybacks at about $880); "
       "**Q4 IN, GOOD** (owner earnings $7,800M–$8,361M five-year, judged about $7bn; named death #11 THE PASS-THROUGH, cyclical, with #18 and #6 as features). **Q5 quit on at $821.58**: expectancy 4.4–8.6 % against ~10 %; value about $220–$600. "
       "**NOT RANKED: watch-list only; no position held and none proposed.** Bands `CAT-floor-band` $222.42 and `CAT-rerun-band` $598.07; each a prompt for a full re-run, never a buy, VOID if a Q2 falsifier fires. |")
L = L[:i[0] + 1] + [row] + L[i[0] + 1:]
open(p, 'w', encoding='utf-8', newline='').write(nl.join(L))
print('portfolio row inserted after line', i[0] + 1)
# ---- survival shapes: #11 later instances + dated note ----
p = 'Screens/SURVIVAL SHAPES - index.md'
raw, nl = rd(p); L = raw.split(nl)
rows = [l for l in L if re.match(r'^\| \d+ \|', l)]
nums = [int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows]
print('shapes table rows', len(rows), 'max', max(nums))
k = [j for j, l in enumerate(L) if l.startswith('| 11 |')]
assert len(k) == 1 and L[k[0]].rstrip().endswith('|') and 'CAT (' not in L[k[0]]
inst = (", CAT (2026-09-28, the mechanism, in its cyclical form, Q4 reached: in over-supplied years the industry gives price back to customers (Caterpillar's own bridge: −$760M in 2016 on *\"excess industry capacity\"*, −$435M in 2020, −$817M in 2025 with volume rising) and the manufacturing margin goes to about zero (1.5% in 2009, 2.1% in 2016) though Caterpillar out-earns every filed rival in every trough; "
        "owner earnings $518M (2012), $797M (2009) and $955M (2008) against $9.2-9.8bn in 2023-2025; #18 THE ROUND TRIP as a feature (Cat Financial finances the dealers' and customers' purchases, write-offs $253M in 2009) and #6 THE BORROWED BALANCE SHEET as a feature (the lender rolls $12.6bn a year); a real possibility for the owner's return, a low-level possibility for the company)")
s = L[k[0]].rstrip()
L[k[0]] = s[:-1].rstrip() + inst + ' |'
note = ("*Dated note, 2026-09-28 (the CAT fold, wave 7 name 89): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** "
        "The table was counted with a line-start regex immediately before writing: **%d rows, maximum number %d**. Caterpillar Inc. passed Q1-Q4 (Q2 NARROW) and was quit on at Q5, so its named death is a Q4 finding: "
        "**#11 THE PASS-THROUGH, entered above as a later instance in its cyclical form** (the GFF form: price given back in over-supplied years, the margin to about zero at the troughs), with **#18 THE ROUND TRIP** (the captive lender financing the buyer) and **#6 THE BORROWED BALANCE SHEET** (the lender's refinancing) as features. No new shape: the mechanism is #11's own, run through a cycle.*" % (len(rows), max(nums)))
while L and L[-1] == '': L.pop()
L.append(note); L.append('')
open(p, 'w', encoding='utf-8', newline='').write(nl.join(L))
print('shapes updated')
