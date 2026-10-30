import json

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
auto = json.load(open(f"{SCRATCH}\\sp500_2008_fates_auto.json"))

# Manual overrides / hand classification, from general knowledge of these
# companies' well-known histories (not individually re-verified via primary
# filings this session -- flagged plainly in the write-up as a lower
# rigor tier than the XBRL-verified failure sample in Part A).
# Categories: FAILED (bankruptcy/conservatorship, equity wiped out or
# near-total loss) / SEVERELY_IMPAIRED (survived but destroyed the large
# majority of shareholder value) / ACQUIRED (bought out at a reasonable/fair
# value) / SPINOFF_OR_MERGED (value preserved via new shares) / SURVIVED
# (still an independent going concern, just fell below the index's size
# threshold).
OVERRIDES = {
    # genuine failures
    "RSH": "FAILED", "EK": "FAILED", "ABK": "FAILED", "DO": "FAILED",
    "FNM": "FAILED", "FRE": "FAILED", "SHLD": "FAILED", "FTR": "FAILED",
    "WIN": "FAILED", "CHK": "FAILED", "DYN": "FAILED", "BTU": "FAILED",
    "WFR": "FAILED", "BIG": "FAILED", "DNR": "FAILED", "CFC": "FAILED",
    "MBI": "FAILED",
    # severely impaired but still an independent going concern
    "ACAS": "SEVERELY_IMPAIRED", "GNW": "SEVERELY_IMPAIRED",
    "PBI": "SEVERELY_IMPAIRED", "LUMN": "SEVERELY_IMPAIRED",
    "XRX": "SEVERELY_IMPAIRED", "NOV": "SEVERELY_IMPAIRED",
    # reclassify auto-classifier mistakes -> ACQUIRED at reasonable value
    "ACE": "SURVIVED", "ALTR": "ACQUIRED", "BMC": "ACQUIRED", "BRCM": "ACQUIRED",
    "CCE": "SPINOFF_OR_MERGED", "EMC": "ACQUIRED", "FRX": "ACQUIRED",
    "HCBK": "ACQUIRED", "HOT": "ACQUIRED", "HSP": "ACQUIRED", "JNY": "ACQUIRED",
    "LSI": "ACQUIRED", "PCL": "ACQUIRED", "PCP": "ACQUIRED", "PLL": "ACQUIRED",
    "RX": "ACQUIRED", "TEG": "ACQUIRED", "DNB": "ACQUIRED",
    # reclassify -> SPINOFF_OR_MERGED (value preserved via new share issue)
    "AA": "SPINOFF_OR_MERGED", "ATI": "SURVIVED", "CSC": "SPINOFF_OR_MERGED",
    "DISCA": "SPINOFF_OR_MERGED", "KFT": "SPINOFF_OR_MERGED",
    "SLE": "SPINOFF_OR_MERGED", "STR": "SPINOFF_OR_MERGED",
    "TGNA": "SURVIVED",
    # reclassify -> SURVIVED (still independent, just fell below the cap
    # threshold at the time; several later re-entered or remain healthy)
    "CNX": "SURVIVED", "GME": "SURVIVED", "S": "SURVIVED", "THC": "SURVIVED",
    "ANF": "SURVIVED", "AVP": "ACQUIRED", "BBBY": "FAILED", "BBWI": "SURVIVED",
    "BC": "SURVIVED", "CAG": "SURVIVED", "CMA": "SURVIVED", "CPB": "SURVIVED",
    "CPRI": "SURVIVED", "CPWR": "ACQUIRED", "CVG": "ACQUIRED", "EMN": "SURVIVED",
    "FLS": "SURVIVED", "GHC": "SURVIVED", "GPS": "SURVIVED", "HOG": "SURVIVED",
    "HRB": "SURVIVED", "IGT": "SURVIVED", "JDSU": "SURVIVED", "JNS": "ACQUIRED",
    "JOY": "ACQUIRED", "JWN": "SURVIVED", "KBH": "SURVIVED", "KSS": "SURVIVED",
    "LEG": "SURVIVED", "LM": "ACQUIRED", "LNC": "SURVIVED", "M": "SURVIVED",
    "MUR": "SURVIVED", "MWW": "ACQUIRED", "NBR": "SURVIVED", "NWL": "SURVIVED",
    "NYT": "SURVIVED", "ODP": "SURVIVED", "OMX": "SURVIVED", "PDCO": "SURVIVED",
    "R": "SURVIVED", "RDC": "ACQUIRED", "RHI": "SURVIVED", "RRC": "SURVIVED",
    "RRD": "ACQUIRED", "SEE": "SURVIVED", "SRCL": "ACQUIRED", "TDC": "SURVIVED",
    "UAA": "SURVIVED", "UNM": "SURVIVED", "URBN": "SURVIVED", "VFC": "SURVIVED",
    "VNO": "SURVIVED", "WHR": "SURVIVED", "WU": "SURVIVED", "X": "SURVIVED",
    "XRAY": "SURVIVED", "ZION": "SURVIVED", "APOL": "ACQUIRED",
    "APOL_note": "went private, for-profit-ed scrutiny, not a formal failure",
}

fates = {}
for t, v in auto.items():
    fates[t] = OVERRIDES.get(t, v["class"])
    if fates[t] in ("MARKET_CAP_DECLINE_UNCLASSIFIED", "OTHER_UNCLASSIFIED"):
        fates[t] = "SURVIVED"  # remaining un-overridden ambiguous ones: treat
        # as ordinary market-cap-decline exits (the conservative default --
        # doesn't inflate the failure count with unverified guesses)

from collections import Counter
c = Counter(fates.values())
print("FINAL fate classification of 218 tickers removed from the reconstructed 2008 S&P 500:")
for k, v in c.most_common():
    print(f"  {k}: {v}  ({100*v/218:.1f}%)")

print()
print("=== FAILED (bankruptcy/conservatorship, equity wiped out) ===")
for t, f in sorted(fates.items()):
    if f == "FAILED":
        print(" ", t)
print()
print("=== SEVERELY_IMPAIRED (survived, but destroyed most shareholder value) ===")
for t, f in sorted(fates.items()):
    if f == "SEVERELY_IMPAIRED":
        print(" ", t)

json.dump(fates, open(f"{SCRATCH}\\sp500_2008_fates_final.json", "w"), indent=1)
