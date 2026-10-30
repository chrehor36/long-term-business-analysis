# Return on capital employed: operating income after tax at 25.8% (2025 effective) against average
# (equity + long-term debt incl. current + line of credit - cash). USD thousands, from the filed statements.
oi={2020:7335,2021:6979,2022:7819,2023:12286,2024:9364,2025:7156}
eq={2020:32188,2021:30029,2022:44394,2023:48620,2024:47604,2025:86616}
debt={2020:115003,2021:113083,2022:108778,2023:105647+2315,2024:122444,2025:133698}
cash={2020:18033,2021:12637,2022:6561,2023:3087,2024:9047,2025:4080}
cap={y:eq[y]+debt[y]-cash[y] for y in eq}
out=[]
for y in range(2021,2026):
    avg=(cap[y]+cap[y-1])/2; r=oi[y]*(1-0.258)/avg
    out.append(r); print(y,'cap',cap[y],'avg',round(avg),'after-tax OI',round(oi[y]*0.742),'return %.1f%%'%(r*100))
print('mean %.1f%%'%(sum(out)/len(out)*100))
print('incremental 2020->2025: capital +%d, after-tax OI %+d'%(cap[2025]-cap[2020], round((oi[2025]-oi[2020])*0.742)))
