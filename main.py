from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"dev": "@majhcc", 
            "profiles": {
                "twitter": "https://twitter.com/majhcc",
                "github": "https://github.com/majhcc",
                "instagram": "https://instagram.com/majhcc",
                "website": "https://majhcc.pw"
            },
            "version": "0.0.1"  
            }  

@app.get("/api/yt")
async def YouTube(url: str):
    from src.youtube import download_youtube_video
    return download_youtube_video(url)

@app.get("/api/tk")
async def TikTok(url: str):
    from src.tiktok import getVideo
    json = getVideo(url)
    json['dev'] = "@majhcc"
    return json

@app.get("/api/twitter")
async def twitter(url: str):
    from src.twitter import download_twitter_video
    return download_twitter_video(url)

@app.get("/api/tw")
async def Twitter_v2(url: str):
    from src.tweet import get_url_download
    return get_url_download(url)

@app.get("/api/BTC")
async def btc():
    from API.BTC import get_btc_price
    return get_btc_price()

@app.get("/api/ETH")
async def eth():
    from API.ETH import get_eth_price
    return get_eth_price()

@app.get("/api/vht")
async def vht(url : str):
    from src.v_ht import short_url
    return short_url()
