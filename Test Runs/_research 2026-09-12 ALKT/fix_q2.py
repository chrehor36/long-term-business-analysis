import io
p="q1q2.md"; s=io.open(p,encoding="utf-8").read()
reps=[
("every 10-K from FY2021 to FY2025 and in the S-1 era language, and US banks","every 10-K from FY2021 to FY2025, and US banks"),
("−14.6% → −10.3% (FY2025)**; gross margin","−14.6% → −9.5% (FY2025)**; gross margin"),
("almost exactly Alkami's FY2025 position ($443.6M, −10.3%)","almost exactly Alkami's FY2025 position ($443.6M, −9.5%)"),
("with a positive GAAP operating margin (5.0%) for the first time.","with a positive GAAP operating margin (5.0%), its first positive year of the six computed (FY2020-FY2025)."),
("**$30.3M of capex\nand capitalised software**","**$31.0M of capex\nand capitalised software**"),
("(EDGAR full-text search for \"Alkami\" in 10-K forms\n  since 2024-06-01: 24 hits, of which the Q2 Holdings 10-Ks for FY2024 and FY2025 are the competitor\n  documents; the rest are Alkami's own filings and director biographies; output `fts_out.txt`.)",
 "(EDGAR full-text search for \"Alkami\" in 10-K forms\n  since 2024-06-01: 24 hits — the Q2 Holdings 10-Ks for FY2024 and FY2025, eighteen documents in Alkami's\n  own 10-Ks, and four documents of three other filers (Matterport 10-K, two NCR Voyix 10-K exhibits,\n  Clearwater Analytics 10-K/As) **that were not opened**; output `fts_out.txt`. The hit list is a prompt,\n  not the naming test; the Q2 Holdings sentence above was read in the document.)"),
("| **owner-earnings margin, latest FY** | **−10.3% ← last** |","| **owner-earnings margin, latest FY** | **−9.5% ← last** |"),
("| **owner-earnings margin, 5 years cumulative** | **−21.7% ← last** |","| **owner-earnings margin, 5 years cumulative** | **−21.4% ← last** |"),
("*n/r = cost of revenue not tagged in a resolving form for Fiserv. ALKT's latest-FY owner-earnings margin\nuses the cash-flow SBC add-back ($76,188k); on the tagged P&L charge ($80,098k, which includes $3.9M of\nMANTL awards settled in cash and already inside operating cash) it is −10.3% to one decimal either way.",
 "*n/r = cost of revenue not tagged in a resolving form for Fiserv. ALKT's owner-earnings cells use the\nfiled cash-flow SBC add-back ($76,188k for FY2025). **The screen's max-rule picks the tagged P&L charge\n($80,098k), which includes $3.9M of MANTL awards settled in cash and already deducted inside operating cash\n— a double count** — and on it the cells read −10.3% (latest) and −21.7% (cumulative). Last either way."),
("Jack Henry at a 25.0% operating margin","Jack Henry at a 25.0% operating margin"),
("cumulative measure (Q2 Holdings −1.4%, nCino −6.6%, Alkami −21.7%)","cumulative measure (Q2 Holdings −1.4%, nCino −6.6%, Alkami −21.4%)"),
("the remaining\nMK intangible and\ncapitalised software assets","the remaining MK intangible and capitalised software assets"),
("written off as having *\"no future economic benefit.\"* **MANTL (account\nopening and loan origination, $375.5M) replaced MK (loan decisioning, ~$20M) in the product line within\nfour years.**",
 "written off because they *\"would not have future economic benefit\"* (10-K FY2025 note 16). **The filing\nties the write-off of the 2021 purchase (~$20M, decisioning) to the 2025 one ($375.5M, onboarding, account\nopening and loan origination) within four years.**"),
("- Primary moat metric and trend: **owner-earnings margin −10.3% (last in the row) and improving;","- Primary moat metric and trend: **owner-earnings margin −9.5% (last in the row) and improving;"),
("- **Unavailable, and the limit stated rather than papered:** **Candescent** (NCR Voyix's former digital\n  banking business, now privately owned), **CSI**, **Lumin Digital**, **Finastra** and **Bottomline** are\n  private; **Backbase** is a private Dutch company. **FIS** is a registrant and was not computed.",
 "- **Unavailable, and the limit stated rather than papered:** **Candescent, CSI, Lumin Digital, Backbase,\n  Finastra and Bottomline** — no entity under any of those names appears in the SEC ticker map\n  (`peers/private_check.txt`), so no periodic filing was available to compute; their ownership is not\n  asserted here. **FIS** is a registrant and was not computed."),
]
for a,b in reps:
    if a not in s: print("MISSING:", a[:80]); continue
    s=s.replace(a,b)
io.open(p,"w",encoding="utf-8").write(s)
