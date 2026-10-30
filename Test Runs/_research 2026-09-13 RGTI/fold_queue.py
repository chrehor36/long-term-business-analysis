import io
p = "Screens/WATCHLIST RUN QUEUE.md"
s = io.open(p, encoding="utf-8").read()
old_roster = "~~SWK~~, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ~~ROKU~~, RGTI, ~~ORCL~~"
assert s.count(old_roster) == 1
s = s.replace(old_roster, "~~SWK~~, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ~~ROKU~~, ~~RGTI~~, ~~ORCL~~")
anchor = "meanwhile is what happened here — the tool failed loudly, concluded nothing, and the filing\n  decided.**"
assert s.count(anchor) == 1
note = io.open("Test Runs/_research 2026-09-13 RGTI/fold_triage_note.md", encoding="utf-8").read().rstrip("\n")
s = s.replace(anchor, anchor + "\n" + note)
head = "## COMPLETED FROM THE QUEUE\n"
assert s.count(head) == 1
entry = io.open("Test Runs/_research 2026-09-13 RGTI/fold_entry.md", encoding="utf-8").read()
s = s.replace(head, head + entry)
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
