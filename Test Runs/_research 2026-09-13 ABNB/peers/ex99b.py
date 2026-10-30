import sys, subprocess, os
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 ABNB')
from fetch import get
H2T = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 ABNB\h2t.py'
for cik,acc,n,out in [(1324424,"0001324424-20-000006","earningsrelease-q42019.htm","10k_EXPE_EX991_Q4_2019"),
 (1324424,"0001324424-21-000013","earningsrelease-q42020.htm","10k_EXPE_EX991_Q4_2020"),
 (1324424,"0001324424-26-000005","earningsrelease-q42025.htm","10k_EXPE_EX991_Q4_2025"),
 (1324424,"0001324424-26-000051","earningsrelease-q22026.htm","10q_EXPE_EX991_Q2_2026")]:
    get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{n}", out+".htm")
    subprocess.run([sys.executable,H2T,out+".htm",out+".txt"]); os.remove(out+".htm")
