@echo off
REM Kickstart Learning Agent - Quick Setup Script for Windows
REM This script helps you get the application running quickly on Windows

echo 🚀 Kickstart Learning Agent - Quick Setup (Windows)
echo ============================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is required but not installed.
    echo Please install Python 3.8+ from https://python.org and try again.
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Create virtual environment if it doesn't exist
if not exist "kickstart_env" (
    echo 📦 Creating virtual environment...
    python -m venv kickstart_env
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call kickstart_env\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Check if .env file exists
if not exist ".env" (
    echo ⚙️  Setting up environment file...
    copy .env.example .env
    echo.
    echo 🔑 IMPORTANT: Please edit .env file with your API keys:
    echo    - Get Google API key from: https://aistudio.google.com/
    echo    - Get Tavily API key from: https://app.tavily.com/
    echo.
    pause
)

REM Test the setup
echo 🧪 Testing setup...
python -c "import flask; import langchain; import dotenv; print('✅ All dependencies imported successfully!')"

echo.
echo 🎉 Setup complete! You can now run the application:
echo.
echo 📱 Web Interface:
echo    python app.py
echo    Then open: http://localhost:5000
echo.
echo 💻 CLI Interface:
echo    python main.py
echo.
echo 📚 For more options, check the README.md file
pause
