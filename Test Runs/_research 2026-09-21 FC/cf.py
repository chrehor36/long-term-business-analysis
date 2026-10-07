import re,sys
def cf(fn):
    t=open(fn,encoding='utf-8').read()
    i=None
    for m in re.finditer(r'(?i)CONSOLIDATED STATEMENTS? OF CASH FLOWS', t):
        seg=t[m.start():m.start()+12000]
        if 'OPERATING ACTIVITIES' in seg.upper() and 'INVESTING' in seg.upper():
            i=m.start(); break
    if i is None: return None
    seg=t[i:i+14000]
    seg=re.sub(r'[ \t]+',' ',seg)
    lines=[l.strip() for l in seg.split('\n')]
    out=[];buf=''
    for l in lines:
        if l=='|' or l=='':
            continue
        if re.match(r'^[\(\$\|\s\-\d,\.\)]+$',l):
            buf+=' '+l.replace('|','').strip()
        else:
            if buf: out.append(buf.strip()); buf=''
            out.append('LBL:'+l.replace('|','').strip())
    if buf: out.append(buf.strip())
    # merge label followed by numbers
    res=[];cur=None
    for x in out:
        if x.startswith('LBL:'):
            if cur: res.append(cur)
            cur=[x[4:],[]]
        elif cur is not None:
            cur[1].append(x)
    if cur: res.append(cur)
    return res
if __name__=='__main__':
    for lbl,nums in cf(sys.argv[1]):
        s=' '.join(nums)
        s=re.sub(r'\$','',s); s=re.sub(r'\s+',' ',s).strip()
        if s or True: print(f'{lbl[:60]:62s} | {s[:60]}')
