# 📈 FIN-SIGHT: Anomaly Detection in Stock Trades

<div align="center">

![FIN-SIGHT](https://img.shields.io/badge/FIN--SIGHT-Anomaly%20Detection-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg?style=for-the-badge&logo=streamlit)

**Identify statistically unusual stock trading activity before major announcements**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Deployment](#-deployment)

</div>

---

## 🎯 Overview

FIN-SIGHT is an advanced anomaly detection tool that programmatically identifies statistically unusual stock trading activity immediately preceding significant public announcements. This tool helps detect potential insider trading patterns by analyzing trading volume anomalies using statistical methods.

### Key Capabilities

- **Real-time Data Collection**: Fetch historical stock data from Alpha Vantage API
- **Statistical Analysis**: Use Z-score analysis to identify volume anomalies
- **Interactive Visualizations**: Beautiful, interactive charts powered by Plotly
- **Event Correlation**: Link anomalies to specific major announcements
- **Export Reports**: Download detailed anomaly reports as CSV

---

## ✨ Features

### 📊 Data Collection

- Multiple time intervals (Daily, Weekly, Intraday)
- Flexible date range selection
- Support for various stock exchanges (BSE, NSE, NYSE, NASDAQ)
- Real-time data fetching from Alpha Vantage API

### 🔍 Anomaly Detection

- **Z-Score Analysis**: Identify statistically significant volume spikes
- **Configurable Thresholds**: Adjust sensitivity based on your needs
- **Pre-Event Windows**: Define custom time windows before announcements
- **Multiple Event Support**: Analyze multiple major events simultaneously

### 📈 Visualization

- Interactive volume charts with anomaly highlighting
- Z-score distribution histograms
- Timeline analysis of trading patterns
- Event day markers and anomaly indicators

### 💼 Professional UI

- Modern, clean interface inspired by leading financial platforms
- Responsive design with gradient accents
- Intuitive sidebar navigation
- Real-time feedback and status updates

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Alpha Vantage API key ([Get one here](https://www.alphavantage.co/support/#api-key))

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd "FIN SIGHT"
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key

The API key is pre-configured in the application, but you can also:

1. Create a `.env` file in the project root:

```bash
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

2. Or enter it directly in the Streamlit app sidebar

---

## 💻 Usage

### Running Locally

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Step-by-Step Guide

1. **Enter Stock Symbol**

   - Example: `RELIANCE.BSE`, `TCS.BSE`, `AAPL`, `MSFT`
   - Format: `SYMBOL.EXCHANGE` (e.g., RELIANCE.BSE)

2. **Select Date Range**

   - Choose start and end dates for analysis
   - Recommended: At least 3 months of data

3. **Choose Data Type**

   - **Daily**: Best for most analyses
   - **Weekly**: For long-term trends
   - **Intraday**: For detailed intraday patterns

4. **Configure Detection Settings**

   - **Pre-Event Window**: Days before event to check (1-7 days)
   - **Z-Score Threshold**: Sensitivity level (2.0-5.0 standard deviations)

5. **Add Event Dates**

   - Enter dates of major announcements (earnings, AGM, etc.)
   - Format: `YYYY-MM-DD` (one per line)

6. **Click "Detect Anomalies"**
   - View results, statistics, and visualizations
   - Download anomaly reports as CSV

---

## 📖 Example Use Cases

### 1. Insider Trading Detection

```python
# Analyze RELIANCE stock before Q4 earnings
Symbol: RELIANCE.BSE
Date Range: 2024-01-01 to 2024-12-31
Event Dates: 2024-04-22 (Q4 Earnings)
Pre-Event Window: 3 days
Z-Score: 3.0
```

### 2. Market Manipulation Analysis

```python
# Check for unusual activity before major announcements
Symbol: TCS.BSE
Date Range: Last 6 months
Event Dates: Multiple earnings dates
Pre-Event Window: 5 days
Z-Score: 2.5 (more sensitive)
```

### 3. Volume Pattern Analysis

```python
# Understand normal trading patterns
Symbol: Any stock
Date Range: 1 year
Focus: Volume distribution and trends
```

---

## 🎨 UI Features

### Modern Design Elements

- **Gradient Headers**: Eye-catching purple gradient
- **Card-Based Layout**: Clean, organized information display
- **Interactive Charts**: Hover, zoom, and pan capabilities
- **Responsive Metrics**: Real-time statistics display
- **Color-Coded Indicators**: Red for anomalies, green for events

### User Experience

- **One-Click Analysis**: Streamlined workflow
- **Real-Time Feedback**: Progress indicators and status messages
- **Export Functionality**: Download reports instantly
- **Reset Capability**: Start fresh analysis easily

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

### Environment Variables

If using `.env` file, add to Streamlit Cloud:

- Go to app settings
- Add environment variable: `ALPHA_VANTAGE_API_KEY`

---

## 📊 Understanding Results

### Anomaly Score

- **Z-Score**: Number of standard deviations above mean
- **Z-Score > 3**: Highly unusual (99.7% confidence)
- **Z-Score > 2**: Unusual (95% confidence)

### Anomaly Threshold

Calculated as: `Average Volume + (Z-Score × Standard Deviation)`

### Interpretation

- **High Volume + Pre-Event**: Potential insider trading
- **Consistent Anomalies**: Pattern worth investigating
- **Isolated Spikes**: May be normal market activity

---

## 🔧 Technical Details

### Architecture

```
FIN-SIGHT/
├── app.py                 # Main Streamlit application
├── data_collector.py      # Alpha Vantage API integration
├── anomaly_detector.py    # Statistical analysis engine
├── requirements.txt       # Python dependencies
└── README.md             # Documentation
```

### Key Technologies

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **Alpha Vantage API**: Stock market data
- **NumPy**: Numerical computations

### Statistical Methods

- **Z-Score Analysis**: Standard deviation-based anomaly detection
- **Volume Analysis**: Trading volume as primary indicator
- **Event Correlation**: Temporal relationship analysis
- **Threshold Optimization**: Configurable sensitivity

---

## 📝 API Rate Limits

Alpha Vantage API has rate limits:

- **Free Tier**: 5 API requests per minute
- **Premium Tier**: 500+ requests per minute

**Tips to avoid rate limits:**

- Use daily data instead of intraday
- Analyze one stock at a time
- Wait between requests if needed

---

## 🐛 Troubleshooting

### Common Issues

**1. API Rate Limit Error**

```
Solution: Wait 60 seconds between requests or upgrade API tier
```

**2. No Data Available**

```
Solution: Check stock symbol format (e.g., RELIANCE.BSE not RELIANCE)
```

**3. Import Errors**

```
Solution: Run pip install -r requirements.txt
```

**4. Date Range Issues**

```
Solution: Ensure start date is before end date
```

---

## 📈 Future Enhancements

- [ ] Multi-stock comparison
- [ ] Machine learning-based detection
- [ ] Email alerts for anomalies
- [ ] Historical pattern analysis
- [ ] Integration with news APIs
- [ ] Portfolio-level analysis
- [ ] Advanced statistical models

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Alpha Vantage**: For providing reliable stock market data
- **Streamlit**: For the amazing web framework
- **Plotly**: For beautiful interactive visualizations
- **Open Source Community**: For inspiration and support

---

## 📞 Support

For questions, issues, or suggestions:

- Open an issue on GitHub
- Contact: [Your Contact Information]

---

<div align="center">

**Built with ❤️ for Financial Analysis**

⭐ Star this repo if you find it useful!

</div>
