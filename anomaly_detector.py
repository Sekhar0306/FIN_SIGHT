"""
Anomaly Detection Module for FIN-SIGHT
Detects statistically unusual trading activity
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class AnomalyDetector:
    """Detects anomalous trading patterns before major events"""
    
    def __init__(self, df):
        """
        Initialize detector with stock data
        
        Args:
            df: DataFrame with Date index and Volume column
        """
        self.df = df.copy()
        self.avg_volume = None
        self.std_dev_volume = None
        self.anomaly_threshold = None
        
    def calculate_baseline(self, z_score=3):
        """
        Calculate baseline statistics for anomaly detection
        
        Args:
            z_score: Number of standard deviations for threshold (default: 3)
        """
        self.avg_volume = self.df['Volume'].mean()
        self.std_dev_volume = self.df['Volume'].std()
        self.anomaly_threshold = self.avg_volume + (z_score * self.std_dev_volume)
        
        return {
            'average_volume': self.avg_volume,
            'std_deviation': self.std_dev_volume,
            'anomaly_threshold': self.anomaly_threshold
        }
    
    def detect_anomalies(self, event_dates, pre_event_window=3, z_score=3):
        """
        Detect anomalies in pre-event windows
        
        Args:
            event_dates: List of datetime objects for major events
            pre_event_window: Number of days before event to check
            z_score: Number of standard deviations for threshold
            
        Returns:
            DataFrame with anomaly flags and statistics
        """
        # Calculate baseline if not already done
        if self.anomaly_threshold is None:
            self.calculate_baseline(z_score)
        
        # Initialize columns
        self.df['Is_Anomaly'] = False
        self.df['Event_Day'] = False
        self.df['Event_Type'] = ''
        self.df['Anomaly_Score'] = 0.0
        self.df['Z_Score'] = 0.0
        
        # Calculate Z-scores for all days
        self.df['Z_Score'] = (self.df['Volume'] - self.avg_volume) / self.std_dev_volume
        
        # Process each event
        for event_date in event_dates:
            # Mark the actual event day
            if event_date in self.df.index:
                self.df.loc[event_date, 'Event_Day'] = True
            
            # Define the pre-event window
            window_end = event_date - pd.Timedelta(days=1)
            window_start = event_date - pd.Timedelta(days=pre_event_window)
            
            # Find suspicious trades in the window
            mask = (self.df.index >= window_start) & (self.df.index <= window_end)
            window_data = self.df[mask]
            
            # Mark anomalies
            if not window_data.empty:
                anomaly_mask = window_data['Volume'] > self.anomaly_threshold
                anomaly_indices = window_data[anomaly_mask].index
                
                if not anomaly_indices.empty:
                    self.df.loc[anomaly_indices, 'Is_Anomaly'] = True
                    # Calculate anomaly score (how many std devs above mean)
                    self.df.loc[anomaly_indices, 'Anomaly_Score'] = (
                        self.df.loc[anomaly_indices, 'Volume'] - self.avg_volume
                    ) / self.std_dev_volume
        
        return self.df
    
    def get_anomaly_summary(self):
        """Get summary of detected anomalies"""
        anomalies = self.df[self.df['Is_Anomaly']].copy()
        
        if anomalies.empty:
            return {
                'total_anomalies': 0,
                'details': []
            }
        
        summary = {
            'total_anomalies': len(anomalies),
            'details': []
        }
        
        for idx, row in anomalies.iterrows():
            summary['details'].append({
                'date': idx,
                'volume': row['Volume'],
                'z_score': row['Z_Score'],
                'anomaly_score': row['Anomaly_Score'],
                'percentage_above_avg': ((row['Volume'] - self.avg_volume) / self.avg_volume) * 100
            })
        
        return summary
    
    def get_statistics(self):
        """Get comprehensive statistics about the data"""
        return {
            'total_days': len(self.df),
            'average_volume': self.avg_volume,
            'std_deviation': self.std_dev_volume,
            'min_volume': self.df['Volume'].min(),
            'max_volume': self.df['Volume'].max(),
            'median_volume': self.df['Volume'].median(),
            'anomaly_threshold': self.anomaly_threshold,
            'anomaly_count': self.df['Is_Anomaly'].sum(),
            'event_day_count': self.df['Event_Day'].sum()
        }
    
    def get_data_with_anomalies(self):
        """Return the full DataFrame with anomaly flags"""
        return self.df

