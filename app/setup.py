from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
                command_executor = 'http://selenium:4444/wd/hub',
                options = options
                )
url="https://www.vleague.jp/record"