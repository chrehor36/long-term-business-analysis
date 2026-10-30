import re, sys, os
sys.stdout.reconfigure(encoding="utf-8")
Q = [
("AMR_0001704715-26-000010", "We operate highly productive, cost-competitive"),
("AMR_0001704715-26-000010", "We operate high-quality, cost-competitive"),
("AMR_0001704715-26-000010", "Of the approximately 73.1 million tons of met"),
("AMR_0001704715-26-000010", "In the export met coal market, we compete"),
("AMR_0001704715-26-000010", "We compete with numerous other coal producers"),
("AMR_0001704715-26-000010", "We compete for U.S. sales with numerous"),
("HCC_0001193125-26-048914", "We are a large-scale, low-cost producer and exporter of premium quality met"),
("HCC_0001193125-26-048914", "We believe our mines are some of the lowest cost"),
("HCC_0001193125-26-048914", "further improving our position in the first-quartile global cost curve"),
("HCC_0001193125-26-048914", "Our highly flexible cost structure provides"),
("HCC_0001193125-26-048914", "We primarily compete with producers of premium"),
("HCC_0001193125-26-048914", "Our major competitors sell into"),
("METC_0001104659-26-086668", "Being a Low-Cost U.S. Producer"),
("METC_0001104659-26-086668", "U.S. metallurgical coal exports compete with Australian"),
("METC_0001104659-26-086668", "Our principal domestic coal competitors include"),
("METC_0001104659-26-086668", "Ramaco Coal bought the property from Core Natural Resources"),
("METC_0001104659-26-086668", "We compete primarily with U.S. coal producers"),
("BTU_0001064728-26-000006", "Peabody is a leading producer"),
("BTU_0001064728-26-000006", "principal U.S. direct coal supply competitors"),
("BTU_0001064728-26-000006", "Major international direct competitors (listed alphabetically) include Anglo"),
("BTU_0001064728-26-000006", "Major international direct coal supply competitors"),
("BTU_0001064728-24-000021", "principal U.S. direct coal supply competitors"),
("BTU_0001064728-24-000021", "Major international direct competitors (listed alphabetically) include Anglo"),
("ARLP_0001104659-26-020468", "remain a low-cost coal producer"),
("ARLP_0001104659-26-020468", "We are the second largest coal producer in the eastern United States and"),
("ARLP_0001104659-26-020468", "Our principal competitors include"),
("ARLP_0001558370-24-001616", "Our principal competitors include"),
("ARLP_0001104659-26-020468", "We also compete directly with smaller producers"),
]
for f, s in Q:
    t = open(os.path.join("cache", f + ".flat.txt"), encoding="utf-8").read().replace("​", "")
    t = re.sub(r"[ \t]+", " ", t)
    i = t.find(s)
    if i < 0:
        print("NOTFOUND", f, s); continue
    # expand to sentence start
    st = max(t.rfind(". ", 0, i) + 2, t.rfind("\n", 0, i) + 1)
    en = t.find("\n", i)
    print(f, "::", t[st:en].strip()[:1200], "\n")
