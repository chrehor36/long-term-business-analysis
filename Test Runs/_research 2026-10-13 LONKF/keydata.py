import fitz,sys,re
for f in sys.argv[1:]:
    d=fitz.open(f)
    for i in range(2,min(d.page_count,25)):
        t=d[i].get_text()
        if re.search('主要会计数据和财务指标',t) and '营业收入' in (t+d[i+1].get_text()) and '目录' not in t:
            s='|'.join(x.strip() for x in (t+d[i+1].get_text()).split('\n') if x.strip())
            k=s.find('主要会计数据和财务指标')
            print('#####',f,'page',i+1); print(s[k:k+2600])
            break
