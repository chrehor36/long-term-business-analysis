import re, sys, datetime, subprocess
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
FOLD = ROOT + r"\Test Runs\_research 2026-09-13 ABNB\fold"
Q = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
RL = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
SS = ROOT + r"\Screens\SURVIVAL SHAPES - index.md"
OL = ROOT + r"\Screens\_daily\OVERNIGHT LOG.md"
PAT = re.compile(r"^- \*\*[A-Z][A-Z.\-]* \(")

def read(p): return open(p, encoding="utf-8", newline="").read()
def write(p, s): open(p, "w", encoding="utf-8", newline="").write(s)

# ---------- 1. queue: register entry + strike ----------
q = read(Q)
nl = "\r\n" if "\r\n" in q else "\n"
lines = q.split(nl)
heads = [i for i, l in enumerate(lines) if l.startswith("## COMPLETED FROM THE QUEUE")]
h = heads[-1]
def count_entries(ls, h):
    return sum(1 for l in ls[h + 1:] if PAT.match(l))
before = count_entries(lines, h)
before_tickers = [l.split(" (")[0] for l in lines[h + 1:] if PAT.match(l)]
if any(t == "- **ABNB" for t in before_tickers):
    sys.exit("ABNB already registered - stop")
entry = read(FOLD + r"\register_entry.md").rstrip("\n").replace("\r\n", "\n").split("\n")
new = lines[:h + 1] + entry + lines[h + 1:]
# strike ABNB in the WAVE 5 table row (only that row)
hits = 0
for i, l in enumerate(new):
    if l.startswith("| capex unresolved [E5-20]: build (c) by hand from the filing |") and " ABNB," in l:
        new[i] = l.replace(" ABNB,", " ~~ABNB~~,", 1); hits += 1
if hits != 1:
    sys.exit(f"strike row hits={hits} - stop")
h2 = [i for i, l in enumerate(new) if l.startswith("## COMPLETED FROM THE QUEUE")][-1]
after = count_entries(new, h2)
after_tickers = [l.split(" (")[0] for l in new[h2 + 1:] if PAT.match(l)]
missing = [t for t in before_tickers if t not in after_tickers]
if after != before + 1 or missing:
    sys.exit(f"count check failed before={before} after={after} missing={missing}")
if len(new) != len(lines) + len(entry):
    sys.exit("line count mismatch - stop")
write(Q, nl.join(new))
print(f"queue: register {before} -> {after}; WAVE 5 strike ok")

# ---------- 2. reading list narrative ----------
rl = read(RL)
if "## UPDATE 2026-09-13 - ABNB:" in rl:
    sys.exit("narrative already present")
rnl = "\r\n" if "\r\n" in rl else "\n"
narr = read(FOLD + r"\narrative.md").replace("{{COUNT}}", str(after)).replace("\r\n", "\n")
narr = narr.replace("moves owner earnings ~8-18%, not the sign", "moves owner earnings ~6-18%, not the sign")
if not rl.endswith(rnl): rl += rnl
write(RL, rl + narr.replace("\n", rnl))
print("reading list: narrative appended")

# ---------- 3. survival shapes index ----------
ss = read(SS)
snl = "\r\n" if "\r\n" in ss else "\n"
sl = ss.split(snl)
if any("**The permit**" in l for l in sl):
    sys.exit("shape already present")
idx16 = [i for i, l in enumerate(sl) if l.startswith("| 16 |")]
if len(idx16) != 1:
    sys.exit("row 16 not found uniquely - stop")
row17 = ("| 17 | **The permit** *(proposed, pending the operator)* | ABNB (2026-09-13) | the product is a use of other people's property that "
         "governments permit, cap or withdraw market by market, while making the platform enforce the rules and collect, and pay, the tax | |")
sl.insert(idx16[0] + 1, row17)
ss2 = snl.join(sl)
old_open = "GFS proposed THE PATRON MBGL proposed THE DOWRY, and IHG proposed THE FLAG, without"
if old_open in ss2:
    ss2 = ss2.replace(old_open, "GFS proposed THE PATRON, MBGL proposed THE DOWRY, IHG proposed THE FLAG and ABNB proposed THE PERMIT, without")
    ss2 = ss2.replace("**All four are listed so briefs count correctly; neither is settled.**", "**All five are listed so briefs count correctly; none is settled.**")
else:
    print("WARNING: open-note wording changed; row added, note left as is")
write(SS, ss2)
print("shapes index: row 17 added")

# ---------- 4. overnight log ----------
ol = read(OL)
onl = "\r\n" if "\r\n" in ol else "\n"
clock = datetime.datetime.now().strftime("%H:%M")
line = (f"- 2026-09-13 {clock} EDT | ABNB | Q1 IN / Q2 OUT (on the business, on [E3-03] criterion 2 as its pricing sentence, [E2-44](1) and [E4-37] test it; "
        "Q3-Q6 recorded, not governing; capex tag gap real - capex moved into other investing from FY2023 and kept only in the MD&A FCF reconciliation, "
        "D&A above capex so the [E5-20] label was wrong; USD 30-yr 5.35% from the US Treasury; Class A 419,529,556 + Class B 170,056,126 = 589,585,682 "
        "(Class H 9.2M subsidiary-held, excluded); host funds in financing not OCF, owner earnings shown with fee float and customer-funds interest removed: "
        "5y 2021-25 $2.0-2.5bn, 5y incl. 2020 $0.8-1.2bn, TTM $3.1bn; SBC/OCF 49.6% since 2020, 31.7% ex-2020; hosts cross-list (Airbnb and Expedia 10-Ks), "
        "Booking.com homes ~2.1M -> ~3.9M listings; take rate flat 13.4-13.6% below Booking 14.5%, single 15.5% host fee take-rate-neutral; marketing 13.0% of "
        "revenue vs Booking 30.4% stated as the fact against; THE PERMIT proposed as seventeenth; COMPUTATION - NOT A CLEARANCE yield 1.1-3.1%, 6.7-8.8% "
        "perpetual growth needed for 10%, value ~$35-60 to $110-140, price above the range; FAIL at Q2) | US$170.19 (2026-09-11 close) | PASS | 5aa53be")
if not ol.endswith(onl): ol += onl
write(OL, ol + line + onl)
print("overnight log: line appended at", clock)
