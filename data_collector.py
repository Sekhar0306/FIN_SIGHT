"""
Data Collection Module for FIN-SIGHT
Handles fetching stock data from Alpha Vantage API
"""

import pandas as pd
import requests
import time
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

class StockDataCollector:
    """Collects stock data from Alpha Vantage API"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('ALPHA_VANTAGE_API_KEY')
        self.base_url = "https://www.alphavantage.co/query"
        
    def fetch_intraday_data(self, symbol, interval='60min', outputsize='full'):
        """
        Fetch intraday stock data
        
        Args:
            symbol: Stock ticker symbol (e.g., 'RELIANCE.BSE')
            interval: Time interval (1min, 5min, 15min, 30min, 60min)
            outputsize: 'compact' (100 data points) or 'full' (all data)
        """
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': interval,
            'apikey': self.api_key,
            'outputsize': outputsize
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if 'Error Message' in data:
                raise ValueError(f"API Error: {data['Error Message']}")
            
            if 'Note' in data:
                raise ValueError("API rate limit reached. Please wait a moment.")
            
            if 'Time Series (60min)' not in data:
                raise ValueError(f"No data available for symbol: {symbol}")
            
            # Convert to DataFrame
            df = pd.DataFrame(data['Time Series (60min)']).T
            df.index = pd.to_datetime(df.index)
            df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            df = df.astype(float)
            
            return df.sort_index()
            
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def fetch_daily_data(self, symbol, outputsize='full'):
        """
        Fetch daily stock data
        
        Args:
            symbol: Stock ticker symbol
            outputsize: 'compact' (100 data points) or 'full' (all data)
        """
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': self.api_key,
            'outputsize': outputsize
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if 'Error Message' in data:
                raise ValueError(f"API Error: {data['Error Message']}")
            
            if 'Note' in data:
                raise ValueError("API rate limit reached. Please wait a moment.")
            
            if 'Time Series (Daily)' not in data:
                raise ValueError(f"No data available for symbol: {symbol}")
            
            # Convert to DataFrame
            df = pd.DataFrame(data['Time Series (Daily)']).T
            df.index = pd.to_datetime(df.index)
            df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            df = df.astype(float)
            
            return df.sort_index()
            
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def fetch_weekly_data(self, symbol):
        """Fetch weekly stock data"""
        params = {
            'function': 'TIME_SERIES_WEEKLY',
            'symbol': symbol,
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if 'Error Message' in data:
                raise ValueError(f"API Error: {data['Error Message']}")
            
            if 'Time Series (Weekly)' not in data:
                raise ValueError(f"No data available for symbol: {symbol}")
            
            # Convert to DataFrame
            df = pd.DataFrame(data['Time Series (Weekly)']).T
            df.index = pd.to_datetime(df.index)
            df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            df = df.astype(float)
            
            return df.sort_index()
            
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def save_data(self, df, filename):
        """Save DataFrame to CSV"""
        df.to_csv(filename)
        return filename

