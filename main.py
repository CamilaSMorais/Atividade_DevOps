from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:8000
@app.get("/Olá Mundo")
async def root():
    return {"message": "Olá Mundo"}

# 127.0.0.1:8000/teste1
@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo"}