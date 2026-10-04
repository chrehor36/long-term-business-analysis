import json

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
auto = json.load(open(f"{SCRATCH}\\sp500_2013_fates_auto.json"))

# Same classification logic/knowledge as the 2008 reconstruction (BT-7 Part
# B) -- reused directly since most names overlap; a few new ones added for
# tickers that only appear in the 2013-specific departure list.
OVERRIDES = {
    "RSH": "FAILED", "EK": "FAILED", "ABK": "FAILED", "DO": "FAILED",
    "FNM": "FAILED", "FRE": "FAILED", "SHLD": "FAILED", "FTR": "FAILED",
    "WIN": "FAILED", "CHK": "FAILED", "DYN": "FAILED", "BTU": "FAILED",
    "WFR": "FAILED", "BIG": "FAILED", "DNR": "FAILED", "CFC": "FAILED",
    "MBI": "FAILED", "BBBY": "FAILED",
    "FOSL": "SEVERELY_IMPAIRED",
    "ACAS": "SEVERELY_IMPAIRED", "GNW": "SEVERELY_IMPAIRED",
    "PBI": "SEVERELY_IMPAIRED", "LUMN": "SEVERELY_IMPAIRED",
    "XRX": "SEVERELY_IMPAIRED", "NOV": "SEVERELY_IMPAIRED",
    "ACE": "SURVIVED", "ALTR": "ACQUIRED", "BMC": "ACQUIRED", "BRCM": "ACQUIRED",
    "CCE": "SPINOFF_OR_MERGED", "EMC": "ACQUIRED", "FRX": "ACQUIRED",
    "HCBK": "ACQUIRED", "HOT": "ACQUIRED", "HSP": "ACQUIRED",
    "LSI": "ACQUIRED", "PCL": "ACQUIRED", "PCP": "ACQUIRED", "PLL": "ACQUIRED",
    "TEG": "ACQUIRED", "DNB": "ACQUIRED",
    "AA": "SPINOFF_OR_MERGED", "ATI": "SURVIVED", "CSC": "SPINOFF_OR_MERGED",
    "DISCA": "SPINOFF_OR_MERGED", "TGNA": "SURVIVED",
    "CNX": "SURVIVED", "GME": "SURVIVED", "S": "SURVIVED", "THC": "SURVIVED",
    "ANF": "SURVIVED", "AVP": "ACQUIRED", "BBWI": "SURVIVED",
    "CAG": "SURVIVED", "CMA": "SURVIVED", "CPB": "SURVIVED",
    "CPRI": "SURVIVED", "EMN": "SURVIVED",
    "FLS": "SURVIVED", "GHC": "SURVIVED", "GPS": "SURVIVED", "HOG": "SURVIVED",
    "HRB": "SURVIVED", "IGT": "SURVIVED", "JDSU": "SURVIVED",
    "JOY": "ACQUIRED", "JWN": "SURVIVED", "KSS": "SURVIVED",
    "LEG": "SURVIVED", "LM": "ACQUIRED", "LNC": "SURVIVED", "M": "SURVIVED",
    "MUR": "SURVIVED", "NBR": "SURVIVED", "NWL": "SURVIVED",
    "PDCO": "SURVIVED",
    "R": "SURVIVED", "RDC": "ACQUIRED", "RHI": "SURVIVED", "RRC": "SURVIVED",
    "SEE": "SURVIVED", "SRCL": "ACQUIRED", "TDC": "SURVIVED",
    "UAA": "SURVIVED", "UNM": "SURVIVED", "URBN": "SURVIVED", "VFC": "SURVIVED",
    "VNO": "SURVIVED", "WHR": "SURVIVED", "WU": "SURVIVED", "X": "SURVIVED",
    "XRAY": "SURVIVED", "ZION": "SURVIVED", "APOL": "ACQUIRED",
    # new to the 2013 list
    "ADT": "ACQUIRED", "AET": "ACQUIRED", "AGN": "ACQUIRED", "AIV": "SURVIVED",
    "ALXN": "ACQUIRED", "AN": "SURVIVED", "ANDV": "ACQUIRED", "APC": "ACQUIRED",
    "ARG": "ACQUIRED", "BWA": "SURVIVED", "CLF": "SURVIVED", "FMC": "SURVIVED",
    "HP": "SURVIVED", "KMX": "SURVIVED", "OI": "SURVIVED", "PRGO": "SURVIVED",
    "SAI": "SPINOFF_OR_MERGED", "TRIP": "SURVIVED", "TYC": "SPINOFF_OR_MERGED",
    "WPX": "ACQUIRED",
}

fates = {}
for t, v in auto.items():
    fates[t] = OVERRIDES.get(t, v["class"])
    if fates[t] in ("MARKET_CAP_DECLINE_UNCLASSIFIED", "OTHER_UNCLASSIFIED"):
        fates[t] = "SURVIVED"

from collections import Counter
c = Counter(fates.values())
print("FINAL fate classification, 2013 reconstruction departures:")
for k, v in c.most_common():
    print(f"  {k}: {v}")
print()
print("FAILED or SEVERELY_IMPAIRED (the ones we want the framework to have avoided):")
for t, f in sorted(fates.items()):
    if f in ("FAILED", "SEVERELY_IMPAIRED"):
        print(" ", t, f)

json.dump(fates, open(f"{SCRATCH}\\sp500_2013_fates_final.json", "w"), indent=1)
