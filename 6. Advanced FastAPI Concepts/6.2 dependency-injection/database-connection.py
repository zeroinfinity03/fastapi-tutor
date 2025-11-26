from fastapi import FastAPI, Depends

app = FastAPI()


# dependency function
def get_db():
    db = {'connection': 'mock_db_connection'}
    try:
        yield db
    finally:
        db.close()

# This function will be executed for every endpoint where Depends(get_db) is used.
# This fn return an instance of a database connection (here, a mock connection).
# in the end point we will accept this instance.

# endpoint
@app.get('/home')
def home(db=Depends(get_db)):
    return {'db_status': db['connection']}



