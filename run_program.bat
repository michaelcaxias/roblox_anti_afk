@echo off
setlocal

REM Configs
set MAIN_SCRIPT=src/main.py

REM Execute the file src/main.py
python %MAIN_SCRIPT%

REM Wait for the user to press Enter to close the window
pause
