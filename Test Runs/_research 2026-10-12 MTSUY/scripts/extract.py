# Pull labelled two-year figures from the Japanese annual tanshin (raw text). Arithmetic only.
import re,sys,json
sys.stdout.reconfigure(encoding='utf-8')
NUM=r'(△?[\d,]+|－|-)'
labels={
 'OCF':'営業活動によるキャッシュ・フロー',
 'ICF':'投資活動によるキャッシュ・フロー',
 'FCF_fin':'財務活動によるキャッシュ・フロー',
 'DA':'減価償却費',
 'eq_inc':'持分法による投資損益',
 'div_recv':'配当金の受取額',
 'int_recv':'利息の受取額',
 'int_paid':'利息の支払額',
 'tax_paid':'法人所得税の支払額',
 'capex':'有形固定資産等の取得による支出',
 'capex_sale':'有形固定資産等の売却による収入',
 'invprop':'投資不動産の取得による支出',
 'invprop_sale':'投資不動産の売却による収入',
 'eqm_buy':'持分法で会計処理される投資の取得による支出',
 'eqm_sell':'持分法で会計処理される投資の売却による収入',
 'biz_buy':'事業の取得による支出',
 'biz_sell':'事業の売却による収入',
 'oth_buy':'その他の投資の取得による支出',
 'oth_sell':'その他の投資の売却による収入',
 'loan_out':'貸付けの実行による支出',
 'loan_in':'貸付金の回収による収入',
 'lease_rep':'リース負債の返済による支出',
 'div_paid':'当社の所有者への配当金の支払額',
 'div_nci':'非支配持分への配当金の支払額',
 'nci_buy':'非支配持分からの子会社持分取得による支出',
 'treas':'自己株式の取得及び売却',
 'cash':'現金及び現金同等物の期末残高',
 'assets':'資産合計',
 'eq_parent':'当社の所有者に帰属する持分合計',
 'equity':'資本合計',
 'NI_parent':'当社の所有者に帰属する当期純利益',
 'tax':'法人所得税',
 'pbt':'税引前利益',
 'fin_cost':'支払利息',
}
def grab(txt,lab):
    for line in txt.splitlines():
        if lab in line:
            m=re.findall(NUM,line[line.index(lab)+len(lab):])
            m=[x for x in m if x not in('-',)]
            if len(m)>=2: return m[-2:]
    return None
def num(s):
    if s in (None,'－','-'):return 0
    s=s.replace(',','');neg=s.startswith('△');s=s.lstrip('△')
    return -int(s) if neg else int(s)
out={}
for fy in sys.argv[1:]:
    t=open(f'cache/tan_{fy}_raw.txt',encoding='utf-8').read()
    out[fy]={k:(lambda g:[num(g[0]),num(g[1])] if g else None)(grab(t,v)) for k,v in labels.items()}
json.dump(out,open('extract.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
for k in labels:
    print(k.ljust(12),' '.join(f"{fy}:{out[fy][k]}" for fy in out))
