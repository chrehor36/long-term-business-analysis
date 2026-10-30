import re,sys,os,html as H
from fetch import get
def strip2(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'\s+',' ',s)
    s=re.sub(r'(?is)</(p|div|tr|h\d|li|table)>','\n',s)
    s=re.sub(r'(?is)<br[^>]*>','\n',s)
    s=re.sub(r'(?is)</t[dh]>','|',s)
    s=re.sub(r'(?s)<[^>]+>','',s)
    s=H.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    # compact table cells
    out=[]
    for line in s.split('\n'):
        if '|' in line:
            cells=[c.strip() for c in line.split('|')]
            cells=[c for c in cells if c not in ('','$',')','%')]
            line=' | '.join(cells)
            line=re.sub(r'\( ','(',line)
        line=line.strip()
        if line: out.append(line)
    return '\n'.join(out)
if __name__=='__main__':
    B='https://www.sec.gov/Archives/edgar/data/'
    for a in range(1,len(sys.argv),2):
        url,out=sys.argv[a],sys.argv[a+1]
        if not url.startswith('http'): url=B+url
        open(out,'w',encoding='utf-8').write(strip2(get(url))); print(out,os.path.getsize(out))
