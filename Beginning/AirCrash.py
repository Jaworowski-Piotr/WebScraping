import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.planecrashinfo.com/database.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")
table = soup.find_all('table')[1]
all_rows = table.find_all('tr')
# dekada do single_crash relacja one to many
for j in all_rows:
    single_td_data = j.find_all('td')[1:]
    for td in single_td_data:
        print(td)
        if td.text.strip() != '':
            link = td.find('a').get('href')
        if link[0] != '/':
            link = '/' + link
        url = f'http://www.planecrashinfo.com{link}'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        inner_rows = soup.find_all('tr')[1:]
        break
        for tr in inner_rows:
            link_2 = tr.find('a').get('href')
            link_2 = re.search(r'\-(.*)', link_2)
            link_2 = link_2.group()
            url = f'http://www.planecrashinfo.com/2020/2020-1.htm'
            url
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'lxml')
            accident_detials_data = soup.find_all('tr')[1].find_all('td')[1].text
            accident_detials_data
            accident_detials = []
            for x in accident_detials_data:
                accident_detial = x.find_all('td')[1].text
                print(accident_detial)
                accident_detials.append(accident_detial)