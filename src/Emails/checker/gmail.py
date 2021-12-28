import requests
import re
import time
import random
from time import gmtime



def getCookiesOfGoogle():
    heasers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    }
    res = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=heasers)
    fr = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res.text).group(2)
    try:
        cookies_part1 = res.cookies['__Host-GAPS']
    except:
        cookies_part1 = '1:q1E2omQYraJ3qfa8iU1dcSUEFHyXqw:kKD-9BOOjjgWCMZv'
    # if cookies_part1 start with '1':
    if cookies_part1.startswith('1:'):
        pass
    else:
        cookies_part1 = '1:q1E2omQYraJ3qfa8iU1dcSUEFHyXqw:kKD-9BOOjjgWCMZv'
    timenow = time.strftime("%H:%M:%S", gmtime())+ " GMT"
    year = time.strftime("%Y", gmtime())
    year = str(int(year) + 2)
    month = time.strftime("%b", gmtime())
    day = time.strftime("%d", gmtime())
    cookies = f'__Host-GAPS={cookies_part1};Path=/;Expires=Sat, {day + "-"+ month+ "-"+ year + " "+ timenow};Secure;HttpOnly;Priority=HIGH'
    return cookies, fr




def get_random_name():
    f = open('names.txt', 'r')
    lines = f.readlines()
    f.close()
    name = random.choice(lines).replace('\n', '').replace('\r', '').replace(' ', '')
    lastname = random.choice(lines).replace('\n', '').replace('\r', '').replace(' ', '')
    return name, lastname






