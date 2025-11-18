from fastapi import FastAPI
from models import User
app = FastAPI()


@app.get('/')
def home():
    return {"message": "Hello World"}


@app.get('/users', response_model = User)
def user():
    return User(id=1, name="John Doe", email="john.doe@example.com")

# response_model se hum yeh bata rahe hain ki jo data hum user ko return karenge,
# uska structure kaisa hoga, aur usme kaunse fields honge.
# Isse FastAPI ko pata chal jata hai ki response ko kaise validate aur serialize karna hai
# jab wo client ko bheja jata hai.



