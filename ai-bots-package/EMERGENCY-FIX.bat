@echo off
color 0E
cls

echo ============================================================
echo         EMERGENCY FIX FOR AI AGENT TEAM
echo ============================================================
echo.
echo This will:
echo   1. KILL all Python processes
echo   2. Wait 5 seconds
echo   3. Start a fresh server with AUTO mode
echo.
echo Press Ctrl+C to cancel, or
pause

cls
echo.
echo [1/3] Killing all Python processes...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM pythonw.exe >nul 2>&1

echo [2/3] Waiting 5 seconds for cleanup...
timeout /t 5 /nobreak >nul

echo [3/3] Starting fresh AI server...
echo.
echo ============================================================
echo.

cd /d "%~dp0"

REM Check Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit /b
)

echo Starting server... Keep this window OPEN.
echo.
echo Your IDE settings:
echo   Base URL: http://localhost:8080/v1
echo   API Key: local
echo   Model: auto
echo.
echo ============================================================
echo.

set TEAM_MAX_TOKENS=1000
python ai-agent-team.py

echo.
echo Server stopped. Press any key to exit.
pause >nul
