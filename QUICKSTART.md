# 🚀 Quick Start Guide

Get FIN-SIGHT up and running in 5 minutes!

## Prerequisites

✅ Python 3.8 or higher  
✅ Internet connection  
✅ Alpha Vantage API key (included: `VO8CV7MCLOI5GNI3`)

## Installation

### Option 1: Using the Launch Script (Recommended)

```bash
cd "FIN SIGHT"
./run.sh
```

### Option 2: Manual Installation

```bash
# Navigate to project directory
cd "FIN SIGHT"

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## First Analysis

### Step 1: Open the App

After running the command, the app will open in your browser at `http://localhost:8501`

### Step 2: Configure Settings

In the sidebar:

- **Stock Symbol**: Enter `RELIANCE.BSE` (or any stock)
- **Date Range**: Select any range (e.g., Jan 2024 - Dec 2024)
- **Data Type**: Choose "Daily"
- **Pre-Event Window**: Set to 3 days
- **Z-Score**: Set to 3.0

### Step 3: Fetch Data

Click **"🔍 Analyze Stock"** button

### Step 4: Add Event Dates

In the main area, enter event dates:

```
2024-01-19
2024-04-22
2024-07-19
2024-10-18
```

### Step 5: Detect Anomalies

Click **"🔍 Detect Anomalies"** button

### Step 6: View Results

- Check the metrics at the top
- Review detected anomalies
- Explore interactive charts
- Download CSV report

## Common Stock Symbols

### Indian Stocks (BSE)

- `RELIANCE.BSE` - Reliance Industries
- `TCS.BSE` - Tata Consultancy Services
- `INFY.BSE` - Infosys
- `HDFCBANK.BSE` - HDFC Bank
- `ICICIBANK.BSE` - ICICI Bank

### US Stocks

- `AAPL` - Apple Inc.
- `MSFT` - Microsoft
- `GOOGL` - Alphabet (Google)
- `AMZN` - Amazon
- `TSLA` - Tesla

## Tips for Best Results

1. **Use Daily Data**: Best for most analyses
2. **3-Month Minimum**: At least 90 days of data
3. **Z-Score 3.0**: Good starting point (99.7% confidence)
4. **3-Day Window**: Standard pre-event window
5. **Multiple Events**: Add all major announcements

## Troubleshooting

### "API rate limit reached"

- Wait 60 seconds and try again
- Use daily data instead of intraday

### "No data available"

- Check symbol format (e.g., RELIANCE.BSE)
- Verify date range is valid
- Ensure stock is listed on the exchange

### Import errors

```bash
pip install --upgrade -r requirements.txt
```

## Next Steps

1. ✅ Complete your first analysis
2. 📊 Try different stocks and date ranges
3. 🔧 Experiment with detection settings
4. 📈 Analyze multiple companies
5. 💾 Save and compare reports

## Need Help?

- 📖 Read the full [README.md](README.md)
- 🐛 Check [Troubleshooting](#troubleshooting)
- 💬 Open an issue on GitHub

---

**Happy Analyzing! 📈**
