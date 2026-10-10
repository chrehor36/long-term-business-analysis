"""Pull the segment sentences (EIG and EMG net sales, operating income, organic growth, acquisition spend)
from each 10-K's MD&A text in cache/k<year>.txt, for reading; prints the matching sentences per year to
cache/segments_out.txt. Transcription aid only: the figures in the run file are read from these sentences."""
import re, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
out = []
pats = [
    r"(?:EIG|Electronic Instruments Group)[’'`s ]*(?:net )?sales (?:for \d{4} )?(?:were|totaled).{0,330}",
    r"(?:EIG|Electronic Instruments Group)[’'`s ]*operating income.{0,330}",
    r"(?:EMG|Electromechanical Group)[’'`s ]*(?:net )?sales (?:for \d{4} )?(?:were|totaled).{0,330}",
    r"(?:EMG|Electromechanical Group)[’'`s ]*operating income.{0,330}",
    r"[Ss]egment operating income for \d{4} was.{0,330}",
    r"[Nn]et sales for \d{4} were.{0,400}",
    r"(?:spent|paid) \$[\d,.]+ (?:million|billion)[^.]{0,250}(?:acqui|purchase)[^.]{0,250}\.",
]
for f in sorted(glob.glob(os.path.join(HERE, "cache", "k20??.txt"))):
    y = os.path.basename(f)[1:5]
    t = open(f, encoding="utf-8").read().replace("\n", " ")
    i = t.find("Results of Operations")
    seen = set()
    out.append(f"\n######## FY{y}")
    for p in pats:
        for m in re.finditer(p, t):
            s = re.sub(r"\s+", " ", m.group(0))
            if s not in seen and len(seen) < 40:
                seen.add(s); out.append("  - " + s[:600])
open(os.path.join(HERE, "cache", "segments_out.txt"), "w", encoding="utf-8").write("\n".join(out))
