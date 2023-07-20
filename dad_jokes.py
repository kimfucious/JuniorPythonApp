import requests

api_url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}


def get_dad_joke():
    resp = requests.get(api_url, headers=headers)
    data = resp.json()
    return data["joke"]
