# 30-year nominal spot from the BoE GLC daily workbook, last dated rows: python boe_30y.py <xlsx>
import sys, openpyxl, datetime
wb = openpyxl.load_workbook(sys.argv[1], read_only=True, data_only=True)
rows = list(wb['4. spot curve'].iter_rows(values_only=True))
hdr = next(r for r in rows if r and r[0] == 'years:')
col = list(hdr).index(30)
dated = [r for r in rows if r and isinstance(r[0], datetime.datetime) and r[col] is not None]
for r in dated[-5:]:
    print(r[0].date(), '30y spot', round(r[col], 4), '| 25y', round(r[list(hdr).index(25)], 4))
