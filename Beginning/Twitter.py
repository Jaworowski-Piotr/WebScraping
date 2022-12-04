# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 03:23:48 2022

@author: Piotr
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

import pandas as pd 
import time


s=Service("C:/Users/Piotr/Desktop/Python/WebScriping/chromedriver_win32/chromedriver.exe")
driver =  webdriver.Chrome(service=s)

driver.get("https://twitter.com/")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a').click()
time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
login.send_keys('jaworowskipiotr95@gmail.com')
driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
time.sleep(2)
login_pass = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
login_pass.send_keys('jakispasik12')
driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
time.sleep(2)
search_box = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search_box.send_keys('The Rock')
search_box.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]').click()



soup = BeautifulSoup(driver.page_source, 'lxml')
posts = soup.find_all('div', class_ = "css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0")
len(posts)

tweets = []

while len(tweets)<150:
    for post in posts:
        tweets.append(post.find('span', class_ = 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0').text)
        break
    driver.execute_script('window.scroll(0, document.body.scrollHeight)')
    time.sleep(1.5)
    posts = soup.find_all('div', class_ = "css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0")
    tweets2 = list(set(tweets))






