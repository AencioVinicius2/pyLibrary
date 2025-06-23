from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def inicio():
    return {"Hello": "World"}