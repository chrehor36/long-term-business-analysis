# OVERNIGHT CYCLE - launched by the Windows Scheduled Task "BRK-overnight".
# One bounded unit of queue work per cycle, under a lock so cycles never overlap.
# WORK HOURS ONLY (2026-10-26, the operator's word: "only during work hours. 8-4 est m-f"). The task fires every
# 30 minutes on weekdays; a cycle starts only between 08:00 and 15:15 local (the PC is on Eastern time), so the
# last one ends near 16:00. -DryRun stops after the hours and lock checks, for testing.
# TEN A DAY, AND AN AUDIT (2026-10-26, the operator's word: "limit it to 10 runs a day and have you audit them"). At most
# ten cycles start on a day (counted from this trace). -Audit runs `_audit_prompt.md` instead, once a weekday after the
# runs (16:00 to 18:30), skipping if today's audit addendum already exists, and shows its one-line result on screen.
param([switch]$DryRun, [switch]$Audit)
$MaxCyclesPerDay = 10
$ErrorActionPreference = "Continue"
$repo   = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path   # was the OneDrive path until the move of 2026-10-25
$dir    = Join-Path $repo "Screens\_daily"
# THE BINARY IS RESOLVED EACH CYCLE, NOT HARDCODED. The path embeds the extension version, so a
# VS Code auto-update overnight would have made every cycle abort. Newest installed version wins.
$exe = Get-ChildItem -Path "$env:USERPROFILE\.vscode\extensions" -Directory -Filter "anthropic.claude-code-*" -ErrorAction SilentlyContinue |
       Sort-Object { [version](($_.Name -replace '^anthropic\.claude-code-','') -replace '-.*$','') } -Descending |
       ForEach-Object { Join-Path $_.FullName "resources\native-binary\claude.exe" } |
       Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
$prompt = Join-Path $dir $(if ($Audit) { "_audit_prompt.md" } else { "_overnight_prompt.md" })
$kind   = if ($Audit) { "audit" } else { "cycle" }
$lock   = Join-Path $dir "_overnight.lock"
$logdir = Join-Path $dir "_overnight_logs"
New-Item -ItemType Directory -Force -Path $logdir | Out-Null
$stamp  = (Get-Date).ToString("yyyy-MM-dd_HHmm")
$runlog = Join-Path $logdir "cycle_$stamp.log"
$trace  = Join-Path $logdir "_scheduler_trace.log"

function Trace($m) { Add-Content -LiteralPath $trace -Value ("{0}  {1}" -f (Get-Date).ToString("yyyy-MM-dd HH:mm:ss"), $m) }

# ---- THE HOURS. Checked before the lock, so a cycle outside them touches nothing.
$now = Get-Date
$today = $now.ToString("yyyy-MM-dd")
$weekday = $now.DayOfWeek -notin @([DayOfWeek]::Saturday, [DayOfWeek]::Sunday)
if ($Audit) {
    $inHours = $now.TimeOfDay -ge [TimeSpan]"16:00" -and $now.TimeOfDay -le [TimeSpan]"18:30"
    if (-not ($weekday -and $inHours)) { Trace "SKIP audit - outside audit hours"; if ($DryRun) { "outside audit hours" }; exit 0 }
    if (Get-ChildItem -LiteralPath (Join-Path $repo "Test Runs") -Filter "ADDENDUM $today - the automated runs of $today audited*" -ErrorAction SilentlyContinue) {
        Trace "SKIP audit - today's audit addendum exists"; if ($DryRun) { "already audited today" }; exit 0 }
    if ((Test-Path -LiteralPath (Join-Path $dir "_audit_result.txt")) -and ((Get-Content -LiteralPath (Join-Path $dir "_audit_result.txt") -Raw) -match "^$today")) {
        Trace "SKIP audit - today's audit already ran (nothing to audit or recorded)"; if ($DryRun) { "already audited today" }; exit 0 }
} else {
    $inHours = $now.TimeOfDay -ge [TimeSpan]"08:00" -and $now.TimeOfDay -le [TimeSpan]"15:15"
    if (-not ($weekday -and $inHours)) { Trace "SKIP - outside work hours ($($now.DayOfWeek) $($now.ToString('HH:mm')))"; if ($DryRun) { "outside work hours" }; exit 0 }
    # A cycle that ended RATE LIMITED within five minutes of starting did no work and does not count (2026-10-28: on
    # 2026-10-27 four such cycles, each dead in two seconds, used up the cap at 12:30 after six real runs).
    $starts = @{}; $idle = 0
    foreach ($l in (Get-Content -LiteralPath $trace -ErrorAction SilentlyContinue)) {
        if ($l -match "^(\S+ \S+)\s+START cycle ($today\S*)") { $starts[$Matches[2]] = [datetime]$Matches[1] }
        elseif ($l -match "^(\S+ \S+)\s+END cycle ($today\S*) - RATE LIMITED" -and $starts.ContainsKey($Matches[2])) {
            if (([datetime]$Matches[1] - $starts[$Matches[2]]).TotalMinutes -lt 5) { $idle++ } }
    }
    $started = $starts.Count - $idle
    if ($started -ge $MaxCyclesPerDay) { Trace "SKIP - daily cap reached ($started of $MaxCyclesPerDay cycles started today)"; if ($DryRun) { "daily cap reached" }; exit 0 }
}

