"""
FIN-SIGHT: Anomaly Detection in Stock Trades
Main Streamlit Application
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time
import os
from data_collector import StockDataCollector
from anomaly_detector import AnomalyDetector

# Page configuration
st.set_page_config(
    page_title="FIN-SIGHT | Anomaly Detection in Stock Trades",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .main-header h1 {
        color: white;
        margin-bottom: 0.5rem;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        margin: 0;
    }
    
    /* Card styling */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Info box styling */
    .info-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    /* Success/Error styling */
    .success-box {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    
    .error-box {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sidebar styling */
    .css-1d391kg {
        padding-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'stock_data' not in st.session_state:
    st.session_state.stock_data = None
if 'detector' not in st.session_state:
    st.session_state.detector = None
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False

def main():
    """Main application function"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📈 FIN-SIGHT</h1>
        <p>Anomaly Detection in Stock Trades - Identify Suspicious Trading Activity</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        
        # API Key input
        api_key = st.text_input(
            "Alpha Vantage API Key",
            value="VO8CV7MCLOI5GNI3",
            type="password",
            help="Enter your Alpha Vantage API key"
        )
        
        st.markdown("---")
        
        # Stock Selection
        st.markdown("### 📊 Stock Selection")
        stock_symbol = st.text_input(
            "Stock Symbol",
            value="RELIANCE.BSE",
            help="Enter stock ticker (e.g., RELIANCE.BSE, TCS.BSE)"
        )
        
        # Data Range
        st.markdown("### 📅 Date Range")
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", value=datetime(2024, 1, 1))
        with col2:
            end_date = st.date_input("End Date", value=datetime(2024, 12, 31))
        
        # Data Type
        data_type = st.selectbox(
            "Data Type",
            ["Daily", "Weekly", "Intraday (60min)"],
            help="Select the time interval for data collection"
        )
        
        st.markdown("---")
        
        # Anomaly Detection Settings
        st.markdown("### 🔍 Detection Settings")
        pre_event_window = st.slider(
            "Pre-Event Window (days)",
            min_value=1,
            max_value=7,
            value=3,
            help="Number of days before event to check for anomalies"
        )
        
        z_score = st.slider(
            "Z-Score Threshold",
            min_value=2.0,
            max_value=5.0,
            value=3.0,
            step=0.5,
            help="Standard deviations above mean for anomaly detection"
        )
        
        st.markdown("---")
        
        # Action Buttons
        if st.button("🔍 Analyze Stock", use_container_width=True):
            with st.spinner("Fetching data and analyzing..."):
                try:
                    # Initialize collector
                    collector = StockDataCollector(api_key)
                    
                    # Fetch data based on type
                    if data_type == "Daily":
                        df = collector.fetch_daily_data(stock_symbol)
                    elif data_type == "Weekly":
                        df = collector.fetch_weekly_data(stock_symbol)
                    else:
                        df = collector.fetch_intraday_data(stock_symbol)
                    
                    # Filter by date range
                    df = df[(df.index >= pd.Timestamp(start_date)) & 
                           (df.index <= pd.Timestamp(end_date))]
                    
                    if df.empty:
                        st.error("No data available for the selected date range")
                    else:
                        st.session_state.stock_data = df
                        st.success(f"✅ Data fetched successfully! ({len(df)} records)")
                        
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        if st.button("🔄 Reset Analysis", use_container_width=True):
            st.session_state.stock_data = None
            st.session_state.detector = None
            st.session_state.analysis_complete = False
            st.rerun()
    
    # Main Content
    if st.session_state.stock_data is not None:
        display_analysis(st.session_state.stock_data, pre_event_window, z_score)
    else:
        display_welcome()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p><strong>FIN-SIGHT</strong> - Powered by Alpha Vantage API</p>
        <p>Detecting suspicious trading patterns with advanced statistical analysis</p>
    </div>
    """, unsafe_allow_html=True)

def display_welcome():
    """Display welcome screen with instructions"""
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Data Collection</h3>
            <p>Fetch historical stock data from Alpha Vantage API with multiple time intervals</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🔍 Anomaly Detection</h3>
            <p>Identify statistically unusual trading activity using Z-score analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Visualization</h3>
            <p>Interactive charts showing anomalies and trading patterns</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h4>🚀 Getting Started</h4>
        <ol>
            <li>Enter your stock symbol in the sidebar (e.g., RELIANCE.BSE)</li>
            <li>Select your date range and data type</li>
            <li>Configure anomaly detection settings</li>
            <li>Click "Analyze Stock" to begin</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Example use cases
    st.markdown("### 💡 Use Cases")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Insider Trading Detection**
        - Identify unusual volume spikes before major announcements
        - Detect suspicious trading patterns
        - Monitor pre-event trading activity
        """)
    
    with col2:
        st.markdown("""
        **Market Analysis**
        - Understand normal trading patterns
        - Identify high-volatility periods
        - Track trading volume trends
        """)

