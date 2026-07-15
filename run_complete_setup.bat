@echo off
REM Complete PhoneHub Setup - Run Everything
echo.
echo ========================================
echo   PHONEHUB COMPLETE SETUP
echo ========================================
echo.
echo This will:
echo  1. Fetch brand logos (1 min)
echo  2. Run full pipeline (10 min)
echo  3. Generate all data files
echo.
set /p confirm="Continue? (Y/N): "
if /i not "%confirm%"=="Y" goto :end

cd phonehub\tools

echo.
echo [1/2] Fetching brand logos...
python brand_logos_fetcher.py

if errorlevel 1 (
    echo ERROR: Brand logos fetcher failed
    pause
    exit /b 1
)

echo.
echo [2/2] Running enhanced pipeline (this may take 10 minutes)...
python run_all_enhanced.py --limit 50

if errorlevel 1 (
    echo ERROR: Pipeline failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCESS!
echo ========================================
echo.
echo Your PhoneHub now has:
echo.
echo  - 50+ products with REAL prices
echo  - Brand logos with colors
echo  - News with images
echo  - High-quality product images
echo.
echo Next steps:
echo.
echo 1. Review generated data:
echo    dir data
echo.
echo 2. Deploy to GitHub:
echo    git add .
echo    git commit -m "Launch ready with real data"
echo    git push origin main
echo.
echo 3. Update frontend for brand logos:
echo    (Tell Kiro: "Update frontend to show brand logos")
echo.
echo 4. Get Pixabay key for more images:
echo    https://pixabay.com/api/docs/
echo.

:end
cd ..\..
pause
