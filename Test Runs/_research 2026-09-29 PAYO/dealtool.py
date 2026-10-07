import sys
sys.path.insert(0,'tools')
import sources as s
for arg in [s.cik_for('PAYO'), 'PAYO', 1845815, '0001845815']:
    try:
        print(repr(arg), '->', s.deal_note(arg))
    except Exception as e:
        print(repr(arg), '-> EXC', type(e).__name__, e)
for arg in [1845815, '0001845815']:
    try:
        print('deal_filings', repr(arg), '->', s.deal_filings(arg))
    except Exception as e:
        print('deal_filings', repr(arg), '-> EXC', type(e).__name__, e)
