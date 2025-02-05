@echo off
setlocal enabledelayedexpansion

:: Define MinGW download URL and installation directory
set "MINGW_URL=https://example.com/mingw.zip"   REM Replace with actual MinGW link
set "MINGW_ZIP=%TEMP%\mingw.zip"
set "MINGW_DIR=C:\MinGW"

:: Step 1: Download MinGW using PowerShell
echo Downloading MinGW...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%MINGW_URL%', '%MINGW_ZIP%')"
if %ERRORLEVEL% neq 0 (
    echo Download failed!
    exit /b 1
)

:: Step 2: Extract MinGW to the specified directory
echo Extracting MinGW...
powershell -Command "Expand-Archive -Path '%MINGW_ZIP%' -DestinationPath '%MINGW_DIR%' -Force"
if %ERRORLEVEL% neq 0 (
    echo Extraction failed!
    exit /b 1
)

:: Step 3: Add MinGW to PATH (Permanent Change)
echo Adding MinGW to PATH...
setx PATH "%MINGW_DIR%\bin;%PATH%" /M
if %ERRORLEVEL% neq 0 (
    echo Failed to update PATH!
    exit /b 1
)

:: Cleanup
del "%MINGW_ZIP%"
echo MinGW installation complete! Restart your terminal for changes to take effect.
