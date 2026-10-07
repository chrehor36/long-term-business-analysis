"""Q3 [E3-48]: the FY2023 down-year guidance record (not on disk at the resume). EX-99.1 releases only, via fetch.py's exhibits()."""
import fetch
for acc, prefix in [("0001045810-22-000008", "8K_2022-02-16"), ("0001045810-22-000073", "8K_2022-05-25"),
                    ("0001045810-22-000133", "8K_2022-08-08"), ("0001045810-22-000136", "8K_2022-08-24"),
                    ("0001045810-22-000163", "8K_2022-11-16"), ("0001045810-23-000014", "8K_2023-02-22")]:
    try:
        fetch.exhibits(acc, prefix)
    except Exception as e:
        print("FAIL", prefix, e)
