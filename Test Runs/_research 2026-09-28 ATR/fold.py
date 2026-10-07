import re, json, sys
sys.stdout.reconfigure(encoding='utf-8')
R = 'Test Runs/_research 2026-09-28 ATR/'
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
    return len(ent), ent[0][:30], sum(1 for l in ent if l.startswith('- **ATR ('))
before = count(L)
assert before[0] == 229 and before[1].startswith('- **PLUS') and before[2] == 0, before
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h[0] + 1] + entry + L[h[0] + 1:]
open(p, 'w', encoding='utf-8', newline='').write(nl.join(L))
after = count(open(p, encoding='utf-8', newline='').read().split(nl))
assert after[0] == 230 and after[1].startswith('- **ATR') and after[2] == 1, after
print('register: heading line', h[0] + 1, 'before', before, 'after', after)
# ---- 2. done file ----
p = 'Screens/_daily/_wave7_done.txt'
raw, nl = rd(p)
assert raw.endswith(nl) and 'ATR' not in raw.split(nl)
open(p, 'w', encoding='utf-8', newline='').write(raw + 'ATR' + nl)
D = open(p, encoding='utf-8', newline='').read().split(nl)[:-1]
print('done file', len(D), 'lines, last', D[-1])
# ---- 3. reading list ----
p = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
raw, nl = rd(p)
note = open(R + 'fold_note.md', encoding='utf-8').read().rstrip('\n').split('\n')
add = nl.join(note) + nl
if not raw.endswith(nl): add = nl + add
open(p, 'w', encoding='utf-8', newline='').write(raw + add)
print('reading list appended', len(note), 'lines; ends:', open(p, encoding='utf-8').read().rstrip()[-40:])
# ---- 4a. alerts ----
p = 'tools/alerts.json'
d = json.load(open(p, encoding='utf-8'))
assert not any(a['id'].startswith('ATR-') for a in d['alerts'])
src = 'Source: Test Runs/2026-09-28 Run - ATR AptarGroup.md.'
d['alerts'].append({"id": "ATR-floor-band", "ticker": "ATR", "currency": "USD", "op": "<=", "threshold": 46.22, "active": True,
 "label": "ATR at/below $46.22: the E4-28 floor is met at g = 3.6% (net sales 2008-2025, purchases included) on the five-year capex-end owner earnings of $188.1M and 63,581,129 cover shares. Q1-Q4 all IN on 2026-09-28 (Q2 NARROW, level, carried by the Pharma segment at 79% of segment operating profit); Q5 quit on at $123.87 (yield 2.39-3.47% five-year against a 5.49% sovereign, expectancy 6.0-9.2%). Prompt for a FULL v4.1 re-run, not a purchase, sized DOWN if it clears (capital-allocation flag live: 2025 buybacks at about $120 against the run's values; purchases into a Beauty segment earning 4% on its assets). VOID if any Q2 falsifier has fired: Pharma segment margin (Adjusted EBITDA less its own depreciation and amortization) below 24.1% two consecutive years without a quantified one-time cause; the filer reporting Pharma price given back two consecutive years; Pharma core sales negative two consecutive years; the company's pre-tax return on operating capital below 12% two consecutive years, or a write-down of a purchased business of $100M or more; the ARS antitrust claim decided against Aptar. " + src})
d['alerts'].append({"id": "ATR-rerun-band", "ticker": "ATR", "currency": "USD", "op": "<=", "threshold": 103.80, "active": True,
 "label": "ATR at/below $103.80: the E4-28 floor is met only if the 5% perpetual-growth ceiling (the JKHY convention under E4-44) is granted on the three-year depreciation-end owner earnings ($330.0M, 2023-2025), above the record's 4.4% (capex end) owner-earnings-per-share growth. Prompt for a FULL v4.1 re-run in which the growth and the (c) end are re-tested before either is spent. Re-derive both ATR bands on the 2026 10-K (about early February 2027); VOID if any falsifier in ATR-floor-band has fired. " + src})
