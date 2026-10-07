import sys, time
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
ciks = {"WBD":"0001437107","DIS":"0001744489","LION":"0002052959","STRZ/old LGF":"0000929351","PSKY":"0002041610","PARA Global":"0000813828","CMCSA":"0001166691"}
for phrase in ["hit-driven", "hit driven"]:
    for k, c in ciks.items():
        try:
            n, url = sources.fts_count(phrase, cik=c, forms="10-K")
        except Exception as e:
            n, url = "ERR " + str(e)[:80], ""
        print(phrase, "|", k, c, "|", n, "|", url)
        time.sleep(0.4)
