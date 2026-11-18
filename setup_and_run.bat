@echo off
setlocal
cd /d "%~dp0"
title Janna Hostel - Setup and Run

echo ==============================================
echo   Janna Gents Hostel - Django setup and run
echo ==============================================
echo.

if not exist "manage.py" (
    echo ERROR: manage.py was not found.
    echo Please keep this BAT file in the janna_hostel_django project folder.
    goto failed
)

set "PY_CMD="
py -3 --version >nul 2>&1
if not errorlevel 1 goto use_py
python --version >nul 2>&1
if errorlevel 1 goto no_python
set "PY_CMD=python"
goto python_ready

:use_py
set "PY_CMD=py -3"

:python_ready
if not exist ".venv\Scripts\python.exe" (
    echo Creating the Python virtual environment...
    %PY_CMD% -m venv .venv
    if errorlevel 1 goto failed
)

set "VENV_PY=%CD%\.venv\Scripts\python.exe"
if not exist ".requirements_installed" (
    echo Installing project packages. Internet is needed for this first setup...
    "%VENV_PY%" -m pip install -r requirements.txt
    if errorlevel 1 goto failed
    echo installed>".requirements_installed"
)

echo Preparing the database...
"%VENV_PY%" manage.py migrate
if errorlevel 1 goto failed

set "HAS_ADMIN="
for /f "delims=" %%A in ('"%VENV_PY%" manage.py shell -c "from django.contrib.auth import get_user_model; print(1 if get_user_model().objects.filter(is_superuser=True).exists() else 0)" 2^>nul') do set "HAS_ADMIN=%%A"
if "%HAS_ADMIN%"=="0" (
    echo.
    echo Create the admin username and password when prompted.
    "%VENV_PY%" manage.py createsuperuser
    if errorlevel 1 goto failed
)

echo.
echo Starting the website...
echo Home page: http://127.0.0.1:8000/
echo Admin page: http://127.0.0.1:8000/admin/
echo Keep this window open while using the website.
echo Press Ctrl+C here to stop the server.
echo.
"%VENV_PY%" manage.py runserver 127.0.0.1:8000
goto end

:no_python
echo ERROR: Python 3.10 or later was not found.
echo Install Python from https://www.python.org/downloads/windows/
echo During installation, enable "Add Python to PATH", then run this BAT file again.
goto failed

:failed
echo.
echo Setup did not finish. Check the message above, fix the issue, and run this BAT file again.

:end
echo.
pause
endlocal
