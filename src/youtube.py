"""
Coded by @majhcc
"""
import re
def youtube_url_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match

    return youtube_regex_match

def download_youtube_video(url):
    if youtube_url_validation(url):
        from pytube import YouTube
        yt = YouTube(url)
        print(yt.streams.get_highest_resolution().url)
        print(yt.streams.get_lowest_resolution().url)
        print(yt.streams.get_audio_only().url)
        urls = {
            'audio': {
                'url' : yt.streams.get_audio_only().url,
                'size':str(( yt.streams.get_audio_only().filesize)/1000000) + 'MB'

            },
            'low': {
                'url':yt.streams.get_lowest_resolution().url,
                'size':str((yt.streams.get_lowest_resolution().filesize)/1000000) + 'MB'
                },
            'high':{
                'url':yt.streams.get_highest_resolution().url,
                'size':str((yt.streams.get_highest_resolution().filesize)/1000000) + 'MB'
            } ,
        }
        try: 
            return {
                'status': "ok",
                'title': yt.title,
                'thumbnail': yt.thumbnail_url,
                'formats': urls,
                "dev": "@majhcc"
            }
        except:
            return {
                'status': "error",
                'title': 'No title',
                'thumbnail': 'No thumbnail',
                'formats': 'No formats',
                "dev": "@majhcc"
            }
    else:
        return {
            'status': "error",
            'title': 'No title',
            'thumbnail': 'No thumbnail',
            'formats': 'No formats',
            "dev": "@majhcc"
        }
print(download_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
