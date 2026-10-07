# Normalise em dashes in the run's OWN prose.
# Rules honoured:
#   - quotations keep whatever the source has (PRIME RULE 1): dashes inside a quoted
#     span are left alone;
#   - the required heading COMPUTATION <emdash> NOT A CLEARANCE is left alone;
#   - everything else becomes a plain hyphen, as the JAKK fold did for its template block.
import io, sys

P = "Test Runs/2026-09-21 Run - CRC California Resources.md"
EM = "—"
GUARD = "COMPUTATION " + EM + " NOT A CLEARANCE"
TOKEN = "\u0001GUARD\u0001"

t = io.open(P, encoding="utf-8").read()
t = t.replace(GUARD, TOKEN)

out = []
in_quote = False
changed = 0
for ch in t:
    if ch == '"':
        in_quote = not in_quote
        out.append(ch)
    elif ch == EM and not in_quote:
        out.append("-")
        changed += 1
    else:
        out.append(ch)
t = "".join(out).replace(TOKEN, GUARD)

io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("replaced", changed)
print("remaining em dashes:", t.count(EM))
