import urllib.request, time, os
UA = {"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        except Exception as e: print("retry",i,e); time.sleep(3)
for acc,name,out in [("0001529274-25-000051","schedule14a-proxystatement.htm","DEF14A_2025.htm"),("0001529274-24-000068","schedule14a-proxystatement.htm","DEF14A_2024.htm"),("0001529274-23-000069","schedule14a-proxystatement.htm","DEF14A_2023.htm")]:
    b=get(f"https://www.sec.gov/Archives/edgar/data/1529274/{acc.replace('-','')}/{name}"); open(out,"wb").write(b); print(out,len(b)); time.sleep(0.4)
