run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - NEGG Newegg Commerce.md"
r = open(run, encoding="utf-8").read()
def rep(a, b):
    global r
    assert a in r, a[:70]
    r = r.replace(a, b)
rep("(The prior stood at\nnine fires and seven failures; this is checked, not assumed.)",
    "(The brief put the prior at nine fires and seven failures; the register already read **ten and seven** after FLNC\nfired it on 2026-09-12. Checked, not assumed.)")
rep("The prior now stands at **ten fires and\n   seven failures.**", "The prior now stands at **eleven fires and\n   seven failures** (SHOP, MRVL, PAY, ARM, CALX, BE, ROKU, SWK, ACVA, FLNC, NEGG; QLYS, CRM, CORT, PLTR, INOD, ACMR, ALKT).")
rep("**The mechanism — a new, eighth shape: THE PENDULUM.**", "**The mechanism — the SIXTH shape (the borrowed balance sheet), in a third form: THE PENDULUM.**")
old = r[r.index("**How it differs from the seven named shapes.**"):r.index("**A secondary\nvector is recorded rather than named as a shape")]
new = """**Why the sixth shape, and why a named form rather than a seventh class.** The register was reconciled on
2026-09-13 at **six** shapes, with FLNC's treadmill folded in as a form of ACVA's borrowed balance sheet *"so the register
stays countable"*. Newegg belongs to the sixth on its defining fact — **payables of $160.3M carried 96% of $166.3M of
inventory at year-end**, liquidity lent by others that runs backwards when the business turns. **What makes it a distinct
form:** ACVA's lender was customers' money in transit, which scales with volume; FLNC's was customer deposits that must
be discharged by building. **Newegg's lender is its suppliers, and supplier credit is pro-cyclical to the same component
price that sets the margin** — the pendulum swings both lines against the owner on the same day. It is not ARM's (SBC is
large but not the whole deficit), BA's, SWK's, ORCL's or BE's. """
r = r.replace(old, new)
rep("\"[E2-49], nine fires and seven failures\" — **fired\n   (ten and seven)**", "\"[E2-49], nine fires and seven failures\" — **stale (the register read ten and seven after FLNC); fired\n   (eleven and seven)**")
rep("(`7c51b61`, `a9eaa6c`). Stale, harmless, recorded.", "(`7c51b61`, `a9eaa6c`). Stale, harmless, recorded. **And \"six to seven named survival shapes\"** — the register\n   was reconciled to **six** on 2026-09-13 (FLNC's treadmill is a form of ACVA's sixth); NEGG is recorded as the sixth's\n   third form, not a seventh.")
rep("Q4 OUT (gruesome; none of\n  the three strengths; THE PENDULUM, a real possibility,", "Q4 OUT (gruesome; none of\n  the three strengths; the sixth shape in the form THE PENDULUM, a real possibility,")
open(run, "w", encoding="utf-8").write(r); print("ok")
