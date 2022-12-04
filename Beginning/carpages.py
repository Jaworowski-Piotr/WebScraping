# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:26:35 2022
 
@author: Piotr
"""

import requests 
from bs4 import BeautifulSoup
import pandas as pd
import re


url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'

page = requests.get(url)
page

df = pd.DataFrame({"Car": [''], "Model": [''], 'Price': ['']})
soup = BeautifulSoup(page.text, 'lxml')

for _ in range(10):
    car_cards = soup.find_all('div', class_ = 'media soft push-none rule')
    for car_card in car_cards:
        car = car_card.find('h4', class_ = 'hN').text
        car_brand = car_card.find('h5', class_ = 'hN').text
        price = car_card.find('strong', class_ = re.compile('delta')).text.strip()
        
        df = df.append({"Car": car, "Model": car_brand, 'Price': price}, ignore_index=True)

link_ = soup.find('a', class_ = 'nextprev').get('href')
url = 'https://www.carpages.ca' + link_
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


































