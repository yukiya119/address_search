import requests


def search_address(zipcode):
    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    # url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" +zipcode 上行と同義
    response = requests.get(url)
    results = response.json()['results']
    pref_name = results[0]['address1']
    city_name = results[0]['address2']
    town_name = results[0]['address3']
    address = f'{pref_name}{city_name}{town_name}'
    return address
