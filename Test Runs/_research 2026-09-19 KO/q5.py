S=4302.549243; P=88.25; cap=P*S
print("cap $M", round(cap))
oes={"default adj 5y capex":9983,"adj 5y D&A":10565,"adj 5y D&A + look-through":11427,"as filed 5y capex":7813,"TTM adj capex":13798}
for k,oe in oes.items():
    y=oe/cap
    g_bond=(0.0534*cap-oe)/(cap+oe); g_floor=(0.10*cap-oe)/(cap+oe)
    print(f"{k}: OE {oe} yield {100*y:.2f}% pts over 5.34: {100*(y-0.0534):+.2f} | g to match bond {100*g_bond:.2f}% | g to reach 10% floor {100*g_floor:.2f}%")
for g in (0.041,0.043,0.061):
    for oe in (9983,11427):
        v=oe*(1+g)/(0.10-g)
        print(f"value at 10% floor, OE {oe}, g {100*g:.1f}%: ${v/1000:,.0f}bn = ${v/S:,.2f}/sh ; expectancy at today's price {100*(oe*(1+g)/cap+g):.1f}%")
print("OE growth 2019-25 capex-end adj", (10448/8216)**(1/6)-1, "OI before charges 2019-25", (15023/10544)**(1/6)-1, "revenue 2019-25", (47941/37266)**(1/6)-1)
