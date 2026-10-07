from fetch_core import *
for acc in ["0001437749-26-028541","0001193125-26-273417","0001193125-26-164338","0001628280-26-026081","0001628280-26-022181","0001193125-26-155150","0001653909-24-000064"]:
    try: print(acc, exhibits(acc))
    except Exception as e: print(acc, "ERR", e)
    time.sleep(0.3)
