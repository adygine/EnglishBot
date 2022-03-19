import requests
import os

url = 'https://quizlet.com/'
api = 'https://quizlet.com/webapi/3.2/terms/'

headers = {
    'accept' : '*/*',
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

def auth() -> dict:
    """Autorithation"""
    return requests.get(url=url, auth=(os.getenv('USER'), os.getenv('PASSWORD'))).json()

def save() -> dict:
    """Save words"""
    return requests.post(api+'save?_method=PUT', headers=headers).json()