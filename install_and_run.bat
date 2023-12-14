@echo off

:: Check if Python 3.10 is installed
python --version 2>NUL | find "Python 3.10" >NUL
if %errorlevel% neq 0 (
    echo Installing Python 3.10...
    start /wait python-3.10-installer.exe /quiet InstallAllUsers=1 PrependPath=1
)

:: Install dependencies from requirements.txt
echo Installing dependencies...
python -m pip install -r requirements.txt

:: Run the Python script
echo Running the script...
python your_script.py

pause
