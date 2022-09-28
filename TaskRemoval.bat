@echo off

Rem This script removes the task from the task scheduler to prevent it continuously encrypting every month.
SCHTASKS /DELETE /TN "WINDOWSTASKS\SECRET" /f