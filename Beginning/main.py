from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup


#Tags

soup.header


tag = soup.header.p
tag.string


#Attributes 
tag = soup.header.a
tag.attrs
tag['data-toggle']

tag['attribute_new '] = 'This is a new attribute'