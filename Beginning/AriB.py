# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:35:31 2022

@author: Piotr
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd 


url = 'https://www.airbnb.pl/s/Honolulu--Hawaje--Stany-Zjednoczone/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=1&query=Honolulu%2C%20Hawaje&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2022-11-14&checkout=2022-11-15&source=structured_search_input_header&search_type=filter_change&ne_lat=21.3731401842534&ne_lng=-157.69998433139085&sw_lat=21.17798669244808&sw_lng=-157.96612813440993&zoom=12&search_by_map=true'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

post = soup.find_all('div', class_ = 'c4mnd7m dir dir-ltr')[0]
a_tag = post.find('a', class ='').get('href')
a_tag

while True:
    postings = soup.find_all('div', class_ = 'dir dir-ltr')
    for post in postings:
        link = post.find('a', class_ = 'ln2bl2p dir dir-ltr').get('href')
        break
    
    next_page_url = 'https://www.airbnb.pl/'+soup.find('a', {'aria-label':'Dalej'}).get('href')
    page = requests.get(next_page_url)
    soup = BeautifulSoup(page.text, 'lxml')
    

