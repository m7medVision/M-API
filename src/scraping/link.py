import re
import requests

def main(url):
    res = requests.get(url)
    html = res.text
    urls = []
    for url in re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', html):
        urls.append(url)
    return urls

