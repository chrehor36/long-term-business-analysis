# arithmetic only on filed Pandora and Off-platform segment figures (US$ millions)
d = {2021:(2072,1140,743,530,1542),2022:(2098,1250,655,522,1576),2023:(2113,1292,638,524,1589),2024:(2146,1270,705,540,1606),2025:(2141,1308,670,526,1615)}
for y,(rev,rs,gp,sub,ad) in d.items():
    print(y, 'RS&R/rev %.1f%%' % (100*rs/rev), 'GP margin %.1f%%' % (100*gp/rev), 'sub share %.1f%%' % (100*sub/rev), 'ad share %.1f%%' % (100*ad/rev))
# TME computed
t = {2021:(7333,11467,31244),2022:(8699,12483,28339),2023:(12096,17325,27752),2024:(15227,21742,28401),2025:(17660,26726,32902)}
for y,(s,m,tot) in t.items():
    print('TME',y,'sub/online music %.1f%%' % (100*s/m), 'online music/total %.1f%%' % (100*m/tot))
