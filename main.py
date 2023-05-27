import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
# from fastapi.responses import FileResponse
# from niconico import NicoNico
# import glob
load_dotenv()

app = FastAPI(
    title='ms'
)


@app.get("/")
def read_root():
    return "Hello World! Please docs --> https://github.com/KuritaMasaya/ms"


@app.get("/foo")
def read_root():
    return {"foo": "bar"}


@app.get("/status")
def read_root():
    return {"status": 200, "stat": "ok"}

# @app.get("/nicodl/{sm}")
# def read_root(sm: int):
#     with NicoNico().video.get_video(f"https://www.nicovideo.jp/watch/sm{sm}") as video:
#         video.download(f"./temp/{video.video.id}.mp4")
#         return FileResponse(f"./temp/{video.video.id}.mp4")

# @app.get("/p/{id}")
# def read_root(id:int):
#     json_result = pixiv.illust_ranking()
#     for illust in json_result.illusts[:3]:
#         pixiv.download(illust.image_urls.large)
#     return "aaaaa"

# @app.get("/files")
# def read_root():
#     return glob.glob("./temp/*")


@app.get("/dblink")
def read_database():
    return os.getenv('mongourl')


@app.get("/db")
def read_database():
    client = MongoClient(os.getenv('mongourl'))
    db = client["chat"]
    collection = db["chat_data"]
    print(collection.find_one())
    return {"message": collection.find_one()["message"]}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


def start():
    uvicorn.run("main:app", host="0.0.0.0", port=443, reload=False)


if __name__ == "__main__":
    start()
