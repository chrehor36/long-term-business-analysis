# Addendum fold: surgical additions only (no existing text rewritten), re-read from disk at edit time.
import re, os
HERE = os.path.dirname(os.path.abspath(__file__))
RUN = 'Test Runs/2026-09-19 Run - AIG American International Group.md'
Q = 'Screens/WATCHLIST RUN QUEUE.md'
RL = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
add = open(os.path.join(HERE, '_addendum.md'), encoding='utf-8').read()
r = open(RUN, encoding='utf-8').read()
assert '## ADDENDUM 2026-09-19' not in r
open(RUN, 'w', encoding='utf-8', newline='').write(r.rstrip('\n') + '\n' + add)
# dated note directly after the AIG register entry (entry ends at the line naming the run file)
t = open(Q, encoding='utf-8').read()
def count(text):
    m1 = re.search(r'(?m)^## COMPLETED FROM THE QUEUE\s*$', text); m2 = re.search(r'(?m)^## THE WRITE-EARLY PROTOCOL', text)
    return sum(1 for l in text[m1.end():m2.start()].split('\n') if l.startswith('- **'))
n0 = count(t)
end_line = "  `Test Runs/2026-09-19 Run - AIG American International Group.md`.\n"
i = t.find('- **AIG (American International Group, Inc.), 2026-09-19')
j = t.find(end_line, i)
assert i >= 0 and j > i and t.count('- **AIG (American International Group') == 1
note = ("  *Dated note, 2026-09-19, same session, by addendum (operator rule 6) - the entry above is not edited: "
        "(1) the Q4 reserve-sensitivity figure \"$5.05bn (12.3% of equity)\" summed alternative shocks within one line; "
        "like-for-like with the CB run (largest deviation per line) it is **$2.8bn, 6.8% of equity, 52% of 2025 adjusted "
        "pre-tax income** against Chubb's 3.7% and 23%; (2) [E4-30]'s cash-tax half was not computed in the run and FIRES, "
        "explained: cash taxes 34.3% -> 18.3% -> 8.5% of pre-tax income 2023-25 on a valuation-allowance release; "
        "(3) the independent second AIG agent (commit c7132f3) reproduced every core figure, and its eight findings are "
        "folded into the run file's ADDENDUM. The Q2 OUT is unchanged.*\n")
k = j + len(end_line)
t = t[:k] + note + t[k:]
assert count(t) == n0, 'entry count must not change'
open(Q, 'w', encoding='utf-8', newline='').write(t)
print('register entries unchanged at', count(open(Q, encoding='utf-8').read()))
# narrative addendum
rl = open(RL, encoding='utf-8').read()
assert '### AIG ADDENDUM' not in rl
rl_add = ("\n### AIG ADDENDUM - the replication, two corrections (same session, after `4ed4627`)\n"
          "- **Two agents ran AIG** (commit `c7132f3`); the second reproduced every core figure independently and refused to overwrite "
          "the committed run. **Its findings are folded, checked first**: an eleventh year (2015, current-accident-year 99.4; eleven-year "
          "mean 99.6, five of eleven above 100); a proxy-against-10-K candor inconsistency (the board letter's *\"For the first time since "
          "2008, we generated more than $2 billion in underwriting income\"* against the filer's own $2,048M in 2022 and $2,349M in 2023); "
          "component 2 nearly nil; restructuring excluded in every year 2021-2025; and a below-gate floor computation averaging 9.36%.\n"
          "- **Correction 1 - my Q3 scored [E4-30] on smoothness alone.** The cash-tax half fires and is explained: cash taxes 34.3% -> "
          "18.3% -> 8.5% of pre-tax income (2023-25; the first two include Corebridge), on a valuation-allowance release.\n"
          "- **Correction 2 - my Q4 summed alternative shocks within one reserve line** ($5.05bn). Like-for-like with CB it is **$2.8bn, "
          "6.8% of equity and 52% of adjusted pre-tax income, against Chubb's 3.7% and 23%**. A defect worth keeping for every insurer run: "
          "**the filer's sensitivity table lists alternatives, not a scenario; sum one per line.**\n"
          "- **Sector-method gap, sharpened:** about $13.2bn of AIG's covered long-tail losses are NICO's (paid or open), so CONVENTION 4 "
          "float prices Berkshire's credit as AIG's funding.\n")
open(RL, 'w', encoding='utf-8', newline='').write(rl.rstrip('\n') + '\n' + rl_add)
print('addendum folded')
