# 🚀 START HERE - FIN-SIGHT

Welcome to **FIN-SIGHT**! This is your starting point for using the anomaly detection tool.

## ⚡ Quick Start (3 Steps)

### 1️⃣ Install Dependencies

```bash
cd "FIN SIGHT"
pip install -r requirements.txt
```

### 2️⃣ Test Setup

```bash
python test_setup.py
```

### 3️⃣ Launch Application

```bash
streamlit run app.py
```

That's it! The app will open in your browser at `http://localhost:8501`

---

## 📚 Documentation Guide

### For First-Time Users

1. **START_HERE.md** ← You are here!
2. **[GETTING_STARTED.md](GETTING_STARTED.md)** - Detailed getting started guide
3. **[QUICKSTART.md](QUICKSTART.md)** - 5-minute tutorial
4. **[README.md](README.md)** - Complete documentation

### For Developers

1. **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Architecture overview
2. **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deploy to production
3. **[SUMMARY.md](SUMMARY.md)** - Project summary

---

## 🎯 What is FIN-SIGHT?

FIN-SIGHT is an advanced anomaly detection tool that:

- 📊 Analyzes stock trading volume patterns
- 🔍 Detects statistically unusual activity
- 📈 Identifies potential insider trading
- 📉 Visualizes trading anomalies
- 💾 Exports detailed reports

---

## 💡 First Analysis Example

### Step 1: Open the App

After running `streamlit run app.py`, the app opens at `http://localhost:8501`

### Step 2: Configure Settings (Sidebar)

- **Stock Symbol**: `RELIANCE.BSE`
- **Date Range**: Jan 2024 - Dec 2024
- **Data Type**: Daily
- **Pre-Event Window**: 3 days
- **Z-Score**: 3.0

### Step 3: Fetch Data

Click **"🔍 Analyze Stock"** button

### Step 4: Add Event Dates

In the main area, enter:

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

---

## 🎨 UI Overview

### Sidebar (Left)

- API Key configuration
- Stock symbol input
- Date range selection
- Data type selection
- Detection settings
- Action buttons

### Main Area (Center)

- Welcome screen (initially)
- Statistics and metrics
- Anomaly details table
- Interactive visualizations
- Raw data viewer

---

## 📊 Understanding Results

### Key Metrics

- **Total Days Analyzed**: Number of trading days
- **Anomalies Detected**: Days with unusual volume
- **Average Volume**: Mean trading volume
- **Anomaly Threshold**: Volume threshold for anomalies

### Anomaly Score

- **Z-Score**: Standard deviations above mean
- **Z-Score > 3**: Highly unusual (99.7% confidence)
- **Z-Score > 2**: Unusual (95% confidence)

### Visualizations

- **Volume Chart**: All trading volume with anomaly markers
- **Z-Score Distribution**: Histogram of Z-scores
- **Z-Score Timeline**: Z-scores over time

---

## 🔧 Common Stock Symbols

### Indian Stocks (BSE)

```
RELIANCE.BSE  - Reliance Industries
TCS.BSE       - Tata Consultancy Services
INFY.BSE      - Infosys
HDFCBANK.BSE  - HDFC Bank
ICICIBANK.BSE - ICICI Bank
```

### US Stocks

```
AAPL  - Apple Inc.
MSFT  - Microsoft
GOOGL - Alphabet (Google)
AMZN  - Amazon
TSLA  - Tesla
```

---

## 🐛 Troubleshooting

### "API rate limit reached"

- Wait 60 seconds and try again
- Use daily data instead of intraday

### "No data available"

- Check symbol format (e.g., RELIANCE.BSE)
- Verify date range is valid
- Ensure stock is listed on exchange

### Import errors

```bash
pip install --upgrade -r requirements.txt
```

### App won't start

```bash
# Check Python version (3.8+)
python --version

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

---

## 📈 Next Steps

1. ✅ Complete your first analysis
2. 📊 Try different stocks and settings
3. 🔧 Experiment with detection parameters
4. 📈 Compare multiple companies
5. 💾 Save and analyze reports
6. 🚀 Deploy to Streamlit Cloud

---

## 🎓 Learning Path

### Beginner

1. Read [GETTING_STARTED.md](GETTING_STARTED.md)
2. Complete first analysis
3. Try different stocks
4. Experiment with settings

### Intermediate

1. Read [README.md](README.md)
2. Understand Z-score analysis
3. Analyze multiple events
4. Export and compare reports

### Advanced

1. Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
2. Customize detection logic
3. Add new features
4. Deploy to production

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy!

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 💬 Getting Help

- 📖 Check the [README.md](README.md)
- 🐛 Review [Troubleshooting](#-troubleshooting)
- 💡 See [GETTING_STARTED.md](GETTING_STARTED.md)
- 📚 Read [QUICKSTART.md](QUICKSTART.md)

---

## 🎉 You're Ready!

You now have everything you need to start using FIN-SIGHT.

### Quick Commands

```bash
# Test setup
python test_setup.py

# Run app
streamlit run app.py

# Run example
python example_analysis.py
```

### Launch Options

```bash
# Unix/Mac
./run.sh

# Windows
run.bat

# Direct
streamlit run app.py
```

---

## 📞 Support

For questions or issues:

- Check documentation files
- Review troubleshooting section
- Open GitHub issue

---

## 🏆 Project Features

✅ **Modern UI** - Professional design  
✅ **Interactive Charts** - Plotly visualizations  
✅ **Easy to Use** - Intuitive interface  
✅ **Well Documented** - Comprehensive guides  
✅ **Production Ready** - Deployment ready  
✅ **Extensible** - Modular architecture

---

## 📦 What's Included

### Application

- Main Streamlit app
- Data collection module
- Anomaly detection engine
- Configuration system
- Utility functions

### Documentation

- Complete README
- Quick start guide
- Deployment guide
- Project structure
- Getting started tutorial

### Scripts

- Launch scripts (Unix/Windows)
- Setup test script
- Example analysis script

---

## 🎯 Success Criteria

After completing the quick start, you should be able to:

- ✅ Launch the application
- ✅ Fetch stock data
- ✅ Detect anomalies
- ✅ View results
- ✅ Export reports
- ✅ Understand the UI

---

## 🚀 Ready to Launch!

Run this command to start:

```bash
streamlit run app.py
```

Then open your browser to: `http://localhost:8501`

**Happy Analyzing! 📈**

---

<div align="center">

**Built with ❤️ for Financial Analysis**

⭐ Star this repo if you find it useful!

</div>
