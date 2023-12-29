import requests
import bs4

url="https://www.vleague.jp/record"
response=requests.get(url)
if not response.ok:
    print(f"fialed status {response.status_code}:{response.reason}")
else:
    html_text=bs4.BeautifulSoup(response.content,"html.parser")
    text=html_text.select("table")
    print(text[1])