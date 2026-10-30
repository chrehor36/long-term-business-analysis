# HRIBF run notes (2026-10-13)

Template copied to the run file before any fetch, 2026-10-13.

## Working notes
- Raw filings in cache/ (gitignored). Text by pdftotext -enc UTF-8 or PyMuPDF (scripts/pdf2txt.py) for older yuho.
- Old five-segment sales / segment profit (¥m), from the yuho segment notes:
  2015 Auto 65,436/5,200 E&P 16,708/1,756 Med 27,669/2,558 Semi 35,353/9,429 Sci 26,748/1,197 total 171,916/20,142
  2016 62,207/3,529 16,753/1,540 26,564/2,806 38,828/9,678 25,738/944 total 170,093/18,499
  2017 73,360/7,680 17,433/1,094 25,187/1,918 53,300/15,642 26,117/498 total 195,399/26,834
  2018 79,656/7,702 19,361/2,027 26,012/1,823 57,785/17,063 27,754/221 total 210,570/28,838
  2019 81,042/6,454 19,500/1,697 25,335/1,302 47,191/10,727 27,170/734 total 200,241/20,916
  2020 63,913/2,465 18,337/1,639 21,035/-426 56,967/14,052 26,825/1,963 total 187,080/19,694
  2021 61,249/-13 20,217/1,947 25,882/148 87,004/28,006 29,958/1,957 total 224,314/32,046
  2022 67,524/-667 22,541/2,101 29,753/-99 114,075/42,005 36,239/2,503 total 270,133/45,843
  2023 80,406/1,209 24,959/2,412 32,678/638 112,872/40,580 39,641/2,456 total 290,558/47,296
  2024 93,498/1,493 28,194/1,835 33,706/-150 120,466/44,178 41,503/982 total 317,369/48,340
- New three segments: 2024 E&E 127,422/4,262 B&H 40,155/-890 M&S 149,791/44,968; 2025 134,407/9,417 42,173/-894 156,500/44,517 (total OP 53,040)

## Checks, 2026-10-13
- python tools/check_framework.py: PASS.
- scripts/check_ids.py on the run file: no E-ids; 32 distinct ids all in principle_ledger_v5.csv; 17 quoted fragments beside ids all in their rows.
- scripts/check_wide.py: one flag, a company quote followed by the template heading's [M1997-127], not a row quote (by design).
