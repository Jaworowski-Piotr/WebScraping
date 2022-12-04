# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:29:57 2022

@author: Piotr
"""


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url = 'https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol'


page = requests.get(url)
page


soup = BeautifulSoup(page.text, 'lxml')
soup

stock_price_box = soup.find('h2', class_ = 'intraday__price')
stock_price = stock_price_box.find(class_ = 'value').text
stock_price

analyst_opition = soup.find('li', class_ = 'analyst__option active')
analyst_opition.text


_week_range = soup.find_all('div', class_ = 'range__header')[2]
lower_price = _week_range.find_all(class_ = 'primary')[0]
higher_price = _week_range.find_all(class_ = 'primary')[1]

lower_price.text, higher_price.text, analyst_opition.text
