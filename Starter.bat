@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
choco install python --version=3.11.0 -y
cls
color 2 
cls
color 3
cls
cls
cls
@echo off
move "Data\start.bat" ""
move "pingtest.py" "Data"
move "py.txt" "Data"
move "start.txt" "Data"
move "end.txt" "Data"
move "README.md" "Data"
attrib +h "Data"
attrib -h "start.bat"
attrib +h "Data\pingtest.py"
attrib +h "Data\py.txt"
attrib +h "Data\start.txt"
attrib +h "Data\end.txt"
attrib +h "Data\README.md"
attrib +h "Data\update.bat"
cls
start "" "%~dp0Data\update.bat"
more Data\py.txt
pause
move "Starter.bat" "Data"