txt = json.dumps(d, ensure_ascii=False, indent=1) + '\n'
json.loads(txt)
open(p, 'w', encoding='utf-8', newline='\n').write(txt)
print('alerts', len(d['alerts']))
# ---- 4b. PORTFOLIO row after EPAC ----
p = 'PORTFOLIO.md'
raw, nl = rd(p); L = raw.split(nl)
i = [k for k, l in enumerate(L) if l.startswith('| - | EPAC |')]
assert len(i) == 1 and not any(l.startswith('| - | ATR |') for l in L)
row = ("| - | ATR | 2.39–3.47 % (5-yr, 2026-09-28; 1.99–4.19 % across every window of 1-18 years; 3.42–3.57 % TTM) | 5.49 % USD | "
       "**below the sovereign on every window and both (c) ends, −3.10 to −2.02 points (5-yr)** | **RUN DONE** (`Test Runs/2026-09-28 Run - ATR AptarGroup.md`, wave 7 name 88): "
       "**Q1–Q4 all IN; Q2 NARROW, level, carried by one segment** (Pharma: nasal pumps, inhaler valves and injectable elastomers, 24.1-30.6 % margins every year 2006-2025, 36-41 % pre-tax on its segment assets before the Stelmi and CSP purchases and 18-23 % after, 79 % of segment operating profit; "
       "Beauty and Closures, 54 % of sales, 3-6 % on their assets since 2020; the filer's own *\"price competition in all product lines and markets\"* every year since 2005 and a 2025 Pharma price concession recorded as the strongest evidence against; the HAS and GRMN precedent, the ABT segment question named for the operator); "
       "**Q3 IN at binary-gate weight** (no disqualifier; [E4-29] fires, Adjusted EBITDA half the cash bonus; guidance beaten 11 of 14 quarters; capital-allocation flag, 2025 buybacks at about $120); "
       "**Q4 IN, GOOD** (owner earnings $188.1M–$273.7M five-year, judged about $250M; named death #10 THE CAMOUFLAGE). **Q5 quit on at $123.87**: expectancy 6.0–9.2 % against ~10 %; value about $45–$105. "
       "**NOT RANKED: watch-list only; no position held and none proposed.** Bands `ATR-floor-band` $46.22 and `ATR-rerun-band` $103.80; each a prompt for a full re-run, never a buy, VOID if a Q2 falsifier fires. |")
L = L[:i[0] + 1] + [row] + L[i[0] + 1:]
open(p, 'w', encoding='utf-8', newline='').write(nl.join(L))
print('portfolio row inserted after line', i[0] + 1)
# ---- survival shapes: #10 later instances + dated note ----
p = 'Screens/SURVIVAL SHAPES - index.md'
raw, nl = rd(p); L = raw.split(nl)
rows = [l for l in L if re.match(r'^\| \d+ \|', l)]
nums = [int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows]
print('shapes table rows', len(rows), 'max', max(nums))
k = [j for j, l in enumerate(L) if l.startswith('| 10 |')]
assert len(k) == 1 and L[k[0]].rstrip().endswith('|') and 'ATR (' not in L[k[0]]
inst = (", ATR (2026-09-28, an instance, Q4 reached: the Pharma segment earned 24.1-30.6% of its sales every year 2006-2025 and 36-41% pre-tax on its segment assets before the Stelmi and CSP purchases; its cash went into purchases and into a beauty and closures half that earns 3-6% on $2.5bn of segment assets and made $127.5M of operating profit in 2025 against $136.8M in 2008; "
        "the owners' pre-tax return on operating capital fell from 17-23% (2012-2017) to 12-16% (2018-2025) while Pharma's margin held; #11 THE PASS-THROUGH as a feature (resin passed through in the consumer half) and #12 THE ADDRESS as a small one (the Russian subsidiary under state administration from 2026-09-21); a real possibility for the owner's return, a low-level possibility for the company)")
s = L[k[0]].rstrip()
L[k[0]] = s[:-1].rstrip() + inst + ' |'
note = ("*Dated note, 2026-09-28 (the ATR fold, wave 7 name 88): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** "
        "The table was counted with a line-start regex immediately before writing: **%d rows, maximum number %d**. AptarGroup, Inc. passed Q1-Q4 (Q2 NARROW) and was quit on at Q5, so its named death is a Q4 finding: "
        "**#10 THE CAMOUFLAGE, entered above as a later instance** (the Pharma segment's cash recycled into purchases and a consumer half earning 3-6%% on its assets), with **#11 THE PASS-THROUGH** and **#12 THE ADDRESS** as features. No new shape: the mechanism is #10's own.*" % (len(rows), max(nums)))
while L and L[-1] == '': L.pop()
L.append(note); L.append('')
open(p, 'w', encoding='utf-8', newline='').write(nl.join(L))
print('shapes updated')
