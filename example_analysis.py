"""
Example Analysis Script for FIN-SIGHT
Demonstrates programmatic usage of the anomaly detection system
"""

from data_collector import StockDataCollector
from anomaly_detector import AnomalyDetector
import pandas as pd
from datetime import datetime

def example_analysis():
    """
    Example: Analyze RELIANCE stock for anomalies before major events
    """
    print("=" * 60)
    print("FIN-SIGHT Example Analysis")
    print("=" * 60)
    print()
    
    # Step 1: Initialize data collector
    print("Step 1: Initializing data collector...")
    collector = StockDataCollector(api_key="VO8CV7MCLOI5GNI3")
    print("✓ Data collector initialized")
    print()
    
    # Step 2: Fetch stock data
    print("Step 2: Fetching stock data for RELIANCE.BSE...")
    try:
        df = collector.fetch_daily_data("RELIANCE.BSE")
        print(f"✓ Data fetched successfully! ({len(df)} records)")
        print(f"  Date range: {df.index.min()} to {df.index.max()}")
        print()
    except Exception as e:
        print(f"✗ Error fetching data: {str(e)}")
        print("  Tip: Check API key and stock symbol")
        return
    
    # Step 3: Initialize anomaly detector
    print("Step 3: Initializing anomaly detector...")
    detector = AnomalyDetector(df)
    print("✓ Anomaly detector initialized")
    print()
    
    # Step 4: Calculate baseline statistics
    print("Step 4: Calculating baseline statistics...")
    baseline = detector.calculate_baseline(z_score=3.0)
    print("✓ Baseline calculated:")
    print(f"  Average Volume: {baseline['average_volume']:,.0f}")
    print(f"  Standard Deviation: {baseline['std_deviation']:,.0f}")
    print(f"  Anomaly Threshold: {baseline['anomaly_threshold']:,.0f}")
    print()
    
    # Step 5: Define event dates
    print("Step 5: Defining major event dates...")
    event_dates = pd.to_datetime([
        "2024-01-19",  # Q3 FY24 Earnings
        "2024-04-22",  # Q4 FY24 Earnings
        "2024-07-19",  # Q1 FY25 Earnings
        "2024-08-29",  # Annual General Meeting
        "2024-10-18"   # Q2 FY25 Earnings
    ])
    print(f"✓ {len(event_dates)} event dates defined:")
    for date in event_dates:
        print(f"  - {date.strftime('%Y-%m-%d')}")
    print()
    
    # Step 6: Detect anomalies
    print("Step 6: Detecting anomalies...")
    detector.detect_anomalies(event_dates, pre_event_window=3, z_score=3.0)
    print("✓ Anomaly detection complete")
    print()
    
    # Step 7: Get results
    print("Step 7: Analyzing results...")
    summary = detector.get_anomaly_summary()
    stats = detector.get_statistics()
    
    print("=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)
    print()
    
    print(f"Total Days Analyzed: {stats['total_days']:,}")
    print(f"Anomalies Detected: {summary['total_anomalies']}")
    print(f"Event Days: {stats['event_day_count']}")
    print()
    
    if summary['total_anomalies'] > 0:
        print("Detected Anomalies:")
        print("-" * 60)
        for detail in summary['details']:
            print(f"Date: {detail['date'].strftime('%Y-%m-%d')}")
            print(f"  Volume: {detail['volume']:,.0f}")
            print(f"  Z-Score: {detail['z_score']:.2f}")
            print(f"  Above Average: {detail['percentage_above_avg']:.1f}%")
            print()
    else:
        print("No anomalies detected with current settings.")
        print("Try adjusting the Z-score threshold or pre-event window.")
        print()
    
    # Step 8: Save results
    print("Step 8: Saving results...")
    output_file = f"RELIANCE_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    detector.df.to_csv(output_file)
    print(f"✓ Results saved to: {output_file}")
    print()
    
    print("=" * 60)
    print("Analysis Complete!")
    print("=" * 60)
    
    return detector

def analyze_multiple_stocks():
    """
    Example: Analyze multiple stocks
    """
    print("=" * 60)
    print("Multi-Stock Analysis Example")
    print("=" * 60)
    print()
    
    stocks = ["RELIANCE.BSE", "TCS.BSE", "INFY.BSE"]
    collector = StockDataCollector(api_key="VO8CV7MCLOI5GNI3")
    
    for stock in stocks:
        print(f"Analyzing {stock}...")
        try:
            df = collector.fetch_daily_data(stock)
            detector = AnomalyDetector(df)
            detector.calculate_baseline()
            stats = detector.get_statistics()
            
            print(f"  ✓ {stock}: {stats['total_days']} days, "
                  f"Avg Volume: {stats['average_volume']:,.0f}")
            print()
            
            # Wait to avoid rate limits
            import time
            time.sleep(12)  # 5 requests per minute limit
            
        except Exception as e:
            print(f"  ✗ Error: {str(e)}")
            print()

if __name__ == "__main__":
    # Run example analysis
    example_analysis()
    
    # Uncomment to run multi-stock analysis
    # analyze_multiple_stocks()

