# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 01:29:09 2022

@author: Piotr
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import pandas as pd 

import time 

s=Service("C:/Users/Piotr/Desktop/Python/WebScriping/chromedriver_win32/chromedriver.exe")
driver =  webdriver.Chrome(service=s)

driver.get("https://www.nike.com/pl/w/wyprzedaz-3yaep")
driver.find_element(By.XPATH, '//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[2]/div/div[2]/div[2]/button').click()

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scroll(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if last_height == new_height: 
        break
    last_height = new_height
    

soup = BeautifulSoup(driver.page_source, 'lxml') 
product_card = soup.find_all('div', class_ = 'product-card__body')

df = pd.DataFrame({"Link": [''], "Title": [''], "Sub_Title": [''], 'Price': ['']})

for product in product_card:
    link = product.find('a', class_ = 'product-card__img-link-overlay').get('href')
    title = product.find('div', class_ = 'product-card__title').text
    sub_title = product.find('div', class_  = 'product-card__subtitle').text
    act_price = product.find('div', class_ = 'product-price is--current-price css-1ydfahe').text
    df = df.append({"Link": link, "Title": title, "Sub_Title": sub_title, 'Price': act_price}, ignore_index=True)













