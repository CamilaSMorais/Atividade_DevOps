from fastapi import FastAPI
import random

app = FastAPI()

# 127.0.0.1:8000
@app.get("/Olá Mundo")
async def root():
    return {"message": "Olá Mundo"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}