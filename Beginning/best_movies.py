# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 07:56:43 2022

@author: Piotr
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


s=Service("C:/Users/Piotr/Desktop/Python/WebScriping/chromedriver_win32/chromedriver.exe")
driver =  webdriver.Chrome(service=s)

url = 'http://www.google.com/'
browser = driver.get(url)

driver.find_element(By.XPATH, '//*[@id="L2AGLb"]').click()

box  = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Top 100 moveis of all time')
box.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a').click()
time.sleep(3)
driver.execute_script('window.scroll(0,10500)') 
driver.save_screenshot("C:/Users/Piotr/Desktop/Python/WebScriping/Screen_shot/movies.png")