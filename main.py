from src.random_str import get_random_str
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, PlainTextResponse, RedirectResponse
from pydantic import BaseModel
from typing import Optional
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import requests
import re
import os
from fastapi.middleware.cors import CORSMiddleware

WEBHOOKURL = os.environ.get('WEBHOOKURL')
description = """
# This is M-API helps you to do some cool stuffs.
<br>
[-] This API is still under development.<br>
[+] This API is working perfectly.<br>
[+] This API is Fast and Simple.<br>
[+] This API is Secure.<br>
[+] This API is Free.<br>
"""


limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="MAJHCC's API", description=description, version="0.5.3")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=RedirectResponse)
def read_root():
    return RedirectResponse("https://محمد-الجهوري.شبكة")


@app.get("/api/tk", tags=['downloading'])
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
    from src.tiktok.tiktok import getVideo
    json = getVideo(url)
    json['dev'] = "@majhcc"
    return json


@app.get("/api/twitter", tags=['downloading'])
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


@app.get("/api/BTC", tags=["crypto"])
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


@app.get("/api/ETH", tags=["crypto"])
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
    url: str
    s: Optional[str]


@app.post("/api/vht")
async def vht(data: postvht):
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
    if data.s == None:
        s = get_random_str(5)
    from src.v_ht import short_url
    try:
        return short_url(data.url, s)
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


@app.get('/api/news/rt', tags=['news'])
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


@app.get('/api/news/bbc', tags=['news'])
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


@app.get('/api/news/cnn', tags=['news'])
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


@app.get('/api/news/nyt', tags=['news'])
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


@app.get('/api/yt/dislike', tags=['youtube'])
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


@app.get('/api/email/checker/google', tags=['Emails'])
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


@app.get('/api/email/checker/microsoft', tags=['Emails'])
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


@app.get('/api/proxy/scrape/free-proxy-list', tags=['proxy'])
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


@app.get('/api/proxy/scrape/freeproxylistsnet', tags=['proxy'])
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


@app.get('/api/tk/check_user_exist')
@limiter.limit("5/minute")
def tk_check_user_exist(request: Request, username: str):
    """
    This API check user exist from tiktok<br>
    <pre>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/tk/check_user_exist?username=edsheeran
    </code>
    """
    from src.tiktok.tiktok_tools import check_username
    try:
        exist = check_username(username)
        return {
            'status': 'success',
            'available': exist
        }
    except Exception as e:
        data = {
            'content': f'Check user exist from tiktok api Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
            'status': 'error'}


@app.get('/api/email/checker/mailru')
@limiter.limit("5/minute")
def email_checker_mailru(request: Request, email: str):
    """
    This API check email from mail.ru<br>
    <pre>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/email/checker/mailru?email=oman4omani@mail.ru
    """
    from src.Emails.checker.mailru import checker
    # regex mail.ru
    if re.match(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]@mail\.ru', email):
        try:
            result = checker(email)
            if result:
                return {
                    'status': 'success',
                    'available': True
                }
            elif not result:
                return {
                    'status': 'success',
                    'available': False
                }
            elif result == None:
                return {
                    'status': 'error please try again or contact us ==> instagram: @majhcc'
                }
            else:
                return {
                    'status': 'error please try again or contact us ==> instagram: @majhcc'
                }
        except Exception as e:
            data = {
                'content': f'Check email from mail.ru api Error: ***{str(e)}***'
            }
            requests.post(WEBHOOKURL, data=data)
            return {
                'status': 'error please try again or contact us ==> instagram: @majhcc'}
    else:
        return {
            'status': 'error',
            'result': 'Invalid email'
        }


@app.get('/api/meaning/ar')
def ar_meaning(name: str):
    from src.names.meaning.ar.main import get_meaing
    return get_meaing(name)


@app.get('/api/dl/yt')
def dl_yt(url: str):
    from src.Youtube.youtube import get_info
    try:
        resopnses = get_info(url)
        return resopnses
    except Exception as e:
        data = {
            'content': f'Download youtube video Error: ***{str(e)}***'
        }
        requests.post(WEBHOOKURL, data=data)
        return {
            'status': 'error'
        }


@app.get('/api/snapchat')
def snapchat(username: str):
    from src.Snapchat.downloader import main
    return main(username)


@app.get('/favicon.ico', include_in_schema=False)
def favicon():
    return FileResponse('static/favicon.ico')
