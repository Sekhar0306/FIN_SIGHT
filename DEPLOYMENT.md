# 🚀 Deployment Guide

Complete guide for deploying FIN-SIGHT to Streamlit Cloud

## Prerequisites

- GitHub account
- Streamlit Cloud account (free tier available)
- Alpha Vantage API key

## Step-by-Step Deployment

### 1. Prepare Your Repository

```bash
# Initialize git repository
cd "FIN SIGHT"
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: FIN-SIGHT Anomaly Detection"

# Create GitHub repository (via GitHub website or CLI)
# Then push your code
git remote add origin https://github.com/YOUR_USERNAME/FIN-SIGHT.git
git branch -M main
git push -u origin main
```

### 2. Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**

   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Create New App**

   - Click "New app" button
   - Select your GitHub repository
   - Select the branch (usually `main`)
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Configure Environment Variables**
   - Go to your app settings (⚙️ icon)
   - Click "Secrets" tab
   - Add your Alpha Vantage API key:
   ```
   ALPHA_VANTAGE_API_KEY=VO8CV7MCLOI5GNI3
   ```

### 3. Verify Deployment

- Your app will be live at: `https://YOUR-APP-NAME.streamlit.app`
- First deployment may take 2-3 minutes
- Check for any errors in the logs

## Streamlit Cloud Configuration

### Recommended Settings

Create `.streamlit/config.toml` in your repository:

```toml
[theme]
primaryColor="#667eea"
backgroundColor="#ffffff"
secondaryBackgroundColor="#f0f2f6"
textColor="#262730"
font="sans serif"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

### Secrets Management

For sensitive data, use Streamlit's secrets management:

1. In Streamlit Cloud, go to Settings → Secrets
2. Add your secrets in TOML format:

```toml
[secrets]
ALPHA_VANTAGE_API_KEY = "your_api_key_here"
```

3. Access in your code:

```python
import streamlit as st
api_key = st.secrets["ALPHA_VANTAGE_API_KEY"]
```

## Alternative Deployment Options

### Option 1: Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:

```bash
docker build -t fin-sight .
docker run -p 8501:8501 fin-sight
```

### Option 2: Heroku Deployment

1. Create `Procfile`:

```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Create `setup.sh`:

```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. Deploy:

```bash
heroku create fin-sight-app
git push heroku main
heroku open
```

### Option 3: AWS EC2 Deployment

1. Launch EC2 instance (Ubuntu)
2. SSH into instance
3. Install dependencies:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

4. Run application:

```bash
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

5. Configure security group to allow port 8501

## Performance Optimization

### For Streamlit Cloud

1. **Reduce API Calls**

   - Cache data using `@st.cache_data`
   - Use daily data instead of intraday
   - Implement rate limiting

2. **Optimize Visualizations**

   - Limit data points in charts
   - Use sampling for large datasets
   - Enable chart caching

3. **Improve Load Times**
   - Lazy load heavy components
   - Use session state for data persistence
   - Minimize imports

### Caching Strategy

```python
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_stock_data(symbol, start_date, end_date):
    # Your data fetching code
    return df
```

## Monitoring and Maintenance

### Check App Health

1. **Logs**: Monitor Streamlit Cloud logs for errors
2. **Performance**: Check response times
3. **API Limits**: Monitor Alpha Vantage API usage

### Common Issues

**Issue**: App crashes on startup

- **Solution**: Check requirements.txt is complete
- **Solution**: Verify Python version compatibility

**Issue**: API rate limit errors

- **Solution**: Implement caching
- **Solution**: Add retry logic with delays

**Issue**: Slow performance

- **Solution**: Optimize data processing
- **Solution**: Reduce chart complexity

## Security Best Practices

1. **API Keys**: Never commit API keys to repository
2. **Secrets**: Use Streamlit secrets management
3. **Validation**: Validate all user inputs
4. **Rate Limiting**: Implement rate limiting
5. **HTTPS**: Always use HTTPS in production

## Cost Considerations

### Free Tier Limits

- **Streamlit Cloud Free**: Unlimited apps, 1GB RAM
- **Alpha Vantage Free**: 5 requests/minute, 500 requests/day
- **Heroku Free**: 550-1000 hours/month

### Paid Options

- **Streamlit Cloud Pro**: $20/month, more resources
- **Alpha Vantage Premium**: $49.99/month, higher limits
- **AWS EC2**: Pay-as-you-go, varies by instance

## Troubleshooting

### Deployment Issues

**Problem**: Import errors in production

```bash
# Solution: Ensure all dependencies are in requirements.txt
pip freeze > requirements.txt
```

**Problem**: App won't start

```bash
# Solution: Check logs for specific errors
# Common issues: missing dependencies, wrong Python version
```

**Problem**: API errors

```bash
# Solution: Verify API key is set correctly
# Check rate limits and implement caching
```

## Support and Resources

- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Streamlit Cloud**: [share.streamlit.io](https://share.streamlit.io)
- **Alpha Vantage Docs**: [alphavantage.co/documentation](https://www.alphavantage.co/documentation)

## Next Steps

1. ✅ Deploy your app
2. 📊 Test all features
3. 🔒 Secure your API keys
4. 📈 Monitor performance
5. 🎉 Share your app!

---

**Happy Deploying! 🚀**
