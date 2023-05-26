import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title='ms'
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

def start():
    uvicorn.run("main:app", host="0.0.0.0", port=443, reload=False)


if __name__ == "__main__":
    start()