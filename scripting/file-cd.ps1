#create 3 new folders
New-Item -ItemType Directory -Path "Script1"
New-Item -ItemType Directory -Path "Script2"
New-Item -ItemType Directory -Path "Script3"
Write-Output "File created"

# create 3 folders into one of the folders
Set-Location -Path "Script1"
New-Item -ItemType Directory -Path "Subscript1"
New-Item -ItemType Directory -Path "Subscript2"
New-Item -ItemType Directory -Path "Subscript3"

#Remove 2 folders from the
Remove-Item -Path "Subscript1" -Recurse
Remove-Item -Path "Subscript2" -Recurse