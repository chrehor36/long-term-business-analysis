"""Fetch an EDGAR document and strip it to text. usage: fetch_sec.py CIK ACCESSION DOC OUT"""
import sys, re, html, urllib.request
cik, acc, doc, out = sys.argv[1:5]
url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
req = urllib.request.Request(url, headers={"User-Agent": "BRK research chrehor36@gmail.com"})
t = urllib.request.urlopen(req).read().decode("utf-8", "replace")
t = re.sub(r"(?i)</(tr|p|div)>", "\n", t)
t = re.sub(r"(?i)<(td|th)[^>]*>", " | ", t)
t = html.unescape(re.sub(r"<[^>]+>", "", t))
t = re.sub(r"[ \t\xa0]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(out, "w", encoding="utf-8").write(t)
print(out, len(t))
