@ECHO OFF

TITLE Stryd Exporter v1

echo Checking dependencies...
pip install -r ../requirements.txt

echo Select an option:
echo 1. October
echo 2. November
echo 3. Exit

set /p choice=Enter your choice (1-3): 

if "%choice%"=="" goto menu
if "%choice%"=="1" goto optionA
if "%choice%"=="2" goto optionB
if "%choice%"=="3" goto :eof

:optionA
cls
echo Option A selected
python october.py
pause
goto menu

:optionB
cls
echo Option B selected
python november.py
pause
goto menu