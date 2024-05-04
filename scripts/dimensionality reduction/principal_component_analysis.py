import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def f_principal_component_analysis(data, n_components):
    """
    Perform Principal Component Analysis (PCA) on the provided data.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the dataset with features.
    n_components (int): The number of principal components to compute.

    Returns:
    DataFrame: A DataFrame containing the principal components.
    array: Explained variance ratio of the computed principal components.
    """
    # Standardizing the features before applying PCA, as PCA is affected by scale
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # PCA: reduce the dimensionality of the data
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(data_scaled)

    # Creating a DataFrame for the principal components
    pca_df = pd.DataFrame(data=principal_components,
                          columns=[f'Principal Component {i+1}' for i in range(n_components)])

    # Explained variance ratio
    explained_variance = pca.explained_variance_ratio_

    return pca_df, explained_variance


