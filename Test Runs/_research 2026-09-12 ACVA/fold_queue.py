R = "C:/Users/chreh/OneDrive/Documents/BRK/"
D = R + "Test Runs/_research 2026-09-12 ACVA/"
p = R + "Screens/WATCHLIST RUN QUEUE.md"
s = open(p, encoding="utf-8").read()

anchor = "## COMPLETED FROM THE QUEUE\n"
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + open(D + "fold_entry.md", encoding="utf-8").read())

old = "~~SWK~~, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ~~ROKU~~, RGTI, ~~ORCL~~, ~~BA~~, ~~ACMR~~, ~~ALKT~~, ~~INTC~~, ACVA, NEGG, FLNC"
assert s.count(old) == 1
s = s.replace(old, old.replace(" ACVA,", " ~~ACVA~~,"))

old2 = ("Read every one of them as unlabelled. *(ALKT RUN 2026-09-12: struck - closed at Q2 on the business; "
        "the SIGN CHANGE it carried was operating cash, not owner earnings.)*")
assert s.count(old2) == 1
s = s.replace(old2, old2 + " *(ACVA RUN 2026-09-12: struck - closed at Q2 on the business; its SIGN CHANGE was operating "
              "cash moved by SELLERS' FLOAT, and ACV is a pending Copart acquisition at $10.50. The SIGN CHANGE sub-class "
              "is now fully run: all three found the label did not describe owner earnings.)*")

old3 = "the label did not describe owner earnings: wrong in direction at ACMR, wrong in object at ALKT.**"
assert s.count(old3) == 1
s = s.replace(old3, old3 + open(D + "fold_label.md", encoding="utf-8").read())

open(p, "w", encoding="utf-8").write(s)
print("queue folded")
