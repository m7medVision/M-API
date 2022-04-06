from yt_dlp import YoutubeDL
import re
def check_url(url):
    regex = re.compile(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.be)\/.+$')
    if regex.match(url):
        return True
    else:
        return False
def get_info(url):
    if check_url(url):
        with YoutubeDL() as ydl:
            jsonres = []
            for i in ydl.extract_info(url, download=False)['formats']:
                js1 = {}
                try:
                    js1['format'] = i['format']
                except:
                    js1['format'] = "None"
                try:
                    js1['ext'] = i['ext']
                except:
                    js1['ext'] = "None"
                try:
                    js1['url'] = i['url']
                except:
                    js1['url'] = "None"
                try:
                    js1['filesize'] = i['filesize']
                except:
                    js1['filesize'] = "None"

                jsonres.append(js1)
            return {  
                'status': 'success',
                'result':jsonres
                }
    else:
        return {'status': 'error', 'message': 'Invalid URL'}
    
