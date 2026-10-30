# ============================================================
#  brk-reports.ps1
#  Personal study copies of Berkshire shareholder letters / reports
#  from berkshire.memorex.ai - saved as one .txt per letter.
#
#  Same site and API as brk-meetings.ps1 (see that script's header
#  for how the API was discovered). This one targets the "letter"
#  documents instead of "transcript" documents:
#    GET /api/documents          -> list of {id, metadata:{type,title,year,...}}
#    GET /api/documents/{id}     -> {id, metadata, html}   (html = letter body)
#
#  Modes:
#    1) probe   - sanity-check the API is reachable/shaped as expected
#    2) index   - list all documents and pick out the letters/reports
#    3) scrape  - download each letter's html, convert to text, save .txt
#
#  Usage:
#    .\brk-reports.ps1 -Mode probe
#    .\brk-reports.ps1 -Mode index
#    .\brk-reports.ps1 -Mode scrape
#
#  Keep the output for personal study only - the archive's notice
#  prohibits reproduction/distribution.
# ============================================================

param(
    [ValidateSet("probe","index","scrape")]
    [string]$Mode = "probe",

    # A known-good document id to probe (1965 letter)
    [string]$ProbeId = "3ecd1cad-1244-413c-9011-bb92a17fce2d",

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

# Turn the letter's HTML body into plain, readable text.
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
        Write-Host "  reload, and find the request that returns the letter JSON."
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
# MODE 2: INDEX - enumerate letter/report document ids
# ------------------------------------------------------------
if ($Mode -eq "index") {
    Write-Host "Fetching document list from $BaseUrl/api/documents ..." -ForegroundColor Cyan
    $docs = Get-Json "$BaseUrl/api/documents"
    Write-Host "Found $($docs.Count) total documents." -ForegroundColor Green

    $reports = $docs |
        Where-Object { $_.metadata.type -eq 'letter' } |
        ForEach-Object {
            [pscustomobject]@{
                Id    = $_.id
                Title = $_.metadata.title
                Year  = $_.metadata.year
            }
        } |
        Sort-Object Year

    Write-Host "$($reports.Count) look like letters/reports." -ForegroundColor Green
    $reports | Export-Csv (Join-Path $OutDir "_reports.csv") -NoTypeInformation
    $reports | Format-Table
    return
}

# ------------------------------------------------------------
# MODE 3: SCRAPE - pull each letter, save as .txt
# ------------------------------------------------------------
if ($Mode -eq "scrape") {
    $csv = Join-Path $OutDir "_reports.csv"
    if (-not (Test-Path $csv)) { Write-Host "Run -Mode index first."; return }
    $reports = Import-Csv $csv

    foreach ($r in $reports) {
        $dest = Join-Path $OutDir (($r.Title -replace '[\\/:*?"<>|]','-') + ".txt")
        if (Test-Path $dest) { Write-Host "Skip (exists): $($r.Title)"; continue }
        try {
            $doc = Get-Json "$BaseUrl/api/documents/$($r.Id)"
            if ($doc.html) {
                $text = Convert-HtmlToText $doc.html
                Save-Text $r.Title $text
            } else {
                Write-Host "No html field for $($r.Title) - check API shape (-Mode probe)." -ForegroundColor Red
            }
        } catch {
            Write-Host "FAILED $($r.Title): $($_.Exception.Message)" -ForegroundColor Red
        }
        Start-Sleep -Seconds $DelaySec
    }
    Write-Host "`nDone. Files in $OutDir" -ForegroundColor Green
}
