# BZFD unit series and row figures, $M, continuing operations on the FY2024/FY2025 10-K basis (FY2022-25), H1 from 10-Qs.
Y=["FY2022","FY2023","FY2024","FY2025"]
rev=[325.777,230.441,189.887,185.266]; adv=[165.356,113.642,94.362,91.685]; con=[109.286,66.748,33.875,37.045]; com=[51.135,50.051,61.650,56.536]
ts=[314.556,306.261,297.903,276.498]   # Time Spent, millions of hours (FY2024 10-K for FY2022-24; FY2025 10-K)
ocf=[6.982,-0.692,-5.686,-18.748]; sbc=[18.580,5.282,5.531,5.820]; cap=[5.424+12.361,0.964+13.934,0.691+12.078,1.958+12.394]
for i,y in enumerate(Y):
    oe=ocf[i]-sbc[i]-cap[i]
    print(f"{y} rev {rev[i]:.1f} ts {ts[i]:.1f}M h  rev/h ${rev[i]/ts[i]:.3f}  adv/h ${adv[i]/ts[i]:.3f}  OE {oe:.1f} OE/rev {oe/rev[i]*100:.1f}%")
print("H1 2026 rev/h %.3f adv/h %.3f ; H1 2025 rev/h %.3f adv/h %.3f" % (67.860/122.918, 34.445/122.918, 82.415/137.722, 43.976/137.722))
oes=[ocf[i]-sbc[i]-cap[i] for i in range(4)]
print("4y OE/rev %.1f%%  rev CAGR FY2022-25 %.1f%%  TTM rev %.1f" % (sum(oes)/sum(rev)*100, ((rev[3]/rev[0])**(1/3)-1)*100, 185.266+67.860-82.415))
print("Time Spent FY2022-25 %.1f%% ; adv per hour %.1f%%" % ((ts[3]/ts[0]-1)*100, ((adv[3]/ts[3])/(adv[0]/ts[0])-1)*100))
# peers
print("PPLI Digital CAGR 2023-25 %.1f%%, Digital adj EBITDA margin 2025 %.1f%%, 3y %.1f%%" % (((1108.391/892.426)**0.5-1)*100, 307.213/1108.391*100, (307.213+289.393+242.969)/(1108.391+1004.417+892.426)*100))
zr25=356.596+183.558+402.353; zr24=361.882+180.276+362.408; zr23=330.557+168.821+361.923
print("ZD Digital Media rev 2023 %.1f 2025 %.1f CAGR %.1f%%; seg op inc 2025 %.1f = %.1f%%" % (zr23, zr25, ((zr25/zr23)**0.5-1)*100, 9.302+53.035+89.384, (9.302+53.035+89.384)/zr25*100))
print("BZFD adj EBITDA 2025 8.797 / rev = %.1f%% ; 3y (2023-25) %.1f%%" % (8.797/185.266*100, (8.797+5.451-11.645)/(185.266+189.887+230.441)*100))
