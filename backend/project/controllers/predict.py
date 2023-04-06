
from joblib import load
from flask import request, jsonify

from backend.project.controllers.utils.prepare_object_for_prediction import prepare_feature_for_prediction

lin_reg_model = load('./ML_models/linear_reg_model.joblib')

app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON payload from the request
    features_obj = request.get_json()

    # Use the prepared_feature_for_prediction function to create a DataFrame from the features object
    features_df = prepare_feature_for_prediction(features_obj)

    # Get the 2D array from the DataFrame
    features_array = features_df.values

    # Use the loaded model to make predictions
    y_pred = lin_reg_model.predict(features_array)

    # Format the output as a JSON object
    output = {'predicted_price': y_pred[0] / 10000}

    return jsonify(output)