#check is new folder exists, create if-folder if it does
if (Test-Path -Path "new_folder") {New-Item -ItemType Directory -Path "if-folder"}
#check if folder exists and create another folder
    if (Test-Path -Path "if-folder") {New-Item -ItemType Directory -Path "hyperionDev"}
    else {New-Item -ItemType Directory -Path "new-projects"}