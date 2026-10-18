"""Parse cache/stmts_<year>.txt into a table of the current-year column for chosen lines.
Arithmetic aid only: every figure is checked against the filed statement for the one cross-check
recorded in the run file. Output: data_statements.csv (RMB'000).
usage: python -I parse_statements.py <cache_dir> <out_csv>"""
import sys, re, os, csv

cache, out = sys.argv[1], sys.argv[2]
NUM = r"\(?-?[\d,]+(?:\.\d+)?\)?|–|-"
ITEMS = [
    # key, section, regex on the joined label (lowercase), take nth occurrence (0 first)
    ("cash", "bs", r"^cash and bank balances"),
    ("notes_rec", "bs", r"^(bills|notes) receivable"),
    ("ar", "bs", r"^accounts receivable"),
    ("rec_fin", "bs", r"^receivables financing"),
    ("prepay", "bs", r"^prepayments"),
    ("other_rec", "bs", r"^other receivables"),
    ("inventories", "bs", r"^inventories"),
    ("contract_assets", "bs", r"^contract assets"),
    ("nca_due1y", "bs", r"^non-current assets due within one year"),
    ("total_current_assets", "bs", r"^total current assets"),
    ("lt_rec", "bs", r"^long-term receivables"),
    ("lt_equity_inv", "bs", r"^long-term equity investments"),
    ("inv_property", "bs", r"^investment propert"),
    ("fixed_assets", "bs", r"^fixed assets"),
    ("cip", "bs", r"^construction in progress"),
    ("intangibles", "bs", r"^intangible assets"),
    ("goodwill", "bs", r"^goodwill"),
    ("other_nca", "bs", r"^other non-current assets"),
    ("total_assets", "bs", r"^total assets"),
    ("st_borrow", "bs", r"^short-term borrowings"),
    ("notes_pay", "bs", r"^(bills|notes) payable"),
    ("ap", "bs", r"^accounts payable"),
    ("receipts_adv", "bs", r"^receipts in advance"),
    ("contract_liab", "bs", r"^contract liabilities"),
    ("other_pay", "bs", r"^other payables"),
    ("ncl_due1y", "bs", r"^non-current liabilities due within one year"),
    ("other_cl", "bs", r"^other current liabilities"),
    ("total_current_liab", "bs", r"^total current liabilities"),
    ("lt_borrow", "bs", r"^long-term borrowings"),
    ("bonds", "bs", r"^bonds payable"),
    ("lease_liab", "bs", r"^lease liabilities"),
    ("lt_payables", "bs", r"^long-term payables"),
    ("total_liab", "bs", r"^total liabilities$|^total liabilities \d"),
    ("perpetual", "bs", r"^other equity instruments"),
    ("retained", "bs", r"^retained (profits|earnings)"),
    ("equity_attrib", "bs", r"^total (shareholders. )?equity attributable"),
    ("minority", "bs", r"^(non-controlling|minority) interests"),
    ("total_equity", "bs", r"^total shareholders. equity"),
    ("revenue", "is", r"^(i\. )?(total )?operating revenue"),
    ("op_costs", "is", r"^including: operating costs|^operating costs"),
    ("taxes_levies", "is", r"^taxes and (levies|surcharges)"),
    ("selling", "is", r"^selling expenses"),
    ("admin", "is", r"^administrative expenses"),
    ("rnd", "is", r"^research and development"),
    ("fin_exp", "is", r"^financ(e|ial) expenses"),
    ("interest_exp", "is", r"^including: interest expense"),
    ("interest_inc", "is", r"^interest income"),
    ("inv_income", "is", r"^investment (income|gains|losses)|^add: investment"),
    ("assoc", "is", r"from investments? in associates"),
    ("credit_impair", "is", r"^credit impairment"),
    ("asset_impair", "is", r"^(asset )?impairment losses|^impairment losses of assets|^asset impairment"),
    ("op_profit", "is", r"^iii\. operating profit|^operating profit"),
    ("total_profit", "is", r"^iv\. total profit|^total profit"),
    ("tax", "is", r"^less: income tax|^income tax expense"),
    ("net_profit", "is", r"^v\. net profit$|^v\. net profit \(|^v\. net profit \d"),
    ("np_attrib", "is", r"^net profit attributable to shareholders"),
    ("np_minority", "is", r"^profit or loss attributable to non-controlling|^profit or loss attributable to minority|^minority interests"),
    ("np_discontinued", "is", r"net profit from discontinued"),
    ("eps", "is", r"^\(i\) basic earnings per share"),
    ("cfo", "cf", r"^net cash flows? (from|generated from) operating"),
    ("capex", "cf", r"^cash payments? (to acquire|for acquisition|for purchase)[^,]*fixed"),
    ("fa_disposal", "cf", r"^net cash receipts from disposals? of fixed"),
    ("acq_subs", "cf", r"^(net )?cash payments? (to acquire|for acquisition of) subsidiaries"),
    ("disp_subs", "cf", r"^net cash receipts from disposal of subsidiaries"),
    ("cfi", "cf", r"^net cash flows? (from|generated from|used in) investing"),
    ("div_int_paid", "cf", r"^cash payments for distribution of dividends"),
    ("div_to_nci", "cf", r"^including: payments for distribution of dividends|^including: dividends or profits paid to non-controlling"),
    ("cff", "cf", r"^net cash flows? (from|generated from|used in) financing"),
    ("cash_eq_close", "cf", r"closing balance of cash and cash equivalents"),
]


