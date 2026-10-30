# ============================================================
#  brk-meetings.ps1
#  Personal study copies of Berkshire annual meeting transcripts
#  from berkshire.memorex.ai - saved as one .txt per meeting.
#
#  The site is a Vue 3 SPA (index.html is an empty shell), but its
#  data comes from a plain JSON API:
#    GET /api/documents          -> list of {id, metadata:{type,title,year,...}}
#    GET /api/documents/{id}     -> {id, metadata, html}   (html = transcript body)
#  Confirmed by reading /js/Root.js, which is what the app itself
#  calls on load and on navigation.
#
#  Modes:
#    1) probe   - sanity-check the API is reachable/shaped as expected
#    2) index   - list all documents and pick out the annual meetings
#    3) scrape  - download each meeting's html, convert to text, save .txt
#
#  Usage:
#    .\brk-meetings.ps1 -Mode probe
#    .\brk-meetings.ps1 -Mode index
#    .\brk-meetings.ps1 -Mode scrape
#
#  Keep the output for personal study only - the archive's notice
#  prohibits reproduction/distribution.
# ============================================================

param(
    [ValidateSet("probe","index","scrape")]
    [string]$Mode = "probe",

    # A known-good document id to probe (1994 annual meeting transcript)
    [string]$ProbeId = "c07efcd8-c21e-4dae-8a7f-72052fd2152c",

    [string]$BaseUrl  = "https://berkshire.memorex.ai",
    [string]$OutDir   = $PSScriptRoot,

    # Seconds between requests. Be a polite guest on a free site.
    [int]$DelaySec = 3
)

$UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PersonalArchive/1.0"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

function Get-Json([string]$u) {
    Invoke-RestMethod -Uri $u -UserAgent $UA
}

# Turn the transcript's HTML body into plain, readable text.
function Convert-HtmlToText([string]$html) {
    $t = $html
    $t = $t -replace '(?s)<h1[^>]*>(.*?)</h1>', "`n`n# `$1`n`n"
    $t = $t -replace '(?s)<h2[^>]*>(.*?)</h2>', "`n`n## `$1`n`n"
    $t = $t -replace '(?s)<h3[^>]*>(.*?)</h3>', "`n`n### `$1`n`n"
    $t = $t -replace '(?s)<p[^>]*>(.*?)</p>', "`$1`n`n"
    $t = $t -replace '<br\s*/?>', "`n"
    $t = $t -replace '(?s)<[^>]+>', ''
    $t = [System.Net.WebUtility]::HtmlDecode($t)
    $lines = ($t -split "`n") | ForEach-Object { $_.Trim() }
    $t = ($lines -join "`n") -replace '(\r?\n){3,}', "`n`n"
    return $t.Trim()
}

function Save-Text([string]$name, [string]$text) {
    $safe = ($name -replace '[\\/:*?"<>|]', '-').Trim()
    $path = Join-Path $OutDir "$safe.txt"
    $text | Out-File -FilePath $path -Encoding UTF8
    Write-Host "Saved: $path  ($([math]::Round($text.Length/1kb)) KB)"
}

# ------------------------------------------------------------
# MODE 1: PROBE - confirm the API shape hasn't changed
# ------------------------------------------------------------
if ($Mode -eq "probe") {
    Write-Host "Probing $BaseUrl/api/documents/$ProbeId ..." -ForegroundColor Cyan
    try {
        $doc = Get-Json "$BaseUrl/api/documents/$ProbeId"
    } catch {
        Write-Host "FAILED to reach API: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "The API may have moved. Manual fallback:"
        Write-Host "  Open $BaseUrl/viewer/$ProbeId in a browser, F12 -> Network -> XHR,"
        Write-Host "  reload, and find the request that returns the transcript JSON."
        return
    }
    if ($doc.html) {
        Write-Host "OK - /api/documents/{id} returns an 'html' field ($($doc.html.Length) chars)." -ForegroundColor Green
        Write-Host "Title: $($doc.metadata.title)  Type: $($doc.metadata.type)  Year: $($doc.metadata.year)"
        Write-Host "`nAPI shape confirmed. Run -Mode index next."
    } else {
        Write-Host "Reached the API but no 'html' field was found - shape may have changed." -ForegroundColor Yellow
        $doc | ConvertTo-Json -Depth 4 | Out-File (Join-Path $OutDir "_probe_document.json") -Encoding UTF8
        Write-Host "Full response saved to _probe_document.json for inspection."
    }
    return
}

# ------------------------------------------------------------
# MODE 2: INDEX - enumerate annual-meeting document ids
# ------------------------------------------------------------
if ($Mode -eq "index") {
    Write-Host "Fetching document list from $BaseUrl/api/documents ..." -ForegroundColor Cyan
    $docs = Get-Json "$BaseUrl/api/documents"
    Write-Host "Found $($docs.Count) total documents." -ForegroundColor Green

    $meetings = $docs |
        Where-Object { $_.metadata.type -eq 'transcript' -and $_.metadata.title -match 'Annual Meeting' } |
        ForEach-Object {
            [pscustomobject]@{
                Id    = $_.id
                Title = $_.metadata.title
                Year  = $_.metadata.year
            }
        } |
        Sort-Object Year

    Write-Host "$($meetings.Count) look like annual meetings." -ForegroundColor Green
    $meetings | Export-Csv (Join-Path $OutDir "_meetings.csv") -NoTypeInformation
    $meetings | Format-Table
    return
}

# ------------------------------------------------------------
# MODE 3: SCRAPE - pull each meeting, save as .txt
# ------------------------------------------------------------
if ($Mode -eq "scrape") {
    $csv = Join-Path $OutDir "_meetings.csv"
    if (-not (Test-Path $csv)) { Write-Host "Run -Mode index first."; return }
    $meetings = Import-Csv $csv

    foreach ($m in $meetings) {
        $dest = Join-Path $OutDir (($m.Title -replace '[\\/:*?"<>|]','-') + ".txt")
        if (Test-Path $dest) { Write-Host "Skip (exists): $($m.Title)"; continue }
        try {
            $doc = Get-Json "$BaseUrl/api/documents/$($m.Id)"
            if ($doc.html) {
                $text = Convert-HtmlToText $doc.html
                Save-Text $m.Title $text
            } else {
                Write-Host "No html field for $($m.Title) - check API shape (-Mode probe)." -ForegroundColor Red
            }
        } catch {
            Write-Host "FAILED $($m.Title): $($_.Exception.Message)" -ForegroundColor Red
        }
        Start-Sleep -Seconds $DelaySec
    }
    Write-Host "`nDone. Files in $OutDir" -ForegroundColor Green
}
