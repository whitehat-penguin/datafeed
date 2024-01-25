import requests
import csv
from datetime import datetime

def get_historical_data(n_bar, time_start, interval):

    # Define the API endpoint
    symbol_id = 'BITSTAMP_SPOT_BTC_USD'
    api_url = f"https://rest.coinapi.io/v1/ohlcv/{symbol_id}/history"
    headers = {
        #  'X-CoinAPI-Key' : '693AF4C5-1296-4C12-B682-8D05BF441A6F'
         'X-CoinAPI-Key' : '8CC6D0BD-C6DC-42BE-93F2-41131919E282'
    }
    # Define the parameters for the API request
    params = {
        'period_id': interval, 
        'time_start': time_start,
        'limit': n_bar,
    }

    # Make the API request
    response = requests.get(api_url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def write_to_csv(historical_data, csv_filename='historical_data.csv'):
    if historical_data is not None:
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['time_period_start', 'price_open', 'price_high', 'price_low', 'price_close', 'volume_traded']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for entry in historical_data:
                # # Format time_period_start to the desired format: 2024-01-23 01:50:00
                # formatted_time = datetime.strptime(entry['time_period_start'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S')

                # Write selected fields to the CSV file
                writer.writerow({
                    'time_period_start': entry['time_period_start'],
                    'price_open': entry['price_open'],
                    'price_high': entry['price_high'],
                    'price_low': entry['price_low'],
                    'price_close': entry['price_close'],
                    'volume_traded': entry['volume_traded']
                })
        print(f"Data written to {csv_filename}")
    else:
        print("No data to write.")


# Example: Get Bitcoin historical data for the last 2 years with 5-minute intervals
interval = '5MIN'  # 5-minute intervals
time_start = '2022-01-01T00:00:00'
n_bar = 105120
historical_data = get_historical_data(n_bar, time_start, interval)

write_to_csv(historical_data)
