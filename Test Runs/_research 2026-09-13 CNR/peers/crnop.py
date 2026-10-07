import re, sys
sys.stdout.reconfigure(encoding="utf-8")
for acc in ["0001562762-26-000024","0001562762-25-000021","0001562762-24-000028","0001562762-23-000044"]:
    t = open(f"cache/CRN_{acc}.flat.txt", encoding="utf-8").read()
    t = re.sub(r"\s+", " ", t)
    print("==", acc)
    for m in re.finditer(r"(Australian Operations|U\.S\. Operations|United States) For Year Ended December 31, \(US\$ in thousands\) (\d{4}) (\d{4}) Change % (.{0,1200}?)Segment Adjusted EBITDA", t):
        body = m.group(4)
        def g(lbl):
            mm = re.search(re.escape(lbl) + r" ([\d.,()—-]+) ([\d.,()—-]+)", body)
            return mm.groups() if mm else None
        print(" ", m.group(1), m.group(2), m.group(3), "vol", g("olume (MMt)"), "price", g("Average realized price per Mt sold ($/Mt)"), "met", g("Average realized Met price per Mt sold ($/Mt)"), "metvol", g("Met sales volume (MMt)"), "mining", g("Mining costs per Mt sold ($/Mt)"), "opcost", g("Operating costs per Mt sold ($/Mt)"))
