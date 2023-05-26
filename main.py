import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from niconico import NicoNico
import glob
import os
from pixivpy3 import *

app = FastAPI(
    title='ms'
)

pixiv = AppPixivAPI()
pixiv.auth(refresh_token="ここにリフレッシュトークン")

@app.get("/")
def read_root():
    return "Hello World! Please docs --> https://github.com/KuritaMasaya/ms"

@app.get("/foo")
def read_root():
    return {"foo": "bar"}

@app.get("/nicodl/{sm}")
def read_root(sm: int):
    with NicoNico().video.get_video(f"https://www.nicovideo.jp/watch/sm{sm}") as video:
        video.download(f"./temp/{video.video.id}.mp4")
        return FileResponse(f"./temp/{video.video.id}.mp4")

# @app.get("/p/{id}")
# def read_root(id:int):
#     json_result = pixiv.illust_ranking()
#     for illust in json_result.illusts[:3]:
#         pixiv.download(illust.image_urls.large)
#     return "aaaaa"

@app.get("/files")
def read_root():
    return glob.glob("./temp/*")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

def start():
    uvicorn.run("main:app", host="0.0.0.0", port=443, reload=False)


if __name__ == "__main__":
    start()