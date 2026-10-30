# -*- coding: utf-8 -*-
p = "Test Runs/2026-09-20 Run - CALM Cal-Maine Foods.md"
s = open(p, encoding="utf-8").read()
MARK = "\x00COMPUTHEAD\x00"
s = s.replace("COMPUTATION \u2014 NOT A CLEARANCE", MARK)
s = s.replace(" \u2014 ", " - ").replace("\u2014", "-")
s = s.replace("\u2212", "-")
s = s.replace(MARK, "COMPUTATION \u2014 NOT A CLEARANCE")
open(p, "w", encoding="utf-8").write(s)
print("em dashes left:", s.count("\u2014"), "| minus signs left:", s.count("\u2212"))
