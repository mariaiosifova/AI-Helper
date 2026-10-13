import requests
import os
from dotenv import load_dotenv 
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_access_key():
    load_dotenv()

    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload={
    'scope': 'GIGACHAT_API_PERS'
    }

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '95c3c340-aaef-4f8a-8139-a852ef2640fb',
    'Authorization': f'Basic {os.getenv("AUTHORIZATION_KEY")}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return response


def get_models_list():
    url = "https://api.giga.chat/v1/models"

    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {get_access_key().json()["access_token"]}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)

if __name__ == '__main__':
    get_models_list()