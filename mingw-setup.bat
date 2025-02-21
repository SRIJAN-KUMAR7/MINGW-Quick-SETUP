@echo off
setlocal enabledelayedexpansion

:: Set the URL for the MinGW installer
set "MINGW_URL=https://cyfuture.dl.sourceforge.net/project/mingw/Installer/mingw-get-setup.exe?viasf=1"
set "MINGW_EXE=%TEMP%\mingw-setup.exe"
set "MINGW_DIR=C:\MinGW"

:: Download the MinGW installer
echo Downloading MinGW installer...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%MINGW_URL%', '%MINGW_EXE%')"
if %ERRORLEVEL% neq 0 (
    echo Error: Download failed! Check your internet connection or try another link.
    exit /b 1
)

:: Check if the installer file was downloaded correctly
if not exist "%MINGW_EXE%" (
    echo Error: MinGW installer was not downloaded correctly!
    exit /b 1
)

:: Run the MinGW installer silently
echo Running MinGW installer...
"%MINGW_EXE%" --mode=install --prefix="%MINGW_DIR%"
if %ERRORLEVEL% neq 0 (
    echo Error: Installation failed!
    exit /b 1
)

:: Add MinGW to the PATH environment variable
echo Adding MinGW to PATH...
setx PATH "%MINGW_DIR%\bin;%PATH%" /M
if %ERRORLEVEL% neq 0 (
    echo Error: Failed to update PATH! Run as Administrator if needed.
    exit /b 1
)

:: Clean up by deleting the installer file
del "%MINGW_EXE%"

echo MinGW installation complete! Restart your terminal for changes to take effect.
