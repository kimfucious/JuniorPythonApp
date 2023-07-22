import requests

BASE_URL = "https://restcountries.com/v3.1/"
headers = {"Accept": "application/json"}


def search_country(search_string):
    resp = requests.get(f"{BASE_URL}/name/{search_string}", headers=headers)
    data = resp.json()
    # print("DATA", data)
    if len(data) == 0:
        return "There is no such country." 
    else:
        first = data[0]
        flag = first["flag"]
        name = first["name"]["common"] 
        return f"{name}'s flag is {flag}"
