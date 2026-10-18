# Pre-tax return on tangible capital = operating income / (total assets - goodwill - intangibles - cash), USD millions,
# from each filer's 10-K XBRL (facts.py logic) with WH trademarks and DAN from its filed balance sheets/notes.
import sys; sys.stdout.reconfigure(encoding="utf-8")
D = {
 # year: (OI, assets, goodwill, intangibles, cash)
 'WH':  {2019:(307,4533,1539,1395+551,94), 2021:(446,4269,1525,1202+473,171), 2022:(558,4123,1525,1232+374,161),
         2023:(503,4033,1525,1232+347,66), 2024:(495,4223,1525,1230+318,103), 2025:(402,4182,1525,1208+282,64)},
 'CHH': {2019:(319,1387,159,290,34), 2021:(429,1932,159,312,512), 2022:(479,2102,219,742,42), 2023:(375,2395,220,811,27),
         2024:(464,2531,220,884,40), 2025:(448,2918,306,1082,45)},
 'HLT': {2019:(1657,14957,5159,4877+780,538), 2023:(2225,15401,5052,4846+298,800), 2024:(2370,16522,5035,4990+429,1301),
         2025:(2693,16774,5081,5023+447,918)},
 'MAR': {2019:(1800,25051,9048,8641,225), 2021:(1750,25553,9073,8926,1393), 2022:(3462,24815,8872,8747,507),
         2023:(3864,25674,8886,9190,338), 2024:(3767,26182,8731,9488,396), 2025:(4141,27540,8907,10336,358)},
}
DAN = {2021:108, 2022:144, 2023:228, 2024:308, 2025:343}
for t, s in D.items():
    print(t, "  ".join(f"{y}: {oi/(a-g-i-c)*100:5.1f}% (cap {a-g-i-c:,})" for y,(oi,a,g,i,c) in sorted(s.items())))
print("WH ex DAN", "  ".join(f"{y}: {D['WH'][y][0]/(D['WH'][y][1]-D['WH'][y][2]-D['WH'][y][3]-D['WH'][y][4]-DAN[y])*100:5.1f}%" for y in DAN))
oi25x = 402+86+74
cap = 4182-1525-1490-64
print("WH 2025 OI before Revo charges and impairment", oi25x, f"{oi25x/cap*100:.1f}%", f"ex DAN {oi25x/(cap-343)*100:.1f}%")
