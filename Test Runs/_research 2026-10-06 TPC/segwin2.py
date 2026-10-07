import re, sys
for f in sys.argv[1:]:
    t = re.sub(r"[\s|﻿]+", " ", open(f, encoding="utf-8").read())
    print("=====", f)
    for seg in ["Civil Segment", "Building Segment", "Specialty Contractors Segment"]:
        for m in re.finditer(seg + r" Revenue and (income|loss|income \(loss\)) ", t, re.I):
            print("--", t[m.start(): m.start()+330]); break
