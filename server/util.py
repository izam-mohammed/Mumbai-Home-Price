import json
import numpy as np
import joblib

# Global variables for storing locations, data columns, and model
__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    """
    Get the estimated price of a house based on location and input features.

    Args:
        location (str): The name of the location.
        sqft (float): Total square footage of the house.
        bhk (int): Number of bedrooms.
        bath (int): Number of bathrooms.

    Returns:
        float: The estimated price of the house.
    """
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    """
    Load saved artifacts including data columns and machine learning model.
    """
    print("Loading saved artifacts... Start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open("./artifacts/saved_model.pkl", "rb") as f:
            __model = joblib.load(f)
    print("Loading saved artifacts... Done")


def get_location_names():
    """
    Get a list of available location names.

    Returns:
        list: A list of location names.
    """
    return __locations


def get_data_columns():
    """
    Get the list of data columns used for prediction.

    Returns:
        list: A list of data columns.
    """
    return __data_columns
