#!/usr/bin/env python3
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, Timeout
from urllib3.util.retry import Retry

"""
In this example, I will handle additional scenarios such as retrying on transient errors, handling timeouts, and providing better error messages.
"""

def get_json(url, retries=3, backoff_factor=0.3, timeout=5):
    """
    Retrieves JSON data from a given URL with retry and timeout handling

    :param url: The URL to fetch the JSON data from.
    :param retries: The maximum number of retries on transient errors.
    :param backoff_factor: The backoff factor for the retry delay
    :param timeout: the timeout for the request in seconds.
    :return: The JSON data parsed into a Python dictionary.
    :raises RequestException: If the request fails.
    """

    session = requests.Session()
    retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("https://", adapter)


    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Timeout as e:
        print(f"Request timed out: {e}")
        raise
    except RequestException as e:
        print(f"Request failed: {e}")
        raise

# Example usage
if __name__ == "__main__":
    url = "https://api.github.com"
    try:
        data = get_json(url)
        print(data)
    except RequestException as e:
        print(f"Error fetching data: {e}")
