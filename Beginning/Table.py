# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:37:44 2022

@author: Piotr
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find(class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
table


table.find_all('th')

headers = []

for i in table.find_all('th'):
    headers.append(i.text)
    
df = pd.DataFrame(columns = headers)


all_rows = table.find_all('tr')[1:]
for j in all_rows:
    row_data = j.find_all('td')
    row = [td.text for td in row_data]
    length = len(df)
    df.loc[length] = row

df.to_csv('C:/Users/Piotr/Desktop/Python/WebScriping/Beginning/table_scraped.csv')





















