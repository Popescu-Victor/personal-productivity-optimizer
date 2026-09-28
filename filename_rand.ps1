$folderPath = Read-Host "Enter the full path of the folder"
 
# Validate the folder exists
if (-not (Test-Path -Path $folderPath -PathType Container)) {
    Write-Host "Error: The folder '$folderPath' does not exist." -ForegroundColor Red
    exit 1
}
 
# Get all files in the folder (top level only)
$files = Get-ChildItem -Path $folderPath -File
 
if ($files.Count -eq 0) {
    Write-Host "No files found in '$folderPath'." -ForegroundColor Yellow
    exit 0
}
 
Write-Host "Found $($files.Count) file(s) in '$folderPath'."
$confirm = Read-Host "Do you want to proceed with randomizing file names? (Y/N)"
 
if ($confirm -notmatch '^[Yy]') {
    Write-Host "Operation cancelled."
    exit 0
}
 
# Keep track of used names to avoid collisions
$usedNames = New-Object System.Collections.Generic.HashSet[string]
 
foreach ($file in $files) {
    $extension = $file.Extension
    do {
        # Generate a random name using a GUID fragment (8 characters)
        $randomName = [guid]::NewGuid().ToString("N").Substring(0, 8) + $extension
    } while (-not $usedNames.Add($randomName))
 
    $newPath = Join-Path -Path $folderPath -ChildPath $randomName
 
    try {
        Rename-Item -Path $file.FullName -NewName $randomName -ErrorAction Stop
        Write-Host "Renamed: $($file.Name) --> $randomName" -ForegroundColor Green
    }
    catch {
        Write-Host "Failed to rename $($file.Name): $_" -ForegroundColor Red
    }
}
 
Write-Host "`nDone. $($files.Count) file(s) processed."
