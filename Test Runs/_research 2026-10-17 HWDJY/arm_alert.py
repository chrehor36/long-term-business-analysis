"""Arm the HWDJY v5 fair-price alert on the London ordinary share in pence, by hand, as the DPMAY and ADRZY folds did,
because tools/v5_rerun_fold.py arms alerts in USD on the register ticker. Figure from the run file (Q7, all-equity)."""
import json
A = r"C:\Users\chreh\OneDrive\Documents\BRK\tools\alerts.json"
raw = open(A, encoding="utf-8", newline="").read(); d = json.loads(raw)
aid = "HWDJY-v5-fair"
d["alerts"] = [a for a in d["alerts"] if a["id"] != aid]
d["alerts"].append({"id": aid, "ticker": "HWDN.L", "currency": "GBp", "op": "<=", "threshold": 499.0, "active": True,
 "label": "HWDJY (Howden Joinery Group Plc; alert on the London ordinary share HWDN.L in pence; one ADS is four ordinaries) at/below 499p (US$26.43 an ADS): the fair price on the all-equity basis of the blind v5 purchase run of 2026-10-17 (Test Runs/2026-10-17 Run - HWDJY Howden Joinery Group.md; OUT at Q7 at 788p; 503p equity-only; value range 780p to 1,044p at the 5.7225% Bank of England 20-year). Set by hand at the fold because tools/v5_rerun_fold.py arms alerts in USD on the register ticker. A prompt to re-run Q7, never a verdict."})
out = json.dumps(d, indent=1, ensure_ascii=True).replace("\n", "\r\n") + ("\r\n" if raw.endswith("\r\n") else "")
open(A, "w", encoding="utf-8", newline="").write(out); print("armed")
