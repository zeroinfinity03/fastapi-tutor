from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, make_batch_predictions
from typing import List

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Welcome to the ML Model Prediction API'}



@app.post('/prediction', response_model=OutputSchema)
def predict(user_input: InputSchema):
    prediction = make_prediction(user_input.model_dump())
    return OutputSchema(predicted_price=prediction)

# In predict.py make_prediction fn expects inputs as a dict, 
# we have user_input in json, so we do user_input.model_dump() to convert into dict.
# we get the prediction as a float value from make_prediction fn.
# Now, we have to return the response in the form of OutputSchema. 


'''
OR:

@app.post('/prediction', response_model=OutputSchema)
def predict(user_input: InputSchema):
    prediction = make_prediction(user_input.model_dump())
    
    # FastAPI automatically is dict ko OutputSchema mein convert kar dega!
    return {"predicted_price": prediction} 

'''







@app.post('/batch_prediction', response_model=List[OutputSchema])
def batch_predict(user_inputs: List[InputSchema]):
    predictions = make_batch_predictions([x.model_dump() for x in user_inputs])
    return [OutputSchema(predicted_price=round(prediction, 2)) for prediction in predictions]




