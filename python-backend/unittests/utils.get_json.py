#!/usr/bin/env python3
import requests

def get_json(url):
    """
    Retrieves JSON data from a given URL.

    :param url: The URL to fetch the JSON data from.
    :return: The JSON data parsed into a Python dictionary.
    :raises requests.RequestException: If the request fails.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

from utils import get_json

url = 'https://api.github.com'
data = get_json(url)
print(data)
