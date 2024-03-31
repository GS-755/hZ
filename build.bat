@echo off 
venv\Scripts\activate.bat
pyinstaller --onefile --windowed --icon=app.ico RefreshRateService.py
pause
