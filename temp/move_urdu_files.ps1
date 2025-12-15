$sourceBasePath = "D:\QUARTER 4\Assignment\Hackathon\Hackathon_One\physical-ai-humanoid-textbook\i18n\ur\docusaurus-plugin-content-docs\"
$destinationBasePath = "D:\QUARTER 4\Assignment\Hackathon\Hackathon_One\physical-ai-humanoid-textbook\i18n\ur\docusaurus-plugin-content-docs\docs\"

# Get all files except current.json (which is a different type of file)
# The glob command should have excluded this. Let's make sure
$filesToMove = @(Get-ChildItem -Path $sourceBasePath -Recurse -File | Where-Object { $_.FullName -notlike "*current.json" -and $_.FullName -notlike "*\docs\*" })

foreach ($file in $filesToMove) {
    $relativePath = $file.FullName.Substring($sourceBasePath.Length)
    $destinationPath = Join-Path $destinationBasePath $relativePath
    $destinationDir = Split-Path $destinationPath -Parent

    # Create destination directory if it doesn't exist
    if (-not (Test-Path $destinationDir)) {
        New-Item -Path $destinationDir -ItemType Directory -Force | Out-Null
        Write-Host "Created directory: $destinationDir"
    }

    # Move the file
    Move-Item -Path $file.FullName -Destination $destinationPath -Force
    Write-Host "Moved: $($file.FullName) to $($destinationPath)"
}

# Remove now empty top-level directories under i18n/ur/docusaurus-plugin-content-docs/
# (Introduction, Module-1, etc.)
Get-ChildItem -Path $sourceBasePath -Directory | ForEach-Object {
    # Ensure it's not the newly created 'docs' directory
    if ($_.Name -ne "docs") {
        if (-not (Get-ChildItem -Path $_.FullName -Recurse -ErrorAction SilentlyContinue)) {
            Remove-Item -Path $_.FullName -Recurse -Force
            Write-Host "Removed empty directory: $($_.FullName)"
        }
    }
}
