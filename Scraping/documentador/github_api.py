import requests
from config import HEADERS


def fazerGet(path):

    response = requests.get(
        path,
        headers=HEADERS
    )

    response.raise_for_status()

    return response.json()


def acessar_arquivo(url):

    response = requests.get(
        url,
        headers=HEADERS
    )

    response.raise_for_status()

    return response.text