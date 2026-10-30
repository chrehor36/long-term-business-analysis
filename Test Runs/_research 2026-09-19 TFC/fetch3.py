"""TFC - second fetch pass: 8-K exhibits (earnings releases, the TIH recast, the merger)."""
import sys, os, re, json, urllib.request, html, time

sys.path.insert(0, os.path.join("C:/Users/chreh/OneDrive/Documents/BRK", "tools"))
import sources
from fetch2 import get, totext, D, CIK


def dump_8k(acc, label):
    a = acc.replace("-", "")
    idx = json.loads(get(
        "https://www.sec.gov/Archives/edgar/data/%s/%s/index.json" % (CIK, a)
    ).decode())
    names = [i["name"] for i in idx["directory"]["item"]]
    print(acc, label, names)
    for n in names:
        if not (n.endswith(".htm") or n.endswith(".txt")):
            continue
        if n.startswith("R") or "xsl" in n.lower():
            continue
        raw = get("https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (CIK, a, n))
        out = os.path.join(D, "8K_%s__%s.txt" % (label, re.sub(r"[^A-Za-z0-9.]", "_", n)))
        open(out, "w", encoding="utf-8").write(totext(raw))
        print("  wrote", os.path.basename(out), len(raw))
        time.sleep(0.25)


if __name__ == "__main__":
    for acc, label in [
        ("0000092230-24-000029", "20240510_recast"),
        ("0000092230-26-000096", "20260717"),
        ("0000092230-26-000039", "20260417"),
        ("0000092230-26-000023", "20260121"),
        ("0000092230-26-000105", "20260915"),
        ("0000092230-26-000006", "20260112"),
    ]:
        try:
            dump_8k(acc, label)
        except Exception as e:
            print("FAIL", acc, e)
