from YouTube_tools import get_last_video_id_by_username
from src.random_str import get_random_str
from logging import debug
from unittest import result
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, PlainTextResponse, RedirectResponse, StreamingResponse
from pydantic import BaseModel
from typing import Optional
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic.types import Json
import requests
import json
import re




WEBHOOKURL = 'https://discord.com/api/webhooks/925364942511673354/uAGAVzxxLSQnM-VB3vJY2F9m8pAH2mUfANW0g86KO52h5PdmdVkgWtV9NtTKRuHJv0No'


description = """
# This is MAJHCC's  (Mohammed Aljahawri)   API helps you to do some cool stuffs.
<br>
[-] This API is still under development.<br>
[+] This API is working perfectly.<br>
[+] This API is Fast and Simple.<br>
[+] This API is Secure.<br>
[+] This API is Free.<br>
"""


limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="MAJHCC's API", description=description, version="0.2.3")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/", response_class=RedirectResponse)
def read_root():
    return RedirectResponse("/docs")
@app.get("/api/yt")
async def YouTube(url: str):
    """
    This can download videos from YouTube.<br>
    and it can also download audio from YouTube.<br>
    and it can also give you title and thumbnail of video from YouTube.<br>
    <pre>
    :param url: YouTube URL<br>
    :return: JSON <br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/yt?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
    </code>


    """
    from src.youtube import download_youtube_video
    return download_youtube_video(url)

@app.get("/api/tk")
async def TikTok(url: str):
    """
    This can download videos from TikTok.<br>
    and it can also download audio from TikTok.<br>
    <pre>
    :param url: TikTok URL either video or audio<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/tk?url=https://www.tiktok.com/@billieeilish/video/7014570556607433990
    </code>
    
    """
    from src.tiktok import getVideo
    json = getVideo(url)
    json['dev'] = "@majhcc"
    return json

@app.get("/api/twitter")
async def twitter(url: str):
    """
    This can download videos from Twitter.<br>
    <pre>
    :param url: Twitter video URL<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/twitter?url=https://twitter.com/AJArabic/status/1476130879437037569
    </code>
    """
    from src.twitter import download_twitter_video
    try:
        return download_twitter_video(url)
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}
@app.get("/api/tw")
async def Twitter_v2(url: str):
    """
    This also can download videos from Twitter but it's faster than Twitter v1.<br>
    <pre>
    :param url: Twitter video URL<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/tw?url=https://twitter.com/AJArabic/status/1476130879437037569
    </code>
    """
    from src.tweet import get_url_download
    try:
        # twitter url regex vailidation
        if re.match(r'https://twitter.com/[A-Za-z0-9_]+/status/[0-9]+', url):
            return get_url_download(url)
        else:
            return {"error": "Invalid URL"}
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}
@app.get("/api/BTC")
async def btc():
    """
    This give you the current price of Bitcoin.<br>
    <pre>
    :return: RAW<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/BTC
    </code>
    """
    from API.BTC import get_btc_price
    try:
        return get_btc_price()
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}



@app.get("/api/ETH")
async def eth():
    """
    This give you the current price of Ethereum.<br>
    <pre>
    :return: RAW<br>
    </pre>
    example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/ETH
    </code>
    """
    from API.ETH import get_eth_price
    try:
        return get_eth_price()
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}


class postvht(BaseModel):
    url : str
    s : Optional[str] = get_random_str(5)


@app.post("/api/vht")
async def vht(data : postvht):
    """
    This can shorten your URL using v.ht servise.<br>
    <pre>
    :return: JSON<br>
    </pre>
    example:<br>
    <br>
    <code>
    import requests</br>
    data = '{"url": "http://127.0.0.1:8000/docs#/default/vht_api_vht_post", "s": "DOdqQ"}'</br>
    response = requests.post('https://server1.majhcc.xyz/api/vht', data=data)
    <code/>
    """
    if data.url == None:
        return {"error": "Please enter a URL"}
    from src.v_ht import short_url
    try:
        return short_url(data.url , data.s)
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}



