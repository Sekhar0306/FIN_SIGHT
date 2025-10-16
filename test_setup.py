"""
Test script to verify FIN-SIGHT setup
Run this to check if all dependencies are installed correctly
"""

import sys

def test_imports():
    """Test if all required packages are installed"""
    print("=" * 60)
    print("FIN-SIGHT Setup Test")
    print("=" * 60)
    print()
    
    print("Testing Python version...")
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print("✓ Python version OK")
    print()
    
    print("Testing required packages...")
    
    packages = {
        'streamlit': 'Streamlit',
        'pandas': 'Pandas',
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'seaborn': 'Seaborn',
        'plotly': 'Plotly',
        'requests': 'Requests',
        'yfinance': 'YFinance'
    }
    
    failed = []
    
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name}")
        except ImportError:
            print(f"❌ {name} - NOT INSTALLED")
            failed.append(name)
    
    print()
    
    if failed:
        print("=" * 60)
        print("FAILED PACKAGES")
        print("=" * 60)
        print(f"Please install: {', '.join(failed)}")
        print()
        print("Run: pip install -r requirements.txt")
        print()
        return False
    else:
        print("=" * 60)
        print("✓ ALL PACKAGES INSTALLED")
        print("=" * 60)
        print()
        print("Setup is complete! You can now run:")
        print("  streamlit run app.py")
        print()
        return True

def test_api_connection():
    """Test Alpha Vantage API connection"""
    print("Testing Alpha Vantage API connection...")
    try:
        from data_collector import StockDataCollector
        
        collector = StockDataCollector(api_key="VO8CV7MCLOI5GNI3")
        print("✓ Data collector initialized")
        
        # Try to fetch a small amount of data
        try:
            df = collector.fetch_daily_data("RELIANCE.BSE")
            print(f"✓ API connection successful! ({len(df)} records)")
            return True
        except Exception as e:
            if "rate limit" in str(e).lower():
                print("⚠ API rate limit reached (this is OK)")
                return True
            else:
                print(f"⚠ API error: {str(e)}")
                return False
                
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print()
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test API connection
        test_api_connection()
        print()
        print("=" * 60)
        print("Setup test complete!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. Run: streamlit run app.py")
        print("2. Open browser to: http://localhost:8501")
        print("3. Start analyzing stocks!")
        print()
    else:
        print()
        print("=" * 60)
        print("Setup incomplete. Please install missing packages.")
        print("=" * 60)
        print()

