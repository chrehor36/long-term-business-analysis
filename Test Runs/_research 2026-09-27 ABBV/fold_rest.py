"""Fold steps 3 (reading list), the wave 7 done file, and the survival-shapes dated note; each file keeps its own newline style."""
import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def load(p):
    raw = open(p, encoding='utf-8', newline='').read()
    return raw, ('\r\n' if '\r\n' in raw else '\n')
# 3. reading list
P = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
raw, nl = load(P)
assert raw.rstrip().endswith('Next in the order file: ABBV.'), raw[-80:]
assert '## UPDATE 2026-09-27 - ABBV' not in raw
note = open('Test Runs/_research 2026-09-27 ABBV/fold_note.md', encoding='utf-8').read().rstrip('\n').replace('\n', nl)
body = raw.rstrip('\r\n') + nl + nl + note + nl
open(P, 'w', encoding='utf-8', newline='').write(body)
print('reading list: appended; ends', repr(body[-40:]))
# done file
P = 'Screens/_daily/_wave7_done.txt'
raw, nl = load(P)
lines = [x for x in raw.split(nl) if x != '']
assert 'ABBV' not in lines and lines[-1] == 'EPAC', lines[-3:]
before = len(lines)
open(P, 'w', encoding='utf-8', newline='').write(raw.rstrip('\r\n') + nl + 'ABBV' + nl)
raw2, _ = load(P); after = len([x for x in raw2.split(nl) if x != ''])
print('done file', before, '->', after)
# survival shapes dated note
P = 'Screens/SURVIVAL SHAPES - index.md'
raw, nl = load(P)
L = raw.split(nl)
rows = [x for x in L if re.match(r'^\| \d+ \|', x)]
nums = [int(re.match(r'^\| (\d+) \|', x).group(1)) for x in rows]
print('shape rows', len(rows), 'max', max(nums))
assert 'the ABBV fold' not in raw
txt = ('*Dated note, 2026-09-27 (the ABBV fold, wave 7 name 79): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** '
       'The table was counted with a line-start regex immediately before writing: **%d rows, maximum number %d**. AbbVie closed at **Q2 OUT**, so Q4 was never opened and the business has no named death. '
       'The run file names, as a signature WITHOUT a verdict, **#10 THE CAMOUFLAGE** (cash from the protected products, Skyrizi and Rinvoq, 42%% of 2025 sales with US compound patents ending in 2033, recycled into purchased candidates that must each win approval, a government-set price and a market before their own exclusivity ends: about $136bn of businesses, pipeline and Apogee bought since 2013, Cerevel\'s lead asset impaired by $4.5bn within four months of closing), '
       'with **#14 THE PATRON** and **#17 THE PERMIT** as features (government-set Medicare prices on four named products, and a January 2026 agreement trading pricing concessions for three years\' exemption) and **#6 THE BORROWED BALANCE SHEET** as a feature (dividends above GAAP earnings, a stockholders\' deficit, $64.3bn of net debt plus a $25.4bn royalty obligation). '
       '**The brief asked that ABBV be entered in the instances column of the shape named; it is not**, for the reason the PAGP, CALM and MRK folds gave: entering a Q2 observation as a Q4 instance would make this index say something the run file does not. '
       'AbbVie is also the filed counter-instance to the MRK file\'s candidate shape "the expiry": it met a dated expiry of the product that carried its sales (Humira, US exclusivity ended 2023-01-31) and survived it with sales held; the candidate stays unadded.*') % (len(rows), max(nums))
body = raw.rstrip('\r\n') + nl + nl + txt + nl
open(P, 'w', encoding='utf-8', newline='').write(body)
print('shapes: note appended')
