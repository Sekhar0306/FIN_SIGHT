"""
Configuration file for FIN-SIGHT
Centralized settings and constants
"""

# API Configuration
ALPHA_VANTAGE_API_KEY = "VO8CV7MCLOI5GNI3"
ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"

# Default Settings
DEFAULT_STOCK_SYMBOL = "RELIANCE.BSE"
DEFAULT_START_DATE = "2024-01-01"
DEFAULT_END_DATE = "2024-12-31"
DEFAULT_DATA_TYPE = "Daily"
DEFAULT_PRE_EVENT_WINDOW = 3
DEFAULT_Z_SCORE = 3.0

# Detection Settings
MIN_PRE_EVENT_WINDOW = 1
MAX_PRE_EVENT_WINDOW = 7
MIN_Z_SCORE = 2.0
MAX_Z_SCORE = 5.0

# Visualization Settings
CHART_HEIGHT = 500
CHART_TEMPLATE = "plotly_white"
ANOMALY_COLOR = "red"
EVENT_COLOR = "green"
VOLUME_COLOR = "rgba(102, 126, 234, 0.6)"

# UI Settings
PAGE_TITLE = "FIN-SIGHT | Anomaly Detection in Stock Trades"
PAGE_ICON = "📈"
LAYOUT = "wide"

# Supported Stock Exchanges
SUPPORTED_EXCHANGES = {
    "BSE": ".BSE",
    "NSE": ".NS",
    "NYSE": "",
    "NASDAQ": ""
}

# Example Event Dates (for demo purposes)
EXAMPLE_EVENT_DATES = [
    "2024-01-19",  # Q3 FY24 Earnings
    "2024-04-22",  # Q4 FY24 Earnings
    "2024-07-19",  # Q1 FY25 Earnings
    "2024-08-29",  # Annual General Meeting
    "2024-10-18"   # Q2 FY25 Earnings
]

# Popular Indian Stocks
POPULAR_STOCKS = {
    "Reliance Industries": "RELIANCE.BSE",
    "Tata Consultancy Services": "TCS.BSE",
    "Infosys": "INFY.BSE",
    "HDFC Bank": "HDFCBANK.BSE",
    "ICICI Bank": "ICICIBANK.BSE",
    "State Bank of India": "SBIN.BSE",
    "Bharti Airtel": "BHARTIARTL.BSE",
    "Bajaj Finance": "BAJFINANCE.BSE"
}

# Popular US Stocks
POPULAR_US_STOCKS = {
    "Apple Inc.": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Tesla": "TSLA",
    "Meta (Facebook)": "META",
    "Netflix": "NFLX",
    "Nvidia": "NVDA"
}

# File Paths
DATA_DIR = "data"
REPORTS_DIR = "reports"

# Rate Limiting
API_RATE_LIMIT = 5  # requests per minute for free tier
API_RATE_LIMIT_WAIT = 60  # seconds to wait

