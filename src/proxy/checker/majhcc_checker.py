# proxy checker
import requests
import re
def regex_proxy(proxy):
    if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$', proxy):
        return True
    else:
        return False
def checker(proxy, timeout=50, url='https://www.google.com/'):
    if regex_proxy(proxy):
        proxies = {'http': 'http://' + proxy,
                'https': 'https://' + proxy,
                'ftp': 'ftp://' + proxy}
        try:
            if requests.get(url, proxies=proxies, timeout=timeout).status_code == 200:
                return True, 'good proxy'
            else:
                return False, 'bad proxy'
        except:
            return False, 'Timeout'
    else:
        return False, 'Invalid proxy format'