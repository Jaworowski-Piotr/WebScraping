# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 08:07:44 2022

@author: Piotr
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/division/2019/REG'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup

div_ = soup.find_all('div', class_ = 'd3-o-table--horizontal-scroll')
div_

for element in div_:
    headers = [i.text for i in element.find_all('th')]
    headers

df = pd.DataFrame(columns=headers)



for element in div_:
    for i in element.find_all('tr')[1:]:
        row = [x.text for x in i.find_all('td')]
        length = len(df)
        df.loc[length] = row


tables = soup.find_all('th')
tables 