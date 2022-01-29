import requests

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=0294102"

response = requests.get(url)
print(response)
print(response.text)
