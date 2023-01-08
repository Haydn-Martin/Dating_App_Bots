import requests

cookies = {
    'session': 's4:101:oGUS8xK0oR7Fw0xZoeGiWmK5GSTuSv4FJsYx5wUa'
}

headers = {
    'Host': 'am1.bumble.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'x-use-session-cookie': '1',
    'Origin': 'https://am1.bumble.com',
    'Content-Length': '193',
    'Accept': '*/*',
    'Connection': 'close'
}

data = {
  "$gpb": "badoo.bma.BadooMessage" ,
  "message_type": 504 ,
  "version": 1 ,
  "message_id": 7 ,
  "object_type": 343 ,
  "body": [
    {
      "$gpb": "badoo.bma.MessageBody" ,
      "client_search_settings": {
        "$gpb": "badoo.bma.ClientSearchSettings" ,
        "context_type": 1 ,
        "current_settings": {
          "$gpb": "badoo.bma.SearchSettingsValues" ,
          "gender": [
            2
          ] ,
          "age": {
            "$gpb": "badoo.bma.SliderValue" ,
            "start": 19 ,
            "end": 28
          }
        }
      }
    }
  ]
}

response = requests.post("https://bumble.com/mwebapi.phtml?SERVER_GET_SEARCH_SETTINGS",
                         headers=headers,
                         cookies=cookies,
                         data=data)

print(response.text)
