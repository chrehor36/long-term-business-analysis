import re,html,sys
def conv(inp,out):
    s=open(inp,encoding='utf-8',errors='replace').read()
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br[^>]*>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|h[1-6]|li|table)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>','\t',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=s.replace('\u00a0',' ')
    s=re.sub(r'[ \t]*\t[ \t]*','\t',s)
    s=re.sub(r'[ ]+',' ',s)
    s=re.sub(r'\n[ \t]*\n+','\n',s)
    open(out,'w',encoding='utf-8').write(s)
    print(out,len(s))
if __name__=='__main__':
    conv(sys.argv[1],sys.argv[2])
