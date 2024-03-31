@echo off 
venv\Scripts\activate.bat
pyinstaller --onefile --windowed --icon=monitor.ico RefreshRateService.py
pause
