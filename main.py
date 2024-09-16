from fastapi import FastAPI

app = FastAPI()

@app.get("/hai..")
def read_root():
    return {"message": "Hello, FastAPI!"}


import uvicorn
uvicorn.run(app)