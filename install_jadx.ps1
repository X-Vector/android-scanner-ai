
$jadxVersion = "1.5.1"
$zipName = "jadx-$jadxVersion.zip"
$downloadUrl = "https://github.com/skylot/jadx/releases/download/v$jadxVersion/$zipName"
$installDir = "installed-tools"
$zipPath = Join-Path $installDir $zipName

if (-Not (Test-Path $installDir)) {
    New-Item -ItemType Directory -Path $installDir | Out-Null
}

Write-Host "[*] Downloading JADX $jadxVersion..."
Invoke-WebRequest -Uri $downloadUrl -OutFile $zipPath

Write-Host "[*] Unzipping..."
Expand-Archive -LiteralPath $zipPath -DestinationPath $installDir -Force

Write-Host "[+] JADX $jadxVersion installed in '$installDir'"