@app.get("/api/ip")
def ip(request: Request):
    """
    This returns your IP address.<br>
    <pre>
    :return: RAW<br>
    </pre>
    """
    client_host = request.client.host
    return {"ip": client_host}
@app.get("/api/fake-address")





def fake_address(request: Request):
    """
    This returns fake address.<br>
    <pre>
    :return: json<br>
    </pre>
    """
    from src.fake_add import fake_add
    try:
        return fake_add()
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}



@app.get('/api/downloader/auto')
def downloader_auto(url: str):
    """
    This can download videos from YouTube, TikTok, Twitter, and other websites.<br>
    <pre>
    :param url: URL<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/downloader/auto?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
    </code>
    """
    # regex youtube url
    try:
        if re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+', url):
            from src.youtube import download_youtube_video
            return download_youtube_video(url)
        # regex tiktok url
        elif re.match(r'(https?://)?(www\.)?(tiktok\.com|tiktok\.net)/.+', url):
            from src.tiktok import getVideo
            json = getVideo(url)
            json['dev'] = "@majhcc"
            return json
        # regex twitter url
        elif re.match(r'(https?://)?(www\.)?(twitter\.com|twitter\.net)/.+', url):
            from src.twitter import download_twitter_video
            return download_twitter_video(url)
        else:
            return {"error": "sorry this site is not available now please try to contact the developer @majhcc"}
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}



@app.get('/api/caller-id')
@limiter.limit("5/minute")
def caller_id(number, country_code, request: Request):
    """
    This can get caller id from any country.<br>
    <pre>
    :param number: Number<br>
    :param country_code: Country Code<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/caller-id?country_code=US&number=123456789
    </code>
    """
    from API.caller_id import get_names
    try:
        return get_names(number=str(number), country=country_code)
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}




@app.get('/api/google_search_results')
@limiter.limit("15/minute")
def google_search_results(query: str, request: Request):
    """
    This can get google search results.<br>
    <pre>
    :param query: Search Query<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/google_search_results?query=majhcc
    </code>
    """
    from src.google_search import get_google_results
    try:
        return {
            'status': 'success',
            'results': get_google_results(query)
            }
    except Exception as e:
        # send to webhook
        data = {
            "content": f"***{e}***"
        }
        requests.post(WEBHOOKURL, data=data)
        return {"error": "Something went wrong"}





@app.get('/api/get_last_videoid_youtube')
@limiter.limit("14/minute")
def get_last_videoid_youtube(channel_id: str, request: Request):
    """
    This can get last video id from YouTube channel.<br>
    <pre>
    :param channel_id: Channel ID<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/get_last_videoid_youtube?channel_id=UCfzuZdqkX2-jyNXRDGoOpNA
    </code>
    """
    from src.YouTube_tools import get_last_video_id_by_channel
    try:
        video_id = get_last_video_id_by_channel(channel_id)
        return {
        'status': 'success',
        "video_id": video_id
        }
    except Exception as e:
        # send error to webhook
        data = {
            'content': f'Get last video from youtube api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'}





@app.get('/api/get_last_videoid_youtube_by_username')
@limiter.limit("14/minute")
def get_last_videoid_youtube(username: str, request: Request):
    """
    This can get last video id from YouTube channel.<br>
    <pre>
    :param channel_id: Channel ID<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/get_last_videoid_youtube?channel_id=UCfzuZdqkX2-jyNXRDGoOpNA
    </code>
    """
    from src.YouTube_tools import get_last_video_id_by_username
    try:
        video_id = get_last_video_id_by_username(username)
        return {
        'status': 'success',
        "video_id": video_id
        }
    except Exception as e:
        # send error to webhook
        data = {
            'content': f'Get last video from youtube api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'}


@app.get('/api/news/rt')
def news_rt():
    from src.news.RT import get_news
    try:
        return {
            'status': 'success',
            'news': get_news()
            }
    except Exception as e:
        data = {
            'content': f'Get news from RT api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'}



