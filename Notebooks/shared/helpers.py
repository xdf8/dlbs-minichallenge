import numpy as np
from scipy.io import loadmat
#import pandas as pd

mat_file = "data/cars_annos.mat"


def mat_to_array(mat_file):
    """
    Convert a MATLAB .mat file containing class names into a NumPy array.

    This function reads a .mat file, specifically one containing class names, and converts
    the class names into a NumPy array for further processing in Python.

    Args:
        mat_file (str): The path to the .mat file containing the class names.

    Returns:
        numpy.ndarray: A 1-dimensional NumPy array containing the class names from the .mat file.
    """

    mat_data = loadmat(mat_file)
    class_names = np.hstack(mat_data["class_names"][0])
    return class_names


print(mat_to_array(mat_file))
# print(pd.Series(class_names))
