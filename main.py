from logging import debug
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

description = """
This is MAJHCC's(Mohammed Aljahawri) API helps you to do some cool stuffs.

[-] This API is still under development.
[+] This API is working perfectly.
[+] This API is Fast and Simple.
[+] This API is Secure.
[+] This API is Open Source.
[+] This API is Free.

"""


app = FastAPI(
    title="MAJHCC",
    description=description,
    version="0.2.0",
    contact={
        "name": "Mohammed Al-jahwari",
        "url": "https:/majhcc.pw/",
        "email": "admin@majhcc.pw",
    })
from src.random_str import get_random_str

@app.get("/")
def read_root():
    return {"dev": "@majhcc", 
            "profiles": {
                "twitter": "https://twitter.com/majhcc",
                "github": "https://github.com/majhcc",
                "instagram": "https://instagram.com/majhcc",
                "website": "https://majhcc.pw"
            },
            "version": "0.0.5"  
            }  

@app.get("/api/yt")
async def YouTube(url: str):
    """
    This can download videos from YouTube.
    and it can also download audio from YouTube.
    and it can also give you title and thumbnail of video from YouTube.

    """
    from src.youtube import download_youtube_video
    return download_youtube_video(url)

@app.get("/api/tk")
async def TikTok(url: str):
    """
    This can download videos from TikTok.
    and it can also download audio from TikTok.
    
    """
    from src.tiktok import getVideo
    json = getVideo(url)
    json['dev'] = "@majhcc"
    return json

@app.get("/api/twitter")
async def twitter(url: str):
    """
    This can download videos from Twitter.
    """
    from src.twitter import download_twitter_video
    return download_twitter_video(url)

@app.get("/api/tw")
async def Twitter_v2(url: str):
    """
    This also can download videos from Twitter but it's faster than Twitter v1.
    """
    from src.tweet import get_url_download
    return get_url_download(url)

@app.get("/api/BTC")
async def btc():
    """
    This give you the current price of Bitcoin.
    """
    from API.BTC import get_btc_price
    return get_btc_price()

@app.get("/api/ETH")
async def eth():
    """
    This give you the current price of Ethereum.
    """
    from API.ETH import get_eth_price
    return get_eth_price()

@app.post("/api/vht")
async def vht(url : str, s : str = get_random_str(5)):
    """
    This can shorten your URL using v.ht servise.
    """
    from src.v_ht import short_url
    return short_url(url, s)

@app.get("/api/ip")
def read_root(request: Request):
    """
    This returns your IP address.
    """
    client_host = request.client.host
    return {"ip": client_host}

@app.get('/favicon.ico', include_in_schema=False)
def favicon():
    return FileResponse('static/favicon.ico')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8011, reload=True)