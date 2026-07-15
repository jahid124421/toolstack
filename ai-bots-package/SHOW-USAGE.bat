@echo off
title AI Agent Team - Usage Monitor
color 0B
cd /d "%~dp0"

echo ============================================================
echo          AI AGENT TEAM - USAGE STATISTICS
echo ============================================================
echo.

python show_usage.py

echo.
pause
