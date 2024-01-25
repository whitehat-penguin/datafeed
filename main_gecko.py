import requests
from datetime import datetime, timedelta

def get_historical_data(symbol, days, interval):
    # Calculate the start date based on the given number of days
    start_date = datetime.now() - timedelta(days=days)

    # Format the start date and current date
    start_date_str = start_date.strftime("%d-%m-%Y")
    end_date_str = datetime.now().strftime("%d-%m-%Y")

    # Define the API endpoint
    api_url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

    # Define the parameters for the API request
    params = {
        'vs_currency': symbol,
        'days': days,
        'interval': interval,
        'precision': 3,
    }

    # Make the API request
    response = requests.get(api_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data['prices']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Example: Get Bitcoin historical data for the last 2 years with 5-minute intervals
symbol = 'usd'  # You can change this to other fiat currencies like 'eur', 'jpy', etc.
days = 365 * 2  # 2 years
interval = 'daily'  # 5-minute intervals

historical_data = get_historical_data(symbol, days, interval)

if historical_data:
    for timestamp, price in historical_data:
        print(f"{datetime.utcfromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')} - {price} {symbol.upper()}")
