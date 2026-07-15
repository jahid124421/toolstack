@echo off
REM PhoneHub Quick Start Script for Windows
REM This script helps you set up and run PhoneHub in 5 minutes

echo.
echo ========================================
echo   PHONEHUB QUICK START
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/5] Python detected: 
python --version
echo.

REM Navigate to tools directory
cd _deploy_staging\phonehub\tools

REM Check if config.json exists
if not exist config.json (
    echo [2/5] Creating config.json from template...
    copy config.enhanced.json config.json
    echo.
    echo IMPORTANT: Edit config.json and add your API keys!
    echo Minimum required:
    echo   - rainforest_api_key: https://www.rainforestapi.com
    echo   - bing_image_api_key: https://portal.azure.com
    echo   - LLM key in ai-bots-package/my-keys.env
    echo.
    pause
) else (
    echo [2/5] config.json already exists
    echo.
)

REM Check if .env exists
if not exist .env (
    echo Creating .env from template...
    copy .env.template .env
    echo Remember to add your API keys to .env file!
    echo.
)

REM Ask user if they want to run a test
echo [3/5] Ready to run initial test?
echo This will:
echo   - Seed 50 products from Wikidata
echo   - Fetch specs for 10 products
echo   - Get prices for 10 products
echo   - Fetch images for 10 products
echo   - Generate 10 AI reviews
echo   - Build the site
echo.
set /p confirm="Continue? (Y/N): "
if /i not "%confirm%"=="Y" goto :skip_test

echo.
echo [4/5] Running test pipeline (this may take 5-10 minutes)...
echo.

python run_all_enhanced.py --limit 10

if errorlevel 1 (
    echo.
    echo ERROR: Pipeline failed. Check the errors above.
    echo Common issues:
    echo   - Missing API keys in config.json or .env
    echo   - Invalid API keys
    echo   - Network connectivity
    echo.
    pause
    exit /b 1
)

echo.
echo [5/5] TEST SUCCESSFUL!
echo.
echo ========================================
echo   NEXT STEPS
echo ========================================
echo.
echo 1. Review the generated data:
echo    - data/specs.json (products)
echo    - data/prices.json (prices)
echo    - data/content.json (reviews)
echo    - data/news.json (news)
echo.
echo 2. Run full pipeline for production:
echo    python run_all_enhanced.py
echo.
echo 3. Deploy to GitHub Pages:
echo    cd ..\..\..
echo    git add .
echo    git commit -m "Initial catalog with real data"
echo    git push origin main
echo.
echo 4. Set up GitHub Actions for auto-updates:
echo    See GITHUB_ACTIONS_SETUP.md
echo.
echo 5. Buy custom domain (recommended):
echo    See SETUP_GUIDE.md section "Domain Setup"
echo.
echo ========================================
echo   USEFUL COMMANDS
echo ========================================
echo.
echo Update prices only:
echo   python run_all_enhanced.py --prices-only
echo.
echo Update images only:
echo   python run_all_enhanced.py --images-only
echo.
echo Quick refresh (skip slow steps):
echo   python run_all_enhanced.py --quick
echo.
echo Full pipeline with limit:
echo   python run_all_enhanced.py --limit 100
echo.

goto :end

:skip_test
echo.
echo Skipped test run. You can run it later with:
echo   cd _deploy_staging\phonehub\tools
echo   python run_all_enhanced.py --limit 10
echo.

:end
cd ..\..\..
pause