@app.get('/api/news/bbc')
def news_bbc():
    from src.news.bbc import get_news
    try:
        return {
            'status': 'success',
            'news': get_news()
            }
    except Exception as e:
        data = {
            'content': f'Get news from BBC api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }



@app.get('/api/news/cnn')
def news_cnn():
    from src.news.CNN import get_news
    try:
        return {
            'status': 'success',
            'news': get_news()
            }
    except Exception as e:
        data = {
            'content': f'Get news from CNN api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }



@app.get('/api/news/fox')
def news_fox():
    from src.news.fox import get_news
    try:
        return {
            'status': 'success',
            'news': get_news()
            }
    except Exception as e:
        data = {
            'content': f'Get news from FOX api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }



@app.get('/api/news/nyt')
def news_nyt():
    from src.news.nyt import get_news
    try:
        return {
            'status': 'success',
            'news': get_news()
            }
    except Exception as e:
        data = {
            'content': f'Get news from NYT api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }



@app.get('/api/yt/dislike')
def yt_dislike(video_id: str):
    from API.youtubedislike import get_dislike
    try:
        return {
            'status': 'success',
            'dislike': get_dislike(video_id)
            }
    except Exception as e:
        data = {
            'content': f'Get dislike from youtube api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }



@app.get('/api/email/checker/google')
@limiter.limit("5/minute")
def email_checker_google(email: str, request: Request):
    from src.Emails.checker.gmail import create_random_call
    try:
        result = create_random_call(email)
        if result:
            return {
                'status': 'success',
                'result': 'Email is valid'
                }
        elif result == False:
            return {
                'status': 'success',
                'result': 'Email is invalid'
                }
        else:
            return {
                'status': 'error'
                }
    except Exception as e:
        data = {
            'content': f'Get email checker from google api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }



@app.get('/api/email/checker/microsoft')
@limiter.limit("5/minute")
def email_checker_microsoft(email: str, request: Request):
    from src.Emails.checker.hotmail import hotmail
    try:
        result = hotmail(email)
        if result:
            return {
                'status': 'success',
                'result': 'Email is valid'
                }
        elif result == False:
            return {
                'status': 'success',
                'result': 'Email is invalid'
                }
        else:
            return {
                'status': 'error'
                }
    except Exception as e:
        data = {
            'content': f'Get email checker from microsoft api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }




@app.get('/api/proxy/scrape/free-proxy-list')
@limiter.limit("5/minute")
def proxy_scrape_free_proxy_list(request: Request):
    """
    This API scrape proxies from free-proxy-list.com<br>
    <pre>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/proxy/scrape/free-proxy-list
    </code>
    """
    from src.proxy.scraper.free_proxy_list import get_list
    try:
        proxies = '\n'.join(get_list())
        return PlainTextResponse(proxies, media_type='text/plain')
    except Exception as e:
        data = {
            'content': f'Scrape proxy from free-proxy-list.com Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }




@app.get('/api/proxy/scrape/freeproxylistsnet')
@limiter.limit("5/minute")
def proxy_scrape_freeproxylistsnet(request: Request):
    """
    This API scrape proxies from freeproxylists.net<br>
    <pre>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/proxy/scrape/freeproxylistsnet
    </code>
    """
    from src.proxy.scraper.freeproxylistsnet import get_list
    try:
        proxies = '\n'.join(get_list())
        return PlainTextResponse(proxies, media_type='text/plain')
    except Exception as e:
        data = {
            'content': f'Scrape proxy from freeproxylists.net Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }



@app.get('/api/tk/getlastvideoid')
@limiter.limit("5/minute")
def tk_getlastvideoid(request: Request, username: str):
    """
    This API get last video id from tiktok<br>
    <pre>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/tk/getlastvideoid?username=edsheeran
    </code>
    """
    from src.tiktok_tools import get_last_video_id
    from src.tiktok import getVideo
    try:
        id_ = get_last_video_id(username)
        return {
            'status': 'success',
            'video_id': id_,
            'tiktok_url': f'https://www.tiktok.com/@{username}/video/{id_}',
            'download_url': getVideo(f'https://www.tiktok.com/@{username}/video/{id_}')['link']

            }
    except Exception as e:
        data = {
            'content': f'Get last video id from youtube api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
        'status': 'error'
        }



@app.get('/favicon.ico', include_in_schema=False)
def favicon():
    return FileResponse('static/favicon.ico')



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8011, debug=True)