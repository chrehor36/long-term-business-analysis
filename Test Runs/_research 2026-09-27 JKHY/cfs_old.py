import re,sys,json
sys.stdout.reconfigure(encoding='utf-8')
def parse(fy):
    s=open(f'tenk/tenk_{fy}.txt',encoding='utf-8').read()
    idx=[m.start() for m in re.finditer(r'(?i)CONSOLIDATED STATEMENTS? OF CASH FLOWS',s)]
    # choose the occurrence followed by 'OPERATING ACTIVITIES' within 3000 chars
    for i in idx:
        if re.search(r'(?i)OPERATING ACTIVITIES',s[i:i+3000]): start=i
    t=s[start:start+12000]
    end=re.search(r'(?i)see (the )?(accompanying )?notes',t)
    t=t[:end.start()] if end else t
    toks=re.split(r'[|\n]',t)
    rows=[];cur=None
    for tok in toks:
        tok=tok.strip()
        if not tok or tok=='$': continue
        m=re.fullmatch(r'\(?\s*\$?\s*([\d,]+)\s*\)?',tok)
        if m and cur is not None:
            v=float(m.group(1).replace(',',''))
            if tok.startswith('('): v=-v
            cur[1].append(v)
        elif re.fullmatch(r'-+|—|–',tok) and cur is not None:
            cur[1].append(0.0)
        elif re.search(r'[A-Za-z]',tok):
            if cur is not None and not cur[1] and len(cur[0])<120: cur=[cur[0]+' '+tok,[]]; rows[-1]=cur
            else: cur=[tok,[]]; rows.append(cur)
    return rows
if __name__=='__main__':
    for fy in sys.argv[1:]:
        print('=====',fy)
        for r in parse(fy):
            if r[1]: print(f'{r[0][:70]:70s}', r[1])
