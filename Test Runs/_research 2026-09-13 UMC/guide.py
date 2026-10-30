"""Extract each quarterly results release: overview bullets and next-quarter guidance. Transcription only."""
import re, os, glob, json
HERE = os.path.dirname(os.path.abspath(__file__))
files = ["2023-01-17_000443__umc-ex99_6.txt","2023-04-26_006236__umc-ex99_6.txt","2023-07-26_034540__umc-ex99.txt","2023-10-25_054991__umc-ex99.txt","2024-01-31_009128__umc-ex99.txt","2024-04-24_047232__umc-ex99.txt","2024-07-31_088210__umc-ex99.txt","2024-10-30_118560__umc-ex99.txt","2025-01-21_006966__umc-ex99.txt","2025-04-23_056948__umc-ex99.txt","2025-07-30_099865__umc-ex99.txt","2025-10-29_254520__umc-ex99.txt","2026-01-28_025557__umc-ex99_1.txt","2026-04-29_188788__umc-ex99.txt","2026-07-29_322027__umc-ex99.txt"]
out = {}
for fn in files:
    t = re.sub(r"\s+", " ", open(os.path.join(HERE, "k", fn), encoding="utf-8").read())
    i = t.find("UMC Reports")
    j = t.find("Outlook & Guidance", i)
    k = t.find("6. Countermeasures", j)
    ov = t[i:i+700]
    g = t[j:k]
    # key sentences
    ship = re.findall(r"wafer shipments[^.]{0,160}\.", t[i:j], flags=re.I)[:3]
    asp = re.findall(r"[^.]{0,120}(?:ASP|average selling price)[^.]{0,160}\.", t[i:j], flags=re.I)[:3]
    out[fn] = {"overview": ov, "guidance": g, "ship": ship, "asp": asp}
    print("=====", fn); print(ov[:620]); print("GUIDE:", g[:420]); print("SHIP:", ship); print("ASP:", asp)
json.dump(out, open(os.path.join(HERE, "guide_out.json"), "w"), indent=1)
