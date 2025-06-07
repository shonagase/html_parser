import requests

url = "https://gotalk.connpass.com/event/355423/participation/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
html = res.text

print(html)  # ← HTML全文が取れるはず

