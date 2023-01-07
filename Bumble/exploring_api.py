import requests

cookies = {
    'session': 's4:101:jkEZWi24GjdbsFANE2Esdk8iDJQJbmOwYqOIOGmh'
}

headers = {
    'Host': 'am1.bumble.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Content-Type': 'text/html',
    'x-use-session-cookie': '1',
    'Origin': 'https://am1.bumble.com',
    'Referer': 'https://am1.bumble.com/app',
    'Content-Length': '342',
    'Accept': '*/*'
}

response = requests.get("https://bumble.com/mwebapi.phtml?SERVER_GET_USER_LIST",
                         headers=headers,
                         cookies=cookies,
                         timeout=10)
print(response.headers)
