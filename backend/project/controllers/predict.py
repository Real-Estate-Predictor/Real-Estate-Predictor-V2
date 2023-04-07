
from joblib import load
from flask import request, Blueprint
from flask import request, jsonify
import sys


sys.path.append("../../../..")
sys.path.append("../../")

from project.utils.prepare_object_for_prediction import prepare_feature_for_prediction

lin_reg_model = load('../ML_models/linear_reg_model.joblib')

predict_bp = Blueprint('/', __name__)

@predict_bp.route('/', methods=['POST'])
def predict():
    # Get the JSON payload from the request
    features_obj = request.get_json()
    if not features_obj:
        return jsonify({'error': 'JSON payload is missing or malformed'}), 400

    # Use the prepare_feature_for_prediction function to create a DataFrame from the features object
    features_df = prepare_feature_for_prediction(features_obj)

    # Get the 2D array from the DataFrame
    features_array = features_df.values

    # Use the loaded model to make predictions
    y_pred = lin_reg_model.predict(features_array)

    # Format the output as a JSON object
    output = {'predicted_price': round(float(y_pred[0] / 10000), 2)}
    return jsonify(output)