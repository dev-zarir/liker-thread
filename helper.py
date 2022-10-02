from requests import post
from time import sleep
from urllib.parse import quote_plus

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

proxies = [
    "https://selenium-liker.onrender.com",
    "https://selenium-liker-1.onrender.com",
    "https://selenium-liker-2.onrender.com",
    "https://selenium-liker-3.onrender.com",
    "https://selenium-liker-4.onrender.com",
]


def liker_machine(react, post_id, cookie):
    # Proxy Count
    pc = 0
    loop = True
    while loop:
        try:
            resp = post(
                proxies[pc] + '/send',
                headers=headers,
                data=f'react={react}&post_id={post_id}&cookie={quote_plus(cookie)}',
                timeout=5*60,
            )
            result = resp.json()
        except:
            pc += 1
            if pc > (len(proxies)-1):
                loop = False
            continue
        if not result['success']:
            if 'Could not solve Captcha' in result['msg']:
                pc += 1
                if pc > (len(proxies)-1):
                    loop = False
                continue
            elif 'Remaining Time' in result['msg']:
                sleep(2*60)
            else:
                loop = False
        else:
            loop = False


