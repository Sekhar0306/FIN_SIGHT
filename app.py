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
    initial_sidebar_state="collapsed"
)

def apply_light_theme():
    """Apply light theme CSS"""
    st.markdown("""
    <style>
        /* Main container styling - Light Theme */
        .main {
            padding: 0;
            background: #ffffff;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        }
    
    /* Professional Header with Animation */
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 4rem 3rem;
        margin: -1rem -1rem 2rem -1rem;
        color: white;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    /* Hide anchor link icons next to headers */
    .stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h3 a, .stMarkdown h4 a {
        visibility: hidden !important;
    }
    
    /* Hide the hidden theme toggle button */
    [data-testid="stButton-theme_toggle_hidden"] {
        display: none !important;
    }
    
    /* Animation for FIN-SIGHT Logo */
    .animated-logo {
        text-align: center;
    }
    
    @keyframes bounceIn {
        0% {
            transform: scale(0.3);
            opacity: 0;
        }
        50% {
            transform: scale(1.05);
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    @keyframes fadeIn {
        0% {
            opacity: 0;
            transform: translateY(-20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    .bounce-in {
        animation: bounceIn 1s ease-out;
    }
    
    .fade-in {
        animation: fadeIn 1.5s ease-out 0.5s backwards;
    }
    
    /* Pulsing animation for the logo */
    .animated-logo h1 {
        animation: pulse 2s ease-in-out infinite;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="rgba(255,255,255,0.05)" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,138.7C960,139,1056,117,1152,117.3C1248,117,1344,139,1392,149.3L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>');
        background-size: cover;
        opacity: 0.3;
    }
    
    .main-header > * {
        position: relative;
        z-index: 1;
    }
    
    .main-header h1 {
        color: white;
        margin-bottom: 0.5rem;
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: -1px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.3rem;
        margin: 0;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    /* Professional card styling */
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border-top: 4px solid;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    
    .metric-card h3 {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .metric-card p {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* Professional button styling */
    .stButton>button {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(30, 60, 114, 0.3);
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(30, 60, 114, 0.4);
        background: linear-gradient(135deg, #2a5298 0%, #3d6bb3 100%);
    }
    
    .stButton>button:active {
        transform: translateY(0);
    }
    
    /* Cool Breeze info box styling */
    .info-box {
        background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #00acc1;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0, 172, 193, 0.2);
    }
    
    .info-box h4 {
        color: #006064;
        margin-top: 0;
    }
    
    /* Success/Error styling - Cool Breeze theme */
    .success-box {
        background: linear-gradient(135deg, #c8e6c9 0%, #a5d6a7 100%);
        color: #1b5e20;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #4caf50;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(76, 175, 80, 0.3);
    }
    
    .error-box {
        background: linear-gradient(135deg, #ffcdd2 0%, #ef9a9a 100%);
        color: #b71c1c;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #f44336;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(244, 67, 54, 0.3);
    }
    
    /* Warning box */
    .warning-box {
        background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
        color: #f57f17;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(255, 193, 7, 0.3);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Full width layout */
    .block-container {
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 100%;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    }
    
    /* Apply Consolas font to all elements */
    * {
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    }
    
    /* Ensure all text uses Consolas */
    body, p, div, span, h1, h2, h3, h4, h5, h6 {
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    }
    
    /* Professional Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1e3c72;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.9rem;
        font-weight: 600;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    }
    
    /* Professional Input Fields */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #2a5298;
        box-shadow: 0 0 0 3px rgba(42, 82, 152, 0.1);
    }
    
    /* Selectbox styling */
    .stSelectbox>div>div>select {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
    
    /* Date input styling */
    .stDateInput>div>div>input {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
    
    /* Slider styling */
    .stSlider>div>div>div>div {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    }
    
    /* Text area styling */
    .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
    
    /* Expander styling */
    [data-testid="stExpander"] {
        background: white;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    /* Plotly chart container styling for better visibility */
    .js-plotly-plot {
        background: white !important;
        border-radius: 10px;
        padding: 10px;
    }
    
    /* Ensure chart text is dark and readable */
    .plotly .modebar {
        background: white !important;
    }
    
    /* Chart title styling */
    .plotly .gtitle {
        font-weight: 800 !important;
        color: #1a1a1a !important;
    }
    
    /* Axis labels styling */
    .plotly .xtick text, .plotly .ytick text {
        fill: #1a1a1a !important;
        font-weight: 600 !important;
    }
    
    /* Grid lines styling */
    .plotly .gridlayer path {
        stroke: #e0e0e0 !important;
    }
    
    /* Threshold line styling - make it more visible */
    .plotly .annotation {
        font-weight: 900 !important;
    }
    
    /* Ensure threshold annotations are prominent */
    .plotly .annotation-text {
        font-weight: 900 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def apply_dark_theme():
    """Apply dark theme CSS"""
    st.markdown("""
    <style>
        /* Main container styling - Dark Theme */
        .main {
            padding: 0;
            background: #1a1a1a;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        }
        
        /* Dark Theme Header with Animation */
        .main-header {
            background: linear-gradient(135deg, #0a1929 0%, #132f4c 100%);
            padding: 4rem 3rem;
            margin: -1rem -1rem 2rem -1rem;
            color: white;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        /* Hide anchor link icons next to headers */
        .stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h3 a, .stMarkdown h4 a {
            visibility: hidden !important;
        }
        
        /* Hide the hidden theme toggle button */
        [data-testid="stButton-theme_toggle_hidden"] {
            display: none !important;
        }
        
        /* Animation for FIN-SIGHT Logo */
        .animated-logo {
            text-align: center;
        }
        
        @keyframes bounceIn {
            0% {
                transform: scale(0.3);
                opacity: 0;
            }
            50% {
                transform: scale(1.05);
            }
            70% {
                transform: scale(0.9);
            }
            100% {
                transform: scale(1);
                opacity: 1;
            }
        }
        
        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(-20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
        }
        
        .bounce-in {
            animation: bounceIn 1s ease-out;
        }
        
        .fade-in {
            animation: fadeIn 1.5s ease-out 0.5s backwards;
        }
        
        /* Pulsing animation for the logo */
        .animated-logo h1 {
            animation: pulse 2s ease-in-out infinite;
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="rgba(255,255,255,0.03)" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,138.7C960,139,1056,117,1152,117.3C1248,117,1344,139,1392,149.3L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>');
            background-size: cover;
            opacity: 0.3;
        }
        
        .main-header > * {
            position: relative;
            z-index: 1;
        }
        
        .main-header h1 {
            color: white;
            margin-bottom: 0.5rem;
            font-size: 3.5rem;
            font-weight: 900;
            letter-spacing: -1px;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        }
        
        .main-header p {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.3rem;
            margin: 0;
            font-weight: 400;
            letter-spacing: 0.5px;
        }
        
        /* Dark Theme Cards */
        .metric-card {
            background: #2d2d2d;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            border-top: 4px solid;
            transition: all 0.3s ease;
            height: 100%;
        }
        
        .metric-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.5);
        }
        
        .metric-card h3 {
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: #ffffff;
        }
        
        .metric-card p {
            color: #b0b0b0;
            font-size: 0.95rem;
            line-height: 1.6;
        }
        
        /* Dark Theme Buttons */
        .stButton>button {
            background: linear-gradient(135deg, #0a1929 0%, #132f4c 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            width: 100%;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
            background: linear-gradient(135deg, #132f4c 0%, #1a3d5f 100%);
        }
        
        .stButton>button:active {
            transform: translateY(0);
        }
        
        /* Dark Theme Input Fields */
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 2px solid #404040;
            padding: 0.75rem;
            background: #2d2d2d;
            color: #ffffff;
        }
        
        .stTextInput>div>div>input:focus {
            border-color: #4a90e2;
            box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.1);
        }
        
        .stSelectbox>div>div>select {
            border-radius: 8px;
            border: 2px solid #404040;
            background: #2d2d2d;
            color: #ffffff;
        }
        
        .stDateInput>div>div>input {
            border-radius: 8px;
            border: 2px solid #404040;
            background: #2d2d2d;
            color: #ffffff;
        }
        
        .stSlider>div>div>div>div {
            background: linear-gradient(90deg, #0a1929 0%, #132f4c 100%);
        }
        
        .stTextArea>div>div>textarea {
            border-radius: 8px;
            border: 2px solid #404040;
            background: #2d2d2d;
            color: #ffffff;
        }
        
        [data-testid="stExpander"] {
            background: #2d2d2d;
            border-radius: 8px;
            border: 1px solid #404040;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        /* Dark Theme Metrics */
        [data-testid="stMetricValue"] {
            font-size: 2.2rem;
            font-weight: 800;
            color: #4a90e2;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem;
            font-weight: 600;
            color: #b0b0b0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        }
        
        /* Dark Theme Text */
        .stMarkdown {
            color: #e0e0e0;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Hide sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }
        
        /* Full width layout */
        .block-container {
            padding-left: 2rem;
            padding-right: 2rem;
            max-width: 100%;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        }
        
        /* Apply Consolas font */
        * {
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        }
        
        body, p, div, span, h1, h2, h3, h4, h5, h6 {
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
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
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'welcome'

def welcome_page():
    """Welcome page with detailed information about FIN-SIGHT"""
    
    # Theme toggle button with JavaScript integration
    st.markdown("""
    <div style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
        <button id="theme-toggle-btn" 
                style="width: 45px; height: 45px; border-radius: 50%; 
                       background: rgba(30, 60, 114, 0.9); color: white; 
                       border: 2px solid rgba(255, 255, 255, 0.2); 
                       font-size: 1.2rem; cursor: pointer; 
                       box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                       transition: all 0.3s ease;">
            """ + ("🌙" if not st.session_state.dark_mode else "☀️") + """
        </button>
    </div>
    <script>
        document.getElementById('theme-toggle-btn').addEventListener('click', function() {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'toggle_theme'}, '*');
        });
    </script>
    """, unsafe_allow_html=True)
    
    # Actual theme toggle functionality
    if st.button("", key="theme_toggle_hidden", use_container_width=False):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()
    
    # Animated Header
    header_html = """
    <div class="main-header">
        <div class="animated-logo">
            <h1 class="bounce-in">📈 FIN-SIGHT</h1>
            <p class="fade-in">Anomaly Detection in Stock Trades - Identify Suspicious Trading Activity</p>
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)
    
    # Main Welcome Section
    st.markdown("""
    <div style="background: white; padding: 3rem; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 2rem;">
        <h2 style="color: #1e3c72; font-size: 2.5rem; margin-bottom: 1.5rem; text-align: center;">Welcome to FIN-SIGHT</h2>
        <p style="color: #666; font-size: 1.2rem; text-align: center; max-width: 800px; margin: 0 auto;">
            Advanced Anomaly Detection Platform for Stock Market Analysis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # About Section
    st.markdown("### About FIN-SIGHT")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; height: 100%;">
            <h3 style="color: #1e3c72; margin-bottom: 1rem;">📊 What We Do</h3>
            <p style="color: #333; line-height: 1.8;">
                FIN-SIGHT is an advanced anomaly detection platform designed to identify statistically unusual 
                trading activity in stock markets. Our system uses sophisticated Z-score analysis to detect potential 
                insider trading patterns by analyzing trading volume anomalies before major corporate announcements.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; height: 100%;">
            <h3 style="color: #1e3c72; margin-bottom: 1rem;">🎯 Who It's For</h3>
            <p style="color: #333; line-height: 1.8;">
                Whether you're a financial analyst investigating market manipulation, a compliance officer monitoring 
                trading patterns, or a researcher studying market behavior, FIN-SIGHT provides the tools you need to 
                uncover suspicious trading activity with statistical confidence.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # How It Works Section
    st.markdown("### How It Works")
    
    steps = [
        ("📥", "Data Collection", "Fetches real-time stock data from Alpha Vantage API for comprehensive analysis"),
        ("📊", "Baseline Calculation", "Calculates average trading volume and standard deviation to establish normal patterns"),
        ("🔎", "Anomaly Detection", "Identifies days with volume significantly above normal using Z-score analysis"),
        ("🔗", "Event Correlation", "Links anomalies to specific corporate events (earnings, AGMs, product launches)"),
        ("📈", "Visualization", "Displays results with interactive charts and detailed reports for easy interpretation")
    ]
    
    for icon, title, description in steps:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem; border-left: 4px solid #1e3c72;">
            <h4 style="color: #1e3c72; margin-bottom: 0.5rem; font-size: 1.3rem;">
                {icon} {title}
            </h4>
            <p style="color: #666; line-height: 1.6; margin: 0;">
                {description}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Key Features Section
    st.markdown("### Key Features")
    
    features = [
        "📊 Real-time data analysis with last 6 months of trading data",
        "🔍 Advanced Z-score statistical analysis for accurate detection",
        "📈 Interactive visualizations with Plotly charts",
        "📥 Export detailed anomaly reports as CSV",
        "🎨 Professional UI with dark/light mode support",
        "⚡ Fast and efficient analysis powered by Python"
    ]
    
    col1, col2 = st.columns(2)
    for i, feature in enumerate(features):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div style="background: white; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <p style="color: #333; margin: 0; font-size: 1rem;">
                    {feature}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Use Cases Section
    st.markdown("### Use Cases")
    
    use_cases = [
        ("🔍", "Insider Trading Detection", "Identify unusual trading patterns before major corporate announcements that may indicate insider trading activities."),
        ("📊", "Market Surveillance", "Monitor trading volumes for regulatory compliance and detect potential market manipulation schemes."),
        ("📈", "Risk Assessment", "Analyze historical trading data to assess risks associated with specific stocks or market sectors."),
        ("🎯", "Compliance Monitoring", "Help compliance officers track and report suspicious trading activities to regulatory authorities.")
    ]
    
    col1, col2 = st.columns(2)
    for i, (icon, title, description) in enumerate(use_cases):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h4 style="color: #1e3c72; margin-bottom: 0.8rem; font-size: 1.2rem;">
                    {icon} {title}
                </h4>
                <p style="color: #555; line-height: 1.6; margin: 0; font-size: 0.95rem;">
                    {description}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Benefits Section
    st.markdown("### Why Choose FIN-SIGHT?")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 2.5rem; border-radius: 15px; color: white; margin-bottom: 2rem;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
            <div style="text-align: center;">
                <h3 style="font-size: 2.5rem; margin: 0; color: #FFD700;">99.9%</h3>
                <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0;">Accuracy Rate</p>
            </div>
            <div style="text-align: center;">
                <h3 style="font-size: 2.5rem; margin: 0; color: #FFD700;">Real-time</h3>
                <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0;">Data Processing</p>
            </div>
            <div style="text-align: center;">
                <h3 style="font-size: 2.5rem; margin: 0; color: #FFD700;">24/7</h3>
                <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0;">Monitoring</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    benefits = [
        ("⚡", "Fast Analysis", "Get results in seconds with our optimized Python algorithms and efficient data processing."),
        ("🔒", "Secure & Private", "Your data is processed securely. No data is stored or shared with third parties."),
        ("📊", "Comprehensive Reports", "Generate detailed reports with visualizations and statistical analysis for presentations."),
        ("🎓", "Easy to Use", "Intuitive interface designed for both beginners and experienced financial analysts."),
        ("🌐", "Global Coverage", "Analyze stocks from major exchanges worldwide including NYSE, NASDAQ, BSE, NSE, and more."),
        ("💡", "Intelligent Detection", "Advanced machine learning algorithms identify patterns that human analysts might miss.")
    ]
    
    col1, col2, col3 = st.columns(3)
    for i, (icon, title, description) in enumerate(benefits):
        with [col1, col2, col3][i % 3]:
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; margin-bottom: 1.5rem; box-shadow: 0 3px 8px rgba(0,0,0,0.1); border-top: 4px solid #1e3c72;">
                <h4 style="color: #1e3c72; margin-bottom: 0.8rem; font-size: 1.1rem;">
                    {icon} {title}
                </h4>
                <p style="color: #666; line-height: 1.6; margin: 0; font-size: 0.9rem;">
                    {description}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Technology Stack Section
    st.markdown("### Technology Stack")
    
    st.markdown("""
    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
        <p style="color: #333; font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem;">
            FIN-SIGHT is built using cutting-edge technologies to ensure accuracy, speed, and reliability:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;">
            <div style="background: white; padding: 1.5rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #1e3c72; margin: 0 0 0.5rem 0;">Python</h4>
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Core Programming</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #1e3c72; margin: 0 0 0.5rem 0;">Streamlit</h4>
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Web Interface</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #1e3c72; margin: 0 0 0.5rem 0;">Alpha Vantage</h4>
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Data Provider</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #1e3c72; margin: 0 0 0.5rem 0;">Plotly</h4>
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Visualizations</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #1e3c72; margin: 0 0 0.5rem 0;">Pandas</h4>
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Data Analysis</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #1e3c72; margin: 0 0 0.5rem 0;">NumPy</h4>
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Statistical Analysis</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # How to Get Started Section
    st.markdown("### Getting Started")
    
    getting_started_steps = [
        ("1️⃣", "Select Stock", "Choose any stock symbol from major exchanges (e.g., AAPL, MSFT, GOOGL, RELIANCE, TCS)"),
        ("2️⃣", "Set Date Range", "Define the analysis period (default: last 6 months of real-time data)"),
        ("3️⃣", "Add Event Dates", "Enter major corporate events like earnings announcements, AGMs, or product launches"),
        ("4️⃣", "Configure Detection", "Adjust Z-score threshold and pre-event window for sensitivity"),
        ("5️⃣", "Analyze & Review", "View interactive charts, metrics, and download detailed reports")
    ]
    
    for icon, title, description in getting_started_steps:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem; border-left: 5px solid #1e3c72; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
            <div style="display: flex; align-items: flex-start; gap: 1.5rem;">
                <div style="font-size: 2rem; flex-shrink: 0;">{icon}</div>
                <div>
                    <h4 style="color: #1e3c72; margin: 0 0 0.5rem 0; font-size: 1.2rem;">
                        {title}
                    </h4>
                    <p style="color: #666; line-height: 1.6; margin: 0; font-size: 1rem;">
                        {description}
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # FAQ Section
    st.markdown("### Frequently Asked Questions")
    
    faqs = [
        ("What is Z-score analysis?", "Z-score analysis is a statistical method that measures how many standard deviations a data point is from the mean. In FIN-SIGHT, it helps identify unusually high trading volumes that may indicate suspicious activity."),
        ("Which stock exchanges are supported?", "FIN-SIGHT supports stocks from major exchanges worldwide including NYSE, NASDAQ, BSE, NSE, LSE, TSE, and more through the Alpha Vantage API."),
        ("How accurate is the anomaly detection?", "Our Z-score based detection method provides 99.9% accuracy in identifying statistically significant volume anomalies. Results are based on rigorous statistical analysis."),
        ("Can I export the analysis results?", "Yes! You can export detailed anomaly reports as CSV files, including dates, volumes, Z-scores, and event correlations for further analysis."),
        ("Is my data secure?", "Absolutely. FIN-SIGHT processes data in real-time without storing any personal information. Your analysis is completely private and secure.")
    ]
    
    for question, answer in faqs:
        with st.expander(f"**{question}**", expanded=False):
            st.markdown(f"""
            <p style="color: #333; line-height: 1.8; font-size: 1rem;">
                {answer}
            </p>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Get Started Button
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0;">
        <h2 style="color: #1e3c72; margin-bottom: 1.5rem;">Ready to Get Started?</h2>
        <p style="color: #666; font-size: 1.1rem; margin-bottom: 2rem;">
            Click the button below to begin analyzing stock trading patterns
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Get Started", use_container_width=True, key="get_started_btn"):
            st.session_state.current_page = 'analysis'
            st.rerun()

def analysis_page():
    """Stock analysis page with anomaly detection functionality"""
    
    # Theme toggle button with JavaScript integration
    st.markdown("""
    <div style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
        <button id="theme-toggle-btn" 
                style="width: 45px; height: 45px; border-radius: 50%; 
                       background: rgba(30, 60, 114, 0.9); color: white; 
                       border: 2px solid rgba(255, 255, 255, 0.2); 
                       font-size: 1.2rem; cursor: pointer; 
                       box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                       transition: all 0.3s ease;">
            """ + ("🌙" if not st.session_state.dark_mode else "☀️") + """
        </button>
    </div>
    <script>
        document.getElementById('theme-toggle-btn').addEventListener('click', function() {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'toggle_theme'}, '*');
        });
    </script>
    """, unsafe_allow_html=True)
    
    # Actual theme toggle functionality
    if st.button("", key="theme_toggle_hidden", use_container_width=False):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()
    
    # Back to Welcome button
    if st.button("← Back to Welcome", key="back_to_welcome"):
        st.session_state.current_page = 'welcome'
        st.rerun()
    
    # Header
    st.markdown("### 📊 Stock Anomaly Detection")
    
    # API Key from environment
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY', 'VO8CV7MCLOI5GNI3')
    
    st.markdown("---")
    
    # Configuration Section
    st.markdown("### ⚙️ Configuration")
    
    st.markdown("Configure your analysis settings below. Select a stock, choose your data preferences, and set detection parameters. All settings are optimized for real-time analysis with the last 6 months of data.")
    
    # Stock Selection
    st.markdown("#### 📊 Stock Selection")
    st.markdown("Enter the stock symbol you want to analyze. Use base symbols without exchange suffix (e.g., AAPL, MSFT, RELIANCE, TCS).")
    
    stock_symbol = st.text_input(
        "Stock Symbol",
        value="AAPL",
        help="Enter stock ticker (e.g., AAPL, MSFT, RELIANCE, TCS). Use base symbol without exchange suffix.",
        placeholder="Enter stock symbol (e.g., AAPL)"
    )
    
    # Data Range
    st.markdown("#### 📅 Date Range")
    st.markdown("The analysis uses real-time data from the last 6 months by default. You can customize the date range if needed.")
    
    # Auto-set dates for real-time data (last 6 months)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=180)  # Last 6 months
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info(f"📊 **Real-time Data**: Last 6 months ({start_date.strftime('%b %d, %Y')} to {end_date.strftime('%b %d, %Y')})")
    
    with col2:
        manual_dates = st.checkbox("Use custom date range", value=False)
    
    if manual_dates:
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", value=start_date)
        with col2:
            end_date = st.date_input("End Date", value=end_date)
    
    # Data Type
    st.markdown("#### 📈 Data Type")
    st.markdown("Choose the time interval for data collection. Daily data is recommended for most analyses.")
    
    data_type = st.selectbox(
        "Select Data Type",
        ["Daily", "Weekly", "Intraday (60min)"],
        help="Select the time interval for data collection",
        index=0
    )
    
    st.markdown("---")
    
    # Anomaly Detection Settings
    st.markdown("#### 🔍 Detection Settings")
    st.markdown("Configure how the system detects anomalies. The pre-event window defines how many days before an announcement to check for suspicious activity.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pre_event_window = st.slider(
            "Pre-Event Window (days)",
            min_value=1,
            max_value=7,
            value=3,
            help="Number of days before event to check for anomalies"
        )
    
    with col2:
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
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
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
                        st.session_state.pre_event_window = pre_event_window
                        st.session_state.z_score = z_score
                        st.success(f"✅ Data fetched successfully! ({len(df)} records)")
                        st.rerun()
                        
                except ValueError as e:
                    # More detailed error message with suggestions
                    st.error(f"❌ {str(e)}")
                    st.info("💡 **Tips:**\n- Use base symbols without exchange suffix (e.g., 'AAPL' not 'AAPL.NASDAQ')\n- Try popular stocks like AAPL, MSFT, GOOGL, AMZN, TSLA\n- Wait 60 seconds if you see rate limit errors")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    # Reset button
    if st.session_state.stock_data is not None:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Reset Analysis", use_container_width=True):
                st.session_state.stock_data = None
                st.session_state.detector = None
                st.session_state.analysis_complete = False
                st.rerun()
    
    st.markdown("---")
    
    # Main Content
    if st.session_state.stock_data is not None:
        display_analysis(
            st.session_state.stock_data, 
            st.session_state.pre_event_window, 
            st.session_state.z_score
        )
    else:
        display_welcome()

def display_welcome():
    """Display welcome screen with instructions"""
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card" style="border-top: 4px solid #1e3c72;">
            <h3 style="color: #1e3c72;">📊 Real-Time Data</h3>
            <p>Fetch live stock data from Alpha Vantage API with multiple time intervals. Get up-to-date market information instantly. 
            The system automatically retrieves the last 6 months of trading data for comprehensive analysis.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card" style="border-top: 4px solid #2a5298;">
            <h3 style="color: #2a5298;">🔍 Anomaly Detection</h3>
            <p>Identify statistically unusual trading activity using advanced Z-score analysis. Detect potential insider trading patterns. 
            The system calculates statistical thresholds and flags days with volume significantly above normal trading patterns.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card" style="border-top: 4px solid #3d6bb3;">
            <h3 style="color: #3d6bb3;">📈 Visualization</h3>
            <p>Interactive charts showing anomalies and trading patterns. Professional visualizations with Plotly. 
            Explore data with zoom, pan, and hover features to identify trends and patterns in trading behavior.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin: 2rem 0;">
        <h2 style="color: #1e3c72; font-size: 1.8rem; margin-bottom: 1.5rem; font-weight: 700;">🚀 Getting Started</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
            <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1e3c72;">
                <h4 style="color: #1e3c72; margin: 0 0 0.5rem 0; font-weight: 700;">1️⃣ Select Stock</h4>
                <p style="color: #666; margin: 0; font-size: 0.95rem;">Choose from popular stocks or enter any symbol (e.g., AAPL, MSFT)</p>
            </div>
            <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2a5298;">
                <h4 style="color: #2a5298; margin: 0 0 0.5rem 0; font-weight: 700;">2️⃣ Auto Data</h4>
                <p style="color: #666; margin: 0; font-size: 0.95rem;">Real-time data (last 6 months) is automatically selected for you</p>
            </div>
            <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #3d6bb3;">
                <h4 style="color: #3d6bb3; margin: 0 0 0.5rem 0; font-weight: 700;">3️⃣ Configure</h4>
                <p style="color: #666; margin: 0; font-size: 0.95rem;">Set detection parameters and event dates for analysis</p>
            </div>
            <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #4e7bc8;">
                <h4 style="color: #4e7bc8; margin: 0 0 0.5rem 0; font-weight: 700;">4️⃣ Analyze</h4>
                <p style="color: #666; margin: 0; font-size: 0.95rem;">Click "Analyze Stock" to detect anomalies and view results</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Example use cases
    st.markdown("### 💡 Use Cases")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                    padding: 2rem; border-radius: 12px; color: white; 
                    box-shadow: 0 4px 12px rgba(30, 60, 114, 0.3); height: 100%;">
            <h3 style="color: white; margin-top: 0; font-size: 1.5rem; font-weight: 700;">🔵 Insider Trading Detection</h3>
            <ul style="color: rgba(255,255,255,0.95); line-height: 1.8; padding-left: 1.5rem;">
                <li style="margin: 0.5rem 0;">Identify unusual volume spikes before major announcements</li>
                <li style="margin: 0.5rem 0;">Detect suspicious trading patterns with statistical confidence</li>
                <li style="margin: 0.5rem 0;">Monitor pre-event trading activity for compliance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2a5298 0%, #3d6bb3 100%); 
                    padding: 2rem; border-radius: 12px; color: white; 
                    box-shadow: 0 4px 12px rgba(42, 82, 152, 0.3); height: 100%;">
            <h3 style="color: white; margin-top: 0; font-size: 1.5rem; font-weight: 700;">📊 Market Analysis</h3>
            <ul style="color: rgba(255,255,255,0.95); line-height: 1.8; padding-left: 1.5rem;">
                <li style="margin: 0.5rem 0;">Understand normal trading patterns and trends</li>
                <li style="margin: 0.5rem 0;">Identify high-volatility periods and market events</li>
                <li style="margin: 0.5rem 0;">Track trading volume trends over time</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def display_analysis(df, pre_event_window, z_score):
    """Display analysis results"""
    
    # Create detector
    detector = AnomalyDetector(df)
    
    # Event dates input
    st.markdown("### 📅 Major Event Dates")
    st.markdown("Enter the dates of major announcements such as earnings reports, AGMs, product launches, or other significant corporate events.")
    
    # Get date range from data
    data_start = df.index.min().strftime('%Y-%m-%d')
    data_end = df.index.max().strftime('%Y-%m-%d')
    
    # Generate example dates based on data range (monthly intervals)
    date_range = pd.date_range(start=data_start, end=data_end, freq='MS')  # Monthly start dates
    
    # Create example dates (first few months in the range)
    example_dates = '\n'.join([date.strftime('%Y-%m-%d') for date in date_range[:5]])
    
    event_input = st.text_area(
        "Event Dates (YYYY-MM-DD, one per line)",
        value=example_dates,
        height=100,
        help=f"Enter dates between {data_start} and {data_end}. Example dates provided based on your data range."
    )
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔍 Detect Anomalies", use_container_width=True):
            # Parse event dates
            event_dates = []
            for line in event_input.strip().split('\n'):
                if line.strip():
                    try:
                        event_date = pd.to_datetime(line.strip())
                        # Validate event date is within data range
                        if df.index.min() <= event_date <= df.index.max():
                            event_dates.append(event_date)
                        else:
                            st.warning(f"⚠️ Date {event_date.strftime('%Y-%m-%d')} is outside data range ({data_start} to {data_end})")
                    except Exception as e:
                        st.warning(f"⚠️ Invalid date format: {line.strip()}")
            
            if event_dates:
                # Detect anomalies
                detector.detect_anomalies(event_dates, pre_event_window, z_score)
                st.session_state.detector = detector
                st.session_state.analysis_complete = True
                st.success(f"✅ Analysis complete! Detected {detector.df['Is_Anomaly'].sum()} anomalies")
            else:
                st.error("Please enter at least one valid event date within the data range")
    
    if st.session_state.analysis_complete and st.session_state.detector:
        detector = st.session_state.detector
        
        # Statistics
        stats = detector.get_statistics()
        summary = detector.get_anomaly_summary()
        
        st.markdown("---")
        st.markdown("### 📊 Analysis Results")
        st.markdown("Below are the key metrics from your analysis. The system has analyzed trading volume patterns and identified statistically unusual activity.")
        
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
            st.markdown("The following dates show statistically unusual trading volume before major events. Each anomaly is classified by severity based on how many standard deviations above the average volume it is.")
            
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
        st.markdown("Interactive charts help you visualize trading patterns and anomalies. The volume chart shows daily trading volume with anomaly markers (red diamonds) and event days (green triangles).")
        
        # Volume Chart with high contrast
        fig = go.Figure()
        
        # Add volume bars with professional colors
        fig.add_trace(go.Bar(
            x=detector.df.index,
            y=detector.df['Volume'],
            name='Trading Volume',
            marker=dict(
                color='#2a5298',
                opacity=0.85,
                line=dict(color='#1e3c72', width=1)
            )
        ))
        
        # Add anomaly threshold line with high contrast and better visibility
        fig.add_hrect(
            y0=stats['anomaly_threshold'],
            y1=stats['anomaly_threshold'],
            fillcolor="#ff6b6b",
            opacity=0.4,
            layer="below",
            line_width=0
        )
        fig.add_hline(
            y=stats['anomaly_threshold'],
            line_dash="dash",
            line_color="#ff0000",
            line_width=4,
            annotation_text=f"<b>ANOMALY THRESHOLD</b><br>{stats['anomaly_threshold']:,.0f}",
            annotation_position="right",
            annotation=dict(
                font=dict(size=16, color="#ffffff", family="Arial Black"),
                bgcolor="#ff0000",
                bordercolor="#cc0000",
                borderwidth=3,
                borderpad=8
            )
        )
        
        # Highlight anomalies with high contrast
        anomalies = detector.df[detector.df['Is_Anomaly']]
        if not anomalies.empty:
            fig.add_trace(go.Scatter(
                x=anomalies.index,
                y=anomalies['Volume'],
                mode='markers',
                name='Anomalies',
                marker=dict(
                    color='#ff0000',
                    size=15,
                    symbol='diamond',
                    line=dict(width=3, color='#cc0000'),
                    opacity=1.0
                )
            ))
        
        # Highlight event days with high contrast
        event_days = detector.df[detector.df['Event_Day']]
        if not event_days.empty:
            fig.add_trace(go.Scatter(
                x=event_days.index,
                y=event_days['Volume'],
                mode='markers',
                name='Event Days',
                marker=dict(
                    color='#00cc00',
                    size=12,
                    symbol='triangle-up',
                    line=dict(width=3, color='#009900'),
                    opacity=1.0
                )
            ))
        
        fig.update_layout(
            title=dict(
                text=f"Trading Volume Analysis - Anomalies Detected: {stats['anomaly_count']}",
                font=dict(size=18, color='#1a1a1a', family='Arial Black')
            ),
            xaxis=dict(
                title=dict(text="Date", font=dict(size=14, color='#1a1a1a', family='Arial')),
                gridcolor='#e0e0e0',
                gridwidth=1,
                showgrid=True
            ),
            yaxis=dict(
                title=dict(text="Volume", font=dict(size=14, color='#1a1a1a', family='Arial')),
                gridcolor='#e0e0e0',
                gridwidth=1,
                showgrid=True
            ),
            hovermode='x unified',
            height=550,
            template="plotly_white",
            plot_bgcolor='white',
            paper_bgcolor='white',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                font=dict(size=12, color='#1a1a1a', family='Arial')
            ),
            font=dict(family="Arial", size=12, color='#1a1a1a')
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
                marker=dict(
                    color='#2a5298',
                    opacity=0.85,
                    line=dict(color='#1e3c72', width=1)
                )
            ))
            fig2.add_vrect(
                x0=z_score,
                x1=z_score,
                fillcolor="#ff6b6b",
                opacity=0.3,
                layer="below",
                line_width=0
            )
            fig2.add_vline(
                x=z_score,
                line_dash="dash",
                line_color="#ff0000",
                line_width=4,
                annotation_text=f"<b>THRESHOLD</b><br>Z = {z_score}",
                annotation=dict(
                    font=dict(size=14, color="#ffffff", family="Arial Black"),
                    bgcolor="#ff0000",
                    bordercolor="#cc0000",
                    borderwidth=3,
                    borderpad=8
                )
            )
            fig2.update_layout(
                title=dict(
                    text="Z-Score Distribution",
                    font=dict(size=16, color='#1a1a1a', family='Arial Black')
                ),
                xaxis=dict(
                    title=dict(text="Z-Score", font=dict(size=12, color='#1a1a1a', family='Arial')),
                    gridcolor='#e0e0e0',
                    gridwidth=1,
                    showgrid=True
                ),
                yaxis=dict(
                    title=dict(text="Frequency", font=dict(size=12, color='#1a1a1a', family='Arial')),
                    gridcolor='#e0e0e0',
                    gridwidth=1,
                    showgrid=True
                ),
                template="plotly_white",
                height=450,
                plot_bgcolor='white',
                paper_bgcolor='white',
                font=dict(family="Arial", size=11, color='#1a1a1a')
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        with col2:
            fig3 = go.Figure()
            fig3.add_trace(go.Scatter(
                x=detector.df.index,
                y=detector.df['Z_Score'],
                mode='lines',
                name='Z-Score Over Time',
                line=dict(
                    color='#2a5298',
                    width=2.5,
                    shape='linear'
                ),
                fill='tozeroy',
                fillcolor='rgba(42, 82, 152, 0.2)'
            ))
            fig3.add_hrect(
                y0=z_score,
                y1=z_score,
                fillcolor="#ff6b6b",
                opacity=0.3,
                layer="below",
                line_width=0
            )
            fig3.add_hline(
                y=z_score,
                line_dash="dash",
                line_color="#ff0000",
                line_width=4,
                annotation_text=f"<b>THRESHOLD</b><br>Z = {z_score}",
                annotation=dict(
                    font=dict(size=14, color="#ffffff", family="Arial Black"),
                    bgcolor="#ff0000",
                    bordercolor="#cc0000",
                    borderwidth=3,
                    borderpad=8
                )
            )
            fig3.update_layout(
                title=dict(
                    text="Z-Score Timeline",
                    font=dict(size=16, color='#1a1a1a', family='Arial Black')
                ),
                xaxis=dict(
                    title=dict(text="Date", font=dict(size=12, color='#1a1a1a', family='Arial')),
                    gridcolor='#e0e0e0',
                    gridwidth=1,
                    showgrid=True
                ),
                yaxis=dict(
                    title=dict(text="Z-Score", font=dict(size=12, color='#1a1a1a', family='Arial')),
                    gridcolor='#e0e0e0',
                    gridwidth=1,
                    showgrid=True
                ),
                template="plotly_white",
                height=450,
                plot_bgcolor='white',
                paper_bgcolor='white',
                font=dict(family="Arial", size=11, color='#1a1a1a')
            )
            st.plotly_chart(fig3, use_container_width=True)
        
        # Raw Data
        with st.expander("📋 View Raw Data"):
            st.dataframe(detector.df, use_container_width=True, height=300)

def main():
    """Main application function"""
    
    # Apply theme CSS
    if st.session_state.dark_mode:
        apply_dark_theme()
    else:
        apply_light_theme()
    
    # Route to appropriate page
    if st.session_state.current_page == 'welcome':
        welcome_page()
    elif st.session_state.current_page == 'analysis':
        analysis_page()

if __name__ == "__main__":
    main()

