import sys, re, os
D = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(D, sys.argv[1] + "_10K_FY2025.txt"), encoding="utf-8").read()
t = re.sub(r"\s*\n\s*", " ", t)
t = re.sub(r"(\|\s*)+\|", "|", t)
t = re.sub(r"\$\s*\|\s*", "$", t)
for mm in re.finditer(r"I[Tt][Ee][Mm]\s+(1A|1B|1C|1|2|7A|7|8|9A)\.?\s*[|]?\s*(Business|Risk Factors|Unresolved|Cybersecurity|Properties|Management|Quantitative|Financial Statements|Controls)", t):
    print(mm.start(), mm.group(0)[:60])
