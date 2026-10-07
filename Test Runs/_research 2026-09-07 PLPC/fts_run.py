import json, sys, time, re
import fts_lib as F

PLPC = "0000080035"

# substantive (non-ownership, non-fund) root forms. 11-K excluded: it is a
# benefit-plan schedule of investments, i.e. a holdings list, not prose.
SUBSTANTIVE = ",".join([
    "10-K", "10-Q", "8-K", "DEF 14A", "PRE 14A", "DEFM14A", "S-1", "S-4", "S-3",
    "424B3", "424B4", "424B5", "20-F", "40-F", "6-K", "10-12G", "10-12B",
    "SD", "CORRESP", "UPLOAD", "S-11", "F-1", "S-2", "SB-2", "10-K405",
])

CIKRE = re.compile(r"CIK (\d{10})")


def entities(phrase, forms, sd, ed):
    """Return (total, {cik: name}, other_count, status)."""
    st, url, j, b = F.fts(phrase, forms=forms, startdt=sd, enddt=ed)
    if j is None:
        return None, {}, None, (st, url, b[:500].decode("utf-8", "replace"))
    total = j["hits"]["total"]
    ents = {}
    agg = j.get("aggregations", {}).get("entity_filter", {})
    for bk in agg.get("buckets", []):
        m = CIKRE.search(bk["key"])
        if m:
            ents[m.group(1)] = (bk["key"], bk["doc_count"])
    return total, ents, agg.get("sum_other_doc_count", 0), None


def sweep(phrase, forms, y0=2001, y1=2026):
    """Enumerate entities over full history, splitting into year windows when
    the 30-bucket aggregation overflows."""
    allents = {}
    windows = []
    total, ents, other, err = entities(phrase, forms, "%d-01-01" % y0, "%d-12-31" % y1)
    if err:
        return None, {}, [("FULL", err)]
    grand = total
    if other == 0:
        allents.update(ents)
        windows.append(("%d-%d" % (y0, y1), total, len(ents), other))
    else:
        for y in range(y0, y1 + 1):
            t, e, o, er = entities(phrase, forms, "%d-01-01" % y, "%d-12-31" % y)
            if er:
                windows.append((str(y), er))
                continue
            if t["value"] == 0:
                continue
            windows.append((str(y), t, len(e), o))
            allents.update(e)
            if o:
                # split the year in half-years
                for a, bnd in [("01-01", "06-30"), ("07-01", "12-31")]:
                    t2, e2, o2, er2 = entities(phrase, forms, "%d-%s" % (y, a), "%d-%s" % (y, bnd))
                    if er2:
                        continue
                    allents.update(e2)
                    windows.append(("%d %s-%s" % (y, a, bnd), t2, len(e2), o2))
    return grand, allents, windows


def details(phrase, forms, cik, sd, ed):
    st, url, j, b = F.fts(phrase, forms=forms, startdt=sd, enddt=ed, ciks=cik)
    if j is None:
        return []
    out = []
    for h in j["hits"]["hits"]:
        s = h["_source"]
        out.append({"form": s.get("form"), "date": s.get("file_date"),
                    "adsh": s.get("adsh"), "file_type": s.get("file_type"),
                    "doc": h["_id"].split(":")[-1],
                    "sic": (s.get("sics") or [None])[0],
                    "name": (s.get("display_names") or [""])[0]})
    return sorted(out, key=lambda r: r["date"] or "", reverse=True)


SEARCHES = [
    ("A_plpc", "Preformed Line Products"),
    ("B_formedwire", "formed wire"),
    ("C_polelinehw", "pole line hardware"),
    ("D1_helicaldeadend", "helical dead-end"),
    ("D2_helicalproducts", "helical products"),
    ("E_spliceclosure", "splice closure"),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    report = {}
    for label, phrase in SEARCHES:
        if only and only != label:
            continue
        print("=" * 78)
        print(label, "|", phrase)
        rec = {"phrase": phrase}
        # all-forms headline count + form breakdown
        st, url, j, b = F.fts(phrase)
        rec["allforms_status"] = st
        rec["allforms_url"] = url
        if j is None:
            rec["error"] = b[:500].decode("utf-8", "replace")
            print("  ALLFORMS ERROR", st, url)
            print("  ", rec["error"])
            report[label] = rec
            continue
        open("fts_%s_allforms.json" % label, "wb").write(b)
        rec["allforms_total"] = j["hits"]["total"]
        rec["form_breakdown"] = [(x["key"], x["doc_count"]) for x in
                                 j["aggregations"]["form_filter"]["buckets"]]
        print("  all-forms total:", rec["allforms_total"])
        print("  forms:", rec["form_breakdown"][:16])

        grand, ents, windows = sweep(phrase, SUBSTANTIVE)
        rec["substantive_total"] = grand
        rec["windows"] = windows
        print("  substantive total:", grand, " entities found:", len(ents))
        rec["registrants"] = {}
        for cik, (name, n) in sorted(ents.items(), key=lambda kv: -kv[1][1]):
            if cik == PLPC:
                print("    [PLPC itself] %s n=%d" % (name, n))
                continue
            rows = details(phrase, SUBSTANTIVE, cik, "2001-01-01", "2026-12-31")
            rec["registrants"][cik] = {"name": name, "count": n, "filings": rows}
            print("    %-62s n=%-4d" % (name[:62], n))
            for r in rows[:12]:
                print("        %-10s %s %s  %s" % (r["form"], r["date"], r["adsh"], r["file_type"]))
            if len(rows) > 12:
                print("        ... %d more" % (len(rows) - 12))
        report[label] = rec
        json.dump(rec, open("fts_report_%s.json" % label, "w"), indent=1)
    json.dump(report, open("fts_report_%s.json" % (only or "ALL"), "w"), indent=1)
