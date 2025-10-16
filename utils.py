"""
Utility functions for FIN-SIGHT
Helper functions for data processing and formatting
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def format_number(num, decimals=0):
    """
    Format number with commas and decimal places
    
    Args:
        num: Number to format
        decimals: Number of decimal places
        
    Returns:
        Formatted string
    """
    if pd.isna(num):
        return "N/A"
    return f"{num:,.{decimals}f}"

def format_percentage(num, decimals=1):
    """
    Format number as percentage
    
    Args:
        num: Number to format
        decimals: Number of decimal places
        
    Returns:
        Formatted percentage string
    """
    if pd.isna(num):
        return "N/A"
    return f"{num:.{decimals}f}%"

def calculate_returns(df, period=1):
    """
    Calculate returns for stock data
    
    Args:
        df: DataFrame with Close prices
        period: Period for return calculation
        
    Returns:
        DataFrame with returns
    """
    df = df.copy()
    df['Returns'] = df['Close'].pct_change(period)
    return df

def calculate_volatility(df, window=30):
    """
    Calculate rolling volatility
    
    Args:
        df: DataFrame with returns
        window: Rolling window size
        
    Returns:
        DataFrame with volatility
    """
    df = df.copy()
    df['Volatility'] = df['Returns'].rolling(window=window).std() * np.sqrt(252)
    return df

def validate_date_range(start_date, end_date):
    """
    Validate date range
    
    Args:
        start_date: Start date
        end_date: End date
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if start_date >= end_date:
        return False, "Start date must be before end date"
    
    if (end_date - start_date).days < 30:
        return False, "Date range must be at least 30 days"
    
    if (end_date - start_date).days > 365:
        return False, "Date range should not exceed 1 year for free API tier"
    
    return True, ""

def validate_stock_symbol(symbol):
    """
    Validate stock symbol format
    
    Args:
        symbol: Stock symbol to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not symbol:
        return False, "Stock symbol cannot be empty"
    
    if len(symbol) < 2:
        return False, "Stock symbol too short"
    
    if len(symbol) > 20:
        return False, "Stock symbol too long"
    
    # Check for valid characters
    if not symbol.replace('.', '').replace('-', '').isalnum():
        return False, "Stock symbol contains invalid characters"
    
    return True, ""

def parse_event_dates(date_string):
    """
    Parse event dates from text input
    
    Args:
        date_string: Multi-line string with dates
        
    Returns:
        List of datetime objects
    """
    dates = []
    for line in date_string.strip().split('\n'):
        line = line.strip()
        if line:
            try:
                dates.append(pd.to_datetime(line))
            except:
                pass
    return dates

def calculate_anomaly_severity(z_score):
    """
    Calculate anomaly severity based on Z-score
    
    Args:
        z_score: Z-score value
        
    Returns:
        Severity level (Low, Medium, High, Critical)
    """
    if z_score < 2:
        return "Low"
    elif z_score < 3:
        return "Medium"
    elif z_score < 4:
        return "High"
    else:
        return "Critical"

def get_anomaly_color(severity):
    """
    Get color for anomaly severity
    
    Args:
        severity: Severity level
        
    Returns:
        Color code
    """
    colors = {
        "Low": "yellow",
        "Medium": "orange",
        "High": "red",
        "Critical": "darkred"
    }
    return colors.get(severity, "gray")

def generate_report_summary(detector, output_format="text"):
    """
    Generate summary report
    
    Args:
        detector: AnomalyDetector instance
        output_format: Output format (text, json, html)
        
    Returns:
        Report string
    """
    stats = detector.get_statistics()
    summary = detector.get_anomaly_summary()
    
    if output_format == "text":
        report = f"""
FIN-SIGHT Analysis Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SUMMARY
-------
Total Days Analyzed: {stats['total_days']:,}
Anomalies Detected: {summary['total_anomalies']}
Event Days: {stats['event_day_count']}

STATISTICS
----------
Average Volume: {format_number(stats['average_volume'])}
Standard Deviation: {format_number(stats['std_deviation'])}
Minimum Volume: {format_number(stats['min_volume'])}
Maximum Volume: {format_number(stats['max_volume'])}
Median Volume: {format_number(stats['median_volume'])}
Anomaly Threshold: {format_number(stats['anomaly_threshold'])}

ANOMALIES
---------
"""
        if summary['total_anomalies'] > 0:
            for detail in summary['details']:
                severity = calculate_anomaly_severity(detail['z_score'])
                report += f"""
Date: {detail['date'].strftime('%Y-%m-%d')}
  Volume: {format_number(detail['volume'])}
  Z-Score: {detail['z_score']:.2f}
  Severity: {severity}
  Above Average: {format_percentage(detail['percentage_above_avg'])}
"""
        else:
            report += "No anomalies detected.\n"
        
        return report
    
    elif output_format == "json":
        import json
        return json.dumps({
            'summary': {
                'total_days': stats['total_days'],
                'anomalies_detected': summary['total_anomalies'],
                'event_days': stats['event_day_count']
            },
            'statistics': {
                'average_volume': stats['average_volume'],
                'std_deviation': stats['std_deviation'],
                'anomaly_threshold': stats['anomaly_threshold']
            },
            'anomalies': summary['details']
        }, indent=2, default=str)
    
    return ""

def save_analysis_report(detector, filename=None):
    """
    Save complete analysis report
    
    Args:
        detector: AnomalyDetector instance
        filename: Output filename (optional)
        
    Returns:
        Filename of saved report
    """
    if filename is None:
        filename = f"fin_sight_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    report = generate_report_summary(detector, output_format="text")
    
    with open(filename, 'w') as f:
        f.write(report)
    
    return filename

def create_directories():
    """Create necessary directories if they don't exist"""
    import os
    directories = ['data', 'reports', 'exports']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

