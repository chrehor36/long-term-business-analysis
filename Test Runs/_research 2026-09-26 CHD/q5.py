import json
rows=json.load(open('oe_rows.json'))
P=96.38; SH=237203907/1e6; CAP=P*SH; SOV=5.49
def mean(k,a,b): 
    ys=[str(y) for y in range(a,b+1)]; return sum(rows[y][k] for y in ys)/len(ys)
oe5c=mean('oe_capex',2021,2025); oe5d=mean('oe_dep',2021,2025); oe3d=mean('oe_dep',2023,2025); oe10c=mean('oe_capex',2016,2025)
g5=(mean('oe_capex',2021,2025)/mean('oe_capex',2016,2020))**(1/5)-1
g10=(mean('oe_capex',2021,2025)/mean('oe_capex',2011,2015))**(1/10)-1
print('cap',round(CAP,1))
print('5y OE capex/dep',round(oe5c,1),round(oe5d,1),'3y dep',round(oe3d,1),'10y capex',round(oe10c,1))
print('yields 5y %.2f%% %.2f%%'%(oe5c/CAP*100,oe5d/CAP*100))
print('OE growth 5y-mean to 5y-mean: 2016-20 to 2021-25 %.1f%%/yr; 2011-15 to 2021-25 %.1f%%/yr'%(g5*100,g10*100))
acq=sum(rows[str(y)]['acq'] for y in range(2016,2026)); print('acquisitions net 2016-25',round(acq,1))
# organic: volume and price/mix 2016-2025 compounded
org=(1.234*1.200)**(1/10)-1; print('organic sales 2016-25 %.2f%%/yr'%(org*100))
sh=(244.3/262.1)**(1/9)-1; print('diluted shares 2016-25 %.2f%%/yr'%(sh*100))
for lab,oe in [('5y capex',oe5c),('5y dep',oe5d),('3y dep',oe3d)]:
    y=oe/CAP*100
    print(lab,'yield %.2f'%y,'need at floor %.2f'%(10-y),'need at sovereign %.2f'%(SOV-y), 'exp g=0 %.2f g=4.0 %.2f g=4.7 %.2f'%(y,y+4.0,y+4.7))
def price(oe,g): return oe/(0.10-g)/SH
print('floor price 5y capex g=4.0: %.2f'%price(oe5c,0.040))
print('floor price 5y dep g=4.0: %.2f'%price(oe5d,0.040))
print('floor price 3y dep g=4.7: %.2f'%price(oe3d,0.047))
print('floor price 5y capex g=0: %.2f; 5y dep g=0 %.2f'%(price(oe5c,0),price(oe5d,0)))
print('sovereign-rate value g=0: %.2f-%.2f'%(oe5c/0.0549/SH,oe3d/0.0549/SH))
