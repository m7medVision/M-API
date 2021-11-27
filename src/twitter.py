import youtube_dl
import re
def twitter_url_validation(url):
    if re.match(r'^https?://twitter.com/', url):
        return True
    else:
        return False
def download_twitter_video(url):
    if twitter_url_validation(url):
        download = False 
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ie_result = ydl.extract_info(url, download)
            try:
                return {
                    'status': "ok",
                    "url" : ie_result["url"],
                    "dev": "@majhcc"}
            except:
                return {"error" : "Contact with the developer @majhcc"}
            
    else:
        return {'status': "error",
            "error" : "Not a valid Twitter URL"}
# print(download_twitter_video("https://twitter.com/ISSAHINAI1990/status/1461927197753630723?s=20"))