import numpy as np

def f_compute_VaR(returns, confidence_level=0.95):
    """
    Calculate the Value at Risk (VaR) for a given set of returns.

    Parameters:
    returns (array-like): Array of returns.
    confidence_level (float): Confidence level for VaR, default is 95%.

    Returns:
    float: The Value at Risk (VaR) at the specified confidence level.
    """
    # Calculate VaR as the inverse of the cumulative distribution function (quantile)
    VaR = np.percentile(returns, 100 * (1 - confidence_level))
    return VaR


def f_compute_CVaR(returns, confidence_level=0.95):
    """
    Calculate the Conditional Value at Risk (CVaR) for a given set of returns.
    Also known as expected shortfall.

    Parameters:
    returns (array-like): Array of returns.
    confidence_level (float): Confidence level for CVaR, default is 95%.

    Returns:
    float: The Conditional Value at Risk (CVaR) at the specified confidence level.
    """
    # Calculate VaR
    VaR = f_compute_VaR(returns, confidence_level)

    # Calculate CVaR as the mean of the returns that are worse than the VaR
    CVaR = returns[returns <= VaR].mean()
    return CVaR

def f_compute_beta(stock_returns, market_returns):
    """
    Compute the beta of a stock.

    Parameters:
    stock_returns (pandas.Series): A pandas Series containing the returns of the stock.
    market_returns (pandas.Series): A pandas Series containing the returns of the market or benchmark, _
                                    must be of same length as stock_returns.

    Returns:
    float: The beta of the stock relative to the market.
    """
    # Concatenate the stock and market returns into a single DataFrame
    data = pd.concat([stock_returns, market_returns], axis=1)
    data.columns = ['Stock', 'Market']

    # Calculate the covariance matrix of the stock and the market returns
    covariance_matrix = data.cov()

    # The covariance between the stock and the market
    covariance_stock_market = covariance_matrix.loc['Stock', 'Market']

    # The variance of the market
    variance_market = data['Market'].var()

    # Beta calculation
    beta = covariance_stock_market / variance_market

    return beta