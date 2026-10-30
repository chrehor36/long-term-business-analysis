import io
P = 'Screens/SURVIVAL SHAPES - index.md'
t = io.open(P, encoding='utf-8').read()
assert 'DIS (2026-09-19' not in t, 'DIS already in the index - ABORT'

# Shape #10 - the mechanism for DIS; also backfill IBM, whose own fold did not update this index.
old10 = ('META (2026-09-18: advertising cash recycled into Reality Labs, $96.7bn lost since FY2019, '
         'and the superintelligence build; #1 and #2 as features) |')
assert t.count(old10) == 1, 'shape 10 anchor not found exactly once'
new10 = (old10[:-2] +
         ', IBM (2026-09-19, the mechanism, with a proposed feature - the company sells the service that '
         'erodes its own franchise; added 2026-09-19 by the DIS fold from the IBM run file, whose fold did '
         'not update this index)'
         ', DIS (2026-09-19, the mechanism, with #1 as a feature: Experiences earns 28.9% pre-tax on 24.3% '
         'of the capital and 56.9% of the segment profit, and its cash is recycled into Entertainment and '
         'Sports, which hold 75.7% of the capital and earn 7.0%; ESPN owns no sport and must re-buy its '
         'advantage at auction - $84,076M of sports rights signed, 29.2x the segment’s operating income - '
         'while the fee-paying base shrinks 7% a year and two distributors refused the offsetting rate rise '
         'in eleven months; the company survives on $94bn of revenue and 4.9x interest coverage, and owner '
         'earnings PER SHARE fell from $7.39 to $7.11 over seven years)' + ' |')
t = t.replace(old10, new10)

old1 = ('META ($349.31bn of commitments and about $347bn of signed leases, a feature of #10) |')
assert t.count(old1) == 1, 'shape 1 anchor not found exactly once'
new1 = (old1[:-2] +
        ', DIS (2026-09-19, a feature of #10: $104,088M of contractual commitments - 59% of the market '
        'capitalisation - of which $84,076M is sports programming rights at $9.1-9.9bn a year through FY2030 '
        'and $36,610M thereafter, against the filer’s own caution that "There can be no assurance that '
        'revenues from programming based on these rights will exceed the cost of the rights")' + ' |')
t = t.replace(old1, new1)

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('shapes index updated: #10 (IBM backfilled, DIS added) and #1 (DIS added)')
