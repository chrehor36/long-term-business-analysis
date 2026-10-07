import re, sys
for f in sys.argv[1:]:
    t = re.sub(r"[\s|﻿]+", " ", open(f, encoding="utf-8").read())
    print("=====", f)
    for key in ["Revenue by Business Segment", "Income from Construction Operations by Business Segment", "Income (Loss) from Construction Operations by Business Segment", "Income (loss) from construction operations by"]:
        for m in list(re.finditer(re.escape(key), t, re.I))[:1]:
            print("--", t[m.start(): m.start()+900])
