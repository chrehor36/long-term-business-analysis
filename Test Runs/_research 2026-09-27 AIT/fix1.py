import io
base = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs'
old_run = '''  1. **The brief's pointer to the "Next in the order file" line is wrong**: it says the III fold wrote "Next in the order file: AIT." near line 22539 of `Screens/WATCHLIST RUN QUEUE.md`; that file has 16,020 lines and no such line for AIT (the III register entry carries none; "Next: AIT" is in the OVERNIGHT LOG line and the III commit message). The AIT register entry carries its own next-name line.'''
new_run = '''  1. **The brief's pointer to the "Next in the order file" line names the wrong file**: it places the III fold's "Next in the order file: AIT." near line 22539 of `Screens/WATCHLIST RUN QUEUE.md`, which has 16,020 lines and no such line; the line is line 22539 of `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, the last line of the III narrative fold. That file is append-only and each fold ends with its own next-name line, so it is not edited; the AIT narrative fold ends with "Next in the order file: CSCO." and the AIT register entry carries the same.'''
old_reg = '''(1) the brief's pointer to a "Next in the order file: AIT." line near line 22539 of this file is wrong (the file has 16,020 lines; no such line; "Next: AIT" is in the OVERNIGHT LOG);'''
new_reg = '''(1) the brief places the III fold's "Next in the order file: AIT." line near line 22539 of this file, which has 16,020 lines; it is line 22539 of the reading list (append-only, not edited; the AIT fold appends its own next-name line);'''
for p, a, b in ((base + r'\2026-09-27 Run - AIT Applied Industrial Technologies.md', old_run, new_run),
                (base + r'\_research 2026-09-27 AIT\body_audit.md', old_run, new_run),
                (base + r'\_research 2026-09-27 AIT\register_entry.md', old_reg, new_reg)):
    s = open(p, encoding='utf-8').read()
    assert a in s, p
    open(p, 'w', encoding='utf-8').write(s.replace(a, b))
print('ok')
