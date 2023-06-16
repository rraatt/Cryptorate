import operator
import os
from datetime import datetime

import requests
from flask import Flask, render_template
import pandas as pd
import plotly
import json
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)


@app.route('/candlestick/<symbol_name>')
def candle(symbol_name):
    # Open file with required symbol name
    file_path = f'data/{symbol_name}.csv'
    if not os.path.exists(file_path):
        return f"No such file found for symbol: {symbol_name}"
    df = pd.read_csv(file_path)  # reading data
    df['openTime'] = pd.to_datetime(df['openTime'], unit='ms') # Convert Unix timestamp to datetime
    fig = go.Figure(data=[go.Candlestick(x=df['openTime'],
                                         open=df['openPrice'],
                                         high=df['highPrice'],
                                         low=df['lowPrice'],
                                         close=df['lastPrice'])])  # creating figure
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)  # encoding plotly figure to json
    return render_template('index.html', fig_json=fig_json, name=symbol_name)  # rendering template


@app.route('/piechart/')
def pie():
    response = requests.get('https://api.binance.com/api/v3/ticker/24hr') # Get data on trading in last 24 hours
    data = response.json()
    data = sorted(data, key=lambda item: float(item["quoteVolume"]), reverse=True) # Sort data by descending quote volume
    df = pd.DataFrame(data[:10])
    fig = px.pie(df, values='quoteVolume', names='symbol', title='Marketcap of 10 most popular symbols')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)  # encoding plotly figure to json
    return render_template('index.html', fig_json=fig_json, name='Piechart')  # rendering template


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
