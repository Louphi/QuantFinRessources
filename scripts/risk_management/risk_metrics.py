import numpy as np

def f_VaR(returns, confidence_level=0.95):
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


def f_CVaR(returns, confidence_level=0.95):
    """
    Calculate the Conditional Value at Risk (CVaR) for a given set of returns.

    Parameters:
    returns (array-like): Array of returns.
    confidence_level (float): Confidence level for CVaR, default is 95%.

    Returns:
    float: The Conditional Value at Risk (CVaR) at the specified confidence level.
    """
    # Calculate VaR
    VaR = f_VaR(returns, confidence_level)

    # Calculate CVaR as the mean of the returns that are worse than the VaR
    CVaR = returns[returns <= VaR].mean()
    return CVaR