import requests

url = "https://pearvideo.com/video_1752360"
contId = url.split("_")[1]
videoStatus = "https://video.pearvideo.com/mp4/short/20220221/cont-{contId}-15829286-hd.mp4"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36 ",
    # 在头部设置防盗链
    "Referer": "https://pearvideo.com/video_1752360"
}

resp = requests.get(videoStatus, headers=headers)
print(resp.json())
