from alpha_vantage.timeseries import TimeSeries

api_key_file = 'alpha_vantage_API_key.txt'
api_key = get_api_key(api_key_file)

def get_api_key(file_name):
    """
    Read the API key from a text file and return it.

    Parameters:
    file_name (str): The name of the file containing the API key.

    Returns:
    str: The API key.
    """
    with open(file_name, 'r') as file:
        api_key = file.read().strip()  # Read the key and strip any extra whitespace
    return api_key

def f_fetch_stock_data(api_key=api_key, symbol, interval='daily', outputsize='compact'):
    """
    Fetch stock time series data from Alpha Vantage.

    Parameters:
    api_key (str): Your Alpha Vantage API key.
    symbol (str): The stock symbol to fetch data for (e.g., 'AAPL' for Apple Inc.).
    interval (str): The interval between data points ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly').
    outputsize (str): The size of the data ('compact' returns the last 100 data points; _
                      'full' returns the full-length time series of up to 20 years of historical data).

    Returns:
    pandas.DataFrame: A DataFrame containing the requested time series data.
    """
    ts = TimeSeries(key=api_key, output_format='pandas')
    if interval == 'daily':
        data, meta_data = ts.get_daily(symbol=symbol, outputsize=outputsize)
    elif interval == 'weekly':
        data, meta_data = ts.get_weekly(symbol=symbol)
    elif interval == 'monthly':
        data, meta_data = ts.get_monthly(symbol=symbol)
    else:
        data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize=outputsize)

    return data