# ---- THE LOCK. A single run has taken 25-40 minutes; an hourly trigger must never start a
# second session on top of one - concurrent runs in this tree have crossed commits five times.
if (Test-Path -LiteralPath $lock) {
    $raw = Get-Content -LiteralPath $lock -Raw
    $lockPid = 0; [int]::TryParse(($raw -split "\s+")[0], [ref]$lockPid) | Out-Null
    $ageMin = ((Get-Date) - (Get-Item -LiteralPath $lock).LastWriteTime).TotalMinutes
    $alive = $lockPid -gt 0 -and (Get-Process -Id $lockPid -ErrorAction SilentlyContinue)
    # AN INTERACTIVE HOLDER GETS 75 MINUTES, NOT 180 (2026-09-13). The interactive session hit the
    # session limit at ~07:46 with the lock freshly written; its process stayed alive but idle, so
    # the 08:35 and 09:35 cycles both SKIPPED after the limit had reset. An interactive session
    # refreshes the lock on every run it launches or folds, so 75 quiet minutes means it is waiting,
    # not working. A headless cycle keeps 180 (one run has taken up to 45 minutes).
    # AN INTERACTIVE LOCK IS HONOURED BY AGE ALONE (2026-09-19, found by the 20:31 cycle).
    # The interactive session writes a PID it believes is its own, and that PID was NOT alive:
    # the trace records "stale lock (pid 21248 alive=False)" at 15:31, 17:31 and 20:31, so three
    # cycles walked through a lock that was being refreshed every few minutes, and two agents ran
    # AIG. A session inside an agent harness cannot reliably name its own OS process, but it CAN
    # prove it is working by rewriting the file - which it does on every launch and every fold.
    # So: an "interactive" lock is respected while it is FRESH, whatever the PID says; a headless
    # cycle's lock still needs a live PID, because a cycle that died leaves a file nobody rewrites.
    $interactive = $raw -match "interactive"
    if ($interactive -and $ageMin -lt 75) {
        Trace "SKIP - interactive session holds the lock, refreshed $([int]$ageMin) min ago"; exit 0
    }
    if (-not $interactive -and $alive -and $ageMin -lt 180) {
        Trace "SKIP - previous cycle pid $lockPid still running ($([int]$ageMin) min)"; exit 0
    }
    Trace "stale lock (interactive=$interactive, pid $lockPid alive=$([bool]$alive), $([int]$ageMin) min) - taking over"
}
if (-not $exe -or -not (Test-Path -LiteralPath $exe)) { Trace "ABORT - no claude.exe found under the VS Code extensions folder"; exit 1 }
if ($DryRun) { "DRY RUN ($kind): in hours, lock free, repo $repo, prompt $(Split-Path $prompt -Leaf)"; exit 0 }
Set-Content -LiteralPath $lock -Value "$PID $(Get-Date -Format s)"
Trace "START $kind $stamp (pid $PID)"

try {
    Set-Location -LiteralPath $repo
    $text = Get-Content -LiteralPath $prompt -Raw
    # ESCAPE EMBEDDED DOUBLE QUOTES (2026-10-03, found by the v5 read cycle's first unit, which runs the
    # same invocation). PowerShell 5.1 does not escape quotes inside a native argument, so the Windows
    # command line ended this prompt at its first `"` (section 3, the BAM/BN paragraph) and every cycle
    # since that paragraph was written received sections 1 to 3 only. The cycles worked because the
    # prompt's early sections send the session to the files. \" is read back as a literal quote.
    $text = $text.Replace('"', '\"')
    & $exe -p $text --model opus --dangerously-skip-permissions *>&1 | Out-File -FilePath $runlog -Encoding utf8
    $code = $LASTEXITCODE
    $tail = (Get-Content -LiteralPath $runlog -Tail 40 -ErrorAction SilentlyContinue) -join "`n"
    if ($tail -match "rate.?limit|usage limit|session limit|hit your|429|reached your") {
        Trace "END cycle $stamp - RATE LIMITED (exit $code); next cycle retries"
    } else {
        Trace "END $kind $stamp - exit $code"
    }
    if ($Audit) {
        $res = Join-Path $dir "_audit_result.txt"
        $msg = if ((Test-Path -LiteralPath $res) -and ((Get-Content -LiteralPath $res -Raw) -match "^$today")) { (Get-Content -LiteralPath $res -Raw).Trim() } else { "$today : the audit session ended without writing a result (exit $code). See $runlog" }
        Add-Type -AssemblyName PresentationFramework
        [System.Windows.MessageBox]::Show($msg, "BRK daily audit") | Out-Null
    }
} catch {
    Trace "ERROR cycle $stamp - $($_.Exception.Message)"
} finally {
    # RELEASE ONLY YOUR OWN LOCK (2026-09-19). This deleted whatever lock file existed, including
    # an interactive session's. On 2026-09-19 the 14:31 cycle finished GFF and removed the
    # interactive lock written at 15:06; the 15:31 cycle then saw no lock and dispatched AIG, which
    # an interactive agent was already running - two agents, one run-file path, 562 committed lines
    # nearly overwritten. Only the write-early protocol and one agent committing first prevented it.
    $held = $null
    if (Test-Path -LiteralPath $lock) { $held = (Get-Content -LiteralPath $lock -Raw) }
    if ($held -and ($held -split "\s+")[0] -eq "$PID") {
        Remove-Item -LiteralPath $lock -Force -ErrorAction SilentlyContinue
    } elseif ($held) {
        Trace "lock left in place - held by $((($held -split '\s+')[0])), not this cycle ($PID)"
    }
}



