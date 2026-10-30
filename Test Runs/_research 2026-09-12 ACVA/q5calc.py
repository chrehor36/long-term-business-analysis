cap=169824232*10.41/1e6
print("cap",cap)
for name,oe in [("5y D&A-ex",-72.316),("5y capex",-87.207),("3y D&A-ex",-64.598),("TTM D&A-ex",-47.673),("TTM capex",-63.989),("worst 3y capex",-93.899),("best 3y D&A-ex",-57.830),("as filed best 3y DAex",-5.986),("as filed 5y capex",-52.936),("screen bottom",-51.947),("screen top",-44.234)]:
    y=oe/cap; print(f"{name}: {oe:.1f} yield {y:.2%} vs 5.35: {(y-0.0535)*100:.2f} pts")
print("needed at 5.35%", 0.0535*cap, "at 10%", 0.10*cap)
print("share of FY26 rev guide mid 850", 0.10*cap/850)
for m in (0.166,0.257,0.142,0.238):
    print("margin",m,"revenue needed",0.10*cap/m, "x guide", 0.10*cap/m/850)
print("per car", 0.10*cap*1e6/829276)
rtf=115.3e6/169824232; print("reverse fee/share", rtf, "unaffected+fee", 7.26+rtf, "downside", (7.26+rtf)/10.41-1, 7.26/10.41-1)
print("ACV fee/share", 57.7e6/169824232)
own_cash=242.259-194.021; ev=cap+80.0-own_cash; print("EV (cap + revolver - own cash)", ev, "EV incl warehouse", cap+205-own_cash)
print("margin TTM capex", -63.989/(759.606-376.4+418.133))
print("deal value to fully diluted", (169824232+10359498+2364836)*10.5/1e6)
