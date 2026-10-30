import re,glob,sys
for f in sorted(glob.glob('filings/*_10-K_*.txt'))+sorted(glob.glob('filings/*_10-Q_*.txt')):
    if f<'filings/2017': continue
    L=open(f,encoding='utf-8').read().split('\n')
    for i,l in enumerate(L):
        if re.search(r'STATEMENTS? OF CASH FLOWS',l) and i+3<len(L) and 'in thousands' in (' '.join(L[i:i+3])).lower():
            print('=====',f,i)
            for x in L[i:i+60]:
                if re.search(r'Investing Activities|Financing',x) and 'Activities' in x and 'Financing' in x: break
                print(x[:220])
            break
