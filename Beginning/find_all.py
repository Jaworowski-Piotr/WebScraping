# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 04:54:02 2022

@author: Piotr
"""

"""
https://webscraper.io/test-sites/e-commerce/allinone/phones/touch
"""


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"


page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

soup.find('div', {'class':'container test-site'})
soup.find('h4', {'class':'pull-right price'})



soup.find('h4', class_ = 'pull-right price')
soup.find_all('h4', class_ = 'pull-right price')[1]
soup.find_all('h4', class_ = 'pull-right price')[6:]
soup.find_all('a', class_ = 'title')
soup.find_all('p', class_ = 'pull-right')


soup.find_all(['h4', 'p'])
soup.find_all(id=True)
soup.find_all('p', string= re.compile('rev'), limit=5)
soup.find_all(string= 'Iphone')
soup.find_all(string=re.compile('Nok'))
soup.find_all(string = ['Iphone', 'Nokia 123'])


soup.find_all(class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'), limit = 3)


#find_all part 3

product_name = soup.find_all('a', class_ = 'title')
product_name

price = soup.find_all('h4', class_ = 'pull-right price')
price

reviews = soup.find_all('p', class_ = re.compile('pull'))
reviews

description = soup.find_all('p', class_ = 'description')
description

product_name_list = []
price_list = []
review_list = []
description_list = []


for i in product_name:
    product_name_list.append(i.text)

for i in price:
    price_list.append(i.text)
    
for i in reviews:
    review_list.append(i.text)
    
for i in description:
    description_list.append(i.text)

table = pd.DataFrame({'Product Name': product_name_list, 
                     'Price': price_list,
                     'Review': review_list,
                     'Description': description_list})


#Extracted data from nested 


boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')[6]

boxes.find(class_ = 'description').text

box2 = soup.find_all('ul', class_ = 'nav')[2]

li_element = box2.find_all('li')[0]
li_element.text




















