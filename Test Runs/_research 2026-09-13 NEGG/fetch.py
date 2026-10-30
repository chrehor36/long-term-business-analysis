import json, os, sys, urllib.request, time
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = "0001474627"

def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            print("retry", url, e); time.sleep(2 + i * 2)
    raise SystemExit("failed " + url)

def save(name, data):
    with open(os.path.join(HERE, name), "wb") as f:
        f.write(data)

if __name__ == "__main__":
    if sys.argv[1] == "base":
        save("submissions.json", get(f"https://data.sec.gov/submissions/CIK{CIK}.json"))
        save("companyfacts.json", get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json"))
        sub = json.load(open(os.path.join(HERE, "submissions.json")))
        r = sub["filings"]["recent"]
        for i in range(len(r["form"])):
            print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i], r.get("primaryDocDescription", [""]*999)[i])
        print(sub.get("filings", {}).get("files"))
    elif sys.argv[1] == "doc":
        # doc <accession> <primarydoc> <outname>
        acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(CIK)}/{acc.replace('-', '')}/{doc}"
        save(out, get(url)); print("saved", out)
    elif sys.argv[1] == "index":
        acc = sys.argv[2]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(CIK)}/{acc.replace('-', '')}/index.json"
        d = json.loads(get(url))
        for it in d["directory"]["item"]:
            print(it["name"], it.get("size"))
