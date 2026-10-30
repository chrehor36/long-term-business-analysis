import urllib.request, ssl, time
UA={'User-Agent':'BRK research chrehor36@gmail.com'}
urls = {
 'ecb_SR_30Y.csv': 'https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y?startPeriod=2026-08-25&format=csvdata',
 'ecb_SR_10Y.csv': 'https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y?startPeriod=2026-08-25&format=csvdata',
 'ecb_EXR_USD.csv': 'https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2025-12-20&format=csvdata',
}
for fn,u in urls.items():
    for att in range(4):
        try:
            d = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
            open('sov/'+fn,'wb').write(d); print(fn, len(d)); break
        except Exception as e:
            print(fn, 'retry', att, e); time.sleep(3)
