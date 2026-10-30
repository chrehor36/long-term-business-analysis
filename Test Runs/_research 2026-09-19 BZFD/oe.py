# Owner earnings from the FILED FACES, continuing operations ($M).
# FY2022-25: FY2024 10-K (FY2022) and FY2025 10-K (FY2023-25) faces, the basis without Complex and First We Feast.
# FY2021: FY2023 10-K face, the basis without Complex but with one month of First We Feast (the only continuing figure filed for FY2021).
# TTM to 2026-06-30 = FY2025 + H1 2026 - H1 2025 (Q2 2026 10-Q face).
# Grant value [E3-70]: RSUs granted x weighted grant-date FV + options granted x weighted FV (equity notes). FY2023: 12,360K RSUs x $0.56
# (pre-split units as filed), options 57K (immaterial). FY2024: 973K RSUs x $1.43 + 7,250K options x $2.19 (the FY2024 10-K's stated
# "weighted average fair value of stock options granted"). FY2025: 3,293K RSUs x $1.90, no options. FY2021-22: grant tables not read;
# the charge is used and said so.
Y    = ["FY2021*","FY2022","FY2023","FY2024","FY2025"]
ocf  = [-22.043, 6.982, -0.692, -5.686, -18.748]
sbc  = [23.565, 18.580, 5.282, 5.531, 5.820]
ppe  = [4.983, 5.424, 0.964, 0.691, 1.958]
sw   = [11.039, 12.361, 13.934, 12.078, 12.394]
da   = [22.093, 22.655, 20.333, 19.146, 15.828]
film = [0.0, 0.0, -1.707, -0.005, -18.525]      # "Film costs" working-capital line inside operating cash (studio outlay)
restr= [None, None, 6.761, 3.179, 3.492]         # restructuring excluded from Adjusted EBITDA (FY2025 10-K reconciliation)
grant= [None, None, 12.360*0.56, 0.973*1.43 + 7.250*2.19, 3.293*1.90]
rev  = [383.804, 325.777, 230.441, 189.887, 185.266]
rows=[]
print(f"{'year':8}{'OCF':>8}{'SBC':>7}{'grant':>7}{'capex+sw':>9}{'D&A':>7}{'film':>7}{'OEcapex':>9}{'OE D&A':>8}{'OEgrant':>9}{'OEexFilm':>9}{'OE/rev':>8}")
for i,y in enumerate(Y):
    cx = ppe[i]+sw[i]
    oc = ocf[i]-sbc[i]-cx
    od = ocf[i]-sbc[i]-da[i]
    g  = grant[i] if grant[i] is not None else sbc[i]
    og = ocf[i]-max(sbc[i], g)-cx
    ox = oc - film[i]
    rows.append((oc,od,og,ox))
    gs = f"{grant[i]:7.1f}" if grant[i] is not None else "    n/r"
    print(f"{y:8}{ocf[i]:8.1f}{sbc[i]:7.1f}{gs}{cx:9.1f}{da[i]:7.1f}{film[i]:7.1f}{oc:9.1f}{od:8.1f}{og:9.1f}{ox:9.1f}{oc/rev[i]*100:7.1f}%")
m=lambda L: sum(L)/len(L)
for lab, sl in [("5y FY2021*-25 (splice of two vintages)", slice(0,5)), ("4y FY2022-25 (one basis)", slice(1,5)), ("3y FY2023-25 (one basis)", slice(2,5))]:
    r=rows[sl]
    print(lab, "capex end %.1f | D&A end %.1f | larger of charge/grant %.1f | capex end without film outlay %.1f" % (
        m([x[0] for x in r]), m([x[1] for x in r]), m([x[2] for x in r]), m([x[3] for x in r])))
# TTM
t_ocf = -18.748 + (-5.300) - (-8.755); t_sbc = 5.820 + 3.102 - 2.703
t_cx = (1.958+12.394) + (0.313+6.890) - (0.834+6.349); t_da = 15.828 + 8.379 - 8.709
t_film = -18.525 + 0.691 - 0.0
oc = t_ocf-t_sbc-t_cx; od = t_ocf-t_sbc-t_da
print("TTM to 2026-06-30: OCF %.1f SBC %.1f capex+sw %.1f D&A %.1f film %.1f -> OE capex end %.1f, D&A end %.1f, capex end without film %.1f" % (t_ocf,t_sbc,t_cx,t_da,t_film,oc,od,oc-t_film))
print("H1 2026 alone: OCF -5.3, SBC 3.1, capex+sw 7.2 -> OE %.1f (half-year)" % (-5.300-3.102-7.203))
# cap and yields
cap = 1.12*83334733/1e6; cap2 = 1.12*85034733/1e6
print("cap cover %.1f ; cap after 2026-09-11 %.1f" % (cap, cap2))
for lab,v in [("5y capex end", m([x[0] for x in rows])),("4y capex end", m([x[0] for x in rows[1:]])),("3y capex end", m([x[0] for x in rows[2:]])),("3y D&A end", m([x[1] for x in rows[2:]])),("TTM capex end", oc)]:
    print("  %-14s OE %6.1f -> yield on cap %6.1f%%" % (lab, v, v/cap*100))
print("OE needed for 10%% on cap: %.1f ; for 5.34%%: %.1f" % (0.10*cap, 0.0534*cap))
