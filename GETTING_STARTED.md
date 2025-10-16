# 🎯 Getting Started with FIN-SIGHT

Welcome to FIN-SIGHT! This guide will help you get up and running in minutes.

## 📋 What is FIN-SIGHT?

FIN-SIGHT is an advanced anomaly detection tool that identifies statistically unusual stock trading activity before major announcements. It helps detect potential insider trading patterns using sophisticated statistical analysis.

## ✨ Key Features

- 🔍 **Automated Anomaly Detection**: Identify suspicious trading patterns
- 📊 **Interactive Visualizations**: Beautiful charts powered by Plotly
- 📈 **Multiple Data Sources**: Daily, weekly, and intraday data
- 🎯 **Event Correlation**: Link anomalies to specific announcements
- 📥 **Export Reports**: Download detailed CSV reports

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Dependencies

```bash
cd "FIN SIGHT"
pip install -r requirements.txt
```

### Step 2: Launch the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Step 3: Run Your First Analysis

1. **Enter Stock Symbol**: `RELIANCE.BSE`
2. **Select Date Range**: Jan 2024 - Dec 2024
3. **Choose Data Type**: Daily
4. **Click "Analyze Stock"**
5. **Add Event Dates**:
   ```
   2024-01-19
   2024-04-22
   2024-07-19
   2024-10-18
   ```
6. **Click "Detect Anomalies"**
7. **View Results**: Check metrics, charts, and anomalies

## 📚 Documentation

### For Beginners

- 📖 [Quick Start Guide](QUICKSTART.md) - Step-by-step tutorial
- 📖 [README](README.md) - Complete documentation

### For Developers

- 🏗️ [Project Structure](PROJECT_STRUCTURE.md) - Architecture overview
- 🚀 [Deployment Guide](DEPLOYMENT.md) - Deploy to production

## 💡 Example Use Cases

### 1. Insider Trading Detection

```
Symbol: RELIANCE.BSE
Date Range: 2024-01-01 to 2024-12-31
Event: Q4 Earnings (2024-04-22)
Pre-Event Window: 3 days
Z-Score: 3.0
```

### 2. Volume Pattern Analysis

```
Symbol: TCS.BSE
Date Range: Last 6 months
Focus: Normal trading patterns
```

### 3. Multi-Event Analysis

```
Symbol: INFY.BSE
Events: All quarterly earnings
Analysis: Compare pre-event patterns
```

## 🎨 UI Overview

### Sidebar

- **Configuration**: API key, stock symbol, date range
- **Detection Settings**: Pre-event window, Z-score threshold
- **Action Buttons**: Analyze, reset, export

### Main Area

- **Statistics**: Key metrics and summaries
- **Anomaly Details**: Table of detected anomalies
- **Visualizations**: Interactive charts
- **Raw Data**: Complete dataset

## 🔧 Configuration

### API Key

The default API key is pre-configured. For production use:

1. Get your own key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. Enter it in the sidebar or set in `.env` file

### Detection Settings

**Pre-Event Window** (1-7 days)

- Shorter window: More precise timing
- Longer window: Broader analysis

**Z-Score Threshold** (2.0-5.0)

- Lower (2.0): More sensitive, more anomalies
- Higher (5.0): Less sensitive, only extreme cases
- Recommended: 3.0 (99.7% confidence)

## 📊 Understanding Results

### Metrics

- **Total Days Analyzed**: Number of trading days
- **Anomalies Detected**: Days with unusual volume
- **Average Volume**: Mean trading volume
- **Anomaly Threshold**: Volume threshold for anomalies

### Anomaly Score

- **Z-Score**: Standard deviations above mean
- **Z-Score > 3**: Highly unusual (99.7% confidence)
- **Z-Score > 2**: Unusual (95% confidence)

### Visualizations

- **Volume Chart**: Shows all trading volume with anomaly markers
- **Z-Score Distribution**: Histogram of Z-scores
- **Z-Score Timeline**: Z-scores over time

## 🎯 Best Practices

### Data Selection

✅ Use daily data for most analyses  
✅ Select at least 3 months of data  
✅ Include multiple major events  
✅ Use recent data for current trends

### Detection Settings

✅ Start with Z-score 3.0  
✅ Use 3-day pre-event window  
✅ Adjust based on results  
✅ Compare multiple stocks

### Analysis

✅ Review both charts and tables  
✅ Check anomaly severity  
✅ Compare with event dates  
✅ Export reports for documentation

## 🐛 Troubleshooting

### Common Issues

**"API rate limit reached"**

- Wait 60 seconds between requests
- Use daily data instead of intraday
- Consider upgrading API tier

**"No data available"**

- Check stock symbol format (e.g., RELIANCE.BSE)
- Verify date range is valid
- Ensure stock is listed on exchange

**Import errors**

```bash
pip install --upgrade -r requirements.txt
```

**App won't start**

```bash
# Check Python version (3.8+)
python --version

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

## 📈 Next Steps

1. ✅ Complete your first analysis
2. 📊 Try different stocks and settings
3. 🔧 Experiment with detection parameters
4. 📈 Compare multiple companies
5. 💾 Save and analyze reports
6. 🚀 Deploy to Streamlit Cloud

## 🎓 Learning Resources

### Statistical Concepts

- **Z-Score**: Standard deviation measure
- **Normal Distribution**: Statistical baseline
- **Anomaly Detection**: Outlier identification

### Financial Concepts

- **Trading Volume**: Number of shares traded
- **Insider Trading**: Illegal trading on non-public info
- **Market Manipulation**: Artificial price/volume changes

### Technical Skills

- **Python**: Programming language
- **Pandas**: Data manipulation
- **Streamlit**: Web app framework
- **Plotly**: Interactive charts

## 💬 Getting Help

- 📖 Check the [README](README.md)
- 🐛 Review [Troubleshooting](#-troubleshooting)
- 💡 See [Example Use Cases](#-example-use-cases)
- 📚 Read the [Quick Start Guide](QUICKSTART.md)

## 🎉 You're Ready!

You now have everything you need to start using FIN-SIGHT. Follow the Quick Start steps above and begin your first analysis!

---

**Happy Analyzing! 📈**

For more information, visit:

- 📖 [Full Documentation](README.md)
- 🚀 [Deployment Guide](DEPLOYMENT.md)
- 🏗️ [Project Structure](PROJECT_STRUCTURE.md)
