#!/usr/bin/env python3
"""Pull the primary documents for the ANF run and strip to plain text for reading.
Rung: SEC EDGAR primary documents (evidence ladder rung 2)."""
import os, re, time, html as H
import urllib.request

OUT = r"c:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-02 ANF"
UA = {"User-Agent": "Long-Term Business Analysis chrehor36@gmail.com"}
BASE = "https://www.sec.gov/Archives/edgar/data/1018840"

DOCS = [
    ("0001018840-26-000012", "anf-20260131.htm", "10K_FY2025"),
    ("0001018840-26-000036", "anf-20260502.htm", "10Q_Q1FY2026"),
    ("0001018840-26-000022", "anf-20260420.htm", "DEF14A_2026"),
    ("0001018840-25-000013", "anf-20250201.htm", "10K_FY2024"),
    ("0001018840-23-000011", "anf-20230128.htm", "10K_FY2022"),
    ("0001018840-22-000011", "anf-20220129.htm", "10K_FY2021"),
    ("0001018840-20-000021", "a201910-k.htm", "10K_FY2019"),
    ("0001018840-17-000013", "a201610-k.htm", "10K_FY2016"),
]


def get(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return open(dest, encoding="utf-8", errors="replace").read()
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    with open(dest, "wb") as f:
        f.write(data)
    time.sleep(0.3)
    return data.decode("utf-8", "replace")


def strip(htm):
    htm = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", htm, flags=re.S | re.I)
    htm = re.sub(r"</(p|div|tr|table|h\d|li)>", "\n", htm, flags=re.I)
    htm = re.sub(r"</t[dh]>", " | ", htm, flags=re.I)
    htm = re.sub(r"<br[^>]*>", "\n", htm, flags=re.I)
    htm = re.sub(r"<[^>]+>", "", htm)
    htm = H.unescape(htm)
    htm = htm.replace("\u00a0", " ")
    htm = re.sub(r"[ \t]+", " ", htm)
    htm = re.sub(r"\n\s*\n+", "\n", htm)
    return htm


for acc, doc, tag in DOCS:
    accn = acc.replace("-", "")
    url = f"{BASE}/{accn}/{doc}"
    raw_p = os.path.join(OUT, f"{tag}.htm")
    txt_p = os.path.join(OUT, f"{tag}.txt")
    try:
        raw = get(url, raw_p)
        if not os.path.exists(txt_p):
            open(txt_p, "w", encoding="utf-8").write(strip(raw))
        print(f"{tag:14s} {len(raw)/1e6:5.1f}MB -> {os.path.getsize(txt_p)/1e6:4.1f}MB text")
    except Exception as e:
        print(f"{tag}: FAILED {e}")

# the Q2 FY2026 8-K: find the press-release exhibit via the filing index
import json
idx = json.loads(get(f"{BASE}/000101884026000041/index.json",
                     os.path.join(OUT, "8K_20260826_index.json")))
for item in idx["directory"]["item"]:
    n = item["name"]
    if n.lower().endswith(".htm"):
        print("8-K item:", n)
