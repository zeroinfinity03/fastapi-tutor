from fastapi import FastAPI
from models import User
app = FastAPI()


@app.get('/')
def home():
    return {"message": "Hello World"}


@app.get('/users', response_model = User)
def user():
    return User(id=1, name="John Doe", email="john.doe@example.com")