def display_analysis(df, pre_event_window, z_score):
    """Display analysis results"""
    
    # Create detector
    detector = AnomalyDetector(df)
    
    # Event dates input
    st.markdown("### 📅 Major Event Dates")
    st.markdown("Enter the dates of major announcements (earnings, AGM, etc.)")
    
    event_input = st.text_area(
        "Event Dates (YYYY-MM-DD, one per line)",
        value="2024-01-19\n2024-04-22\n2024-07-19\n2024-08-29\n2024-10-18",
        height=100
    )
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔍 Detect Anomalies", use_container_width=True):
            # Parse event dates
            event_dates = []
            for line in event_input.strip().split('\n'):
                if line.strip():
                    try:
                        event_dates.append(pd.to_datetime(line.strip()))
                    except:
                        pass
            
            if event_dates:
                # Detect anomalies
                detector.detect_anomalies(event_dates, pre_event_window, z_score)
                st.session_state.detector = detector
                st.session_state.analysis_complete = True
                st.success(f"✅ Analysis complete! Detected {detector.df['Is_Anomaly'].sum()} anomalies")
            else:
                st.error("Please enter at least one valid event date")
    
    if st.session_state.analysis_complete and st.session_state.detector:
        detector = st.session_state.detector
        
        # Statistics
        stats = detector.get_statistics()
        summary = detector.get_anomaly_summary()
        
        st.markdown("---")
        st.markdown("### 📊 Analysis Results")
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Days Analyzed", f"{stats['total_days']:,}")
        
        with col2:
            st.metric("Anomalies Detected", f"{stats['anomaly_count']}", 
                     delta=f"{stats['anomaly_count']/stats['total_days']*100:.1f}%")
        
        with col3:
            st.metric("Average Volume", f"{stats['average_volume']:,.0f}")
        
        with col4:
            st.metric("Anomaly Threshold", f"{stats['anomaly_threshold']:,.0f}")
        
        # Detailed Statistics
        with st.expander("📈 Detailed Statistics"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Volume Statistics**")
                st.json({
                    "Minimum Volume": f"{stats['min_volume']:,.0f}",
                    "Maximum Volume": f"{stats['max_volume']:,.0f}",
                    "Median Volume": f"{stats['median_volume']:,.0f}",
                    "Average Volume": f"{stats['average_volume']:,.0f}",
                    "Standard Deviation": f"{stats['std_deviation']:,.0f}"
                })
            
            with col2:
                st.markdown("**Detection Settings**")
                st.json({
                    "Z-Score Threshold": z_score,
                    "Pre-Event Window": f"{pre_event_window} days",
                    "Anomaly Threshold": f"{stats['anomaly_threshold']:,.0f}",
                    "Event Days": stats['event_day_count']
                })
        
        # Anomaly Details
        if summary['total_anomalies'] > 0:
            st.markdown("### 🚨 Detected Anomalies")
            
            anomaly_df = pd.DataFrame(summary['details'])
            anomaly_df['date'] = pd.to_datetime(anomaly_df['date'])
            anomaly_df = anomaly_df.sort_values('date')
            
            st.dataframe(
                anomaly_df.style.format({
                    'volume': '{:,.0f}',
                    'z_score': '{:.2f}',
                    'anomaly_score': '{:.2f}',
                    'percentage_above_avg': '{:.1f}%'
                }),
                use_container_width=True,
                height=200
            )
            
            # Download button
            csv = anomaly_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Anomaly Report",
                data=csv,
                file_name=f"anomaly_report_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.info("ℹ️ No anomalies detected with current settings. Try adjusting the Z-score threshold or pre-event window.")
        
        # Visualizations
        st.markdown("---")
        st.markdown("### 📊 Interactive Visualizations")
        
        # Volume Chart
        fig = go.Figure()
        
        # Add volume bars
        fig.add_trace(go.Bar(
            x=detector.df.index,
            y=detector.df['Volume'],
            name='Trading Volume',
            marker_color='rgba(102, 126, 234, 0.6)'
        ))
        
        # Add anomaly threshold line
        fig.add_hline(
            y=stats['anomaly_threshold'],
            line_dash="dash",
            line_color="orange",
            annotation_text="Anomaly Threshold",
            annotation_position="right"
        )
        
        # Highlight anomalies
        anomalies = detector.df[detector.df['Is_Anomaly']]
        if not anomalies.empty:
            fig.add_trace(go.Scatter(
                x=anomalies.index,
                y=anomalies['Volume'],
                mode='markers',
                name='Anomalies',
                marker=dict(
                    color='red',
                    size=12,
                    symbol='diamond',
                    line=dict(width=2, color='darkred')
                )
            ))
        
        # Highlight event days
        event_days = detector.df[detector.df['Event_Day']]
        if not event_days.empty:
            fig.add_trace(go.Scatter(
                x=event_days.index,
                y=event_days['Volume'],
                mode='markers',
                name='Event Days',
                marker=dict(
                    color='green',
                    size=10,
                    symbol='triangle-up',
                    line=dict(width=2, color='darkgreen')
                )
            ))
        
        fig.update_layout(
            title=f"Trading Volume Analysis - Anomalies Detected: {stats['anomaly_count']}",
            xaxis_title="Date",
            yaxis_title="Volume",
            hovermode='x unified',
            height=500,
            template="plotly_white",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Z-Score Distribution
        col1, col2 = st.columns(2)
        
        with col1:
            fig2 = go.Figure()
            fig2.add_trace(go.Histogram(
                x=detector.df['Z_Score'],
                nbinsx=50,
                name='Z-Score Distribution',
                marker_color='rgba(102, 126, 234, 0.6)'
            ))
            fig2.add_vline(
                x=z_score,
                line_dash="dash",
                line_color="orange",
                annotation_text="Threshold"
            )
            fig2.update_layout(
                title="Z-Score Distribution",
                xaxis_title="Z-Score",
                yaxis_title="Frequency",
                template="plotly_white",
                height=400
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        with col2:
            fig3 = go.Figure()
            fig3.add_trace(go.Scatter(
                x=detector.df.index,
                y=detector.df['Z_Score'],
                mode='lines',
                name='Z-Score Over Time',
                line=dict(color='rgba(102, 126, 234, 0.8)')
            ))
            fig3.add_hline(
                y=z_score,
                line_dash="dash",
                line_color="orange",
                annotation_text="Threshold"
            )
            fig3.update_layout(
                title="Z-Score Timeline",
                xaxis_title="Date",
                yaxis_title="Z-Score",
                template="plotly_white",
                height=400
            )
            st.plotly_chart(fig3, use_container_width=True)
        
        # Raw Data
        with st.expander("📋 View Raw Data"):
            st.dataframe(detector.df, use_container_width=True, height=300)

if __name__ == "__main__":
    main()

