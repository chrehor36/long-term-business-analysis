p='Screens/SURVIVAL SHAPES - index.md'
note=("*Dated note, 2026-09-26 (the LNN fold, wave 7 name 46): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** "
"The table was counted with a line-start regex immediately before writing: **30 rows, maximum number 30**. Lindsay Corporation closed at **Q2 OUT**, so Q4 was never opened and the business has no named death. "
"The run file names, as a signature WITHOUT a verdict, **#11 THE PASS-THROUGH** (irrigation price follows steel in both directions by the registrant's own MD&A and slips in soft years, while the filer's own after-tax return on invested capital ran 5.9-7.2% in FY2015-FY2018 and 1.6% in FY2019) "
"**with [E2-58]'s farm-income cycle as a feature** (the seven lean years FY2015-FY2021 averaged $14.6M a year of capex-end owner earnings). "
"**None of these is entered in an instances column**, for the reason the PAGP, CALM, USPH, BDC, PPG and MATX folds gave: a Q2 observation entered as a Q4 instance would make this index say something the run file does not.*")
b=open(p,'rb').read()
nl=b'\r\n' if b.endswith(b'\r\n') else b'\n'
assert b.endswith(nl)
open(p,'wb').write(b+note.encode('utf-8')+nl)
print('ok',nl)
