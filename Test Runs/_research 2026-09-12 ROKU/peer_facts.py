import sys, os, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources

TICKERS = ["AMZN","GOOGL","AAPL","NFLX","TTD","CMCSA","CHTR","WMT","ROKU"]
for t in TICKERS:
    try:
        cik = sources.cik_for(t)
        print(t, cik)
    except Exception as e:
        print(t, "ERR", e)
