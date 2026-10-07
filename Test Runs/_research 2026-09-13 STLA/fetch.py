import json, os, sys, urllib.request, time, re, html
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = "0001605484"


def get(url, ua=UA):
    last = None
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=ua)
            return urllib.request.urlopen(req, timeout=90).read()
        except Exception as e:
            last = e
            print("retry", url, e)
            time.sleep(2 + i * 2)
    raise SystemExit("failed " + url + " " + str(last))


def save(name, data):
    p = os.path.join(HERE, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as f:
        f.write(data)


def strip(raw):
    t = raw.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>|</table>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "base":
        save("submissions.json", get(f"https://data.sec.gov/submissions/CIK{CIK}.json"))
        sub = json.load(open(os.path.join(HERE, "submissions.json")))
        out = []
        r = sub["filings"]["recent"]
        for i in range(len(r["form"])):
            out.append("\t".join([r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i], r["primaryDocDescription"][i]]))
        for f in sub.get("filings", {}).get("files", []):
            d = json.loads(get("https://data.sec.gov/submissions/" + f["name"]))
            for i in range(len(d["form"])):
                out.append("\t".join([d["filingDate"][i], d["form"][i], d["accessionNumber"][i], d["primaryDocument"][i], d["reportDate"][i], d["primaryDocDescription"][i]]))
        open(os.path.join(HERE, "filings_list.txt"), "w", encoding="utf-8").write("\n".join(out))
        print(sub.get("name"), sub.get("formerNames"))
        print(len(out), "filings")
    elif cmd == "doc":
        # doc <accession> <primarydoc> <outname>  (saves raw and stripped .txt)
        acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(CIK)}/{acc.replace('-', '')}/{doc}"
        raw = get(url)
        save(out + ".htm", raw)
        txt = "SOURCE " + url + " accession " + acc + "\n" + strip(raw)
        save(out + ".txt", txt.encode("utf-8"))
        print("saved", out, len(raw))
    elif cmd == "index":
        acc = sys.argv[2]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(CIK)}/{acc.replace('-', '')}/index.json"
        d = json.loads(get(url))
        for it in d["directory"]["item"]:
            print(it["name"], it.get("size"))
    elif cmd == "url":
        url, out = sys.argv[2], sys.argv[3]
        raw = get(url, {"User-Agent": "Mozilla/5.0"} if "sec.gov" not in url else UA)
        save(out, raw)
        print("saved", out, len(raw))
