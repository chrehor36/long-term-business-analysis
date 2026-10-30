import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
f='Screens/SURVIVAL SHAPES - index.md'
s=open(f,encoding='utf-8').read()
rows=re.findall(r'^\| (\d+) \|',s,flags=re.M)
print('rows',len(rows),'max',max(map(int,rows)))
L=s.split('\n')
i=[k for k,x in enumerate(L) if x.startswith('| 19 | **The shelf**')]; assert len(i)==1
row=L[i[0]]; assert row.endswith(' |') and 'CHD' not in row
inst="; CHD (2026-09-26, the mechanism, Q4 opened: owned brands, the route to the buyer rented from four retailers taking 44% of sales, Walmart 23%, with private label named by the filer in stain fighters, pregnancy tests and oral analgesics; VitaFusion bought for $652.3M and sold for $160.3M after *\"significant product competition coming from new category entrants, including private label\"*; a real possibility that erodes the owners' return, not a solvency death; #24 THE BOUGHT AVERAGE as a feature: the premium mix and the gross-margin step from 29.7% to 43.7% were bought, and purchased goodwill and intangibles are 89% of operating capital)"
L[i[0]]=row[:-2]+inst+' |'
note="\n*Dated note, 2026-09-26 (the CHD fold, wave 7 name 59): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** The table was counted with a line-start regex immediately before writing: **"+str(len(rows))+" rows, maximum number "+str(max(map(int,rows)))+"**. Church & Dwight cleared Q1-Q4 (Q2 NARROW), so **Q4 was opened and the run names a death**: **#19 THE SHELF as the mechanism, with #24 THE BOUGHT AVERAGE as a feature**, likelihood *a real possibility*, not a solvency death. **CHD is therefore entered in #19's instances column**, unlike the Q2-closed wave 7 names, whose signatures stay out of the columns. Recorded, not fixed: **the PG run of 2026-09-25 also named #19 as its mechanism at an opened Q4 (with #11 as a feature) and is not in the column**; its fold did not update this index, and this fold does not write another run's entry.*\n"
out='\n'.join(L)
if not out.endswith('\n'): out+='\n'
out+=note
open(f,'w',encoding='utf-8',newline='\n').write(out)
rows2=re.findall(r'^\| (\d+) \|',out,flags=re.M); print('after rows',len(rows2))
