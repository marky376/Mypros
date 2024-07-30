import requests

def get_json(url):
    """
    Makes a GET request to the given URL and returns the JSON response.
    
    Args:
        url (str): The URL to make the request to.
    
    Returns:
        dict: The JSON response from the URL.
    """
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

