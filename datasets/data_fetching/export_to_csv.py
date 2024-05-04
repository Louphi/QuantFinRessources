import pandas as pd
import os
from datetime import datetime

def f_export_to_csv(data, filename, datatype):
    """
    Export a matrix or array of data to a CSV file in a specified subdirectory with date in the filename.

    Parameters:
    data (array-like or DataFrame): The data to be exported. Can be a list of lists, numpy array, or DataFrame.
    filename (str): The base name of the file to save the CSV to, without extension.
    datatype (str): The type of data to be exported ("raw" or "processed"), which determines the subdirectory.

    Returns:
    None
    """
    # Validate datatype
    if datatype not in ['raw', 'processed']:
        raise ValueError("datatype must be 'raw' or 'processed'")

    # Check if the input data is a DataFrame or not
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)

    # Define the directory based on datatype, adjusting path to go up one level
    current_dir = os.path.dirname(__file__)  # gets the directory where the script is located
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))  # navigate to the parent directory
    directory = os.path.join(parent_dir, f"{datatype}_data")  # path to the correct dataset subdirectory

    # Ensure directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Format filename to include the current date
    date_str = datetime.now().strftime("%Y-%m-%d")
    full_path = os.path.join(directory, f"{filename}_{date_str}.csv")

    # Save the DataFrame to a CSV file
    data.to_csv(full_path, index=False)
    print(f"Data successfully exported to {full_path}")