def gmail_call_n1(username):
    name, lastname = get_random_name()
    cookies, fr = getCookiesOfGoogle()
    headers = {
        'authority': 'accounts.google.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'x-same-domain': '1',
        'dnt': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'google-accounts-xsrf': '1',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=6345dd7f-ea9b-4902-84f5-bd97a0e8f849,sync_account_id=101117672224618069553,signin_mode=all_accounts,signout_mode=show_confirmation',
        'origin': 'https://accounts.google.com',
        'x-client-data': 'CJe2yQEIpLbJAQjBtskBCKmdygEIw4LLAQjq8ssBCJ75ywEI1vzLAQjnhMwBCLWFzAEIy4nMAQitjswBCNKPzAEI2ZDMARiOnssB',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://accounts.google.com/signin/v2/queryname?flowName=GlifWebSignIn&flowEntry=ServiceLogin',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cookie': cookies,
    }
    params = (
        ('hl', 'en'),
        ('_reqid', '41999'),
        ('rt', 'j'),
    )

    data = {
    'flowEntry': 'ServiceLogin',
    'flowName': 'GlifWebSignIn',
    'continue': 'https://accounts.google.com/ManageAccount?nc=1',
    'f.req': '["'+ username +'","' + fr +'",[],null,null,"' + name + '","' + lastname + '",1,false,null,[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin?flowName=GlifWebSignIn&flowEntry=ServiceLogin",null,[],4,[],"GlifWebSignIn",null,[],true],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"6345dd7f-ea9b-4902-84f5-bd97a0e8f849",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,true,null,null,null,null,null,null,null,null,[]],null,null,null,null,null,null,[]]',
    'bgRequest': '["username-recovery","<RYlqicQCAAa4w6ckuMON5FroRgBJhIf0ACkAIwj8RndYlbIWPRlr08Ezk_CvyHmv5jG9T4Lc_552zQzX0-aVEqbPwM0AAAV7nQAAAB6nAQdWCUTNiJHxDT4J-RNTrgsxBuryc5N6KkenKZjfaPjWSRFD0YUc3PYbxVa6ow_B9RjZYpHaDMb4WyOwyTTqNqChgujpsfZpZArXu_RFe7XgzuDMz6flHKKKYDRkGhAIzdj8LWvN3F2WIgVbqKKF66AThrqoyYKAZm87-lu2nvqI18okH2Qp1OoLjkx7VkXPImSVxfqVzMte2wWwqjs4KSI9nQfuiCJs3_KqmZu10B5a-4KzhZPJ6nXXv_kVOPoEc0MGjWHRNMJP96YWYoaOT2Hhoq7Z11aNXl5krxHTOILAjqlbOhJrCC59QnAnQeST2s26RArTrf1b2pA9qoL58xCFWdTe72wBseAsYdD5iEoq_X8KTryxbj2d5wGcFhYUOsRNNMKiK8_Z1pcZHyxJfoBo74tTNcSFg-sgbBsMA5f7Nh2ObpIEU_hE3vTOdYpaWGP_hdYwFcK93OeW9P-t7WDJtRt2dm1q_e6GBZv_kncyjV9c-FYELnYfBtwI4wc6t3a595Tsp3H9xL7dzGVcOwN1lG9P-yWilQuwNiO8dwsRTzPsPLv8ThZ5cq-Sc5lMRamyJYnwqBiO-EIDZx9VKpGYhXC0PTmzOsOl7K1BaGlxCZTCWw1joNKBJl0uUj-NkaOfuS9Hssk5HluPCANjcFMl4hxd-PQQzAewSp2MrcvfvjmO9j55N9eTGlZfYXsFobMWa9-gGoKsfYTC-lxg4ij_rY6LT1zEvlL_Cr5dZ1SRy8-jN7lW7DRf1sf-_Q_z2rZ62qC66tXiJBxriuqK7yddiQkgH73tFW9-x9ecc6_1ipSeaA1PlCOBL1-VDYRZ5HDHmyyQjSjDlT3UL2CsCI-6gDoZ78i_fAo8i6aEl9jmwlxNdBMYowxtLe_v4T7T4jHMCrhNiqpceYNHAdn_DHBQ6YIYXZC6PPGhfy7yA6jimQpZh73apI67wMY3Xw-A_-TB_HcPHoEEj0YoFxDhrY89dWp80cwTh9u-XjVkTU5D2l3aRPEbbWWBObjmhODGmUz6OPdDI6Mwdu_h_q6ORSErQEvqFwlmFpU5uDY-zddpcp-BH6jece8acBmzeOSY0xE0e44myd1OKzvzA02LhNrpACLw3HLIjnPMrTv6T1F0QeMeILvpkiQMfaOYoP-GA-RRAiXyfpPNipmYhrok8Bcol933pE-VaDmD56DEaaNkpq29iQgyCCuEI_ZdkVkDb-U6W0rHQgJDYZ_Q7onum_Cp1UlTBCbkUKC1HXK8nJTMOzeqDklW5LoUq1M_XVahtCTlud28uEghu3BLx01ISLyBqIcYXosMZNCBT0RNvkIZ6gJFQA-ytx-4-x5sQRtZcWM57bEpcVW75iYeReA2KM0IYpvQ6T5aI_GGJ4RSCyU_wIfNxJzYCl6XKOMZRL2ubRq-duThIi2urzW3eqGqeyMcvFZ12-oIDwI1ryduudNxUczUwtl2nBArTv2y7fXldVUmHh3JE9OXlx1n4gzUXxztoYNkBcDzC-NldTrlDFM7N_LXLYtqXZI8GNWu5FTRPXu_8OnlEcX4iV6w595KS0FDoIhsod5pjokcGAjsJqfo-1nHbwHFJAHIX2cHmHITHQExwwKT1KoAzI186O2SdhjSGJHKZf9ti9ps3xr4cGNAQ5J7JkGso1IH2TKbO2Nt_J5nFPuHQuf4KAAVLjwDxMfX7ntQ315aYbJh1GSqyrS2XqB68QI0Q6_pg5Q40CsN0ogqm0zRSxkSiQ879RDPxo7MLavboQmsDATseVVKGiH1TQ-e89ShwfuXMrLE3QjchkcfsO01MM7AUq5JP3o54qDHK6RPWh3-2rNvmRpwpGD-IdHVaPm84lfBC_7BgHFcpesA4riBknZ0W42DtKEtWkCkrnvQqjGB_ULDFZTvhE8oY6Sxxv_Ht2e57CErukp7oCSdAR3emkDkqAlQXpqOyt8Aeg4Sm2U_QTAJiVg-YD5dAAf1R32d5-sFGKgbvxt2k1s8xdMIjKTSJxdhzj5ciuagcntq2jWuCws_kNENzXoWNOcd5n0Ajy4W72cmLLLn8WYLAOSd6Aq1b-cJMKJnRT0f81-DawFkXMwYbpjaW66gwCVa3-iZAlyPgpEPNymQuo_nDmea3UpaNz7zK8yCuxA0sz9fWTqRD7sdhccr6ZEAEd-BXyGDa7erAY6e2Df0XDlVkq9ucjIdbxLznY6gK6VFXLQK_57bdDXlg94OebeEThwzAhNlRMoepIYyI7fd-om_qhJlNnal0frjNsntR3_9eBl-AHHJL06vgOeVeGPFs0ysEOfG_oS8KU-1wjqwK3qKqGONW_s4DmTQ77qrWXDePUg5nygZWQqp2Pe-QCKcE0w5oN0WCriqsQwG8mZQdfuAJC8AxdqUCb50TbWjLYcb3_6eBAgmoHNHUmB0iV374kE-pZjKqXeAlcQTmakrGkOk3Yk5tsntz3vHoN2yZyMs6v6SgwiVSqugz_cjSLQP1PHxBTQiG3fJt2M47VfUKlz0ku0LqIbhBvUX-JWQkoJi3BcFAmo7cQsFdA9teo9kjMHpqOz8puDijlwgkW2vMpxDsIC_ErxuOHjiNe8TldWccVttpOi_lBvDQjJbg1Hc4qOz_w1TuefsUfad5nzjBqzAqs8IqjU5e4ndfLK_Mn8xyS_OLVX6qPWCCO7Q8Zcw0Mraba7fdVyRIxmsVl3bMcFB1xV1Dqt4fKlR9ouHEpPAJpbVw0wAQfr2iSMEKkpWDlSSB4xd37GvbCKZvI2bx5U-msNrJ3YlDOkZWY8irD7DRmXKZnf-wOtZ_S2xEVtRdvRSQH-EcBjwVKT_mO5XySDjeFqldUySAkI75so3wXeORamVFdJhJQaECij2pBEb4IOaWR6Lq2k7H3dASdh_4cn5VWU8JjqaKONgpvNLxmvCYKaLfZLyRSCOG52ZxgnFU5GgOBeI2eH0Np_57n48rD20iIwfSiwcsaPB3TFDvY7PGgEhh-mC1jFK6TAFCWnZ2zLtiaJCGxc-cUeXdjtDKtbSOqpI5_BFz6_4gJ444qOta1jf_2SgM3yBKxn6oJ3L7mo7kNaTR2ITwXQDiUG236YnVY5ECQTO7yF_u8KFSI6eYDwCPP4a5LvEb4trcUaR3NEjhIuwCIY0rzSQDQablifNL8z6HUIeJxZCVg0i18n3AEFWQHQ_og"]',
    'at': 'AFoagUU3nZjawuiFGbY2_H10oI3vbd7PJg:1639640369692',
    'azt': 'AFoagUUN1-K40newvTjWfwoozm-fzHiqPw:1639640369692',
    'cookiesDisabled': 'false',
    'deviceinfo': '[null,null,null,[],null,"DE",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"6345dd7f-ea9b-4902-84f5-bd97a0e8f849",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
    'gmscoreversion': 'undefined',
    'checkConnection': 'youtube:474:0',
    'checkedDomains': 'youtube',
    'pstMsg': '1'
    }

    response = requests.post('https://accounts.google.com/_/lookup/accountlookup', headers=headers, params=params, data=data)
    if ',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]' in response.text:
        return False
    else:
        return True






