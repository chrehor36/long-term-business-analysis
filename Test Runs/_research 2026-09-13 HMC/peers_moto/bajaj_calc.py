# Bajaj Auto, INR crore. Standalone MD&A tables; consolidated Automotive segment note.
yrs = ["FY22", "FY23", "FY24", "FY25", "FY26"]
rev = [33145, 36428, 44685, 50010, 58732]          # "Total operating income" (FY22, FY24 ARs) / "Revenue from operations" (FY26 AR)
ebitda = [5389, 6551, 8825, 10101, 12019]
op = [5111, 6229, 8422, 9633, 11535]               # "Operating profit" = EBITDA - interest - D&A per tables
seg_rev = [33271.47, 36665.03, 44870.14, 49982.13, 60530.43]   # Automotive "External sales and other income"
seg_res = [6505.57, 6905.24, 8708.15, 8769.75, 12016.19]       # Automotive "Segment result"
seg_ast = [7512.66, 7552.14, 8837.56, 12061.70, 30161.47]      # Automotive "Segment assets" (excl. investment in associate)
seg_tot = [11576.45, 12436.17, 13657.96, 15749.97, 30330.65]   # Automotive "Total assets" (incl. investment in associate)
for i, y in enumerate(yrs):
    print(f"{y}: SA EBITDA {ebitda[i]:,}/{rev[i]:,} = {100*ebitda[i]/rev[i]:.1f}% | SA Operating profit {op[i]:,}/{rev[i]:,} = {100*op[i]/rev[i]:.1f}%"
          f" | Cons Auto seg result {seg_res[i]:,.2f}/{seg_rev[i]:,.2f} = {100*seg_res[i]/seg_rev[i]:.1f}%"
          f" | /seg assets {100*seg_res[i]/seg_ast[i]:.1f}% | /auto total assets {100*seg_res[i]/seg_tot[i]:.1f}%")
