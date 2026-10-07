from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
J = [("2026-08-06","0001422930-26-000029","q226pressrelease.htm"),("2026-08-06b","0001422930-26-000029","ex992pubmaticcforetirement.htm"),
("2026-05-07","0001422930-26-000023","q126pressrelease.htm"),("2026-04-22","0001422930-26-000016","pubmpressreleaserepreannou.htm"),
("2026-02-26","0001422930-26-000008","fy25pressrelease.htm"),("2025-11-10","0001422930-25-000048","q325pressrelease.htm"),
("2025-08-11","0001422930-25-000038","q225pressrelease.htm"),("2025-05-08","0001422930-25-000023","q125pressrelease.htm"),
("2025-02-27","0001422930-25-000009","fy24pressrelease.htm"),("2024-11-12","0001422930-24-000045","q324pressrelease.htm"),
("2024-08-08","0001422930-24-000039","q224pressrelease.htm"),("2024-05-07","0001422930-24-000025","q124pressrelease.htm"),
("2024-02-26","0001422930-24-000004","fy23pressrelease.htm"),("2023-11-08","0001422930-23-000056","q323pressrelease.htm"),
("2023-08-08","0001422930-23-000036","q223pressrelease.htm"),("2023-05-09","0001422930-23-000021","q123pressrelease.htm"),
("2023-02-28","0001422930-23-000006","fy22pressrelease.htm"),("2022-11-08","0001422930-22-000053","q322pressrelease.htm"),
("2022-08-08","0001422930-22-000039","q222pressrelease.htm"),("2022-05-09","0001422930-22-000024","q122pressrelease.htm"),
("2022-02-28","0001422930-22-000004","fy21pressrelease.htm"),("2021-11-09","0001422930-21-000052","q321pressrelease.htm"),
("2021-08-10","0001422930-21-000043","q221pressrelease.htm"),("2021-05-13","0001422930-21-000024","pressrelease.htm")]
for d, acc, doc in J:
    try: grab(acc, doc, "EX991_"+d)
    except Exception as e: print("ERR", d, e)
grab("0001422930-23-000006","ex31arbylawsfebruary2023.htm","BYLAWS_2023")
