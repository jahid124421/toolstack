@echo off
title Free AI Agent Team - Enhanced Model Selector
color 0E
cd /d "%~dp0"

:MAIN_MENU
cls
echo ============================================================
echo      FREE AI AGENT TEAM - ENHANCED MODEL SELECTOR
echo ============================================================
echo.
echo Select your use case:
echo.
echo   [1] CODING TASKS (Private APIs First)
echo       - Best models for code generation, debugging, refactoring
echo       - Priority: GROQ ^> CEREBRAS ^> CLOUDFLARE ^> FREEMODEL ^> OpenRouter
echo.
echo   [2] BUSINESS ANALYST WORK (Best for BA Tasks)
echo       - Best models for analysis, planning, documentation, research
echo       - Priority: CEREBRAS ^> GROQ ^> FREEMODEL ^> CLOUDFLARE ^> OpenRouter
echo.
echo   [3] AUTO MODE (Smart Selection)
echo       - Let the system choose the best available model
echo.
echo   [4] EXIT
echo.
echo ============================================================
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto CODING_MODE
if "%choice%"=="2" goto BA_MODE
if "%choice%"=="3" goto AUTO_MODE
if "%choice%"=="4" goto END
goto MAIN_MENU

:CODING_MODE
cls
echo ============================================================
echo                    CODING MODE ACTIVATED
echo ============================================================
echo.
echo Priority Order (Private APIs First):
echo   1. GROQ - llama-3.3-70b-versatile
echo   2. CEREBRAS - gpt-oss-120b
echo   3. CLOUDFLARE - @cf/meta/llama-3.3-70b-instruct-fp8-fast
echo   4. FREEMODEL - gpt-5.4
echo   5. OpenRouter - qwen3-coder:free
echo.
echo Setting up coding-optimized configuration...
echo.
REM Set environment variables for coding mode
set AI_MODE=CODING
set TEAM_MAX_TOKENS=1200
set PRIMARY_PROVIDER=GROQ
set BEST_MODEL=llama-3.3-70b-versatile

REM Write mode configuration
echo CODING > mode_config.txt
echo llama-3.3-70b-versatile > current_model.txt

goto START_SERVER

:BA_MODE
cls
echo ============================================================
echo              BUSINESS ANALYST MODE ACTIVATED
echo ============================================================
echo.
echo Priority Order (Best for Analysis):
echo   1. CEREBRAS - gpt-oss-120b (120B reasoning)
echo   2. GROQ - llama-3.3-70b-versatile
echo   3. FREEMODEL - gpt-5.4
echo   4. CLOUDFLARE - @cf/meta/llama-3.3-70b-instruct-fp8-fast
echo   5. OpenRouter - qwen3-next-80b-a3b-instruct:free
echo.
echo Setting up BA-optimized configuration...
echo.

REM Set environment variables for BA mode
set AI_MODE=BA_WORK
set TEAM_MAX_TOKENS=1500
set PRIMARY_PROVIDER=CEREBRAS
set BEST_MODEL=gpt-oss-120b

REM Write mode configuration
echo BA_WORK > mode_config.txt
echo gpt-oss-120b > current_model.txt

goto START_SERVER

:AUTO_MODE
cls
echo ============================================================
echo                  AUTO MODE ACTIVATED
echo ============================================================
echo.
echo The system will automatically select the best available model
echo based on provider response time and availability.
echo.

REM Set environment variables for auto mode
set AI_MODE=AUTO
set TEAM_MAX_TOKENS=1000
set PRIMARY_PROVIDER=AUTO
set BEST_MODEL=auto

REM Write mode configuration
echo AUTO > mode_config.txt
echo auto > current_model.txt

goto START_SERVER

:START_SERVER
REM --- Make sure Python is available ---
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Install Python from https://www.python.org/downloads/
    echo Then run this file again.
    echo.
    pause
    exit /b
)

REM --- Make sure required packages are installed (quietly) ---
python -c "import flask, requests" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages ^(one-time^)...
    python -m pip install flask requests --quiet
    echo Done.
    echo.
)

echo.
echo ============================================================
echo                  SERVER STARTING...
echo ============================================================
echo.
echo   MODE: %AI_MODE%
echo   PRIMARY PROVIDER: %PRIMARY_PROVIDER%
echo   PRIMARY MODEL: %BEST_MODEL%
echo   MAX TOKENS PER CALL: %TEAM_MAX_TOKENS%
echo.
echo   Keep THIS window open while you use your IDE.
echo   To stop the AI, just close this window.
echo.
echo ------------------------------------------------------------
echo   IDE SETTINGS ^(copy these into your IDE^):
echo.
echo     Base URL :  http://localhost:8080/v1
echo     API Key  :  local
echo     Model    :  %BEST_MODEL%
echo.
echo   USAGE TRACKING:
echo     Check real-time usage: http://localhost:8080/usage
echo     Server status: http://localhost:8080/
echo.
echo   LOG FILE:
echo     %~dp0ai-agent-team.log
echo ------------------------------------------------------------
echo.
echo Starting AI Agent Team in %AI_MODE% mode...
echo.

python "%~dp0ai-agent-team.py"

echo.
echo AI stopped. Press any key to return to menu or close window.
pause
goto MAIN_MENU

:END
echo.
echo Thank you for using Free AI Agent Team!
echo.
timeout /t 2 >nul
exit /b
