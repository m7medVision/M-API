from bs4 import BeautifulSoup
import re
import ast
import requests
# suonubutt
def check_username(username):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
        'TE': 'trailers',
    }
    res = requests.get('https://api.brandsnag.com/api/social-media/username-available-by-source?username={}&source=tiktok'.format(username) , headers=headers)
    try:
        json_res = res.json()
        if json_res['success']:
            return json_res['data']['tiktok']
        else:
            return False
    except:
        return "ERROR"


def get_last_video_id(username):
    """
    Get the last video id from a user's profile page.
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        }

    response = requests.get('https://www.tiktok.com/@{}'.format(username), headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    lastvideoid = ast.literal_eval("["+re.search(r'"ItemList":{"user-post":{"list":\[(.*?)\]', soup.find_all('script')[5].text.strip().replace('window[\'SIGI_STATE\']=', '')).group(1)+"]")[0]
    return lastvideoid


def get_account_info(username):
    """
    Get account info
    it return name, bio
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    res = requests.get('https://www.tiktok.com/@{}'.format(username), headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    script_codes = soup.find_all('script')[5].text.strip().replace('window[\'SIGI_STATE\']=', '')

    regex_res = re.search(r'"authorStats":(.*?),"privateItem":', script_codes)
    json_return = ast.literal_eval(regex_res.group(1))

    name = re.search(r'nickname":"(.*?)","author', script_codes)
    json_return['name'] = name.group(1)

    bio = re.search(r'"signature":"(.*?)"', script_codes)
    json_return['bio'] = bio.group(1)
    
    some_video_ids = ast.literal_eval("["+re.search(r'"ItemList":{"user-post":{"list":\[(.*?)\]', soup.find_all('script')[5].text.strip().replace('window[\'SIGI_STATE\']=', '')).group(1)+"]")
    json_return['some_video_ids'] = some_video_ids

    return json_return
