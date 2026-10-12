# read the BoE GLC nominal daily workbook: python boe_read.py <xlsx>
import sys, openpyxl
wb = openpyxl.load_workbook(sys.argv[1], read_only=True, data_only=True)
print(wb.sheetnames)
for sn in wb.sheetnames:
    rows = list(wb[sn].iter_rows(values_only=True))
    print('==', sn, len(rows))
    for r in rows[:4]:
        print([x for x in r if x is not None][:3], '...', [x for x in r if x is not None][-4:])
    for r in rows[-4:]:
        print(r[0], [x for x in r if x is not None][-4:])
