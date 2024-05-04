from alpha_vantage.timeseries import TimeSeries
import os

def get_api_key(filename="alpha_vantage_API_key.txt"):
    """
    Reads an API key from a file.

    Parameters:
    filename (str): Filename where the API key is stored.

    Returns:
    str: The API key.
    """
    # Construct the full path to the file
    current_dir = os.path.dirname(__file__)  # gets the directory where the script is located
    file_path = os.path.join(current_dir, filename)  # constructs full file path

    # Open and read the API key from the file
    with open(file_path, 'r') as file:
        api_key = file.read().strip()  # read the file and strip any extra newline characters
    return api_key

api_key_file = 'alpha_vantage_API_key.txt'
api_key = get_api_key(api_key_file)

def f_fetch_stock_data(symbol, api_key, start_date, end_date, interval='daily', outputsize='full'):
    """
    Fetch stock time series data from Alpha Vantage between specific dates.

    Parameters:
    symbol (str): The stock symbol to fetch data for (e.g., 'AAPL' for Apple Inc.).
    api_key (str): Your Alpha Vantage API key.
    start_date (str): The start date for the data in 'YYYY-MM-DD' format.
    end_date (str): The end date for the data in 'YYYY-MM-DD' format.
    interval (str): The interval between data points ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly').
    outputsize (str): The size of the data ('compact' returns the last 100 data points; 'full' returns the full-length time series of up to 20 years of historical data).

    Returns:
    pandas.DataFrame: A DataFrame containing the requested time series data filtered by the specified dates.
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

    # Filter data for the specified date range
    data = data[(data.index >= start_date) & (data.index <= end_date)]

    return data
