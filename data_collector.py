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
            response = requests.get(self.base_url, params=params, timeout=30)
            data = response.json()
            
            # Check for various error types
            if 'Error Message' in data:
                error_msg = data['Error Message']
                # Provide helpful suggestions based on error
                if 'Invalid API call' in error_msg:
                    raise ValueError(
                        f"Invalid API call for symbol '{symbol}'. "
                        f"Common issues:\n"
                        f"1. Symbol format - Try without exchange suffix (e.g., 'RELIANCE' instead of 'RELIANCE.BSE')\n"
                        f"2. Symbol doesn't exist on Alpha Vantage\n"
                        f"3. API key may be invalid\n\n"
                        f"Popular symbols: AAPL, MSFT, GOOGL, AMZN, TSLA, RELIANCE, TCS, INFY"
                    )
                else:
                    raise ValueError(f"API Error: {error_msg}")
            
            if 'Note' in data:
                raise ValueError(
                    "API rate limit reached. Alpha Vantage free tier allows 5 API calls per minute.\n"
                    "Please wait 60 seconds and try again, or upgrade to a premium API key."
                )
            
            if 'Information' in data:
                info_msg = data['Information']
                raise ValueError(f"API Information: {info_msg}")
            
            if 'Time Series (Daily)' not in data:
                # Try to provide helpful error message
                if 'Meta Data' in data:
                    raise ValueError(
                        f"Unexpected data format for symbol '{symbol}'. "
                        f"The API returned data but not in the expected format."
                    )
                else:
                    raise ValueError(
                        f"No data available for symbol '{symbol}'.\n"
                        f"Try using the base symbol without exchange suffix:\n"
                        f"- Use 'AAPL' instead of 'AAPL.NASDAQ'\n"
                        f"- Use 'RELIANCE' instead of 'RELIANCE.BSE'\n"
                        f"- Use 'TCS' instead of 'TCS.BSE'"
                    )
            
            # Convert to DataFrame
            df = pd.DataFrame(data['Time Series (Daily)']).T
            df.index = pd.to_datetime(df.index)
            df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            df = df.astype(float)
            
            return df.sort_index()
            
        except requests.exceptions.Timeout:
            raise Exception("Request timeout. Please check your internet connection and try again.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {str(e)}")
        except ValueError as e:
            raise e
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

