import re,sys
txt=open(sys.argv[1],encoding='utf-8').read().split('\n')
endyear=int(sys.argv[2])
# find titles preceding "Net Incurred Loss and Allocated"
res=[]
for i,l in enumerate(txt):
    if l.strip().startswith('Net Incurred Loss and Allocated Loss Adjustment Expenses') or l.strip().startswith('Incurred Loss and Allocated'):
        # title: search backward for a line containing '—' and 'tail' or segment name
        t=''
        for j in range(i-1,max(i-15,0),-1):
            if re.search(r'(Insurance|Reinsurance).*(—|-).*', txt[j]) and len(txt[j])<140:
                t=txt[j].strip(); break
        rows={}
        k=i+1
        while k<i+40:
            m=re.match(r'^\s*(\d{4}) \|(.*)$',txt[k])
            if m and m.group(1)!='Accident':
                y=int(m.group(1))
                nums=[float(x.replace(',','').replace('(','-').replace(')','')) for x in re.findall(r'\(?[\d,]+\)?',m.group(2))]
                n=endyear-y+1
                if len(nums)>=n: rows[y]=nums[:n]
            if txt[k].strip().startswith('Total'):
                break
            k+=1
        res.append((t,rows))
for t,rows in res:
    print('##',t)
    tot_i=tot_l=0
    for y in sorted(rows):
        r=rows[y]; d=r[-1]-r[0]
        print(y, f"initial {r[0]:9.0f} latest {r[-1]:9.0f} dev {d:8.0f} ({d/r[0]*100:5.1f}%)")
        tot_i+=r[0]; tot_l+=r[-1]
    if rows: print('sum', tot_i, tot_l, tot_l-tot_i)
