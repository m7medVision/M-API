import requests
import re
def main(username):
    try:
        url = "https://www.snapchat.com/add/{}}".format(username)

        res = requests.get(url, headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        })
        snaps = re.findall(r'"snapUrls":{"mediaUrl":"(.*?)"', res.text)
        return {
            'status': True,
            "media": snaps 
            }
    except Exception as e:
        return {
            'status': False,
            'message': str(e)
            }