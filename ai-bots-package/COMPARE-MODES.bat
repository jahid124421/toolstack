@echo off
title AI Agent Team - Mode Comparison
color 0E

cls
echo ============================================================
echo          AI AGENT TEAM - MODE COMPARISON
echo ============================================================
echo.
echo Choose what you want to compare:
echo.
echo   [1] Show CODING vs BA mode differences
echo   [2] Show provider priority orders
echo   [3] Show token limits by mode
echo   [4] Show all comparisons
echo   [5] Exit
echo.
echo ============================================================
set /p choice="Enter choice (1-5): "

if "%choice%"=="1" goto SHOW_MODES
if "%choice%"=="2" goto SHOW_PROVIDERS
if "%choice%"=="3" goto SHOW_TOKENS
if "%choice%"=="4" goto SHOW_ALL
if "%choice%"=="5" exit /b
goto :EOF

:SHOW_MODES
cls
echo ============================================================
echo                  CODING vs BA MODES
echo ============================================================
echo.
echo CODING MODE
echo -----------
echo   Best For:  Code generation, debugging, refactoring
echo   Priority:  Private APIs First (Fast ^& Generous)
echo   Tokens:    3000 per call
echo   Speed:     FAST (GROQ ^& CEREBRAS are blazing)
echo.
echo BA MODE
echo -------
echo   Best For:  Analysis, planning, documentation, research
echo   Priority:  Best Reasoning First (CEREBRAS 120B)
echo   Tokens:    4000 per call
echo   Quality:   COMPREHENSIVE (more context)
echo.
echo AUTO MODE
echo ---------
echo   Best For:  General mixed tasks
echo   Priority:  Smart auto-selection
echo   Tokens:    2000 per call
echo   Balance:   FLEXIBLE
echo.
pause
goto :EOF

:SHOW_PROVIDERS
cls
echo ============================================================
echo              PROVIDER PRIORITY BY MODE
echo ============================================================
echo.
echo CODING MODE - Private APIs First
echo ================================
echo   1st: GROQ       - llama-3.3-70b-versatile (FREE, FAST)
echo   2nd: CEREBRAS   - gpt-oss-120b (FREE, FAST, SMART)
echo   3rd: CLOUDFLARE - llama-3.3-fp8-fast (FREE, FAST)
echo   4th: FREEMODEL  - gpt-5.4 (FREE CREDITS)
echo   5th: OPENROUTER - qwen3-coder:free (FREE, SLOW)
echo.
echo BA MODE - Best Reasoning First
echo ==============================
echo   1st: CEREBRAS   - gpt-oss-120b (FREE, 120B REASONING)
echo   2nd: GROQ       - llama-3.3-70b-versatile (FREE, FAST)
echo   3rd: FREEMODEL  - gpt-5.4 (FREE CREDITS)
echo   4th: CLOUDFLARE - llama-3.3-fp8-fast (FREE, FAST)
echo   5th: OPENROUTER - qwen3-next:free (FREE, SLOW)
echo.
echo AUTO MODE - Best Available
echo ==========================
echo   Automatically tries fastest responding provider
echo   Falls back through all available providers
echo.
pause
goto :EOF

:SHOW_TOKENS
cls
echo ============================================================
echo              TOKEN LIMITS BY MODE
echo ============================================================
echo.
echo   MODE         MAX TOKENS    WHY?
echo   ------------------------------------------------
echo   CODING       3000          Balance speed ^& completeness
echo   BA           4000          More context for analysis
echo   AUTO         2000          General purpose
echo.
echo What are tokens?
echo   - Roughly 4 characters = 1 token
echo   - 1000 tokens ≈ 750 words
echo   - Both input AND output count toward limit
echo.
echo Examples:
echo   CODING: "Write a React component" = ~2500 tokens response
echo   BA:     "Analyze this system" = ~3500 tokens response
echo.
pause
goto :EOF

:SHOW_ALL
cls
echo ============================================================
echo              COMPLETE MODE COMPARISON
echo ============================================================
echo.
echo +------------------+------------------+------------------+
echo ^|    FEATURE       ^|   CODING MODE    ^|    BA MODE       ^|
echo +------------------+------------------+------------------+
echo ^| Primary Provider ^| GROQ             ^| CEREBRAS         ^|
echo ^| Max Tokens       ^| 3000             ^| 4000             ^|
echo ^| Best For         ^| Code             ^| Analysis         ^|
echo ^| Speed Priority   ^| HIGH             ^| MEDIUM           ^|
echo ^| Quality Priority ^| BALANCED         ^| HIGH             ^|
echo ^| Cost             ^| FREE             ^| FREE             ^|
echo +------------------+------------------+------------------+
echo.
echo Provider Order Comparison:
echo.
echo CODING:  GROQ ^> CEREBRAS ^> CLOUDFLARE ^> FREEMODEL ^> OR
echo BA:      CEREBRAS ^> GROQ ^> FREEMODEL ^> CLOUDFLARE ^> OR
echo.
echo Key Differences:
echo   • CODING prioritizes GROQ for speed
echo   • BA prioritizes CEREBRAS for 120B reasoning
echo   • CODING has tighter token limit for faster responses
echo   • BA has higher token limit for comprehensive analysis
echo   • Both use FREE providers only
echo.
pause
goto :EOF
