from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# Step1:
# user sends userid and password, token endpoint will be used,
# and in this endpoint we will verify the user_id and password if its Correct then we will give back a token else raise error.


# Step2:
# user want to access the profile, profile end point will used,
# and in this endpoint we will accept the token that was generated in step1, and if its a valid token then we will give back the profile info else raise error.




@app.post('/token')
def login(username: str = Form(...), password: str = Form(...)):     # required value will be specifies via(...)
    if username == 'john' and password == 'pass123':
        return {'access_token': 'valid_token', 'token_type': 'bearer'}
    raise HTTPException(status_code=400, detail='Invalid Credentials')


def decode_token(token: str):
    if token == 'valid_token':
        return {'name': 'john'}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid Authentication Credentials'
    )



# to get the user we need the valid token which depends on oauth2_scheme.
# this line that we have written will give the token:    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
# and this token we need to decode.
def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)



# this endpoint will just give back the user details.
@app.get('/profile')
def get_profile(user=Depends(get_current_user)):
    return {'username': user['name']}



















