# Connpass HTML Fetcher

このスクリプトは、[Connpass](https://connpass.com) のイベントページから**HTMLソース全体を取得するための簡易Pythonスクリプト**です。  
参加者一覧ページなど、JavaScriptなしで直接アクセス可能なHTMLを取得する用途に向いています。

---

## ✅ 機能

- 指定したConnpassイベントページの**HTML全文を取得**
- `User-Agent` ヘッダーを付加して、403エラー（アクセス拒否）を回避

---

## 🧪 使用例

```python
import requests

url = "https://gotalk.connpass.com/event/355423/participation/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
html = res.text

print(html)  # ← HTML全文が取れるはず
