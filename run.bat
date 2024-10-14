@echo off
REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Run the Python script
python main.py

REM Deactivate the virtual environment
call deactivate

REM Pause to keep the console window open (optional)
pause