p='frag_q2.md'; s=open(p,encoding='utf-8').read()
R=[("| 36.8 | 35.2 (H1) |","| 36.8 | 35.5 (H1) |"),
("the H1 2026 ratio is $23,835 thousand on $67.9M of company restaurant sales in the 10-Q","the H1 2026 ratio is $23,835 thousand on $67,170 thousand of company restaurant sales in the 10-Q"),
("remove them and the 2019-2025 compound falls to about +31% (1.111 x 1.080 x 1.034 x 0.967), in the peers' range.","remove those three years and the remaining four (2019, 2021, 2022, 2025) compound to about +20% (1.111 x 1.080 x 1.034 x 0.967), below every peer's full seven-year figure."),
("The years that carry the record are the ones the screen row flags: 2020 (+21.4%, the delivery year) and 2023-2024","The years that carry the record are the ones the screen row flags: 2020 (+21.4%) and 2023-2024"),
("a wing brand with 16 sauces, national advertising and a network of 1,200 restaurants lost its comparable sales within four years","a wing brand with *\"16 signature sauces\"* and its own franchise system went from +6.5% franchised same-store sales (2012) to (2.7)% (2016) and was private within two years"),
("*\"Low-single digit decline\"*, 2026-04-28;","*\"Low-single digit decline\"*, 2026-04-29;"),
("Michael Skipworth has been chief executive since 2022 after serving as chief financial officer; the filings do not show the business depending on one person, and the ground here is not [E4-23].","The filings read do not show the business depending on one person (the chief executive's own letter speaks of *\"our brand partners\"* and the system), and the ground here is not [E4-23]."),
("the record reads as **wave-riding** (the delivery and digital shift: digital sales at 73.2% of system sales, the +21.4% of 2020)","the record reads as **wave-riding** (the shift to digital ordering: *\"Digital sales increased to 73.2% of system-wide sales\"*; the +21.4% of 2020)"),
("and KFC's US figures sit inside a global division in Yum's filings, so KFC is not in the row.","and no KFC US comparable-sales figure was found in the Yum filings read (KFC is reported as a global division), so KFC is not in the row."),
]
for a,b in R:
    assert a in s, a[:60]; s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
print('ok')
