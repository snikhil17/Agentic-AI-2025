#!/bin/bash

# Kickstart Learning Agent - Quick Setup Script
# This script helps you get the application running quickly

set -e

echo "🚀 Kickstart Learning Agent - Quick Setup"
echo "========================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8+ and try again."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "kickstart_env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv kickstart_env
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source kickstart_env/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚙️  Setting up environment file..."
    cp .env.example .env
    echo ""
    echo "🔑 IMPORTANT: Please edit .env file with your API keys:"
    echo "   - Get Google API key from: https://aistudio.google.com/"
    echo "   - Get Tavily API key from: https://app.tavily.com/"
    echo ""
    read -p "Press Enter after you've updated the .env file with your API keys..."
fi

# Test the setup
echo "🧪 Testing setup..."
python3 -c "
import flask
import langchain
import dotenv
print('✅ All dependencies imported successfully!')
"

echo ""
echo "🎉 Setup complete! You can now run the application:"
echo ""
echo "📱 Web Interface:"
echo "   python app.py"
echo "   Then open: http://localhost:5000"
echo ""
echo "💻 CLI Interface:"
echo "   python main.py"
echo ""
echo "📚 For more options, check the README.md file"
