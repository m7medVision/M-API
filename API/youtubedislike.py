import requests

def get_dislike(video_id):
    url = 'https://returnyoutubedislikeapi.com/votes?videoId=' + video_id
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return r.json()['dislikes']
