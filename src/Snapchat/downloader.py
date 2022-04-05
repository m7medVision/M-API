import requests
from lxml import html
import re


def main(username):

    try:
        media = []
        res = requests.get(
            f'https://a7.ae/snapchat/index.php?snap={username}&page=1')
        tree = html.fromstring(res.content)
        try:
            if tree.xpath('//div[@class="alert-warning alert"]')[0].text == "عذراً لا توجد نتيجة لبحثك .. اسم المُستخدم خاطئ":
                return {
                    "status": False,
                    "message": "Username not found"
                }
        except:
            pass
        number_of_pages = tree.xpath(
            '/html/body/center/ul/li/a')[-1].xpath('@href')[0]
        media.extend(tree.xpath(
            '//td/span/img/@src | //td/span/video/source/@src'))
        max_number_of_pages = re.search(
            r'index.php\?snap=(.*)&page=(.*)', number_of_pages).group(2)

        for i in range(2, int(max_number_of_pages) + 1):
            res = requests.get(
                f'https://a7.ae/snapchat/index.php?snap={username}&page=' + str(i))
            tree = html.fromstring(res.content)
            media.extend(tree.xpath(
                '//td/span/img/@src | //td/span/video/source/@src'))
        return {
            "status": True,
            "media": media
        }

    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }


print(main('hatanbado'))
