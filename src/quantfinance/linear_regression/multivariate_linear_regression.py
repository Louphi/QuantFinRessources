import statsmodels.api as sm

def f_multivariate_linear_regression(data, dependent_vars, independent_vars):
    """
    Perform multivariate multiple linear_regression.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the dataset.
    dependent_vars (list): A list of names of the dependent variables.
    independent_vars (list): A list of names of the independent variables.

    Returns:
    RegressionResults: The results of the regression, including coefficients and statistics.
    """
    # Extract the dependent variables
    Y = data[dependent_vars]

    # Extract the independent variables and add a constant for the intercept
    X = data[independent_vars]
    X = sm.add_constant(X)

    # Fit the model
    model = sm.OLS(Y, X).fit()

    return model