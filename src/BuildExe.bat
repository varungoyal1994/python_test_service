@echo off
REM C:\Python27\Scripts\pyi-grab_version.exe Starter version.rc   
REM python -O -m PyInstaller -F Starter.py --icon=ico.ico
C:\Python27\Scripts\pyinstaller.exe -F TestService.py --icon=ico.ico --version-file version.rc
set /p DUMMY=Hit ENTER to continue...