def parse_num(tok):
    if tok in ("–", "-"):
        return 0
    neg = tok.startswith("(")
    v = float(tok.strip("()").replace(",", ""))
    return -v if neg else v


def section_of(header):
    h = header.lower()
    if "balance sheet" in h:
        return "bs"
    if "income statement" in h:
        return "is"
    if "cash flow" in h:
        return "cf"
    return None


results = {}
for fn in sorted(os.listdir(cache)):
    m = re.match(r"stmts_(\d{4})\.txt$", fn)
    if not m:
        continue
    year = m.group(1)
    lines = open(os.path.join(cache, fn), encoding="utf-8").read().split("\n")
    sec = None
    buf = ""
    got = {}
    page_head = []
    for ln in lines:
        if ln.startswith("=== page"):
            page_head = []
            sec_line_count = 0
            continue
        page_head.append(ln)
        if len(page_head) <= 8:
            s = section_of(ln)
            if s:
                sec = s
                buf = ""
                continue
        toks = ln.split(" ")
        # strip trailing numeric tokens
        nums = []
        while toks and re.fullmatch(NUM, toks[-1]):
            nums.insert(0, toks.pop())
        own = " ".join(toks).strip()
        label = (buf + " " + own).strip()
        label = re.sub(r"\s+(vii\s?\d+(\(\d\))?|xv\d|note.*|\d{1,2})$", "", label.lower()).strip()
        label = re.sub(r"\bvii\s?\d+(\(\d\))?\b", "", label).strip()
        if not nums:
            buf = label if len(label) < 160 else ""
            continue
        buf = ""
        # with a note column the first token may be the note number (1-2 digits, no comma)
        if len(nums) >= 3 and re.fullmatch(r"\d{1,2}", nums[0]):
            nums = nums[1:]
        if len(nums) < 2:
            continue
        for key, s, rx in ITEMS:
            ownl = re.sub(r"vii\s?\d+(\(\d\))?", "", own.lower()).strip()
            if s == sec and key not in got and (re.search(rx, label) or re.search(rx, ownl)):
                got[key] = parse_num(nums[0])
    results[year] = got

years = sorted(results)
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["item"] + years)
    for key, s, rx in ITEMS:
        w.writerow([key] + [results[y].get(key, "") for y in years])
print("wrote", out)
