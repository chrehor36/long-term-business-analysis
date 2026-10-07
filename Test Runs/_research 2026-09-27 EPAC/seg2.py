import re,glob
def flat(f):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\(\s*([\d,.]+)\s*\)',r'(\1)',s); s=re.sub(r'\$\s+','$',s); s=re.sub(r'\s+',' ',s)
    s=re.sub(r'(\d) %','\1%',s)
    return s
if __name__=="__main__":
 for f in sorted(glob.glob('filings/*_10-K_*.txt')):
    s=flat(f)
    print('=====',f)
    for m in re.finditer(r'(?i)(summary results of operations for the ([A-Za-z &]+?) segment|([A-Z][A-Za-z &]+) Segment(?: Results)?\s+\(in millions\))',s):
        print('  ',s[m.start():m.start()+420])
