P = "Test Runs/2026-10-17 Run - AMTM Amentum.md"
s = open(P, encoding="utf-8").read()
R = [
("is not owner cash and is not used (Part VII; Q4 below).", "is not owner cash and is not used (Part VII; the computation under Q7 below)."),
("with the CMS half's FY2024 filed for nine months only (see Q4), and", "with the CMS half's FY2024 filed for nine months only (see the computation under Q7), and"),
("distributions to minority partners ($24M, $6M, $35M) are on the statement and are taken at Q4. The run builds owner cash itself from the filed statements of both halves at Q4.",
 "distributions to minority partners ($24M, $6M, $35M) are on the statement and are taken in the computation. The run builds owner cash itself from the filed statements of both halves, in the computation under Q7."),
("carried $4,112M of debt against $415M of equity at 2023-09-29", "carried $4,112M of debt against $415M of total equity at 2023-09-29"),
("**VERDICT: IN.** The economics of the deciding part, a fee on cost for labour and engineering on government sites with almost no capital, gives",
 "**VERDICT: IN.** The economics of the deciding part, a fee on cost for labour and engineering on government sites with almost no capital, give"),
("The five-year window is not fully filed on the combined segment basis (the FY2021 and FY2022 predecessors reported differently), so the share",
 "The five-year window is not filed on the two-segment basis (Legacy Amentum reported \"one business segment\" in its FY2024 10-K; the FY2023 and FY2024 segment figures are the FY2025 10-K's recast, and FY2021 and FY2022 have none), so the share"),
]
for a, b in R:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
open(P, "w", encoding="utf-8").write(s)
print("ok")
