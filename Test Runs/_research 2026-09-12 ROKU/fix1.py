p=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-12 Run - ROKU Roku.md"
t=open(p,encoding='utf-8').read()
reps=[
 ("| 2017 | $250.8M | **+$29.3M** | $170.5M | 85.3% |",
  "| 2015 | $270.0M | **+$48.6M** | $41.2M | 45.9% |\n| 2016 | $293.9M | **+$44.1M** | $76.9M | 63.6% |\n| 2017 | $287.4M | **+$29.3M** | $170.5M | 85.3% |\n| 2018 | $325.6M | **+$35.8M** | $296.3M | 89.2% |"),
 ("| 2019 | $259.0M | **+$17.1M** | $478.1M | 96.5% |",
  "| 2019 | $388.1M | **+$17.1M** | $478.1M | 96.5% |"),
]
for a,b in reps:
    assert a in t, a[:40]
    t=t.replace(a,b)
open(p,'w',encoding='utf-8').write(t)
print('ok')
