rows="""2010 7.179 2.184 0.428 0.843
2011 7.226 1.245 0.378 0.915
2012 9.612 1.358 0.274 0.965
2013 9.494 0.998 0.627 0.940
2014 2.876 4.339 0.721 1.157
2015 13.285 1.538 0.859 1.253
2016 12.480 1.125 0.722 1.255
2017 10.412 1.128 0.582 1.297
2018 18.862 0.563 0.398 1.352
2019 11.156 0.447 0.162 1.212
2020 12.349 0.870 0.116 1.233
2021 11.766 0.551 0.116 1.183
2022 16.477 0.636 0.074 1.054
2023 19.837 0.626 0.258 1.135
2024 20.002 0.313 0.733 1.135
2025 25.240 0.225 0.993 0.957
2026 18.234 0.370 1.132 0.925"""
D={}
for l in rows.split('\n'):
    y,o,c,s,d=l.split(); D[int(y)]=(float(o),float(c),float(s),float(d))
print('FY  OCF  SBC  capex  D&A  OE_lo  OE_hi  SBC/OCF')
for y,(o,c,s,d) in D.items():
    print(y,o,s,c,d,round(o-s-max(c,d),3),round(o-s-min(c,d),3),f"{s/o*100:.1f}%")
def win(a,b):
    ys=[y for y in D if a<=y<=b]
    lo=sum(D[y][0]-D[y][2]-max(D[y][1],D[y][3]) for y in ys)/len(ys)
    hi=sum(D[y][0]-D[y][2]-min(D[y][1],D[y][3]) for y in ys)/len(ys)
    return len(ys),lo,hi
cap=386.4
for name,(a,b) in {'3y FY2024-26':(2024,2026),'5y FY2022-26':(2022,2026),'10y FY2017-26':(2017,2026),'12y FY2015-26 (10.8% royalty era)':(2015,2026),'17y FY2010-26':(2010,2026),'5y ex-FY2025 best year':(2021,2024),'5y prior FY2017-21':(2017,2021)}.items():
    n,lo,hi=win(a,b); print(f"{name:38s} n={n} OE ${lo:.2f}M to ${hi:.2f}M  yield {lo/cap*100:.2f}%-{hi/cap*100:.2f}%")
