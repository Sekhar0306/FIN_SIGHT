@echo off
REM FIN-SIGHT Launch Script for Windows
echo Starting FIN-SIGHT...
echo Anomaly Detection in Stock Trades
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Please install pip.
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Checking dependencies...
pip install -r requirements.txt --quiet

REM Run Streamlit app
echo.
echo Dependencies installed!
echo Launching application...
echo.
streamlit run app.py

pause

