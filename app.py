import requests

zipcode = "0294102"
# zipcode = input("郵便番号〈ハイフン無し〉は？ >> ")

url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
# url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" +zipcode 上行と同義

response = requests.get(url)
print(response)
print(response.text)
