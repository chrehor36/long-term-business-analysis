import re
_cache={}
def lines(f):
    if f not in _cache:
        _cache[f]=open(f,encoding="utf-8").read().split("\n")
    return _cache[f]
def norm(s): return re.sub(r"\s+"," ",s).strip()
CELL=re.compile(r"^(\||\$|%|%\)|\)%|\)|-|\(?\s*-?[\d,]+(\.\d+)?%?)?$")
def is_cell(s): return bool(CELL.match(s.strip()))
def join(f,a,b):  # inclusive
    return norm(" ".join(lines(f)[a:b+1]))
def row_end(f,s,stop_year=False):
    L=lines(f); j=s+1
    while j<len(L) and is_cell(L[j]) and not (stop_year and re.match(r"^\s*\d{4}\s*$",L[j])):
        j+=1
    # trim trailing
    return j-1
def row(f,s,stop_year=False):
    e=row_end(f,s,stop_year)
    return join(f,s,e),s,e
def find(f,pat,start=0,end=None):
    L=lines(f); end=end or len(L)
    for i in range(start,end):
        if re.search(pat,L[i]): return i
    raise ValueError(f"{pat} not found in {f} from {start}")
def q(text,f,a,b=None):
    src=f"Source: {f} line {a}" + (f" (row continues to line {b})" if b is not None and b!=a else "")
    return f"> {text}\n{src}\n"
def qrow(f,s,stop_year=False):
    t,a,b=row(f,s,stop_year); return q(t,f,a,b)
def qjoin(f,a,b): return q(join(f,a,b),f,a,b)
def sent(f,i,pat):
    L=lines(f); m=re.search(pat,L[i])
    if not m: raise ValueError(f"sentence {pat!r} not on {f} line {i}")
    return q(norm(m.group(0)),f,i)
def comp_table(f,h):
    """component table from header line h through Net Sales increase/decrease row"""
    L=lines(f); out=[]
    j=h+1
    while is_cell(L[j]) or re.match(r"^\s*(December 31, \d{4})\s*$",L[j]): j+=1
    out.append(q(join(f,h,j-1),f,h,j-1))
    while True:
        t,a,b=row(f,j); out.append(q(t,f,a,b))
        if re.match(r"\s*Net Sales (increase|decrease)",L[j]): break
        j=b+1
    return "".join(out)
