import requests

def fetch_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=D6VY1SJG7T3H8SB2'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        time_series_data = data.get('Time Series (5min)')
        if time_series_data:
            latest_data_timestamp = max(time_series_data.keys())
            latest_data = time_series_data[latest_data_timestamp]
            return latest_data.get('4. close')
        else:
            return None
    else:
        return None