def gmail_call_n2(username):
    cookies, fr = getCookiesOfGoogle()
    username = username.replace('@gmail.com', '')
    headers = {
    'authority': 'accounts.google.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'x-same-domain': '1',
    'dnt': '1',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'origin': 'https://accounts.google.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fprogrammatic_auth%3Fclient_id%3D1070009224336-sdh77n7uot3oc99ais00jmuft6sk2fg9.apps.googleusercontent.com%26scope%3Dhttps%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%26access_type%3Doffline%26set_oauth_token_cookie%3Dtrue%26from_login%3D1%26as%3DjKaTwe7YDwCP-UXB2d8_7UNEiXJZK0ypPavA-Fu7kss&ltmpl=embedded&hl=en&dsh=S-352068999%3A1639823292967746&parent_directed=true&flowName=GlifWebSignIn&flowEntry=SignUp',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': cookies,
    }


    params = (
        ('hl', 'en'),
        ('_reqid', '52253'),
        ('rt', 'j'),
    )


    data = {
    'continue': 'https://accounts.google.com/o/oauth2/programmatic_auth?client_id=1070009224336-sdh77n7uot3oc99ais00jmuft6sk2fg9.apps.googleusercontent.com&scope=https://www.google.com/accounts/OAuthLogin&access_type=offline&set_oauth_token_cookie=true&from_login=1&as=jKaTwe7YDwCP-UXB2d8_7UNEiXJZK0ypPavA-Fu7kss',
    'flowEntry': 'SignUp',
    'flowName': 'GlifWebSignIn',
    'hl': 'en',
    'ltmpl': 'embedded',
    'dsh': 'S-352068999:1639823292967746',
    'f.req': f'["{fr}","","","{username}",true,"S-352068999:1639823292967746",1]',
    'azt': 'AFoagUW-Tb1mBoWdsusqEN3OlNTSONNG6g:1639823409156',
    'cookiesDisabled': 'false',
    'deviceinfo': '[null,null,null,[],null,"DE",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
    'gmscoreversion': 'undefined'
    }

    response = requests.post('https://accounts.google.com/_/signup/webusernameavailability', headers=headers, params=params, data=data)
    if '[[["gf.wuar",1,[]],["e",2,null,null,47]]]' in response.text:
        return False
    else:
        return True




def create_random_call(email):
    x = random.randint(1, 2)
    if x == 1:
        try:
            return gmail_call_n1(email)
        except:
            return gmail_call_n2(email)
    else:
        try:
            return gmail_call_n2(email)
        except:
            return gmail_call_n1(email)