import operator

import pandas as pd
import requests
import plotly.express as px



response = requests.get('https://api.binance.com/api/v3/ticker/24hr')
data = response.json()
data = sorted(data, key=lambda item: float(item["quoteVolume"]), reverse=True)
df = pd.DataFrame(data[:10])
fig = px.pie(df, values='quoteVolume', names='symbol', title='Marketcap of 10 most popular symbols')
fig.show()