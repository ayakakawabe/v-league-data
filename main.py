import requests
import bs4

url="https://www.vleague.jp/record"
response=requests.get(url)
if not response.ok:
    print(f"fialed status {response.status_code}:{response.reason}")
else:
    soup=bs4.BeautifulSoup(response.content,"html.parser")
    print(soup)