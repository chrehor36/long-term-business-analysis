# Owner earnings from the filed cash-flow faces (continuing operations), $M. CONVENTION per v4: OCF - SBC - (c).
# Sources: FY2021 10-K (FY2019-21), FY2023 10-K (FY2022-23), FY2025 10-K (FY2024-25), 10-Q Q2 2026 and Q2 2025 (H1).
Y   = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
OCF = [0.222, -27.934, 17.857, -3.418, 88.636, 65.415, 13.813]
CAPX= [4.122, 3.312, 11.844, 2.279, 3.419, 3.193, 2.777]
DA  = [4.002, 3.907, 4.913, 4.883, 4.362, 4.801, 5.887]
SBC = [2.797, 3.978, 3.237, 3.424, 5.394, 6.270, 4.131]
REV = [611.786, 603.713, 658.394, 640.949, 625.625, 654.693, 606.852]
cap = 13442332*31.64/1e6
def win(n):
    s=slice(len(Y)-n,len(Y)); m=lambda L: sum(L[s])/n
    return m(OCF), m(CAPX), m(DA), m(SBC)
print("cap $M", round(cap,1))
print("by year OCF-SBC-capex:", {y: round(o-s-c,1) for y,o,s,c in zip(Y,OCF,SBC,CAPX)})
print("by year OCF-SBC-DA:   ", {y: round(o-s-d,1) for y,o,s,d in zip(Y,OCF,SBC,DA)})
for n in (7,5,3):
    o,c,d,s=win(n); a=o-s-c; b=o-s-d
    print(f"{n}y FY{Y[-n]}-25: OCF {o:.1f} capex {c:.1f} DA {d:.1f} SBC {s:.1f} -> capex end {a:.1f} ({100*a/cap:.2f}%)  DA end {b:.1f} ({100*b/cap:.2f}%)")
# TTM to 2026-06-30
ocf_ttm = 13.813 - (-23.773) + 61.543; capx_ttm = 2.777 - 1.466 + 0.895; sbc_ttm = 4.131 - 2.008 + 2.596
da_ttm = 5.887 - 2.518 + 5.406
oe = ocf_ttm - capx_ttm - sbc_ttm
print(f"TTM OCF {ocf_ttm:.1f} capex {capx_ttm:.1f} SBC {sbc_ttm:.1f} DA {da_ttm:.1f} -> OE {oe:.1f} ({100*oe/cap:.1f}%); less IEEPA refund 36.5 -> {oe-36.5:.1f} ({100*(oe-36.5)/cap:.1f}%)")
# operating earnings check: operating profit after 25% tax + DA - capex - SBC? (not used; displayed only)
OP=[None,37.4,31.5,38.8,35.1,43.2,36.6]
print("5y mean operating profit", round(sum(OP[2:])/5,1), "after 25.8% tax", round(sum(OP[2:])/5*(1-0.258),1))
print("floor: OE needed for 10% on cap", round(0.10*cap,1))
print("SBC/OCF 5y", round(100*sum(SBC[2:])/sum(OCF[2:]),1))
