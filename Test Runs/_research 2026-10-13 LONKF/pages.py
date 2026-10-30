import fitz,sys,re
f=sys.argv[1]; pat=sys.argv[2]; maxp=int(sys.argv[3]) if len(sys.argv)>3 else 2
d=fitz.open(f)
hits=[i for i in range(d.page_count) if re.search(pat,d[i].get_text())]
for i in hits[:maxp]:
    t=d[i].get_text()
    print('=====PAGE',i+1); print('|'.join(x.strip() for x in t.split('\n') if x.strip()))
