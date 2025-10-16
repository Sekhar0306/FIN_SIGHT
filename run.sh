#!/bin/bash

# FIN-SIGHT Launch Script
echo "🚀 Starting FIN-SIGHT..."
echo "📈 Anomaly Detection in Stock Trades"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null
then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

# Install dependencies if needed
echo "📦 Checking dependencies..."
pip3 install -r requirements.txt --quiet

# Run Streamlit app
echo ""
echo "✅ Dependencies installed!"
echo "🌐 Launching application..."
echo ""
streamlit run app.py

