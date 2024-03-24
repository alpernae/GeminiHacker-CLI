# Directory containing the geminihacker script
$scriptDir = "C:\path\to"

# Add geminihacker directory to PATH
$currentPath = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
$newPath = $currentPath + ";$scriptDir"
[System.Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")

Write-Host "Geminihacker is now globally accessible on Windows."
