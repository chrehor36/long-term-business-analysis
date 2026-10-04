$repo = "C:\Users\chreh\OneDrive\Documents\BRK"
$out  = Join-Path $repo "Screens\_daily\WAKE - four-hour timer fired.md"
$body = @"
# WAKE NOTE - the four-hour timer fired

Set 2026-09-12 at 18:35 local (22:35 GMT) by the Opus session, to fire at 22:35 local as a Windows Scheduled Task, so it survives
the session ending. The in-session background sleep pings only a LIVE session; this file is the
durable layer and needs no session at all.

## Resume here
- Read first: Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md - every tooling
  change made that session, six of my own errors, and eight source limits already tested.
- Standing count 73 runs: 26 gate-clearers all failed at Q5 on price, 44 Q2 OUT, 2 Q4 OUT
  (ORCL, ARM), 1 Q1 UNKNOWABLE (HHH).
- In flight when the timer was set: SWK and ACMR, launched 22:20. Check whether they folded
  themselves (register entry, roster strike, narrative fold) before doing it for them.
- Remaining unrun: ALKT, ACVA, FLNC, NEGG, plus CNR (the CONSOL/Arch merger - build owner
  earnings pro forma from both predecessors) and RGTI (at-the-market dilution, not a perimeter
  change, so runnable with the ground stated).
- The queue is 331 priced, not 361: the SBC-of-zero fix moved 30 names to unpriced with the
  ground stated, and 27 of those were never run and had been ranked on an overstated yield.
- Two armed bands carry a live-deal annotation: ACLS is party to a real merger so its band
  tracks deal terms, and AVGO was read and cleared as an exchange offer.

Fired: TIMESTAMP
"@
$body = $body.Replace("TIMESTAMP", (Get-Date).ToString("yyyy-MM-dd HH:mm:ss"))
Set-Content -Path $out -Value $body -Encoding utf8

