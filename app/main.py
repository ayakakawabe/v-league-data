from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
driver = webdriver.Remote(
             command_executor = 'http://selenium:4444/wd/hub',
             options = options
             )
driver.get("https://www.vleague.jp/record")
time.sleep(3)
driver.quit()
print("finish main.py")


# import requests
# import bs4

# url="https://www.vleague.jp/record"
# response=requests.get(url)
# if not response.ok:
#     print(f"fialed status {response.status_code}:{response.reason}")
# else:
#     html_text=bs4.BeautifulSoup(response.content,"html.parser")
#     text=html_text.select("table")
#     print(text[1])