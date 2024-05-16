import numpy as np

def f_compute_svd(matrix):
    """
    Compute the Singular Value Decomposition (SVD) of a given matrix.

    Parameters:
    matrix (numpy.ndarray): The matrix to decompose.

    Returns:
    U (numpy.ndarray): An m x m matrix where m is the number of rows in the input matrix.
    Sigma (numpy.ndarray): An m x n diagonal matrix of singular values, where m is the number of rows
                           and n is the number of columns in the input matrix.
    Vt (numpy.ndarray): An n x n matrix where n is the number of columns in the input matrix.
    """
    # Compute the SVD
    U, s, Vt = np.linalg.svd(matrix, full_matrices=False)

    # Create the Sigma diagonal matrix
    Sigma = np.diag(s)

    # Return the three matrices
    return U, Sigma, Vt