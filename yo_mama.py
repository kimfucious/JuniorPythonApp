import requests

api_url = "https://api.yomomma.info/"
headers = {"Accept": "application/json"}


def get_yo_mama_joke():
    resp = requests.get(api_url, headers=headers)
    data = resp.json()
    return data["joke"]
