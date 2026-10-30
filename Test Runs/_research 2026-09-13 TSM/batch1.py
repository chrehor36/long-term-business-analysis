import subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
jobs = [
 ("0001628280-26-025362","tsm-20251231.htm","20F_FY2025"),
 ("0001193125-25-083423","d896993d20f.htm","20F_FY2024"),
 ("0001193125-24-099840","d592628d20f.htm","20F_FY2023"),
 ("0001193125-23-107214","d428519d20f.htm","20F_FY2022"),
 ("0001193125-22-104891","d204786d20f.htm","20F_FY2021"),
 ("0001193125-21-118512","d94821d20f.htm","20F_FY2020"),
 ("0001193125-18-121866","d459142d20f.htm","20F_FY2017"),
 ("0001046179-26-000658","tsm-revenue20260910.htm","6K_2026-09-10_revenue"),
 ("0001046179-26-000552","tsm-dividendadjustmentx202.htm","6K_2026-09-01_dividend"),
 ("0001046179-26-000545","tsm-monthend6kx20260825.htm","6K_2026-08-25_monthend"),
 ("0001046179-26-000541","tsm-fsx20260814x6k.htm","6K_2026-08-14_fsQ2"),
 ("0001046179-26-000536","tsm-boardx20260811.htm","6K_2026-08-11_board"),
 ("0001046179-26-000539","sonysemiconductorsolutions.htm","6K_2026-08-11_sony"),
 ("0001046179-26-000451","tsm-20260716x6k.htm","6K_2026-07-16_Q2results"),
 ("0001046179-26-000199","tsm-20260416x6k.htm","6K_2026-04-16_Q1results"),
 ("0001046179-26-000201","tsm_20260416.htm","6K_2026-04-16_other"),
 ("0001046179-26-000278","tsm-fsx20260515x6k.htm","6K_2026-05-15_fsQ1"),
 ("0001046179-26-000280","tsmctosell81ofvanguardinte.htm","6K_2026-05-15_vanguard"),
 ("0001046179-26-000302","tsm-agmx20260604x6k.htm","6K_2026-06-04_agm"),
 ("0001046179-26-000008","tsm-20260115x6k.htm","6K_2026-01-15_Q4results"),
 ("0001046179-26-000024","tsm-fsx20260226x6k.htm","6K_2026-02-26_fsFY"),
 ("0001046179-26-000017","tsm-boardx20260210x6k.htm","6K_2026-02-10_board"),
 ("0001046179-26-000274","tsm-boardx20260512.htm","6K_2026-05-12_board"),
 ("0001046179-26-000381","a20260702changeofaztreasur.htm","6K_2026-07-02_aztreas"),
 ("0001046179-26-000076","a20260317.htm","6K_2026-03-17"),
]
for acc, doc, out in jobs:
    if os.path.exists(os.path.join(HERE, out + ".txt")):
        continue
    subprocess.run([sys.executable, os.path.join(HERE, "get.py"), "doc", acc, doc, out])
