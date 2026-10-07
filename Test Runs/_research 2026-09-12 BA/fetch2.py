import sys, os, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
exec(open("Test Runs/_research 2026-09-12 BA/fetch.py").read().split('if __name__')[0])
for args in [
  ("12927","0000012927-24-000010","ba-20231231.htm","10K_FY2023"),
  ("12927","0000012927-23-000007","ba-20221231.htm","10K_FY2022"),
  ("12927","0000012927-21-000011","ba-20201231.htm","10K_FY2020"),
  ("12927","0000012927-19-000010","a201812dec3110k.htm","10K_FY2018"),
  ("12927","0000012927-16-000099","a201512dec3110k.htm","10K_FY2015"),
]:
    try: grab(*args)
    except Exception as e: print("FAIL", args[-1], e)
    time.sleep(0.4)
