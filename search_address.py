import requests


def search_address(zipcode):
    if len(zipcode) != 7:
        return "郵便番号はハイフンなしの7桁で入力してください！(*｀･ω･´)"
    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    # url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" +zipcode 上行と同義
    response = requests.get(url)
    results = response.json()['results']

    address = []
    for index in range(len(results)):
        pref_name = results[index]['address1']
        city_name = results[index]['address2']
        town_name = results[index]['address3']
        address.append(f'{pref_name}{city_name}{town_name}')

    return address
