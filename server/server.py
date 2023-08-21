"""
Home Price Prediction Flask App

This Flask application provides two routes for predicting home prices:
1. /get_location_names (GET): Get a list of available location names.
2. /predict_home_price (GET/POST): Predict the price of a home based on input
    parameters.

Usage:
- Run this script to start the Flask server for home price prediction.
- Access the routes using appropriate HTTP methods and parameters.
"""

from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    """
    Get a list of available location names.

    Returns:
        JSON response containing location names.
    """
    response = jsonify({"locations": util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/predict_home_price", methods=["GET", "POST"])
def predict_home_price():
    """
    Predict the price of a home based on input parameters.

    POST Parameters:
        total_sqft (float): Total square footage of the home.
        location (str): Location name.
        bhk (int): Number of bedrooms.
        bath (int): Number of bathrooms.

    Returns:
        JSON response containing the estimated home price.
    """
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify(
        {"estimated_price": estimated_price}
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
