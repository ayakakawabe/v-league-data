from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import bs4
import time
from setup import driver,url
from get_data import latest_rank


try:
    driver.get(url)
    latest_rank.latest(driver)
    driver.quit()
except Exception as e:
    print("error:",e)
    driver.quit()