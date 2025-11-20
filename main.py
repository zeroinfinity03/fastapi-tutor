import asyncio
from fastapi import FastAPI
from timeit import default_timer as timer

app = FastAPI()


@app.get("/")
def read():
    return {"Hello": "World"}