from niconico import NicoNico

with NicoNico().video.get_video(f"https://www.nicovideo.jp/watch/$VideoIDhere") as video:
        video.download(f"./temp/{video.video.id}.mp4")