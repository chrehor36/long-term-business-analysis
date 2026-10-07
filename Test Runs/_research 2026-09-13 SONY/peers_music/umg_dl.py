import urllib.request, subprocess, os
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
docs={
"UMG_PR_FY25":"https://assets.ctfassets.net/e66ejtqbaazg/29H5pgbmmYOowQgJET2Wh8/4355ccb601037ecc345ccef3a9d9bc74/UMG_Q4___FY25_results_press_release.pdf",
"UMG_PR_FY24":"https://assets.ctfassets.net/e66ejtqbaazg/1Y06bSVvRmv2QhNwI9rb8c/879342db19bd0967324c084b9139d8c9/UMG_4Q___FY24_Press_release.pdf",
"UMG_PR_FY23":"https://assets.ctfassets.net/e66ejtqbaazg/1psEFHkZbqpN6GxbUUYhPL/eae1981f98c7c682e5d09a2b324e1df0/UMG_4Q___FY23_Press_Release.pdf",
"UMG_AR_2025":"https://assets.ctfassets.net/e66ejtqbaazg/7HObJrt5UDQfjjfKYN454B/201bf057190c5ed4ee185b04a34ec095/UMG_2025_Annual_Report.pdf",
"UMG_AR_2024":"https://downloads.ctfassets.net/e66ejtqbaazg/3lVdyJmpf8DQTPMRcxChSQ/80752d027f61e3846f4b5e2a5a62a958/UMG_2024_Annual_Report.pdf",
}
for k,u in docs.items():
    pdf=os.path.join("cache",k+".pdf"); os.makedirs("cache",exist_ok=True)
    if not os.path.exists(pdf):
        try:
            d=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
            open(pdf,"wb").write(d)
        except Exception as e:
            print("FAIL",k,u,repr(e)); continue
    subprocess.run(["pdftotext","-layout",pdf,"tmp.txt"],check=True)
    t=open("tmp.txt",encoding="utf-8",errors="replace").read()
    open(k+".txt","w",encoding="utf-8").write(f"SOURCE {u}\n"+t)
    os.remove("tmp.txt")
    print(k,os.path.getsize(pdf),len(t))
