import requests
import os

def get_token():
    return os.getenv('TOKEN')
