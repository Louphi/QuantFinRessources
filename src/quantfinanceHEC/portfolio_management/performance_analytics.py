import pandas as pd
import numpy as np

def f_calculate_return(prices, return_type='simple'):
    """
    Calculate returns from a series of prices.
    
    Parameters:
    prices (pd.Series): A pandas Series of prices.
    return_type (str): The type of return to calculate. Either 'regular' or 'log'.
    
    Returns:
    pd.Series: A pandas Series of returns.
    """
    if return_type == 'simple':
        returns = prices.pct_change().dropna()
    elif return_type == 'log':
        returns = np.log(prices / prices.shift(1)).dropna()
    else:
        raise ValueError("return_type must be either 'regular' or 'log'")
    
    return returns

def f_calculate_covariance_matrix(dataframe):
    """
    Calculate the variance-covariance matrix from a dataframe.
    
    Parameters:
    dataframe (pd.DataFrame): A pandas DataFrame of prices.
    
    Returns:
    pd.DataFrame: A pandas DataFrame representing the variance-covariance matrix.
    """
    return dataframe.cov()