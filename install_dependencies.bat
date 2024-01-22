@echo off
setlocal

REM Configs
set REQUIREMENTS_FILE=requirements.txt

REM Update pip
pip install --upgrade pip

REM Install the Python libraries listed in file requirements.txt
pip install -r %REQUIREMENTS_FILE%

REM Warn the user that the installation is complete
echo Installation completed!

REM Wait for the user to press Enter to close the window
pause
