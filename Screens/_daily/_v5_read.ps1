# v5 READ CYCLE - launched hourly by the Windows Scheduled Task "BRK-v5-read" (2026-10-03).
# One meeting session per cycle, read blind for ledger rows, under the SAME lock as the overnight
# queue cycle so the two can never run together (one git index, one usage budget). The lock,
# binary-resolution and release logic are copied from _overnight.ps1 unchanged; only the prompt,
# the log folder and the trace wording differ. The prompt file is the document that says what a
# cycle does: Screens\_daily\_v5_read_prompt.md.
$ErrorActionPreference = "Continue"
$repo   = "C:\Users\chreh\OneDrive\Documents\BRK"
$dir    = Join-Path $repo "Screens\_daily"
# THE BINARY IS RESOLVED EACH CYCLE, NOT HARDCODED (see _overnight.ps1).
$exe = Get-ChildItem -Path "$env:USERPROFILE\.vscode\extensions" -Directory -Filter "anthropic.claude-code-*" -ErrorAction SilentlyContinue |
       Sort-Object { [version](($_.Name -replace '^anthropic\.claude-code-','') -replace '-.*$','') } -Descending |
       ForEach-Object { Join-Path $_.FullName "resources\native-binary\claude.exe" } |
       Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
$prompt = Join-Path $dir "_v5_read_prompt.md"
$lock   = Join-Path $dir "_overnight.lock"      # SHARED with the overnight cycle, on purpose
$logdir = Join-Path $dir "_v5_logs"
New-Item -ItemType Directory -Force -Path $logdir | Out-Null
$stamp  = (Get-Date).ToString("yyyy-MM-dd_HHmm")
$runlog = Join-Path $logdir "cycle_$stamp.log"
$trace  = Join-Path $logdir "_scheduler_trace.log"

function Trace($m) { Add-Content -LiteralPath $trace -Value ("{0}  {1}" -f (Get-Date).ToString("yyyy-MM-dd HH:mm:ss"), $m) }

# ---- THE LOCK, verbatim from _overnight.ps1: an interactive holder is honoured while fresh under
# 75 minutes whatever its PID says; a headless holder needs a live PID under 180 minutes.
if (Test-Path -LiteralPath $lock) {
    $raw = Get-Content -LiteralPath $lock -Raw
    $lockPid = 0; [int]::TryParse(($raw -split "\s+")[0], [ref]$lockPid) | Out-Null
    $ageMin = ((Get-Date) - (Get-Item -LiteralPath $lock).LastWriteTime).TotalMinutes
    $alive = $lockPid -gt 0 -and (Get-Process -Id $lockPid -ErrorAction SilentlyContinue)
    $interactive = $raw -match "interactive"
    if ($interactive -and $ageMin -lt 75) {
        Trace "SKIP v5 - interactive session holds the lock, refreshed $([int]$ageMin) min ago"; exit 0
    }
    if (-not $interactive -and $alive -and $ageMin -lt 180) {
        Trace "SKIP v5 - previous cycle pid $lockPid still running ($([int]$ageMin) min)"; exit 0
    }
    Trace "stale lock (interactive=$interactive, pid $lockPid alive=$([bool]$alive), $([int]$ageMin) min) - v5 taking over"
}
if (-not $exe -or -not (Test-Path -LiteralPath $exe)) { Trace "ABORT v5 - no claude.exe found under the VS Code extensions folder"; exit 1 }
# First token PID, second the time, third a tag; _overnight.ps1 reads only the first and tests for "interactive".
Set-Content -LiteralPath $lock -Value "$PID $(Get-Date -Format s) v5"
Trace "START v5 cycle $stamp (pid $PID)"

try {
    Set-Location -LiteralPath $repo
    $text = Get-Content -LiteralPath $prompt -Raw
    # ESCAPE EMBEDDED DOUBLE QUOTES (2026-10-03, found by the first unit's own error report). PowerShell
    # 5.1 wraps a native argument in quotes but does not escape quotes inside it, so the Windows command
    # line ended the prompt at the first `"` in section 3 and the session received sections 1 to 3 only.
    # CommandLineToArgvW reads \" as a literal quote, so the whole file now arrives.
    $text = $text.Replace('"', '\"')
    & $exe -p $text --model opus --dangerously-skip-permissions *>&1 | Out-File -FilePath $runlog -Encoding utf8
    $code = $LASTEXITCODE
    $tail = (Get-Content -LiteralPath $runlog -Tail 40 -ErrorAction SilentlyContinue) -join "`n"
    if ($tail -match "rate.?limit|usage limit|session limit|hit your|429|reached your") {
        Trace "END v5 cycle $stamp - RATE LIMITED (exit $code); next cycle retries"
    } else {
        Trace "END v5 cycle $stamp - exit $code"
    }
} catch {
    Trace "ERROR v5 cycle $stamp - $($_.Exception.Message)"
} finally {
    # RELEASE ONLY YOUR OWN LOCK (the 2026-09-19 rule; see _overnight.ps1).
    $held = $null
    if (Test-Path -LiteralPath $lock) { $held = (Get-Content -LiteralPath $lock -Raw) }
    if ($held -and ($held -split "\s+")[0] -eq "$PID") {
        Remove-Item -LiteralPath $lock -Force -ErrorAction SilentlyContinue
    } elseif ($held) {
        Trace "lock left in place - held by $((($held -split '\s+')[0])), not this cycle ($PID)"
    }
}
