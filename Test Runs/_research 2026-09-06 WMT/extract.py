import os,re,json
D=os.path.dirname(os.path.abspath(__file__))
order=['q4fy18','q1fy19','q2fy19','q3fy19','q4fy19','q1fy20','q2fy20','q3fy20','q4fy20',
'q1fy21','q2fy21','q3fy21','q4fy21','q1fy22','q2fy22','q3fy22','q4fy22','q1fy23','q2fy23',
'q3fy23','q4fy23','q1fy24','q2fy24','q3fy24','q4fy24','q1fy25','q2fy25','q3fy25','q4fy25',
'q1fy26','q2fy26','q3fy26','q4fy26','q1fy27','q2fy27']

def cells(l):
    return [c.strip() for c in l.split('|') if c.strip()]

def vals_for(lines,i):
    """label line i; values on same line after label, else on next non-empty line"""
    c=cells(lines[i])
    v=[x for x in c[1:] if re.match(r'^[~<>(-]?\s*[\d.]|^NP|^flat|^N/A|^--|^bps', x, re.I) or 'bps' in x or '%' in x]
    if len(v)>=2: return v, i
    for j in range(i+1, min(i+4,len(lines))):
        c2=cells(lines[j])
        if c2 and not re.match(r'^[A-Za-z]', c2[0]):
            return c2, j
        if c2 and re.match(r'^(flat|NP|~|<|>|\(|-?\d)', c2[0], re.I):
            return c2, j
    return None, i

out={}
for q in order:
    p=os.path.join(D,f"8k-{q}-ex991.txt")
    lines=open(p,encoding='utf-8',errors='replace').read().split('\n')
    blocks=[]
    for i,l in enumerate(lines):
        s=l.strip()
        if re.match(r'^\|?\s*(Transactions|Traffic)\s*\d?\s*\|', s, re.I) or \
           re.match(r'^\|?\s*(Transactions|Traffic)\s*\d?\s*$', s, re.I):
            # walk back for comp sales + header + net sales
            comp=None; hdr=None; ns=None
            for j in range(i-1, max(-1,i-20), -1):
                sj=lines[j].strip()
                if comp is None and re.match(r'^\|?\s*Comp(arable)? [Ss]ales \(ex\. fuel\)', sj, re.I):
                    comp=vals_for(lines,j)[0]
                if ns is None and re.match(r'^\|?\s*Net sales\s*\|', sj, re.I):
                    ns=cells(sj)
                if hdr is None and re.search(r'(Walmart U\.?S\.?|Sam.{1,3}s Club|International)', sj) and 'Comp' not in sj:
                    hdr=sj[:60]
            tr=vals_for(lines,i)[0]
            tk=None; ec=None
            for j in range(i+1, min(i+8,len(lines))):
                sj=lines[j].strip()
                if tk is None and re.match(r'^\|?\s*(Average [Tt]icket|Ticket)\s*\d?\s*(\||$)', sj, re.I):
                    tk=vals_for(lines,j)[0]
                if ec is None and re.match(r'^\|?\s*eCommerce contribution', sj, re.I):
                    ec=vals_for(lines,j)[0]
            blocks.append({'line':i,'hdr':hdr,'netsales':ns,'comp':comp,'trans':tr,'ticket':tk,'ecomm':ec})
    out[q]=blocks
    print("="*72); print(q, len(blocks),"blocks")
    for b in blocks:
        print("  hdr:",b['hdr'])
        print("   NS  ",b['netsales'])
        print("   COMP",b['comp'])
        print("   TRAN",b['trans'])
        print("   TICK",b['ticket'])
        print("   ECOM",b['ecomm'])
json.dump(out,open(os.path.join(D,'extract.json'),'w'),indent=1)
