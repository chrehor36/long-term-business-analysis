import sys, time, json
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\tools')
import sources as s
peers = {'CarMax':'0001170010','Carvana':'0001690820','AutoNation':'0000350698','Lithia':'0001023128','Sonic':'0001043509',
 'Group1':'0001031203','Asbury':'0001144980','Penske':'0001019849','CarMart':'0000799850','Vroom':'0001580864','Copart':'0000900075',
 'TrueCar':'0001327318','OPENLANE':'0001395942','ACVA':'0001637873','CarGurus':'0001494259','Cars.com':'0001683606','RBGlobal':'0001046102',
 'Experian?':None}
out={}
for name,cik in peers.items():
    if cik is None: continue
    row={}
    for ph in ['CARFAX','AutoCheck']:
        try:
            n,_=s.fts_count(ph, cik=cik, forms='10-K'); row[ph]=n
        except Exception as e:
            row[ph]='ERROR '+str(e)[:60]
        time.sleep(0.25)
    out[name]=row; print(name, row, flush=True)
json.dump(out, open('fts_dealers.json','w'), indent=1)
