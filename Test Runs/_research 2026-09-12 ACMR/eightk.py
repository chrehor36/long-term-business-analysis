import urllib.request, json, time, re
UA={"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read()
        except Exception as e: print("retry",e); time.sleep(3)
    return b""
CIK="1680062"
accs = ["0001628280-26-059251","0001628280-26-054581","0001628280-26-044506","0001628280-26-042833",
        "0001140361-26-023310","0001628280-26-037552","0001140361-26-021661","0001140361-26-020717",
        "0001628280-26-031688","0001628280-26-027353","0001628280-26-025599","0001628280-26-020846",
        "0001628280-26-019811","0001628280-26-011998","0001680062-26-000020","0001680062-26-000016",
        "0001680062-26-000012","0001680062-26-000009","0001680062-26-000003"]
for a in accs:
    j = get(f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany")  # noop
    u = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a.replace('-','')}/index.json"
    b = get(u)
    if not b: print(a,"NOIDX"); continue
    d = json.loads(b)
    names=[i["name"] for i in d["directory"]["item"]]
    print(a, "|", ", ".join(n for n in names if n.endswith(".htm") or n.endswith(".txt")))
    time.sleep(0.3)
