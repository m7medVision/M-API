import requests
import json


def get_names(number, country):
#     try:
#         url = f"https://devappteamcall.site/data/search_name?country={country}"
#         payload = {
#             'phoneNumber': number
#         }
#         headers = {
#             'Authorization': 'Basic YWEyNTAyOnp1enVBaGgy',
#             'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/QP1A.190711.020)',
#             'Host': 'devappteamcall.site',
#             'Connection': 'Keep-Alive',
#             'Accept-Encoding': 'gzip',
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'Content-Length': '21',
#         }
#         response = requests.post(url, headers=headers, data=payload)
#         id_s = response.json()['result']
#         jsona = json.loads(id_s)
#         naMes = []
#         for i in jsona:
#             naMes.append(i['Name'])
#         return {
#             'status': 'success',
#             'names': naMes
#         }
#     except:
#         return {
#             "error": "Something went wrong",
#             'error_code': '500'
#         }
    return {
        "error": "This service is not available",
    }
