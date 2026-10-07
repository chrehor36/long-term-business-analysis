import json, sys
cik, tag, pref = sys.argv[1], sys.argv[2], sys.argv[3]
f = json.load(open(f'facts_{cik}.json', encoding='utf-8'))
for it in f['facts']['us-gaap'][tag]['units']['USD']:
    if it['end'].startswith(pref):
        print(it.get('form'), it.get('fp'), it.get('start'), it['end'],
              format(it['val'], ','), it['accn'])
