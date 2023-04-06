# %%
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Remember to exclude PRICE from this list
# this list changes dynamically
model_parameters = ['gross_tax', 'bedrooms', 'bathrooms', 'property_views', 'lot_size',
       'year_built', 'lot_width', 'lot_length', 'age', 'bungalow', 'storey',
       'basement', 'laneway_house', 'garage', 'split_entry', 'latitude',
       'longitude', 'community_arbutus', 'community_quilchena',
       'community_shaughnessy', 'community_south granville',
       'community_southlands', 'community_southwest marine',
       'community_university (ubc)']


def preprocess_features(features, model_parameters):
    for param in model_parameters:
        if param not in features:
            features[param] = 0
    return features

def encode_categorical_columns(df, cat_cols):
    '''
    Encode categorical columns in pandas dataframe using one-hot encoding.
    
    Parameters:
    df (pandas dataframe): The dataframe to encode.
    cat_cols (list): A list of column names to encode.
    
    Returns:
    A new pandas dataframe with the specified categorical columns replaced by their encoded values.
    '''
    # check if specified columns exist in the dataframe
    missing_cols = set(cat_cols) - set(df.columns)
    if missing_cols:
        raise KeyError(f"The following columns were not found in the dataframe: {list(missing_cols)}")
    
    # create a new dataframe with the encoded columns
    for col in cat_cols:
        df_encoded = pd.get_dummies(df[col], prefix=col)
        df = df.drop(col, axis=1)
        df = df.join(df_encoded)
    
    return df


def prepare_feature_for_prediction(data):
    categorical_columns = [
        'community'
    ]

    data = pd.DataFrame(data, index=[0])
    data = encode_categorical_columns(data, categorical_columns)
    data = preprocess_features(data, model_parameters)

    return data