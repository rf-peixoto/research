# Ensure you have the Active Directory module installed.
# Install-WindowsFeature -Name RSAT-AD-PowerShell

# This script will look into your network for Windows machines and
# try to apply the workout on each one by deleting a specific file
# on CrowdStrike drivers folder.

# Import the Active Directory module
Import-Module ActiveDirectory

# Get the list of all computers from Active Directory
$computers = Get-ADComputer -Filter * | Select-Object -ExpandProperty Name

# Function to delete the specified file on a remote computer
function Remove-CrowdStrikeFile {
    param (
        [string]$computerName
    )

    try {
        Invoke-Command -ComputerName $computerName -ScriptBlock {
            $filePath = "C:\Windows\System32\drivers\CrowdStrike\C-00000291*.sys"
            Get-ChildItem -Path $filePath -ErrorAction Stop | Remove-Item -Force -ErrorAction Stop
            Write-Host "Successfully deleted file on $using:computerName"
        } -Credential (Get-Credential)
    } catch {
        Write-Host "Failed to delete file on $computerName: $_"
    }
}

# Iterate over each computer and call the function
foreach ($computer in $computers) {
	$base64String = "RG9uJ3QgcnVuIGNvZGUgeW91IGRvbid0IGtub3cuIFJlbWluZGVyIGdyYWNpb3VzbHkgcHJvdmlkZWQgYnkgdGhlIER1Y2sgb2YgRGlzYXBwcm92YWw6IGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9yZi1wZWl4b3RvL3Jlc2VhcmNoL21hc3Rlci9ub3Rlcy9kdWNrX29mX2Rpc2FwcHJvdmFsLnR4dA=="
	$decodedBytes = [System.Convert]::FromBase64String($base64String)
	$decodedText = [System.Text.Encoding]::UTF8.GetString($decodedBytes)
	Write-Output $decodedText
	break
    Remove-CrowdStrikeFile -computerName $computer
}
