import urllib.request, urllib.parse, re, time, json, os

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
UA = "BRK-Framework research chrehor36@gmail.com"

NAMES = {
    "ACE": "ACE LTD", "AET": "AETNA INC", "AGN": "ALLERGAN PLC", "ALTR": "ALTERA CORP",
    "ALXN": "ALEXION PHARMACEUTICALS", "ANDV": "ANDEAVOR", "APOL": "APOLLO EDUCATION GROUP",
    "ARG": "AIRGAS INC", "AVP": "AVON PRODUCTS", "BCR": "BARD C R INC",
    "BHI": "BAKER HUGHES INC", "BMC": "BMC SOFTWARE", "BMS": "BEMIS CO",
    "BRCM": "BROADCOM CORP", "CA": "CA INC", "CAM": "CAMERON INTERNATIONAL",
    "CCE": "COCA COLA ENTERPRISES", "CELG": "CELGENE CORP", "CERN": "CERNER CORP",
    "CFN": "CAREFUSION CORP", "CMA": "COMERICA INC", "COL": "ROCKWELL COLLINS",
    "COV": "COVIDIEN PLC", "CSC": "COMPUTER SCIENCES CORP", "CTRA": "CABOT OIL & GAS",
    "CTXS": "CITRIX SYSTEMS", "CVC": "CABLEVISION SYSTEMS", "CVH": "COVENTRY HEALTH CARE",
    "DF": "DEAN FOODS", "DFS": "DISCOVER FINANCIAL SERVICES", "DISCA": "DISCOVERY COMMUNICATIONS",
    "DNB": "DUN & BRADSTREET", "DPS": "DR PEPPER SNAPPLE", "DTV": "DIRECTV",
    "EMC": "EMC CORP", "ESRX": "EXPRESS SCRIPTS", "ESV": "ENSCO PLC",
    "ETFC": "E TRADE FINANCIAL", "FDO": "FAMILY DOLLAR STORES", "FII": "FEDERATED INVESTORS",
    "FLIR": "FLIR SYSTEMS", "FRX": "FOREST LABORATORIES", "GAS": "AGL RESOURCES",
    "GPS": "GAP INC", "HAR": "HARMAN INTERNATIONAL", "HCBK": "HUDSON CITY BANCORP",
    "HES": "HESS CORP", "HNZ": "HEINZ H J CO", "HOT": "STARWOOD HOTELS",
    "HSP": "HOSPIRA INC", "IGT": "INTERNATIONAL GAME TECHNOLOGY", "IPG": "INTERPUBLIC GROUP",
    "JCP": "PENNEY J C CORP", "JDSU": "JDS UNIPHASE", "JNPR": "JUNIPER NETWORKS",
    "JOY": "JOY GLOBAL", "JWN": "NORDSTROM INC", "K": "KELLOGG CO",
    "KRFT": "KRAFT FOODS GROUP", "LLL": "L 3 COMMUNICATIONS", "LLTC": "LINEAR TECHNOLOGY",
    "LM": "LEGG MASON", "LO": "LORILLARD INC", "LSI": "LSI CORP",
    "MJN": "MEAD JOHNSON NUTRITION", "MOLX": "MOLEX INC", "MON": "MONSANTO CO",
    "MRO": "MARATHON OIL CORP", "NBL": "NOBLE ENERGY", "NFX": "NEWFIELD EXPLORATION",
    "NYX": "NYSE EURONEXT", "PBCT": "PEOPLES UNITED FINANCIAL", "PCL": "PLUM CREEK TIMBER",
    "PCP": "PRECISION CASTPARTS", "PCS": "METROPCS COMMUNICATIONS", "PDCO": "PATTERSON COMPANIES",
    "PETM": "PETSMART INC", "PLL": "PALL CORP", "PXD": "PIONEER NATURAL RESOURCES",
    "QEP": "QEP RESOURCES", "RAI": "REYNOLDS AMERICAN", "RDC": "ROWAN COMPANIES",
    "RHT": "RED HAT INC", "RTN": "RAYTHEON CO", "SAI": "SAIC INC",
    "SCG": "SCANA CORP", "SEE": "SEALED AIR CORP", "SIAL": "SIGMA ALDRICH",
    "SNI": "SCRIPPS NETWORKS INTERACTIVE", "SPLS": "STAPLES INC", "SRCL": "STERICYCLE INC",
    "STJ": "ST JUDE MEDICAL", "SWN": "SOUTHWESTERN ENERGY", "SWY": "SAFEWAY INC",
    "TEG": "INTEGRYS ENERGY GROUP", "TGNA": "TEGNA INC", "TIF": "TIFFANY & CO",
    "TSS": "TOTAL SYSTEM SERVICES", "TWC": "TIME WARNER CABLE", "TWX": "TIME WARNER INC",
    "TYC": "TYCO INTERNATIONAL", "VAR": "VARIAN MEDICAL SYSTEMS", "VIAB": "VIACOM INC",
    "WBA": "WALGREENS BOOTS ALLIANCE", "WFM": "WHOLE FOODS MARKET", "WPX": "WPX ENERGY",
    "WYN": "WYNDHAM WORLDWIDE", "X": "UNITED STATES STEEL", "XL": "XL GROUP",
    "XLNX": "XILINX INC", "YHOO": "YAHOO INC",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()

results = {}
unresolved = []
for i, (ticker, name) in enumerate(NAMES.items()):
    q = urllib.parse.quote(name)
    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company={q}&type=10-K&dateb=&owner=include&count=3&output=atom"
    try:
        data = fetch(url).decode("utf-8", errors="ignore")
    except Exception as e:
        unresolved.append((ticker, name, f"FETCH_FAIL {e}"))
        time.sleep(0.2)
        continue
    m = re.search(r"CIK=(\d+)", data)
    name_m = re.search(r"<conformed-name>([^<]*)</conformed-name>", data)
    if m:
        results[ticker] = int(m.group(1))
        if (i % 20) == 0:
            print(f"[{i}] {ticker} -> {m.group(1)} ({name_m.group(1) if name_m else '?'})")
    else:
        # ambiguous / company search feed -- grab first CIK listed
        cik_m = re.search(r"<cik>(\d+)</cik>", data)
        if cik_m:
            results[ticker] = int(cik_m.group(1))
        else:
            unresolved.append((ticker, name, "NO_MATCH"))
    time.sleep(0.2)

print(f"\nResolved: {len(results)} / {len(NAMES)}")
print(f"Still unresolved: {len(unresolved)}")
for t, n, r in unresolved:
    print(" ", t, n, r)

json.dump(results, open(os.path.join(SCRATCH, "sp500_2013_remaining_ciks.json"), "w"), indent=1)
json.dump(unresolved, open(os.path.join(SCRATCH, "sp500_2013_still_unresolved.json"), "w"), indent=1)
