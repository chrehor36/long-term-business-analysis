#!/bin/bash
cd "/c/Users/chreh/OneDrive/Documents/BRK/Test Runs/_research 2026-10-13 APEMY/cache"
B=https://www.aperam.com/sites/default/files/documents
get() {
  for i in $(seq 1 40); do
    curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -C - --connect-timeout 30 --max-time 900 --retry 5 --retry-delay 60 --retry-all-errors -o "$2" "$B/$1"
    if tail -c 2048 "$2" 2>/dev/null | grep -aq "%%EOF" && pdftotext -l 1 "$2" - >/dev/null 2>&1; then echo "$2 OK $(stat -c %s "$2")"; return; fi
    sleep 60
  done; echo "$2 FAILED"
}
get Aperam_AnnualReport_2025.pdf AR2025.pdf
get Aperam_HYR_2026.pdf HYR2026.pdf
get Annual_Report_2023.pdf AR2023.pdf
get Annual_Report_2021.pdf AR2021.pdf
get "Annual%20Report%202019.pdf" AR2019.pdf
get "Annual_Report_2017__0.pdf" AR2017.pdf
get 2016_Annual_Report.pdf AR2016.pdf
get AnnualReport_2024_compressed.pdf AR2024.pdf
get Q2_2026_ER_PressRelease_EN.pdf Q2_2026_PR.pdf
get Aperam_Q3-26_Update.pdf Q3_26_update.pdf
echo ALLDONE
