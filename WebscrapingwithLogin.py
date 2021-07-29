from pathlib import Path
from bs4 import BeautifulSoup
import requests
from lxml import etree


with open("mylogin.txt") as file:
    # reader=file.read()  # To read content of a file
    # print(reader)
    # How read  username and password from an external file
    reader = file.read().split("\n")
    username = reader[0]
    password = reader[1]

payload = {
    "wpName": username,
    "wpPassword": password,
    "wpLoginattempt": "Log in",
    "wpEditToken": "+\\",
    "title": "Special:UserLogin",
    "authAction": "login",
    "force": "",
    "wpForceHttps": "1",
    "wpFromhttp": "1",
    #  "name":"captchaWord"
    #  "wpLoginToken":""

}


def get_login_token(responses):
    soup = BeautifulSoup(responses.text, "lxml")
    token = soup.find("input", {"name": "wpLoginToken"}).get("value")
    return token


def get_login_captcha(responses):
    soup = BeautifulSoup(responses.text, "lxml")
    captcha = soup.find("input", {"name": "mw-input-captchaId"}).get("value")
    return captcha


with requests.session() as s:  # The Session works like requests.get to  and continually check the response code
    responses = s.get(
        "https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")

    # from the function above once a response is sent and a token is generated  this function extract and send it into the dictionry
    payload["wpLoginToken"] = get_login_token(responses)
    payload["captchaId"] = get_login_token(responses)
    responses_post = s.post("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&action=submitlogin&type=login", data=payload
                            )
    responses = s.get(
        "https://en.wikipedia.org/wiki/Special:Watchlist")
    print(responses)
    soup1 = BeautifulSoup(responses.content, "lxml")
    print(soup1.find("div", {"id": "mw-content-text"}).get_text())
