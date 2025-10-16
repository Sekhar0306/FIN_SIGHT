# 📁 Project Structure

Complete overview of FIN-SIGHT project structure

```
FIN SIGHT/
│
├── 📄 app.py                      # Main Streamlit application
├── 📄 data_collector.py           # Alpha Vantage API integration
├── 📄 anomaly_detector.py         # Statistical analysis engine
├── 📄 config.py                   # Configuration and constants
├── 📄 utils.py                    # Utility functions
├── 📄 example_analysis.py         # Example usage script
│
├── 📄 requirements.txt            # Python dependencies
├── 📄 LICENSE                     # MIT License
│
├── 📄 README.md                   # Main documentation
├── 📄 QUICKSTART.md               # Quick start guide
├── 📄 DEPLOYMENT.md               # Deployment guide
├── 📄 PROJECT_STRUCTURE.md        # This file
│
├── 📄 run.sh                      # Launch script (Unix/Mac)
│
├── 📁 .streamlit/
│   └── config.toml               # Streamlit configuration
│
├── 📁 data/                       # Data storage (gitignored)
├── 📁 reports/                    # Generated reports (gitignored)
└── 📁 exports/                    # Exported files (gitignored)
```

## File Descriptions

### Core Application Files

#### `app.py`

**Main Streamlit Application**

- Entry point for the web application
- UI components and layout
- User interaction handling
- Visualization rendering
- Session state management

**Key Functions:**

- `main()`: Main application function
- `display_welcome()`: Welcome screen
- `display_analysis()`: Analysis results display

#### `data_collector.py`

**Data Collection Module**

- Alpha Vantage API integration
- Multiple data interval support (daily, weekly, intraday)
- Error handling and rate limiting
- Data caching and persistence

**Key Classes:**

- `StockDataCollector`: Main data collection class

**Key Methods:**

- `fetch_daily_data()`: Fetch daily stock data
- `fetch_weekly_data()`: Fetch weekly stock data
- `fetch_intraday_data()`: Fetch intraday stock data

#### `anomaly_detector.py`

**Anomaly Detection Engine**

- Statistical analysis using Z-scores
- Baseline calculation
- Anomaly detection logic
- Event correlation
- Result summarization

**Key Classes:**

- `AnomalyDetector`: Main detection class

**Key Methods:**

- `calculate_baseline()`: Calculate statistical baseline
- `detect_anomalies()`: Detect anomalies in data
- `get_anomaly_summary()`: Get summary of anomalies
- `get_statistics()`: Get comprehensive statistics

#### `config.py`

**Configuration File**

- API keys and endpoints
- Default settings
- Supported exchanges
- Popular stocks list
- UI configuration

#### `utils.py`

**Utility Functions**

- Number formatting
- Date validation
- Report generation
- Data processing helpers

**Key Functions:**

- `format_number()`: Format numbers with commas
- `format_percentage()`: Format as percentage
- `validate_date_range()`: Validate date inputs
- `generate_report_summary()`: Generate text reports

#### `example_analysis.py`

**Example Usage Script**

- Demonstrates programmatic usage
- Example analysis workflow
- Multi-stock analysis example

### Documentation Files

#### `README.md`

**Main Documentation**

- Project overview
- Features and capabilities
- Installation instructions
- Usage guide
- API documentation
- Troubleshooting

#### `QUICKSTART.md`

**Quick Start Guide**

- 5-minute setup guide
- First analysis tutorial
- Common stock symbols
- Quick tips

#### `DEPLOYMENT.md`

**Deployment Guide**

- Streamlit Cloud deployment
- Docker deployment
- Heroku deployment
- AWS EC2 deployment
- Performance optimization

#### `PROJECT_STRUCTURE.md`

**This File**

- Complete project structure
- File descriptions
- Architecture overview

### Configuration Files

#### `requirements.txt`

**Python Dependencies**

```
streamlit==1.28.1
pandas==2.1.3
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
plotly==5.18.0
alpha-vantage==2.3.1
requests==2.31.0
python-dotenv==1.0.0
yfinance==0.2.32
```

#### `.streamlit/config.toml`

**Streamlit Configuration**

- Theme settings
- Server configuration
- Browser settings

#### `.gitignore`

**Git Ignore Rules**

- Python cache files
- Virtual environments
- Data files
- Environment variables
- IDE settings

### Scripts

#### `run.sh`

**Launch Script**

- Automated setup
- Dependency checking
- Application launch

### Directory Structure

#### `data/`

**Data Storage**

- Downloaded stock data
- Cached API responses
- Historical data files

#### `reports/`

**Generated Reports**

- Analysis reports
- Anomaly summaries
- Export files

#### `exports/`

**Exported Files**

- CSV exports
- JSON exports
- PDF reports

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│              Streamlit Web UI                    │
│         (app.py - Main Interface)                │
└─────────────────┬───────────────────────────────┘
                  │
                  ├──────────────────────────────┐
                  │                              │
                  ▼                              ▼
        ┌──────────────────┐         ┌──────────────────┐
        │ Data Collector   │         │ Anomaly Detector │
        │ (Alpha Vantage)  │────────▶│ (Z-Score Analysis)│
        └──────────────────┘         └──────────────────┘
                  │                              │
                  │                              │
                  ▼                              ▼
        ┌──────────────────┐         ┌──────────────────┐
        │   Stock Data     │         │  Anomaly Results │
        │   (CSV/JSON)     │         │  (Reports/Charts)│
        └──────────────────┘         └──────────────────┘
```

## Data Flow

1. **User Input** → Streamlit UI
2. **API Request** → Data Collector
3. **Data Fetch** → Alpha Vantage API
4. **Data Processing** → Pandas DataFrame
5. **Analysis** → Anomaly Detector
6. **Results** → Visualizations & Reports

## Key Technologies

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib
- **API**: Alpha Vantage
- **Deployment**: Streamlit Cloud

## Dependencies

### Core Dependencies

- `streamlit`: Web framework
- `pandas`: Data manipulation
- `numpy`: Numerical computing
- `plotly`: Interactive charts

### API Dependencies

- `alpha-vantage`: Alpha Vantage API client
- `requests`: HTTP requests
- `yfinance`: Alternative data source

### Utility Dependencies

- `python-dotenv`: Environment variables
- `matplotlib`: Static charts
- `seaborn`: Statistical visualization

## Development Workflow

1. **Setup**: Install dependencies
2. **Develop**: Edit Python files
3. **Test**: Run locally with Streamlit
4. **Deploy**: Push to GitHub → Streamlit Cloud

## File Size Estimates

- `app.py`: ~15 KB
- `data_collector.py`: ~5 KB
- `anomaly_detector.py`: ~7 KB
- `config.py`: ~3 KB
- `utils.py`: ~8 KB
- `example_analysis.py`: ~6 KB
- Documentation: ~50 KB
- **Total**: ~100 KB (excluding data)

## Version Control

### Recommended Git Workflow

```bash
# Initial setup
git init
git add .
git commit -m "Initial commit"

# Feature development
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "Add new feature"
git push origin feature/new-feature

# Merge to main
git checkout main
git merge feature/new-feature
git push origin main
```

## Maintenance

### Regular Tasks

- Update dependencies monthly
- Monitor API rate limits
- Review and optimize code
- Update documentation
- Check for security issues

### Backup Strategy

- Git repository (primary)
- Local backups of data
- Cloud storage for reports

---

**Project maintained by: [Your Name]**
**Last updated: 2024**
