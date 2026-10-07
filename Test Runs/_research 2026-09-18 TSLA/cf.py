import json, os
from fetch_core import *
p = os.path.join(HERE, "companyfacts.json")
if not os.path.exists(p):
    open(p, "w").write(get("https://data.sec.gov/api/xbrl/companyfacts/CIK0001318605.json"))
print(os.path.getsize(p))
