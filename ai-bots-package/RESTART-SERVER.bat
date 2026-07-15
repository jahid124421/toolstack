@echo off
title Restart AI Agent Team Server
color 0C

echo ============================================================
echo          RESTARTING AI AGENT TEAM SERVER
echo ============================================================
echo.
echo Stopping any running Python servers...

REM Kill any Python processes running ai-agent-team.py
taskkill /F /FI "WINDOWTITLE eq Free AI Agent Team*" 2>nul
taskkill /F /FI "IMAGENAME eq python.exe" /FI "MEMUSAGE gt 50000" 2>nul

timeout /t 2 /nobreak >nul

echo.
echo All Python processes stopped.
echo.
echo Now start the server again using:
echo   START-TEAM-ENHANCED.bat
echo.
pause
