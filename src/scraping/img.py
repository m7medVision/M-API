import re
import requests

def main(url):
    res = requests.get(url)
    html = res.text
    images = []
    for img in re.findall(r'(https?:\/\/.*\.(?:png|jpg))', html):
        images.append(img)
    return images
