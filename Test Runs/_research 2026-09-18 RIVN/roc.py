# pre-tax return on capital employed net of cash: op income / (total assets - current liabilities - cash - ST investments), year-end
bs = {2023:(16778,2487,7857,1511),2024:(15410,2251,5294,2406),2025:(14864,3693,3579,2503)}
oi = {2023:-5739,2024:-4689,2025:-3585}
eq = {2022:13799,2023:9141,2024:6562,2025:4594}
for y,(a,cl,c,s) in bs.items():
    ce=a-cl-c-s; print(y,"capital employed",ce,"op loss",oi[y],f"ROCE {oi[y]/ce*100:.0f}%", "equity",eq[y], f"equity lost in year {eq[y]-eq[y-1]}")
print("cumulative accumulated deficit 2026-06-30: 28,200; APIC 33,305")
