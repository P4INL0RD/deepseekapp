from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend de FastAPI desplegado correctamente en Azure"}