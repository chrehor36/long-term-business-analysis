"""TFC competitor row, SECOND SOURCE: the FDIC Call Report, from the issuing authority.

The ACNB run of 2026-09-19 left a standing ruling for the banks still queued: "the competitor
row for a bank should be built from the FDIC Call Report FIRST - all insured institutions with
an office in the footprint, from the issuing authority, which is the only instrument that can
see the private and mutual banks an SEC row cannot."

For Truist that ruling behaves differently than it did for ACNB, and the difference is stated
in the run: ACNB's market is nine counties, where 56 insured institutions compete and most are
private or mutual. Truist Bank has 1,927 branches across 14 states and DC; at its scale the
banks it actually competes with for a corporate relationship or a multi-state deposit book are
all SEC registrants. What the Call Report adds here is therefore not the invisible private
competitor - it is a SECOND, INDEPENDENT measurement of the same nine banks from the regulator
that collects it, on the regulator's own uniform definitions, which no filer can choose.

Truist Bank CERT is looked up rather than assumed.
"""
import urllib.request, json, urllib.parse, time, os, sys

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
D = os.path.dirname(os.path.abspath(__file__))

# CERTs resolved by EXACT NAME filter and printed for the record.  DEFECT FOUND AND RECORDED:
# the FDIC API's `search=NAME:"..."` parameter is a FULL-TEXT match, not an exact one, so a
# first pass that searched "TRUIST BANK" and took max(ASSET) returned **JPMorgan Chase Bank
# (CERT 628)** and "CITIZENS BANK" returned **Wells Fargo Bank (CERT 3511)**.  Any row built
# that way is wrong and looks plausible.  `filters=NAME:"<exact legal name>" AND ACTIVE:1` is
# the correct call, and each CERT below was verified against the institution's city and state.
BANKS = {
    "TFC":  (9846,  "Truist Bank", "Charlotte NC"),
    "PNC":  (6384,  "PNC Bank, National Association", "Wilmington DE"),
    "USB":  (6548,  "U.S. Bank National Association", "Cincinnati OH"),
    "FITB": (6672,  "Fifth Third Bank, National Association", "Cincinnati OH"),
    "KEY":  (17534, "KeyBank National Association", "Cleveland OH"),
    "RF":   (12368, "Regions Bank", "Birmingham AL"),
    "CFG":  (57957, "Citizens Bank, National Association", "Providence RI"),
    "MTB":  (588,   "Manufacturers and Traders Trust Company", "Buffalo NY"),
    "HBAN": (6560,  "The Huntington National Bank", "Columbus OH"),
}

FIELDS = ("CERT,NAME,REPDTE,ASSET,DEP,DEPUNINS,DEPNIDOM,COREDEP,NIMY,INTEXPY,EEFFR,"
          "ROE,ROA,ROAPTX,EQ,LNLSDEPR,NTLNLSQ,LNATRESR,OFFDOM")
DATES = ["20211231", "20221231", "20231231", "20241231", "20251231", "20260630"]


def q(path, **kw):
    url = "https://banks.data.fdic.gov/api/" + path + "?" + urllib.parse.urlencode(kw)
    for _ in range(4):
        try:
            return json.loads(urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=90).read())
        except Exception as e:
            print("retry", e)
            time.sleep(3)
    raise SystemExit("failed " + url)


def find_cert(name):
    r = q("institutions", search='NAME:"%s"' % name,
          fields="CERT,NAME,CITY,STALP,ASSET,ACTIVE", limit="20",
          sort_by="ASSET", sort_order="DESC")
    rows = [x["data"] for x in r["data"] if x["data"].get("ACTIVE") in (1, "1", True)]
    return rows


if __name__ == "__main__":
    certs = {}
    for t, (cert, nm, where) in BANKS.items():
        r = q("institutions", filters='CERT:%d' % cert,
              fields="CERT,NAME,CITY,STALP,ASSET,ACTIVE", limit="5")
        d = r["data"][0]["data"]
        assert d["NAME"] == nm, (t, d["NAME"], nm)
        certs[t] = d
        print("%-5s CERT %-7s %-44s %s %s  assets $%s" % (
            t, d["CERT"], d["NAME"], d.get("CITY"), d.get("STALP"),
            f"{(d.get('ASSET') or 0):,}"))
        time.sleep(0.15)
    json.dump(certs, open(os.path.join(D, "fdic_certs.json"), "w"), indent=1)

    out = {}
    for t, c in certs.items():
        out[t] = {}
        for dt in DATES:
            r = q("financials", filters="REPDTE:%s" % dt, search="CERT:%s" % c["CERT"],
                  fields=FIELDS, limit="5")
            rows = [x["data"] for x in r["data"]]
            if not rows:
                print("  no data", t, dt)
                continue
            out[t][dt] = rows[0]
            time.sleep(0.2)
    json.dump(out, open(os.path.join(D, "fdic_peers.json"), "w"), indent=1)

    for metric, label in [("INTEXPY", "cost of funding earning assets %"),
                          ("NIMY", "net interest margin %"),
                          ("EEFFR", "efficiency ratio %"),
                          ("ROAPTX", "pre-tax return on assets %"),
                          ("ROE", "return on equity %"),
                          ("NTLNLSQ", "net charge-offs / loans, qtr ann. %")]:
        print("=" * 86)
        print(label, " - FDIC Call Report, the issuing authority's own uniform definition")
        print("%-6s" % "" + "".join("%11s" % d[:6] for d in DATES) + "     mean 21-25")
        for t in BANKS:
            if t not in out:
                continue
            vals = [out[t].get(d, {}).get(metric) for d in DATES]
            five = [v for v in vals[:5] if v is not None]
            print("%-6s" % t + "".join(
                ("%11.3f" % v) if v is not None else "        n/a" for v in vals)
                + (("   %10.3f" % (sum(five) / len(five))) if five else "        n/a"))
    print("=" * 86)
    print("UNINSURED DEPOSIT SHARE (DEPUNINS / DEP), Call Report")
    for t in BANKS:
        if t not in out:
            continue
        r = out[t].get("20251231", {})
        if r.get("DEP") and r.get("DEPUNINS") is not None:
            print("%-6s %6.1f%%   uninsured $%sM of $%sM" % (
                t, 100.0 * r["DEPUNINS"] / r["DEP"],
                f"{r['DEPUNINS']:,}", f"{r['DEP']:,}"))
