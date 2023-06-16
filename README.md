## Crypto trading info app

This app provides a script to collect data on desired symbol trading in intervals of 1h, 4h or 24h and store them in csv format.
Flask UI contains endpoints to build candlestick graphs for symbols, data on which was collected.
Also, there is an endpoint to visualize market cap data on 10 symbols with the largest quote volume in last 24 hours.

### Technologies:

<div style="display:flex; align-items: center; gap:10px">
     Python
</div>
<div style="display:flex; align-items: center; gap:10px">
     Flask
</div>
<div style="display:flex; align-items: center; gap:10px">
     Pandas
</div>
<div style="display:flex; align-items: center; gap:10px">
     Requests
</div>
<div style="display:flex; align-items: center; gap:10px">
     Plotly
</div>

### Installation:

 ```bash
  git clone https://github.com/rraatt/FoodVoteApp.git
```

Create and activate a virtual environment:

 ```bash
  python -m venv /path/to/new/virtual/environment
  python -m venv c:\path\to\myenv
```

Install requirements

 ```bash
  pip install -r requirements.txt       
```

To fetch data for desired symbol

 ```bash
  python fetch.py --symbol desired_symbol --windowSize 1h/4h/1d
  ```   

To start Flask UI

 ```bash
  python app.py
  ```   

### Usage:

Access at localhost:

 http://localhost:5000/candlestick/desired_symbol
 
 http://localhost:5000/piechart/
 

To deploy the script, so it collects data in desired intervals of time there are different variants.
If this program is to be used locally on Windows machine, we can set up a task scheduler to run our script automatically.
If we desire to deploy this program on server or any other UNIX system we can use cron to schedule our script.
Another variant is to rewrite the program to use a relational database and configure celery task manager and beat 
scheduler in different containers and use this app via docker compose.

To store the data in a relational database we could store it as served by Binance api for future flexibility or
just store used fields: symbol, openPrice, highPrice, lowPrice, closePrice, openTime. There's no need for complex schema
and all data can be stored in one table, unless more functionality is planned for program in which case we could consider
storing symbol in different table and reference it via foreign key, so we could fetch data from different tables associated with this symbol.
