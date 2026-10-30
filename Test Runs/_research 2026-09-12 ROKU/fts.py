import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
for ph in ["webOS", "Tizen", "Samsung TV Plus", "SmartCast", "Google TV", "Fire TV"]:
    try:
        print("%-18s %s" % (ph, sources.fts_count(ph)))
    except Exception as e:
        print(ph, "ERR", repr(e))
