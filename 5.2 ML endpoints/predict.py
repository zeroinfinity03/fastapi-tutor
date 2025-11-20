import joblib
import numpy as np
from typing import List

saved_model = joblib.load('model.joblib')
print('Loaded the Model')


# users se data json me aayega and when it comes to this fn call, 
# we will get it as a dict and this will return a floting value the actual predicted value.
# also our model expects a numpy 2d array as input to make predictions.
# json -> dict -> numpy 2d array -> model prediction -> float
# we use something like user_input.model_dump() in main.py to convert json into dict.

def make_prediction(data: dict) -> float:
    features = np.array([
        [
            data['longitude'],
            data['latitude'],
            data['housing_median_age'],
            data['total_rooms'],
            data['total_bedrooms'],
            data['population'],
            data['households'],
            data['median_income']
        ]
    ])
    return saved_model.predict(features)[0]
# 2 brackets [[]] so 2d numpy array but the inside bracket is only 1[] => so 1 row and 8 columns
# 2d numpy arry size = (1, 8)
# predict karte time user do data bhejega woh multiple rows/record toh bhejega nhi, so 1 row hi hoga hamesha with all the features/columns data.

# sckit learn returns prediction in this format: array([ 452600.55, 4524322.45, 45242.32 ])
# but since we will send only 1 record all the time, we will get only 1 value in the array:  array([ 452600.55]) => so we do [0] to get the first value from the array.






def make_batch_predictions(data: List[dict]) -> np.array:
    X = np.array([
        [
            x['longitude'],
            x['latitude'],
            x['housing_median_age'],
            x['total_rooms'],
            x['total_bedrooms'],
            x['population'],
            x['households'],
            x['median_income']
        ]
        for x in data
    ])
    return saved_model.predict(X)



