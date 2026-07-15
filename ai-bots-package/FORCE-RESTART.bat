@echo off
title Force Restart AI Server
color 0C

echo ============================================================
echo         FORCE RESTARTING AI AGENT TEAM
echo ============================================================
echo.
echo Step 1: Killing all Python processes...

taskkill /F /IM python.exe 2>nul

echo.
echo Step 2: Waiting 3 seconds...
timeout /t 3 /nobreak >nul

echo.
echo Step 3: Starting fresh server...
echo.

cd /d "%~dp0"
START-TEAM-ENHANCED.bat
