# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:02:26 2022

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


#driver.get('https://www.goat.com/sneakers')
#driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div[2]').text


#/*[@id="grid-body"]/div/div[1]/div[1]/a/div[1]/div[2]/div/div/span
#//*[@id="grid-body"]/div/div[1]/div[2]/a/div[1]/div[2]/div/div/span


url = 'http://www.google.com/'
browser = driver.get(url)

box  = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('What is webscraping')
box.send_keys(Keys.ENTER)


#Clicking on a button 

button  = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
button

link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[3]/div/div/div[1]/div/a')
link.send_keys(Keys.ENTER)


#taking a screen shot 

driver.save_screenshot("C:/Users/Piotr/Desktop/Python/WebScriping/Screen_shot/screenshot.png")


#full example 

s=Service("C:/Users/Piotr/Desktop/Python/WebScriping/chromedriver_win32/chromedriver.exe")
driver =  webdriver.Chrome(service=s)
url = 'http://www.google.com/'
browser = driver.get(url)

box  = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Giraffe')
box.send_keys(Keys.ENTER)

images  = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
images.send_keys(Keys.ENTER)

image_of_giraffe = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[4]/a[1]/div[1]/img').screenshot("C:/Users/Piotr/Desktop/Python/WebScriping/Screen_shot/giraffe.png")


# Self scrolling 

driver.execute_script('return document.body.scrollHeight')

driver.execute_script('window.scroll(0,16941)')
height = 0

while height < 25000:
    height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script(f'window.scroll(0,{height})')


#wait times 


s=Service("C:/Users/Piotr/Desktop/Python/WebScriping/chromedriver_win32/chromedriver.exe")
driver =  webdriver.Chrome(service=s)
url = 'http://www.google.com/'
browser = driver.get(url)

box  = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Giraffe')
time.sleep(3)
box.send_keys(Keys.ENTER)


element = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, 'cnt')))  #jeżeli będzie nie poprawy adres to wyskoczy timeout 

images  = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
images.send_keys(Keys.ENTER)















