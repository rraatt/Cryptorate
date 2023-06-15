import csv
import os

import requests
import pandas as pd
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--symbol", help="Symbols to fetch")
parser.add_argument("--windowSize", choices=['1h', '4h', '1d'], help="Time window size")
args = parser.parse_args()

symbol = args.symbol

windowSize = args.windowSize

# The base URL of the Binance API
url = "https://api.binance.com/api/v3/ticker"
file_path = f'data/{symbol}.csv'

# Construct the URL for this symbol
params = {"symbol": symbol, "windowSize": windowSize}
# Send a GET request to the Binance API
response = requests.get(url, params=params)

# If the request was successful
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame([data])
    if not os.path.isfile(file_path):
        df.to_csv(file_path, mode='a', index=False)
    else:
        df.to_csv(file_path, mode='a', index=False, header=False)
else:
    raise ValueError('Error occured during API request')

