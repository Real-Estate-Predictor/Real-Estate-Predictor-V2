from joblib import dump, load
import pandas as pd
from prepare_object_for_prediction import prepare_feature_for_prediction


lin_reg_model = load('./linear_reg_model.joblib')

def predict_with_lin_reg_model(features_obj):

    features_df = prepare_feature_for_prediction(features_obj)
    # Get the 2D array from the DataFrame
    features_array = features_df.values

    # Use the loaded model to make predictions
    y_pred = lin_reg_model.predict(features_array)
    return y_pred[0] / 10000

# price: 7000000
feature_input1 = {
 'gross_tax': 23411,
 'bedrooms': 9,
 'bathrooms': 10,
 'community': 'arbutus',
 'property_views': 547.0,
 'lot_size': 8500.0,
 'year_built': 2020,
 'lot_width': 45.0,
 'lot_length': 45.0,
 'age': 3,
 'bungalow': 0,
 'storey': 2,
 'basement': 1,
 'laneway_house': 0,
 'garage': 0,
 'split_entry': 0,
 'latitude': 49.257141,
 'longitude': -123.1764991
}

#'price' 4360000
feature_input2 = { 'gross_tax': 15988,
 'bedrooms': 7,
 'bathrooms': 5,
 'community': 'arbutus',
 'property_views': 688.0,
 'lot_size': 6100.0,
 'year_built': 1989,
 'lot_width': 50.0,
 'lot_length': 50.0,
 'age': 34,
 'bungalow': 0,
 'storey': 3,
 'basement': 0,
 'laneway_house': 0,
 'garage': -1,
 'split_entry': 0,
 'latitude': 49.2535102,
 'longitude': -123.1529908}


feature_input_list = [feature_input1, feature_input2]
def linear_reg_prediction_test():

    for feature_input in feature_input_list:
        y_pred = predict_with_lin_reg_model(feature_input)
        print(y_pred)


if __name__ == "__main__":
    linear_reg_prediction_test()