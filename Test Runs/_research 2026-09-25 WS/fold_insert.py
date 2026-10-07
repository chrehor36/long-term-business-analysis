import subprocess, sys
R = r"C:\Users\chreh\OneDrive\Documents\BRK"
D = R + r"\Test Runs\_research 2026-09-25 WS"
Q = "Screens/WATCHLIST RUN QUEUE.md"
HEAD_H = "## COMPLETED FROM THE QUEUE"
entry = open(D + r"\register_entry.md", encoding="utf-8").read().rstrip("\n").split("\n")


def insert(text):
    L = text.split("\n")
    h = [i for i, l in enumerate(L) if l == HEAD_H]
    assert len(h) == 1, h
    w = [i for i, l in enumerate(L) if l.startswith("## THE WRITE-EARLY PROTOCOL")]
    assert len(w) == 1, w
    before = sum(1 for l in L[h[0] + 1:w[0]] if l.startswith("- **"))
    assert not any(l.startswith("- **WS ") for l in L[h[0] + 1:w[0]]), "duplicate"
    L2 = L[:h[0] + 1] + entry + L[h[0] + 1:]
    h2 = [i for i, l in enumerate(L2) if l == HEAD_H][0]
    w2 = [i for i, l in enumerate(L2) if l.startswith("## THE WRITE-EARLY PROTOCOL")][0]
    sl = [l for l in L2[h2 + 1:w2] if l.startswith("- **")]
    after = len(sl)
    assert sl[0].startswith("- **WS "), sl[0][:40]
    assert sum(1 for l in sl if l.startswith("- **WS ")) == 1
    return "\n".join(L2), before, after, h[0], w[0]


# 1. HEAD blob + entry -> index
head = subprocess.run(["git", "show", "HEAD:" + Q], cwd=R, capture_output=True).stdout.decode("utf-8")
staged, b, a, hi, wi = insert(head)
print("HEAD blob: heading", hi, "write-early", wi, "entries", b, "->", a)
open(D + r"\q_staged.md", "w", encoding="utf-8", newline="").write(staged)
blob = subprocess.run(["git", "hash-object", "-w", "--stdin"], cwd=R, input=staged.encode("utf-8"),
                      capture_output=True).stdout.decode().strip()
mode = subprocess.run(["git", "ls-files", "-s", Q], cwd=R, capture_output=True).stdout.decode().split()[0]
subprocess.run(["git", "update-index", "--cacheinfo", f"{mode},{blob},{Q}"], cwd=R, check=True)
print("staged blob", blob, "mode", mode)

# 2. same insert into the working tree (keeps the CRM hunks)
wt_path = R + "\\" + Q.replace("/", "\\")
raw = open(wt_path, "rb").read()
crlf = b"\r\n" in raw
wt = raw.decode("utf-8").replace("\r\n", "\n")
wt2, b2, a2, hi2, wi2 = insert(wt)
print("working tree: heading", hi2, "write-early", wi2, "entries", b2, "->", a2, "crlf", crlf)
out = wt2.replace("\n", "\r\n") if crlf else wt2
open(wt_path, "wb").write(out.encode("utf-8"))
